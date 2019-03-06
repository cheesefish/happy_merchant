package cheesefish.happy_merchant;

import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;

public class JsonParserTests {

    @Test
    public void JsonParser_readBasicJson_returnNamePopulationAreaOfFirstSettlement() {

        String path = "src/test/resources/basicWorld.json";

        String expectedName = "Town1";
        int expectedPopulation = 1000;
        int expectedArea = 1000;

        World world = JsonParser.parseJson(path);
        ArrayList<Settlement> settlements = world.getSettlements();

        Assert.assertEquals(expectedName, settlements.get(0).getName());
        Assert.assertEquals(expectedPopulation, settlements.get(0).getPopulation());
        Assert.assertEquals(expectedArea, settlements.get(0).getArea());
    }
}
