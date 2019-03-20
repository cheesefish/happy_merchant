package cheesefish.happy_merchant;

import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.json.JsonReader;

import java.io.*;
import java.util.ArrayList;

import static javax.json.Json.createReader;

/**
 * Parses Json files to be used in the game
 * Should be used when starting the game only once
 * Or when loading a saved world file
 *
 * Currently only parses items and settlements into world object.
 *
 * @author cheesefish
 * @version 2.1
 */
public class JsonParser {

    /**
     * Reads object list in world.json
     * Creates a World object.
     *
     * @param path to world.json file
     * @return world object parsed from world.json
     */
    public static World parseWorld(String path) {

        File inputFile = new File(path);
        InputStream is;
        JsonObject worldObject;

        World world = new World();

        try {
            is = new FileInputStream(inputFile);
            JsonReader reader = createReader(is);
            worldObject = reader.readObject();
            reader.close();
        }
        catch(FileNotFoundException e) {
            return null;
        }

        //Add all items to World Object
        JsonArray itemTypesArray = worldObject.getJsonArray("itemTypes");
        ArrayList<ItemType> worldItemTypes = new ArrayList<>();
        for(int i = 0; i < itemTypesArray.size(); i++) {
            JsonObject current = itemTypesArray.getJsonObject(i);
            String name = current.getString("name");
            String category = current.getString("category");
            int volume = current.getInt("volume");
            int weight = current.getInt("weight");

            ItemType itemType = new ItemType(name, category, volume, weight);

            worldItemTypes.add(itemType);
        }

        world.setItemTypes(worldItemTypes);

        //Add all settlements to World Object
        JsonArray settlementsArrayObject = worldObject.getJsonArray("settlements");
        for(int i = 0; i < settlementsArrayObject.size(); i++) {
            JsonObject current = settlementsArrayObject.getJsonObject(i);

            double xPosition = current.getJsonNumber("xPosition").doubleValue();
            double yPosition = current.getJsonNumber("yPosition").doubleValue();
            int mapID = current.getInt("mapID");
            int area = current.getInt("area");

            JsonArray JsonNeighbors = current.getJsonArray("neighbors");
            ArrayList<Integer> neighbors = new ArrayList<>();
            for(int j = 0; j < JsonNeighbors.size(); j++) {
                neighbors.add(JsonNeighbors.getInt(j));
            }
            String name = current.getString("name");

            JsonObject marketObject = current.getJsonObject("market");
            JsonArray suppliesArray = marketObject.getJsonArray("supplies");
            ArrayList<ItemBatch> supplies = new ArrayList<>();

            for(int j = 0; j < suppliesArray.size(); j++) {

                JsonObject supplyObject = suppliesArray.getJsonObject(j);
                String itemName = supplyObject.getString("name");
                int itemAmount = supplyObject.getInt("amount");

                String itemCategory = "";
                int itemVolume = 0;
                int itemWeight = 0;

                for(ItemType itemType : worldItemTypes) {
                    if(itemType.getName() == itemName) {
                        itemCategory = itemType.getCategory();
                        itemVolume = itemType.getVolume();
                        itemWeight = itemType.getWeight();
                    }
                }

                ItemBatch supply = new ItemBatch(itemName, itemCategory, itemVolume, itemWeight, itemAmount);
                supplies.add(supply);
            }

            Market market = new Market(supplies);

            JsonArray populationArray = current.getJsonArray("populations");
            ArrayList<Population> populations = new ArrayList<>();
            for (int j = 0; j < populationArray.size(); j++) {
                JsonObject populationObject = populationArray.getJsonObject(j);
                String populationName = populationObject.getString("name");
                int populationNumber = populationObject.getInt("number");

                JsonArray needsArray = populationObject.getJsonArray("needs");
                ArrayList<ItemBatch> needs = new ArrayList<>();
                for (int k = 0; k < needsArray.size(); k++) {
                    JsonObject needObject = needsArray.getJsonObject(k);
                    String itemName = needObject.getString("name");
                    int itemAmount = needObject.getInt("amount");

                    String itemCategory = "";
                    int itemVolume = 0;
                    int itemWeight = 0;

                    for(ItemType itemType : worldItemTypes) {
                        if(itemType.getName() == itemName) {
                            itemCategory = itemType.getCategory();
                            itemVolume = itemType.getVolume();
                            itemWeight = itemType.getWeight();
                        }
                    }

                    ItemBatch need = new ItemBatch(itemName, itemCategory, itemVolume, itemWeight, itemAmount);
                    needs.add(need);
                }

                JsonArray productionsArray = populationObject.getJsonArray("production");
                ArrayList<ItemBatch> productions = new ArrayList<>();
                for (int k = 0; k < productionsArray.size(); k++) {
                    JsonObject productionObject = productionsArray.getJsonObject(k);
                    String itemName = productionObject.getString("name");
                    int itemAmount = productionObject.getInt("amount");

                    String itemCategory = "";
                    int itemVolume = 0;
                    int itemWeight = 0;

                    for(ItemType itemType : worldItemTypes) {
                        if(itemType.getName() == itemName) {
                            itemCategory = itemType.getCategory();
                            itemVolume = itemType.getVolume();
                            itemWeight = itemType.getWeight();
                        }
                    }

                    ItemBatch production = new ItemBatch(itemName, itemCategory, itemVolume, itemWeight, itemAmount);
                    productions.add(production);
                }

                JsonArray inventoriesArray = populationObject.getJsonArray("inventory");
                ArrayList<ItemBatch> inventories = new ArrayList<>();
                for (int k = 0; k < inventoriesArray.size(); k++) {
                    JsonObject inventoryObject = inventoriesArray.getJsonObject(k);
                    String itemName = inventoryObject.getString("name");
                    int itemAmount = inventoryObject.getInt("amount");

                    String itemCategory = "";
                    int itemVolume = 0;
                    int itemWeight = 0;

                    for(ItemType itemType : worldItemTypes) {
                        if(itemType.getName() == itemName) {
                            itemCategory = itemType.getCategory();
                            itemVolume = itemType.getVolume();
                            itemWeight = itemType.getWeight();
                        }
                    }

                    ItemBatch inventory = new ItemBatch(itemName, itemCategory, itemVolume, itemWeight, itemAmount);
                    inventories.add(inventory);
                }

                Population population = new Population(populationName, populationNumber, needs, productions, inventories);
                populations.add(population);
            }

            Settlement settlement = new Settlement(
                    xPosition, yPosition, mapID, neighbors, name, market, populations, area);

            world.addSettlement(settlement);
        }

        return world;

    }
}