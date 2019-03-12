package cheesefish.happy_merchant;

import java.util.*;
import cheesefish.happy_merchant.graphics.*;

import static org.lwjgl.glfw.GLFW.*;

/**
 * Abstract application state. Handles the window and game loop
 *
 * @author Klaxel
 * @version 1.0
 */
public abstract class AppState {

	protected Window window;
	protected Stack<AppState> appStateStack;

	protected boolean shouldChangeState = false;
	protected boolean shouldInitialize = true;
	protected boolean shouldTerminateAutomatically = true;

	/**
	 * Run state as new app. Creates new window and new state-stack.
	 * Manages app level loop by going through the state stack until empty.
	 */
	public void run() {
		this.appStateStack = new Stack<AppState>();
		this.appStateStack.push(this);
		this.window = new Window();
		while(!this.appStateStack.isEmpty()) {
			this.appStateStack.pop().loop();
		}
		this.window.terminateWindow();
	}

	/**
	 * State level loop. Calls abstract methods.
	 *
	 * @see #initialize()
	 * @see #preloop()
	 * @see #update()
	 * @see #render()
	 * @see #postloop()
	 * @see #terminate()
	 */
	private void loop() {
		if(this.window.shouldNotClose()) {
			if(this.shouldInitialize) {
				initialize();
				this.shouldInitialize = false;
			}
			preloop();
			while(this.window.shouldNotClose() && !this.shouldChangeState) {
				glfwPollEvents(); //poll input events
				update();
				this.window.clear(); //clear window to bg color
				render();
			}
			postloop();
		}
		if(isTerminateConditionsMet()) {
			terminate();
			this.shouldInitialize = true; //must be reinitialized if terminated
		}
		this.shouldChangeState = false;
	}

	/**
	 * Leaves this state and enters the other state.
	 */
	protected void enterState(AppState otherAppState) {
		otherAppState.appStateStack = this.appStateStack;
		otherAppState.window = this.window;
		this.appStateStack.push(this);
		this.appStateStack.push(otherAppState);
		this.shouldChangeState = true;
	}

	/**
	 * Leaves this state end enters the previous state in the stack.
	 */
	protected void exitState() {
		this.shouldChangeState = true;
	}

	/**
	 * @param bool Set if the terminate method should be called automatically
	 * when termination conditions are met. True by default.
	 */
	protected void setShouldTerminateAutomatically(boolean bool) {
		this.shouldTerminateAutomatically = bool;
	}

	/**
	 * @return Returns true if state isn't in the stack. Also returns true if
	 * window is closing.
	 */
	private boolean isTerminateConditionsMet() {
		if(this.window.shouldNotClose()) {
			boolean isStateNotInStack = this.appStateStack.search(this) == -1;
			return isStateNotInStack && this.shouldTerminateAutomatically;
		} else {
			return true;
		}
	}

	/**
	 * Is called automatically the first time this state is entered.
	 */
	protected abstract void initialize();

	/**
	 * Is called automatically when this state is entered, after initialize.
	 */
	protected abstract void preloop();

	/**
	 * Is called automatically and repeatedly until leaving this state.
	 * Handle logic and input here. Is called before render.
	 */
	protected abstract void update();

	/**
	 * Is called automatically and repeatedly until leaving this state.
	 * Handle graphics here. Is called after update.
	 */
	protected abstract void render();

	/**
	 * Is called automatically when leaving this state, before terminate.
	 */
	protected abstract void postloop();

	/**
	 * Is called automatically when leaving this state if conditions are met.
	 * See 'isTerminateConditionsMet' metod for condition details. Can be set to
	 * not be called automatically.
	 *
	 * @see #setShouldTerminateAutomatically(boolean bool)
	 * @see #isTerminateConditionsMet()
	 */
	protected abstract void terminate();

}