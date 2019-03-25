
package cheesefish.happy_merchant;

import java.lang.reflect.Array;
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
    public ArrayList<Population> populations;
    public int area;

    /**
     * Constructor used when initializing settlements
     *
     * @param xPosition of settlement on map
     * @param yPosition of settlement on map
     * @param mapID unique to settlement, used in neighbors array
     * @param neighbors array of MapIDs of neighbors
     * @param market housing the goods currently for sale
     * @param populations list of populations in settlement
     * @param area available to exploitation
     */
    public Settlement(double xPosition, double yPosition, int mapID, ArrayList<Integer> neighbors,
                      String name, Market market, ArrayList<Population> populations, int area) {
        this.xPosition = xPosition;
        this.yPosition = yPosition;
        this.mapID = mapID;
        this.neighbors = neighbors;
        this.name = name;
        this.market = market;
        this.populations = populations;
        this.area = area;
    }

    /**
     * @param xPosition to be set to the settlement
     */
    public void setXPosition(double xPosition) {
        this.xPosition = xPosition;
    }

    /**
     * @return xPosition of the settlement
     */
    public double getXPosition() {
        return xPosition;
    }

    /**
     * @param yPosition of the settlement
     */
    public void setYPosition(double yPosition) {
        this.yPosition = yPosition;
    }

    /**
     * @return yPosition of the settlement
     */
    public double getYPosition() {
        return yPosition;
    }

    /**
     * @param mapID to be set to the settlement
     */
    public void setMapID(int mapID) {
        this.mapID = mapID;
    }

    /**
     * @return mapId of the settlement
     */
    public int getMapID() {
        return mapID;
    }

    /**
     * @param name of the settlement to be set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return name of the settlement
     */
    public String getName() {
        return name;
    }

    /**
     * @param market to be set
     *               Replaces old market
     */
    public void setMarket(Market market) {
        this.market = market;
    }

    /**
     * @return market of the settlement
     */
    public Market getMarket() {
        return market;
    }

    /**
     * @param populations list ot replace current list of populations
     */
    public void setPopulations(ArrayList<Population> populations) {
        this.populations = populations;
    }

    /**
     * @return list of all populatiosn of a settlement
     */
    public ArrayList<Population> getPopulations() {
        return populations;
    }
}

