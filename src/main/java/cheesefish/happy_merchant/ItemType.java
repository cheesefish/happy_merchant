
package cheesefish.happy_merchant;

/**
 * Items available in the world
 *
 * @author cheesefish
 * @version 1.0
 */

public class ItemType {
    public String name;
    public String category;
    public int volume;
    public int weight;

    public ItemType(String name, String category, int volume, int weight) {
        this.name = name;
        this.category = category;
        this.volume = volume;
        this.weight = weight;
    }

    public String getName() {
        return name;
    }

    public String getCategory() {
        return category;
    }

    public int getVolume() {
        return volume;
    }

    public int getWeight() {
        return weight;
    }
}