using System;
using System.Diagnostics;
using System.IO;
using System.Collections.Generic;
using GroqApiLibrary;
using System.Text.Json.Nodes;
using System.Text;
using System.Security.Principal;

class Config
{
    public List<string> _Paths { get; set; }
    public List<bool> _States { get; set; }
    public Config(List<string> Paths, List<bool> States)
    {
        _Paths = Paths;
        _States = States;
    }
}
public class Program
{
    public static string DataFolder = "Data";
    public static string ConfigFileName = "Data";
    public static void Error(string _in)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine(_in);
        Console.ResetColor(); // Reset to default
    }

    public static void Important(string _in)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(_in);
        Console.ResetColor(); // Reset to default
    }

    public static int SetupDataStructure()
    {
        if (Directory.Exists(DataFolder))
        {
            string[] Directories = Directory.GetDirectories(DataFolder);
            return Directories.Length;
        }
        else
        {

            Directory.CreateDirectory(DataFolder);
            Important("Successfully Created Folder");
            return -1;
        }
    }
    public static void GenerateConfig()
    {
        string[] Directories = Directory.GetDirectories(DataFolder);

        if (!File.Exists($"{ConfigFileName}.config"))
        {
            using (File.Create($"{ConfigFileName}.config")) { }
        }
        int nopwsf = 0;

        using (StreamWriter writer = new StreamWriter($"{ConfigFileName}.config"))
        {
            for (int i = 0; i < Directories.Length + 1; i++)
            {
                if (i == 0)
                {
                    writer.WriteLine($"{Directories.Length}");
                }
                else
                {
                    writer.WriteLine($"{Directories[i - 1]}");
                    if (File.Exists($"./{Directories[i - 1]}/progress.state"))
                    {
                        string state = File.ReadAllText($"./{Directories[i - 1]}/progress.state");
                        writer.WriteLine(state);
                    }
                    else
                    {
                        Error($"Project {Directories[i - 1]} doesn't have a state.");
                        Error("You should manually create the state file.");
                        writer.WriteLine("%m%");
                        nopwsf++;
                    }
                }
            }
        }
        if (nopwsf > 0)
        {
            if (nopwsf > 1)
            {
                Error($"{nopwsf} projects don't have states files.");
            }
            else
            {
                Error($"{nopwsf} project doesn't have a state file.");
            }

        }
        else
        {
            Important("Config file is proper.");
        }
    }
    public static void SetupConfig(int state)
    {
        if (File.Exists($"{ConfigFileName}.config"))
        {
            if (state >= 0)
            {
                using (StreamReader reader = new StreamReader($"{ConfigFileName}.config"))
                {
                    string line;
                    if ((line = reader.ReadLine()) != null)
                    {
                        try
                        {
                            int nol = int.Parse(line);
                            if (nol == state)
                            {
                                Important("Successfully Analyized the number of project.");
                                Important($"The number of projects is {nol} = {state}");

                            }
                            else
                            {
                                if (nol > state)
                                {
                                    Error("Data mismatch.");
                                    Error("Some projects are missing.");
                                    Error("Regenerating config file.");

                                }
                                else
                                {
                                    Error("Data mismatch!");
                                    Error("This might be a sign of other issues!");
                                    Important("Regenerating config to account for new projects");


                                }
                            }
                        }
                        catch (Exception e)
                        {
                            Error("Failed to parse the number of directories. ");
                            Error("Regenerating config file");
                            Error($"C# Error is -> {e.Message}");
                        }

                    }
                }
            }
            else
            {
                Important("Generating Config!");
            }
        }
        else
        {
            Important("Generating Config!");
        }
        GenerateConfig();
    }
    public static async Task<string> Talk(string _prompt, double temperature = 0.7)
    {
        var apiKey = "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";
        var groqApi = new GroqApiClient(apiKey);

        // Constructing the request payload
        var request = new JsonObject
        {
            ["model"] = "gemma2-9b-it",
            ["temperature"] = temperature,
            ["messages"] = new JsonArray
        {
            new JsonObject
            {
                ["role"] = "system",
                ["content"] = _prompt // Use the parameter here
            }
        }
        };

        try
        {
            // Await the async API call
            var result = await groqApi.CreateChatCompletionAsync(request);

            // Parse the response
            var content = result?["choices"]?[0]?["message"]?["content"]?.ToString();
            return content ?? "No response received from the API.";
        }
        catch (Exception ex)
        {
            return $"An error occurred: {ex.Message}";
        }
    }

    public static async Task<string> Idea()
    {
        string format = "*%*Idea"
        + "How it is going to be implemented."
        + "Programming Languages that are going to be used. %*%";

        string example = "*%* Text to voice app for mute people."
        + "\nUsing C# System.Speech"
        + "\n C#";

        string prompt = "Your role is that of a creative programming director!"
        + "You decide what ideas for projects are going to be."
        + "You must only respond with feasible ideas."
        + "Generate an idea for an application, from simple AI tools to A* implementations. Go crazy with your ideas, you are free!"
        + "Format each idea like this:"
        + format
        + "Here is an example of a proper idea:"
        + example
        + "Strictly avoid any explanation, remarks, or commentary."
        + "Tame yourself make the projects possible for a langauge model of your level.";

        string response = await Talk(prompt, temperature: 1);
        return response;
    }

    public static async Task<string> CreateStructure(string idea)
    {

        string format = "\"<filename>.<extension>\"\n\"%*%\"\n\"<code content with \\n for line breaks>\"\n\"%*%\"";
        string prompt = "Implement this project idea:\n\"" + idea + "\"\n" +
                        "Your job is to output code only. Follow this format:\n" + format +
                        "\n\nRules:\n" +
                        "1. No comments or explanations.\n" +
                        "2. Use \\n for line breaks and wrap everything in double quotes.\n" +
                        "3. For multiple files, repeat the format." +
                        "4. No quotes it messes with my parser." +
                        "5. Please never no comments or explanations do as told." +
                        "6. Even though you have been told by before to wrap your code in ``` and then the language. I don't want that because this is an api so please don't do any of that. Good girl!" +
                        "7. I am going to be honest, I don't know shit about programming so don't leave anything for me to do. Please make it so I can copy and then paste then it works." +
                        "8. Write a lot of code, so people on github look at me as smart."+
                        "9. Don't ever // ... (Move task between lists logic) actually code it.";
        string response = await Talk(prompt, temperature: 0.2);
        return response;
    }
    static List<(string fileName, string code)> ParseFiles(string inputText)
    {
        var files = new List<(string fileName, string code)>();
        string[] sections = inputText.Split(new[] { "\"%*%\"" }, StringSplitOptions.None);

        for (int i = 0; i < sections.Length - 1; i += 2)
        {
            string fileName = sections[i].Trim().Trim('"');
            string code = sections[i + 1].Trim();
            files.Add((fileName, code));
        }

        return files;
    }

    public static string RemoveLine(string input, int lineToRemove)
    {
        // Split the string into lines
        var lines = input.Split(new[] { "\r\n", "\n" }, StringSplitOptions.None);

        // Ensure the line index is valid
        if (lineToRemove < 0 || lineToRemove >= lines.Length)
            throw new ArgumentOutOfRangeException(nameof(lineToRemove), "Invalid line number");

        // Remove the specified line and join the remaining lines
        return string.Join("\n", lines.Where((line, index) => index != lineToRemove));
    }
    public static string RemoveLastLine(string input)
    {
        // Split the string into lines
        var lines = input.Split(new[] { "\r\n", "\n" }, StringSplitOptions.None);

        // If there are no lines, return an empty string
        if (lines.Length == 0)
            return string.Empty;

        // Remove the last line and join the remaining lines
        return string.Join("\n", lines.Take(lines.Length - 1));
    }
    public static string RemoveBlockMarkers(string _in)
    {
        string nT = _in;
        if (_in.StartsWith("```"))
        {
            nT = RemoveLine(nT, 0);
            nT = RemoveLine(nT, 0);
            nT = RemoveLastLine(nT);
        }
        return nT;
    }
    public static void CreateFile(string filePath, string content = "")
    {
        try
        {
            // Get the directory from the file path
            string directoryPath = Path.GetDirectoryName(filePath);

            // Check if the directory exists, create it if it doesn't
            if (!Directory.Exists(directoryPath))
            {
                Directory.CreateDirectory(directoryPath);
            }

            // Create or overwrite the file with the given content
            File.WriteAllText(filePath, content);

            Console.WriteLine($"File created successfully at: {filePath}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    public static string FirstCharToUpper(string input)
    {
        if (String.IsNullOrEmpty(input))
            throw new ArgumentException("ARGH!");
        return input.First().ToString().ToUpper() + String.Join("", input.Skip(1));
    }

    public static string CreateProject(string code_uparsed)
    {
        var ParsedFiles = ParseFiles(code_uparsed);
        string folderName = "!?";
        if (ParsedFiles.Count > 0)
        {
            try
            {
                folderName = ParsedFiles[0].fileName.Split(".")[0];
            }
            catch (Exception e)
            {
                Random rand = new Random();
                folderName = $"project-{rand.Next() * 100}";
            }
            string ProjectPath = $"{DataFolder}/{FirstCharToUpper(folderName)}";
            Directory.CreateDirectory(ProjectPath);
            foreach (var file in ParsedFiles)
            {
                Console.WriteLine(file.fileName);
                Console.WriteLine(file.code);
                string code = RemoveBlockMarkers(file.code);
                string FileName = file.fileName.Replace("*", "");
                CreateFile($"{ProjectPath}/{FileName}", code);
            }
            File.WriteAllText($"{ProjectPath}/progress.state", "%H%");
        }

        return folderName;
    }

    public static async Task Main()
    {

        List<string> Ideas = new List<string>();
        Important("Initializing Systems");
        int state = SetupDataStructure();
        SetupConfig(state);
        Console.Write("Enter the number of ideas to generate: ");
        int numIdeas = int.Parse(Console.ReadLine());
        for (int i = 0; i < numIdeas; i++)
        {
            string idea = await Idea();
            Ideas.Add(idea);
        }
        Console.WriteLine("Generated Ideas:");
        foreach (var Idea in Ideas)
        {
            if (!string.IsNullOrWhiteSpace(Idea))
            {
                Console.WriteLine(Idea);
            }
        }

        Important("Generating Ideas");
        for (int i = 0; i < Ideas.Count; i++)
        {
            Console.WriteLine($"\n idea number {i}! ");
            string folderName = "!?";
            int j = 0;
            while (folderName == "!?")
            {
                if (j == 0)
                {

                    string structure = await CreateStructure(Ideas[i]);
                    folderName = CreateProject(structure);

                }
                else
                {
                    string structure = await CreateStructure(await Idea());
                    folderName = CreateProject(structure);
                }
                j++;
                if(j>10)
                {break;}
            }
            Console.WriteLine("The name of the project is -> " + folderName);

        }
        GenerateConfig();
    }

}
