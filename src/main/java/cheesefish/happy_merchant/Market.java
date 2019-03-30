
package cheesefish.happy_merchant;

import java.util.ArrayList;

/**
 * Basis for markets found in settlements
 *
 * @author cheesefish
 * @version 1.1
 */
public class Market {
    public ArrayList<ItemBatch> supplies;

    /**
     * Constructor used when initializing a market
     *
     * @param supplies of the market
     */
    public Market(ArrayList<ItemBatch> supplies) {
        this.supplies = supplies;
    }

    /**
     * Sets the supplies of a market and replaces current supplies
     *
     * @param supplies to be set
     */
    public void setSupplies(ArrayList<ItemBatch> supplies) {
        this.supplies = supplies;
    }

    /**
     * @return list of supplies of a market
     */
    public ArrayList<ItemBatch> getSupplies() {
        return supplies;
    }
}