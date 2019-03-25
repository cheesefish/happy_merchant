
package cheesefish.happy_merchant;

import java.util.ArrayList;

/**
 * A group of similar people statistically treated as a single unit
 *
 * @author cheesefish
 * @version 2.2
 */
public class Population {
    public String name;
    public int number;
    public ArrayList<ItemBatch> needs;
    public ArrayList<ItemBatch> productions;
    public ArrayList<ItemBatch> inventories;

    /**
     * Constructor used when initializing a population
     *
     * @param name of the population
     * @param number of members of the population
     * @param needs to sustain the population and its production
     * @param productions of the population
     * @param inventories current supplies of the population and its productions
     */
    public Population(String name, int number,
                      ArrayList<ItemBatch> needs,
                      ArrayList<ItemBatch> productions,
                      ArrayList<ItemBatch> inventories) {
        this.name = name;
        this.number = number;
        this.needs = needs;
        this.productions = productions;
        this.inventories = inventories;
    }

    /**
     * @param name to replace current name of the population
     */
    public void setName(String name){
        this.name = name;
    }

    /**
     * @return name of the population
     */
    public String getName() {
        return name;
    }

    /**
     * @param number to replace current number of members of the population
     */
    public void setNumber(int number) {
        this.number = number;
    }

    /**
     * @return number of members of the population
     */
    public int getNumber() {
        return number;
    }

    /**
     * @param change to be applied to the number of members of a population
     */
    public void changeNumber(int change) {
        if (this.getNumber() + change >= 0) {
            this.number += change;
        }
        else {
            this.number = 0;
        }
    }

    /**
     * @param needs to replace current list of needs of the population
     */
    public void setNeeds( ArrayList<ItemBatch> needs){
        this.needs = needs;
    }

    /**
     * @return list of needs of the population
     */
    public ArrayList<ItemBatch> getNeeds(){
        return needs;
    }

    /**
     * @param need to be added to the needs of the population
     */
    public void addNeed( ItemBatch need) {
        this.needs.add(need);
    }

    /**
     * @param productions to replace current list of productions of the population
     */
    public void setProductions( ArrayList<ItemBatch> productions) {
        this.productions = productions;
    }

    /**
     * @return list of productions of the population
     */
    public ArrayList<ItemBatch> getProductions() {
        return productions;
    }

    /**
     * @param production to be added to the population
     */
    public void addProduction( ItemBatch production) {
        this.productions.add(production);
    }

    /**
     * @param inventories to replace the current list of inventories of the population
     */
    public void setInventories( ArrayList<ItemBatch> inventories) {
        this.inventories = inventories;
    }

    /**
     * @return list of inventories of the settlement
     */
    public ArrayList<ItemBatch> getInventories() {
        return inventories;
    }

    /**
     * @param inventory to be added to population inventories
     */
    public void addInventory( ItemBatch inventory) {
        this.inventories.add(inventory);
    }
}
