package cheesefish.happy_merchant;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashSet;

/**
 * JUnit test cases for JsonParser and related classes
 * Related classes include:
 * World.java
 * Settlement.java
 *
 * @author cheesefish
 * @version 2.1
 */
public class JsonParserTests {

    @Test
    public void JsonParser_readBasicWorldJson_returnPositionMapIDNameOfFirstSettlement() {
        String path = "src/test/resources/basicWorld.json";
        World world = JsonParser.parseWorld(path);

        double expectedXPosition = 1.1;
        double expectedYPosition = 1.1;
        int expectedMapID = 1;
        String expectedName = "town1";

        ArrayList<Settlement> settlements = world.getSettlements();

        Assert.assertEquals(expectedXPosition, settlements.get(0).getXPosition(), 0.01);
        Assert.assertEquals(expectedYPosition, settlements.get(0).getYPosition(), 0.01);
        Assert.assertEquals(expectedMapID, settlements.get(0).getMapID());
        Assert.assertEquals(expectedName, settlements.get(0).getName());
    }

    @Test
    public void JsonParser_checkIfItemTypesInSettlementsAreValid_returnTrue() {
        String path = "src/test/resources/basicWorld.json";
        World world = JsonParser.parseWorld(path);

        //Fetch names of itemTypes
        ArrayList<ItemType> itemTypes = world.getItemTypes();
        HashSet<String> itemTypeNames = new HashSet<>();
        for (int i = 0; i < itemTypes.size(); i++) {
            itemTypeNames.add(itemTypes.get(i).getName());
        }

        //Fetch settlements
        ArrayList<Settlement> settlements = world.getSettlements();

        //Fetch markets of all settlements
        ArrayList<Market> markets = new ArrayList<>();
        for (int i = 0; i < settlements.size(); i++) {
            markets.add(settlements.get(i).getMarket());
        }

        //Fetch supplies of all markets
        ArrayList<ItemBatch> supplies = new ArrayList<>();
        for (int i = 0; i < markets.size(); i++) {
            Market market = markets.get(i);
            for (int j = 0; j < market.getSupplies().size(); j++) {
                supplies.add(market.getSupplies().get(j));
            }
        }

        //Fetch names of itemTypes in supplies
        ArrayList<String> supplyNames = new ArrayList<>();
        for (int i = 0; i < supplies.size(); i++) {
            supplyNames.add(supplies.get(i).getName());
        }

        //Check names itemTypes in supplies against names of world itemTypes
        for (int i = 0; i < supplyNames.size(); i++) {
            Assert.assertTrue(itemTypeNames.contains(supplyNames.get(i)));
        }

        //Fetch populations of all settlements
        ArrayList<Population> populations = new ArrayList<>();
        ArrayList<ArrayList<Population>> populationsList= new ArrayList<>();
        for (int i = 0; i < settlements.size(); i++) {
            populationsList.add(settlements.get(i).getPopulations());
        }

        for (int i = 0; i < populationsList.size(); i++) {
            for (int j = 0; j < populationsList.get(i).size(); j++) {
                populations.add(populationsList.get(i).get(j));
            }
        }

        //Fetch needs of all populations
        ArrayList<ItemBatch> needs = new ArrayList<>();
        ArrayList<ItemBatch> productions = new ArrayList<>();
        ArrayList<ItemBatch> inventories = new ArrayList<>();
        for (int i = 0; i < populations.size(); i++) {
            Population population = populations.get(i);
            for (int j = 0; j < population.getNeeds().size(); j++) {
                needs.add(population.getNeeds().get(j));
            }
            for (int j = 0; j < population.getProductions().size(); j++){
                productions.add(population.getProductions().get(j));
            }
            for (int j = 0; j < population.getInventories().size(); j++){
                inventories.add(population.getInventories().get(j));
            }
        }

        //Fetch names of itemTypes in needs
        ArrayList<String> needNames = new ArrayList<>();
        for (int i = 0; i < needs.size(); i++) {
            needNames.add(needs.get(i).getName());
        }

        //Check names of itemTypes in needs against names of world itemTypes
        for (int i = 0; i < needNames.size(); i++) {
            Assert.assertTrue(itemTypeNames.contains(needNames.get(i)));
        }

        //Fetch names of itemTypes in productions
        ArrayList<String> productionNames = new ArrayList<>();
        for (int i = 0; i < productions.size(); i++) {
            productionNames.add(productions.get(i).getName());
        }

        //Check names of itemTypes in productions against names of world itemTypes
        for (int i = 0; i < productionNames.size(); i++) {
            Assert.assertTrue(itemTypeNames.contains(productionNames.get(i)));
        }

        //Fetch names of itemTypes in inventories
        ArrayList<String> inventoryNames = new ArrayList<>();
        for (int i = 0; i < inventories.size(); i++) {
            inventoryNames.add(inventories.get(i).getName());
        }
        //Check names of itemTypes in inventories against names of world itemTypes
        for (int i = 0; i < inventoryNames.size(); i++) {
            Assert.assertTrue(itemTypeNames.contains(inventoryNames.get(i)));
        }

    }
}
