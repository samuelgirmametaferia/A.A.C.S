import java.util.Random;

public class VirtualPet {
  private String name;
  private int hunger;
  private int happiness;
  private State currentState;

  public enum State {
    SLEEPING,
    PLAYING,
    EATING
  }

  public VirtualPet(String name) {
    this.name = name;
    this.hunger = 5;
    this.happiness = 5;
    this.currentState = State.SLEEPING;
  }

  public void update() {
    Random random = new Random();
    switch (currentState) {
      case SLEEPING:
        if (random.nextInt(10) == 0) {
          currentState = State.PLAYING;
        }
        break;
      case PLAYING:
        happiness++;
        if (random.nextInt(10) == 0) {
          currentState = State.EATING;
        }
        break;
      case EATING:
        hunger--;
        if (random.nextInt(10) == 0) {
          currentState = State.SLEEPING;
        }
        break;
    }
    if (hunger <= 0) {
      currentState = State.SLEEPING;
    }
    if (happiness >= 10) {
      currentState = State.PLAYING;
    }
  }

  public void feed() {
    hunger = 10;
    currentState = State.EATING;
  }

  public void play() {
    happiness = 10;
    currentState = State.PLAYING;
  }

  public String getName() {
    return name;
  }

  public int getHunger() {
    return hunger;
  }

  public int getHappiness() {
    return happiness;
  }

  public State getCurrentState() {
    return currentState;
  }
}