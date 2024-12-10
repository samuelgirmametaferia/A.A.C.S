import java.util.Timer;
import java.util.TimerTask;

public class PomodoroTimer {
  private static final int WORK_TIME = 25 * 60; // 25 minutes
  private static final int BREAK_TIME = 5 * 60; // 5 minutes

  private Timer timer;
  private int remainingTime;

  public void start() {
    timer = new Timer();
    remainingTime = WORK_TIME;
    timer.scheduleAtFixedRate(new TimerTask() {
      @Override
      public void run() {
        // ... (Update timer and handle work/break intervals)
      }
    }, 0, 1000);
  }

  public void stop() {
    timer.cancel();
  }
}