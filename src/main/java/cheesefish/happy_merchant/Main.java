package cheesefish.happy_merchant;

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

public class Main {

	public static void main(String[] args) {
		Graphics.initGraphics();
		Window window = new Window();
		while(window.isWindowOpen()) {
			window.clearWindow(); //clear window to bg color
			glfwPollEvents(); //poll input events
			/* DO LOOPY THINGS */
		}
		window.terminateWindow();
		Graphics.terminateGraphics();
	}

}
