package cheesefish.happy_merchant;

import java.util.Stack;
import cheesefish.happy_merchant.graphics.Window;
import cheesefish.happy_merchant.graphics.Graphics;

/**
 * Abstract application state. Handles the window and game loop
 *
 * @author Klaxel
 * @version 1.1
 */
public abstract class AppState {

	protected static Stack<AppState> appStateStack = new Stack<AppState>();
	private static boolean isRunning = false;

	protected boolean shouldChangeState = false;
	protected boolean shouldInitialize = true;
	protected boolean shouldTerminateAutomatically = true;

	/**
	 * Run app with this state as root. Creates window and initializes gl.
	 * Manages app level loop by going through the state stack until empty.
	 * Cleans up when done. Will return immediately if called a second time
	 * if first call hasn't returned yet (i.e. you can only run one app at a
	 * time).
	 */
	public void run() {
		if(this.isRunning) {
			return;
		} else {
			this.isRunning = true;
		}

		//create/init
		Window.create();
		Graphics.initialize();

		//app-level loop
		this.appStateStack.push(this);
		while(!this.appStateStack.isEmpty()) {
			this.appStateStack.pop().loop(); //state-level loop
		}

		//clean up
		Graphics.terminate();
		Window.destroy();

		this.isRunning = false;
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
		if(Window.shouldNotClose()) {
			if(this.shouldInitialize) {
				initialize();
				this.shouldInitialize = false;
			}
			preloop();
			while(Window.shouldNotClose() && !this.shouldChangeState) {
				Graphics.clear(); //clear front buffer
				Window.update(); //swap front and back buffers (show back one)
				update();
				render(); //render on back buffer
			}
			postloop();
		}
		if(isTerminateConditionsMet()) {
			terminate();
			this.shouldInitialize = true;
		}
		this.shouldChangeState = false;
	}

	/**
	 * Leaves this state and enters the other state.
	 */
	protected void enterState(AppState otherAppState) {
		this.appStateStack.push(this);
		this.appStateStack.push(otherAppState);
		exitState();
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
		if(Window.shouldNotClose()) {
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