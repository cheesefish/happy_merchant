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

import cheesefish.happy_merchant.graphics.*;

public class Window {

	public final long windowHandle;

	public Window() {
		this.windowHandle = createWindow();
	}

	private long createWindow() {
		//Configure window
		glfwWindowHint(GLFW_RESIZABLE, GLFW_TRUE);
		glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
		glfwWindowHint(GLFW_DECORATED, GLFW_TRUE);
		glfwWindowHint(GLFW_FOCUSED, GLFW_FALSE);
		glfwWindowHint(GLFW_AUTO_ICONIFY, GLFW_TRUE);
		glfwWindowHint(GLFW_FLOATING, GLFW_FALSE);
		glfwWindowHint(GLFW_MAXIMIZED, GLFW_FALSE);

		//Create window
		long windowHandle = glfwCreateWindow(640, 480, "Happy Merchant the Game!", NULL, NULL);
		if ( windowHandle == NULL )
			throw new RuntimeException("Failed to create the GLFW window");

		//Setup callback: Close window on ESCAPE key-press
		glfwSetKeyCallback(windowHandle, (window, key, scancode, action, mods) -> {
			if ( key == GLFW_KEY_ESCAPE && action == GLFW_RELEASE )
				glfwSetWindowShouldClose(windowHandle, true); // We will detect this in the rendering loop
		});

		// Get the thread stack and push a new frame
		try ( MemoryStack stack = stackPush() ) {
			IntBuffer pWidth = stack.mallocInt(1); // int*
			IntBuffer pHeight = stack.mallocInt(1); // int*

			// Get the window size passed to glfwCreateWindow
			glfwGetWindowSize(windowHandle, pWidth, pHeight);

			// Get the resolution of the primary monitor
			GLFWVidMode vidmode = glfwGetVideoMode(glfwGetPrimaryMonitor());

			// Center the window
			glfwSetWindowPos(
				windowHandle,
				(vidmode.width() - pWidth.get(0)) / 2,
				(vidmode.height() - pHeight.get(0)) / 2
			);
		}

		glfwMakeContextCurrent(windowHandle);
		glfwSwapInterval(1); // Enable v-sync
		glfwShowWindow(windowHandle);
		GL.createCapabilities(); //Enables interoperation w/ GLFW's OpenGL context
		glClearColor(0.0f, 0.0f, 0.0f, 0.0f); //Set bg color

		return windowHandle;
	}

	public boolean isWindowOpen() {
		return !glfwWindowShouldClose(this.windowHandle);
	}

	public void clearWindow() {
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // clear the framebuffer
		glfwSwapBuffers(this.windowHandle); // swap the color buffers
	}

	public void terminateWindow() {
		glfwFreeCallbacks(this.windowHandle);
		glfwDestroyWindow(this.windowHandle);
	}
}
