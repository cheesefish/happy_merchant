package cheesefish.happy_merchant.graphics;

import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;
import java.nio.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

/**
 * Window object.
 *
 * @author Klaxel
 * @version 1.0
 */
public class Window {

	public final long windowHandle; //id

	/**
	 * Constructor. Creates window, saves handle.
	 */
	public Window() {
		initializeGLFW();
		configureWindow();
		this.windowHandle = createWindow(640, 480, "Happy Merchant the Game!");
		centerWindow();
		showWindow();
	}

	/**
	 * Initializes, creates, and shows window.
	 *
	 * @return Returns window handle.
	 */
	private void initializeGLFW() {
		// Setup an error callback. The default implementation
		// will print the error message in System.err.
		GLFWErrorCallback.createPrint(System.err).set();

		// Initialize GLFW. Most GLFW functions will not work before doing this.
		if ( !glfwInit() )
			throw new IllegalStateException("Unable to initialize GLFW");
	}

	/**
	 * Set window properties.
	 */
	private void configureWindow() {
		glfwWindowHint(GLFW_RESIZABLE, GLFW_TRUE);
		glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
		glfwWindowHint(GLFW_DECORATED, GLFW_TRUE);
		glfwWindowHint(GLFW_FOCUSED, GLFW_FALSE);
		glfwWindowHint(GLFW_AUTO_ICONIFY, GLFW_TRUE);
		glfwWindowHint(GLFW_FLOATING, GLFW_FALSE);
		glfwWindowHint(GLFW_MAXIMIZED, GLFW_FALSE);
	}

	/**
	 * Creates window with given properties.
	 *
	 * @param width Screen width in pixels
	 * @param height Screen height in pixels
	 * @param title Screen title
	 * @return Returns window handle (id)
	 */
	private long createWindow(int width, int height, String title) {
		long windowHandle = glfwCreateWindow(width, height, title, NULL, NULL);
		if ( windowHandle == NULL )
			throw new RuntimeException("Failed to create the GLFW window");
		return windowHandle;
	}

	/**
	 * Centers window on the screen.
	 */
	public void centerWindow() {
		// Get the thread stack and push a new frame
		try ( MemoryStack stack = stackPush() ) {
			IntBuffer pWidth = stack.mallocInt(1); // int*
			IntBuffer pHeight = stack.mallocInt(1); // int*

			// Get the window size passed to glfwCreateWindow
			glfwGetWindowSize(this.windowHandle, pWidth, pHeight);

			// Get the resolution of the primary monitor
			GLFWVidMode vidmode = glfwGetVideoMode(glfwGetPrimaryMonitor());

			// Center the window
			glfwSetWindowPos(
				this.windowHandle,
				(vidmode.width() - pWidth.get(0)) / 2,
				(vidmode.height() - pHeight.get(0)) / 2
			);
		}
	}

	/**
	 * Makes some final setup and shows the window.
	 */
	private void showWindow() {
		glfwMakeContextCurrent(this.windowHandle);
		glfwSwapInterval(1); // Enable v-sync
		glfwShowWindow(this.windowHandle);
		GL.createCapabilities(); //Enables interoperation w/ GLFW's OpenGL context
		glClearColor(0.0f, 0.0f, 0.0f, 0.0f); //Set bg color
	}

	/**
	 * Destroys window.
	 */
	public void terminateWindow() {
		glfwFreeCallbacks(this.windowHandle);
		glfwDestroyWindow(this.windowHandle);
		glfwTerminate();
		glfwSetErrorCallback(null).free();
	}

	/**
	 * Clears window to background color, preparing it for fresh rendering.
	 */
	public void clear() {
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // clear the framebuffer
		glfwSwapBuffers(this.windowHandle); // swap the color buffers
	}

	/**
	 * @return True while window isn't set to close.
	 */
	public boolean shouldNotClose() {
		return !glfwWindowShouldClose(this.windowHandle);
	}

}
