using UnityEngine;
using UnityEngine.UI;

public class MusicLearningApp : MonoBehaviour
{
    public Text instructionText;
    public Button nextButton;
    private int currentLesson = 0;
    private MusicLesson[] lessons;

    void Start()
    {
        // Initialize your music lessons here
        lessons = new MusicLesson[] {
            new MusicLesson("C Major Scale", "Play the notes C-D-E-F-G-A-B-C"),
            // Add more lessons
        };
        UpdateLesson();
    }

    void UpdateLesson()
    {
        instructionText.text = lessons[currentLesson].instruction;
        nextButton.onClick.AddListener(NextLesson);
    }

    void NextLesson()
    {
        currentLesson++;
        if (currentLesson < lessons.Length)
        {
            UpdateLesson();
        }
        else
        {
            // End of lessons
        }
    }
}

public class MusicLesson
{
    public string title;
    public string instruction;

    public MusicLesson(string title, string instruction)
    {
        this.title = title;
        this.instruction = instruction;
    }
}