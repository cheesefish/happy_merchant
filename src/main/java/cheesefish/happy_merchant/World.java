package cheesefish.happy_merchant;

import java.util.ArrayList;


/**
 * World objects fetched from world.json file
 * At this point only features settlements
 *
 * @author cheesefish
 * @version 1.1
 */
public class World {

    public ArrayList<ItemType> itemTypes;
    public ArrayList<Settlement> settlements;

    /**
     * Basis of world object to which things are added in the JsonParser
     */
    public World() {
        settlements = new ArrayList<>();
    }

    /**
     * @param settlements of the world.
     *                    Replaces current list of settlements
     */
    public void setSettlements(ArrayList<Settlement> settlements) {
        this.settlements = settlements;
    }

    /**
     * @return full list of settlements in world object
     */
    public ArrayList<Settlement> getSettlements() {
        return settlements;
    }

    /**
     * @param settlement to be added to world object
     */
    public void addSettlement(Settlement settlement) {
        settlements.add(settlement);
    }

    /**
     * @return total number or settlements in the world object
     */
    public int settlementAmount() {
        return settlements.size();
    }

    public void setItemTypes(ArrayList<ItemType> itemTypes) {
        this.itemTypes = itemTypes;
    }

    public ArrayList<ItemType> getItemTypes() {
        return itemTypes;
    }

    public void addItemType(ItemType itemType) {
        this.itemTypes.add(itemType);
    }
}