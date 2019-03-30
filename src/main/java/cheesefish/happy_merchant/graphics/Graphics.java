package cheesefish.happy_merchant.graphics;

import java.nio.*;
import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

/**
 * Static graphics class. Contains functions handling rendering (openGL).
 *
 * @author Klaxel
 * @version 1.1
 */
public class Graphics {

	private long shaderProgram;

	/**
	 * Private constructor. Static class, no instantiation.
	 */
	private Graphics() {}

	/**
	 * Initializes graphics.
	 */
	public static void initialize() {
		GL.createCapabilities();
		//glViewport(0, 0, Window.getWidth(), Window.getHeight());
	}

	/**
	 * Terminates graphics.
	 */
	public static void terminate() {
		//nothing to terminate yet
	}

	/**
	 * Clears graphic (front buffer) back to background color.
	 */
	public static void clear() {
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	}

}
