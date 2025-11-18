# 🛡️ CYBER-SECURITY-PROJECTS Overview

This repository hosts a collection of Python-based desktop applications designed for educational and practical demonstrations of fundamental cyber security concepts. The tools use **Tkinter** for an intuitive Graphical User Interface (GUI) and leverage specialized libraries to perform advanced analysis and data manipulation. 
---

## 📝 Project Summary

The repository currently contains two primary tools: a **Password Strength Analyzer and Custom Wordlist Generator** and a **Steganography Tool (Data Hider)**.

### 🔑 Password Strength Analyzer and Custom Wordlist Generator

This tool is designed to help users understand and test password security against both generic and social engineering attacks.

* **Primary Functions:**
    * **Analyze Password Strength:** Uses the **zxcvbn** library to provide a modern, detailed security analysis (0-4 score), including estimated crack time and specific suggestions for improvement.
    * **Generate Targeted Wordlists:** Creates context-aware wordlists based on personal inputs (Name, Date, Pet).
* **Wordlist Generation Features:** The generator automatically includes various high-probability permutations, such as **case variations**, **Leetspeak substitutions** (e.g., s -> 5, e -> 3), **common date/year formats**, and year appending for a configurable range.
* **Technology:** Built with Python and **Tkinter** for the GUI, relying on **zxcvbn** for the core analysis.

---

### 🎭 Data Hider - Steganography Tool (LSB Method)

This application demonstrates the basic concept of information hiding using a classic steganography technique.

* **Core Concept:** Hides secret text messages inside image files using the **Least Significant Bit (LSB)** steganography technique.
* **Primary Functions:**
    * **Hide Data:** Embeds a text message within a selected image (PNG or JPG).
    * **Show Data:** Extracts the hidden text message from a steganographically altered image.
* **Technology:** Features a GUI built with Python's **Tkinter** and uses the **Pillow (PIL)** and **Stegano** libraries for image manipulation and LSB embedding. The final steganographically altered image is saved as `hidden.png`.

---

## 🤝 Contributing
Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
* Fork the Project
* Create your Feature Branch (git checkout -b feature/AmazingFeature)
* Commit your Changes (git commit -m 'Add some AmazingFeature')
* Push to the Branch (git push origin feature/AmazingFeature)
* Open a Pull Request

---

## ⚖️ License
Distributed under the MIT License. See [(`LICENSE`)] for more information.

