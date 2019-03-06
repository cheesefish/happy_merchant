package cheesefish.happy_merchant;

public class Settlement {

    private String name;
    private int population;
    private int area;

    public Settlement(String name, int population, int area) {
        this.name = name;
        this.population = population;
        this.area = area;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPopulation() {
        return population;
    }

    public void changePopulation(int change) {
        this.population += change;
    }

    public int getArea() {
        return area;
    }
}