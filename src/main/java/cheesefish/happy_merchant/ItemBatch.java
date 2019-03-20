
package cheesefish.happy_merchant;

/**
 * Batch of available in the world
 * Used in trade, supply and so on
 *
 * @author cheesefish
 * @version 1.1
 */

public class ItemBatch extends ItemType {
    private int amount;

    public ItemBatch(String name, String itemType, int volume, int weight, int amount) {
        super(name, itemType, volume, weight);
        this.amount = amount;
    }
}