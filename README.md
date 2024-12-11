### README for Project
A.A.C.S(Automatic Application Creation System) is a LLM powered program creation system.

#### Overview
This project utilizes a Groq API for generating programming ideas and automating the creation of project files based on those ideas. The program allows the user to:
1. Generate programming ideas from a creative prompt.
2. Create a project structure based on those ideas.
3. Set up and maintain configuration files to manage project data.

#### Dependencies
- **Groq API**: Used to generate ideas and project structures. You will need a Groq API key to use this functionality.

#### Getting a Groq API Key

To use the Groq API, follow these steps:
1. **Create an Account**: Go to [Groq's website](https://www.groq.com/) and sign up for an account.
2. **Obtain the API Key**: After signing up and logging in, you should be able to access the API key from your account dashboard. This key is required to make requests to the Groq API.
3. **Set the API Key in the Code**: Once you have your API key, replace the existing key in the code:
   ```csharp
   var apiKey = "ApiKey";
   ```
   with your own Groq API key.

#### Key Features
- **Idea Generation**: The `Idea` function queries the Groq API to generate a new project idea based on a creative programming prompt.
- **Code Structure Creation**: The `CreateStructure` function takes the generated idea and creates a corresponding code structure. This includes generating code files and saving them in a designated project folder.
- **Project Setup and State Management**: The project setup involves checking for existing folders and creating configuration files that track project states and directories.
- **File Management**: The program automatically creates necessary project files and directories, ensuring that all required files are set up for each project.

#### How to Use
1. **Install Dependencies**:
   - Ensure that the necessary libraries and packages are installed. This project uses `System.IO` for file operations, `GroqApiLibrary` for interacting with the Groq API, and other basic .NET libraries.
   
2. **Run the Program**:
   - The program will prompt you to enter the number of ideas you wish to generate.
   - After generating the ideas, the program will create corresponding project files and directories for each idea.
   
3. **Project Files**:
   - The program will save generated project files in the `Data` directory, with a subfolder for each project.
   - Each project will contain code files as well as a `progress.state` file to track the project's state.

4. **Configuration Management**:
   - The program checks and regenerates configuration files to ensure consistency between the number of projects and their respective states.
5. **Example Projects**:
   - In the data folder of the program, there are several projects that you can inspect.

#### Error Handling
The program includes basic error handling for issues such as missing state files or data mismatches. It will prompt you with error messages and guide you through resolving them.

#### Future Enhancements In development
Uploading Projects Directly to Github with AI generated readme files.(I had to create this repository on my own.)

#### License
This project is licensed under a custom license. See LICENSE for more details.
