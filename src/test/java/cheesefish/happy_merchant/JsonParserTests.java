package cheesefish.happy_merchant;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

/**
 * JUnit test cases for JsonParser and related classes
 * Related classes include:
 * World.java
 * Settlement.java
 *
 * @author cheesefish
 * @version 2.0
 */
public class JsonParserTests {

    @Test
    public void JsonParser_readBasicWorldJson_returnPositionMapIDNameOfFirstSettlement() {

        String path = "src/test/resources/basicWorld.json";

        double expectedXPosition = 1.1;
        double expectedYPosition = 1.1;
        int expectedMapID = 1;
        String expectedName = "town1";

        World world = JsonParser.parseWorld(path);

        ArrayList<Settlement> settlements = world.getSettlements();

        Assert.assertEquals(expectedXPosition, settlements.get(0).getXPosition(), 0.01);
        Assert.assertEquals(expectedYPosition, settlements.get(0).getYPosition(), 0.01);
        Assert.assertEquals(expectedMapID, settlements.get(0).getMapID());
        Assert.assertEquals(expectedName, settlements.get(0).getName());
    }
}
