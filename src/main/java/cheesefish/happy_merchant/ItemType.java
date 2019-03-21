
package cheesefish.happy_merchant;

/**
 * Items available in the world
 *
 * @author cheesefish
 * @version 1.1
 */
public class ItemType {
    public String name;
    public String category;
    public int volume;
    public int weight;

    /**
     * Constructor used when initializing itemTypes
     *
     * @param name of the itemType
     * @param category of the itemType. I.e food, industrial etc.
     * @param volume of a single unit of the itemType
     * @param weight of a single unit of the itemType
     */
    public ItemType(String name, String category, int volume, int weight) {
        this.name = name;
        this.category = category;
        this.volume = volume;
        this.weight = weight;
    }

    /**
     * @return name of the itemType
     */
    public String getName() {
        return name;
    }

    /**
     * @return name of the category of the itemType
     */
    public String getCategory() {
        return category;
    }

    /**
     * @return volume of a single unit of the itemType
     */
    public int getVolume() {
        return volume;
    }

    /**
     * @return weight of a single unit of the itemType
     */
    public int getWeight() {
        return weight;
    }
}