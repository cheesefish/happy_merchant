package cheesefish.happy_merchant;

import java.util.ArrayList;

public class World {

    private ArrayList<Settlement> settlements;

    public World() {
        settlements = new ArrayList<>();
    }

    public void setSettlements(ArrayList<Settlement> settlements) {
        this.settlements = settlements;
    }

    public ArrayList<Settlement> getSettlements() {
        return settlements;
    }

    public void addSettlement(Settlement settlement) {
        settlements.add(settlement);
    }

    public int settlementAmount() {
        return settlements.size();
    }
}