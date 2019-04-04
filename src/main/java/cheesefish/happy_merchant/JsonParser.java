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
 * @version 2.2
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
            ArrayList<ItemBatch> supplies = pairItemTypes(suppliesArray, worldItemTypes);

            Market market = new Market(supplies);

            JsonArray populationArray = current.getJsonArray("populations");
            ArrayList<Population> populations = new ArrayList<>();
            for (int j = 0; j < populationArray.size(); j++) {
                JsonObject populationObject = populationArray.getJsonObject(j);
                String populationName = populationObject.getString("name");
                int populationNumber = populationObject.getInt("number");

                JsonArray needsArray = populationObject.getJsonArray("needs");
                ArrayList<ItemBatch> needs = pairItemTypes(needsArray, worldItemTypes);

                JsonArray productionsArray = populationObject.getJsonArray("production");
                ArrayList<ItemBatch> productions = pairItemTypes(productionsArray, worldItemTypes);

                JsonArray inventoriesArray = populationObject.getJsonArray("inventory");
                ArrayList<ItemBatch> inventories = pairItemTypes(inventoriesArray, worldItemTypes);

                Population population = new Population(populationName, populationNumber, needs, productions, inventories);
                populations.add(population);
            }

            Settlement settlement = new Settlement(
                    xPosition, yPosition, mapID, neighbors, name, market, populations, area);

            world.addSettlement(settlement);
        }

        return world;

    }

    /**
     * Reads the JsonArrays fetched in parseWorld and checks the names of the items
     * and the adds to weight, volume and category of all the items.
     * Thus making sure that all items of the same type have the same
     * weight, volume and category.
     *
     * @param array of jsonobjects which are the names and amounts of items.
     * @param worldItemTypes List of available item types in the world
     * @return an arraylist of itembatches
     */
    public static ArrayList<ItemBatch> pairItemTypes(JsonArray array, ArrayList<ItemType> worldItemTypes) {
        ArrayList<ItemBatch> itemBatches = new ArrayList<>();

        for(int j = 0; j < array.size(); j++) {

            JsonObject object = array.getJsonObject(j);
            String itemName = object.getString("name");
            int itemAmount = object.getInt("amount");

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

            ItemBatch itemBatch = new ItemBatch(itemName, itemCategory, itemVolume, itemWeight, itemAmount);
            itemBatches.add(itemBatch);
        }

        return itemBatches;
    }
}