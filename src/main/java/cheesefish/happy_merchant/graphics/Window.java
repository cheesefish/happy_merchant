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
 * Static window class. Creates a window and rendering context (GLFW).
 *
 * @author Klaxel
 * @version 1.1
 */
public class Window {

	private static long handle;
	private static int width, height;

	/**
	 * Private constructor. Static class, no instantiation.
	 */
	private Window() {}

	/**
	 * Creates window and configures window/glfw settings.
	 */
	public static void create() {
		//Setup GLFW to print errors to System.err
		GLFWErrorCallback.createPrint(System.err).set();

		//Initializes GLFW
		if(!glfwInit()) {
			throw new IllegalStateException("Unable to initialize GLFW");
		}

		//Preconfigure OpenGL version.
		glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); //for MacOSX

    	//Preconfigure window properties
		glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
		glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
		glfwWindowHint(GLFW_DECORATED, GLFW_TRUE);
		glfwWindowHint(GLFW_FOCUSED, GLFW_FALSE);
		glfwWindowHint(GLFW_AUTO_ICONIFY, GLFW_TRUE);
		glfwWindowHint(GLFW_FLOATING, GLFW_FALSE);
		glfwWindowHint(GLFW_MAXIMIZED, GLFW_FALSE);

		//Create window
		String title = "Happy Merchant the Game!";
		handle = glfwCreateWindow(width = 640, height = 480, title, NULL, NULL);
		if(handle == NULL) {
			throw new RuntimeException("Failed to create the GLFW window");
		}

		//Center window
		GLFWVidMode vidmode = glfwGetVideoMode(glfwGetPrimaryMonitor());
		glfwSetWindowPos(
			handle,
			(vidmode.width() - width) / 2,
			(vidmode.height() - height) / 2
		);

		//Final setup
		glfwMakeContextCurrent(handle);
		glfwSwapInterval(1); //vsync
		glfwShowWindow(handle);
	}

	/**
	 * Destroys window, terminates glfw, frees error callbacks.
	 */
	public static void destroy() {
		glfwFreeCallbacks(Window.handle);
		glfwDestroyWindow(handle);
		glfwTerminate();
		glfwSetErrorCallback(null).free();
	}

	/**
	 * Updates screen, swapping the front and back color buffers.
	 */
	public static void update() {
		glfwSwapBuffers(handle);
		glfwPollEvents();
	}

	/**
	 * @return True while window isn't set to close.
	 */
	public static boolean shouldNotClose() {
		return !glfwWindowShouldClose(handle);
	}

	/**
	 * @return Returns window handle (GLFW-window id).
	 */
	public static long getHandle() {
		return handle;
	}

	/**
	 * @return Returns window width.
	 */
	public static int getWidth() {
		return width;
	}

	/**
	 * @return Returns window height.
	 */
	public static int getHeight() {
		return height;
	}

	public static boolean isKey(int key, int mode) {
		return glfwGetKey(handle, key) == mode;
	}

}
