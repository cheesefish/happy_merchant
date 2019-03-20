
package cheesefish.happy_merchant;

import java.util.ArrayList;

/**
 * A group of similar people statistically treated as a single unit
 *
 * @author cheesefish
 * @version 2.1
 */

public class Population {
    public String name;
    public int number;
    public ArrayList<ItemBatch> needs;
    public ArrayList<ItemBatch> productions;
    public ArrayList<ItemBatch> inventory;

    public Population(String name, int number,
                      ArrayList<ItemBatch> needs,
                      ArrayList<ItemBatch> productions,
                      ArrayList<ItemBatch> inventory) {
        this.name = name;
        this.number = number;
        this.needs = needs;
        this.productions = productions;
        this.inventory = inventory;
    }
}