
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

    public Market(ArrayList<ItemBatch> supplies) {
        this.supplies = supplies;
    }

    public void setSupplies(ArrayList<ItemBatch> supplies) {
        this.supplies = supplies;
    }

    public ArrayList<ItemBatch> getSupplies() {
        return supplies;
    }
}