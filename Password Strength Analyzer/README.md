# 🔐 Password Strength Analyzer and Custom Wordlist Generator (GUI)

---

## 🎯 Overview:

The Password Strength Analyzer and Custom Wordlist Generator is a Python-based desktop application built with Tkinter for the GUI and zxcvbn for advanced password analysis.

---

## 🛠 This tool serves two primary functions:

Analyze Password Strength: Provides a detailed, modern analysis (0-4 score) of a password's security, including estimated crack time and specific suggestions.
Generate Targeted Wordlists: Creates highly specific, context-aware wordlists based on personal inputs (Name, Date, Pet) with common permutations (leetspeak, date formats, year appending). This is useful for security testing, auditing, or understanding how easily personal information can lead to guessed passwords.

---

##🚀 Features: 

GUI Interface: Easy-to-use tabbed interface built with Tkinter.
Modern Strength Analysis: Uses the powerful zxcvbn library (developed by Dropbox) for entropy calculation and pattern matching.
Contextual Analysis: Allows input of personal details (user inputs) to see how easily a password can be guessed if the attacker has that context.
Custom Wordlist Generation: Takes user inputs (name, date, pet) and generates a large dictionary of high-probability passwords.
Pattern Generation: Automatically includes:
Case variations (e.g., John, john, JOHN).
Leetspeak substitutions (e.g., s -> 5, e -> 3).
Common date and year formats (e.g., MMDD, DDMMYY, YYYY).
Year appending for a configurable range (e.g., password2023).
Export: Exports the generated wordlist directly to a .txt file.

---

## 🖥️ Installation and Setup:

###Prerequisites:
You need Python installed on your system (Python 3.6+ is recommended).

### Steps:

    Clone the Repository:
    Bash
    git clone [YOUR_REPO_URL]
    cd [YOUR_REPO_NAME]
    
Install Dependencies: The core functionality relies on zxcvbn. Tkinter is usually included with standard Python installations.

    Bash
    pip install zxcvbn
    Run the GUI Application:
    Bash
    python pass_tool_gui.py

---

## 📚 Usage Guide:

### The tool opens a window with two main tabs:

1.	Password Analysis Tab
This tab evaluates the strength of a specific password.
Enter the password in the Enter Password field. Use the Show checkbox to toggle visibility.
Optionally, enter known personal information (like the user's name or birthdate) in the User Inputs field. This helps zxcvbn accurately gauge security risk against social engineering attacks.
Click Analyze Password.
The results section will display the Score (0-4), Estimated Crack Time, and Feedback/Suggestions.

2.	Wordlist Generation Tab
This tab creates a highly targeted dictionary file.
Input Personal Details: Fill in the Target Name, Date (YYYY-MM-DD), and Pet Name fields. At least one field is required.
Set Years Back to Append: Define the range of recent years (plus the next two) to append to base words (default is 10 years).
Select Output File: Use the Browse button to choose the name and location for the output .txt file.
Click Generate Wordlist & Export.
The Generation Report will confirm the save location and the total number of unique words generated.

---
