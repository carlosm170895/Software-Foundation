# CSV Data Processing Program

This is a simple Python project that reads user data (Name, Age, Height in meters) from a CSV file, performs basic calculations, and outputs the results to another CSV file. It demonstrates basic data processing, file handling, and formatted string output using standard Python libraries.

##  Project Structure

```
data-processing-project/
├── input.csv             # Input data with Name, Age, Height
├── output.csv            # Generated output with processed results
├── process_data.py       # Main Python script
└── run_process.sh        # Optional: Shell script for Linux/macOS users
```

##  How to Run

### In Visual Studio Code (VS Code)
1. Open the folder in VS Code.
2. Open a terminal (`Ctrl + backtick`).
3. Run:
   ```bash
   python process_data.py input.csv
   ```

### From Command Line (Windows CMD or PowerShell)
1. Open the terminal and navigate to the folder:
   ```bash
   cd path\to\project
   ```
2. Run:
   ```bash
   python process_data.py input.csv
   ```

##  What It Does
For each person in the CSV:
- Calculates their age 10 years in the future.
- Converts their height to centimeters.
- Generates a greeting with both current and future values.

##  Example Output (output.csv)
```
Name,Age,Future Age,Height (m),Height (cm),Greeting
Alice,30,40,1.65,165.0,"Hello, Alice! You are 30 years old and 1.65 m tall. In 10 years, you'll be 40 years old and 165.0 cm tall."
...
```

##  License
This project is open-source and free to use under the MIT License.
