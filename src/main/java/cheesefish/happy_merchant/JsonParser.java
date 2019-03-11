package cheesefish.happy_merchant;

import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.json.JsonReader;

import java.io.*;

import static javax.json.Json.createReader;

/**
 * Parses Json files to be used in the game
 * Currently only parses settlements into world object.
 *
 * @author cheesefish
 * @version 1.0
 */
public class JsonParser {

    /**
     * Reads settlement list in world.json
     * Creates a World object.
     *
     * @param path to world.json file
     * @return world object parsed from world.json
     */
    public static World parseJson(String path) {

        File inputFile = new File(path);
        InputStream is;

        World world = new World();

        try {
            is = new FileInputStream(inputFile);
            JsonReader reader = createReader(is);
            JsonObject worldObject = reader.readObject();
            reader.close();
            JsonArray arrayObject = worldObject.getJsonArray("settlements");
            for(int i = 0; i < arrayObject.size(); i++) {
                String name = arrayObject.getJsonObject(i).getString("name");
                int population = arrayObject.getJsonObject(i).getInt("population");
                int area = arrayObject.getJsonObject(i).getInt("area");

                Settlement settlement = new Settlement(name, population, area);

                world.addSettlement(settlement);
            }

        }
        catch(FileNotFoundException e) {
            return null;
        }

        return world;

    }
}