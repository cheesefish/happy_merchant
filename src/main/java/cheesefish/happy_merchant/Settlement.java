
package cheesefish.happy_merchant;

/**
 * Settlement Objects fetched from world.json
 *
 * @author cheesefish
 * @version 1.0
 */

public class Settlement {

    private String name;
    private int population;
    private int area;

    /**
     * Constructor used when initializing Settlements
     *
     * @param name              name of the settlement
     * @param population        population of the settlement
     * @param area              area of the settlement
     */
    public Settlement(String name, int population, int area) {
        this.name = name;
        this.population = population;
        this.area = area;
    }

    /**
     * @return name of the settlement
     */
    public String getName() {
        return name;
    }

    /**
     * @param name of settlement. Must be a String.
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return population of the settlement
     */
    public int getPopulation() {
        return population;
    }

    /**
     * @param change in population for the settlement.
     *               Must be greater than inverse of current population.
     */
    public void changePopulation(int change) {
        this.population += change;
    }

    /**
     * @return area of the settlement
     */
    public int getArea() {
        return area;
    }
}