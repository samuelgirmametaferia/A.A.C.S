import java.util.Scanner;

public class Storybook {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Welcome to the Interactive Storybook!");
    System.out.println("You find yourself at a crossroads.");
    System.out.println("Do you go left or right? (left/right)");
    String choice = scanner.nextLine();
    if (choice.equals("left")) {
      System.out.println("You encounter a friendly dragon.");
      // ... (Continue the story based on the left choice)
    } else if (choice.equals("right")) {
      System.out.println("You stumble upon a hidden treasure chest.");
      // ... (Continue the story based on the right choice)
    } else {
      System.out.println("Invalid choice. Please try again.");
    }
  }
}