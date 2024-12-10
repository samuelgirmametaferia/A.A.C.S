import java.util.ArrayList;
import java.util.List;

public class StudyPlanner {

  public static void main(String[] args) {
    List<Task> tasks = new ArrayList<>();
    tasks.add(new Task("Math", 2));
    tasks.add(new Task("Physics", 3));
    tasks.add(new Task("Chemistry", 2));
    tasks.add(new Task("History", 1));

    List<Task> optimizedSchedule = optimizeSchedule(tasks);
    System.out.println("Optimized Study Schedule:");
    for (Task task : optimizedSchedule) {
      System.out.println(task.name + " - " + task.duration + " hours");
    }
  }

  static class Task {
    String name;
    int duration;

    public Task(String name, int duration) {
      this.name = name;
      this.duration = duration;
    }
  }

  public static List<Task> optimizeSchedule(List<Task> tasks) {
    // Implement A* pathfinding algorithm here
    // ...
    return tasks;
  }
}