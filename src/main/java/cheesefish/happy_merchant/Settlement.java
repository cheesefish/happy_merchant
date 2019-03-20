
package cheesefish.happy_merchant;

import java.util.ArrayList;

/**
 * Settlement Objects fetched from world.json
 *
 * @author cheesefish
 * @version 2.1
 */

public class Settlement extends MapVertex {
    public String name;
    public Market market;
    public ArrayList<Population> population;
    public int area;

    /**
     * Constructor used when initializing settlements
     *
     * @param xPosition of settlement on map
     * @param yPosition of settlement on map
     * @param mapID unique to settlement, used in neighbors array
     * @param neighbors array of MapIDs of neighbors
     * @param market housing the goods currently for sale
     * @param population list of populations in settlement
     * @param area available to exploitation
     */

    public Settlement(double xPosition, double yPosition, int mapID, ArrayList<Integer> neighbors,
                      String name, Market market, ArrayList<Population> population, int area) {
        this.xPosition = xPosition;
        this.yPosition = yPosition;
        this.mapID = mapID;
        this.neighbors = neighbors;
        this.name = name;
        this.market = market;
        this.population = population;
        this.area = area;
    }

    public void setXPosition(double xPosition) {
        this.xPosition = xPosition;
    }

    public double getXPosition() {
        return xPosition;
    }

    public void setYPosition(double yPosition) {
        this.yPosition = yPosition;
    }

    public double getYPosition() {
        return yPosition;
    }

    public void setMapID(int mapID) {
        this.mapID = mapID;
    }

    public int getMapID() {
        return mapID;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

