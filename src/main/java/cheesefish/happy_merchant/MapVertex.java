
package cheesefish.happy_merchant;


import java.util.ArrayList;

/**
 * Serves are basis for all objects on the map
 * Can be fitted to a graph
 *
 * @author cheesefish
 * @version 1.0
 */

public class MapVertex {

    public double xPosition;
    public double yPosition;
    public int mapID;
    public ArrayList<Integer> neighbors;

}