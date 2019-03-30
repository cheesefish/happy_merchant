
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

    /**
     * Constructor used when initializing a new ItemBatch
     *
     * @param name of ItemType. Used to link ItemType to ItemBatch
     * @param category Name of the ItemType category
     * @param volume of a single unit of the item
     * @param weight of a single unit of the item
     * @param amount of units of the item
     */
    public ItemBatch(String name, String category, int volume, int weight, int amount) {
        super(name, category, volume, weight);
        this.amount = amount;
    }
}