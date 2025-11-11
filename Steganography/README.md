# 🎭 Data Hider - Steganography Tool (LSB Method)

## ✍️ Overview :
**Data Hider** is a simple graphical user interface (GUI) application built with **Python's Tkinter** library that allows users to hide secret text messages inside image files using the **Least Significant Bit (LSB)** steganography technique.

This tool is perfect for demonstrating a basic concept of information hiding and cyber security.

---

## ✨ Features :

* **GUI Interface:** Easy-to-use application window powered by Tkinter.
* **Hide Data:** Embed a text message within a selected PNG or JPG image.
* **Show Data:** Extract the hidden text message from a steganographically altered image.
* **Image Handling:** Supports opening image files and saving the steganographically altered image as a new **`hidden.png`** file.

---

## ⚙️ Prerequisites :

To run this application, you need **Python 3** installed on your system. You also need the following libraries:

* **`tkinter`**: Usually comes bundled with standard Python installations.
* **`Pillow` (PIL)**: For image manipulation.
* **`stegano`**: The core library for LSB steganography.

---

### Installation :

You can install the required libraries using `pip`:

```bash
pip install Pillow stegano
````
---

## 🚀 How to Run :

1.  **Clone the Repository:**

    ```bash
    git clone [Repository-Link]
    cd Data-Hider
    ```

2.  **Ensure Prerequisites are Met:**
    Make sure you have installed `Pillow` and `stegano` as described above.

3.  **Run the Python Script:**

    ```bash
    python "Data Hider.py"
    ```

-----

## 📝 Usage :

### Hiding Data

1.  Click the **"Open Image"** button to select a host image (preferably a PNG file, as JPEG compression can corrupt the hidden data).
2.  Type the secret message into the large text area on the right.
3.  Click the **"Hide Data"** button. The message is now embedded in the image data.
4.  Click the **"Save Image"** button. This will save the new image containing the hidden data as **`hidden.png`** in the same directory as the script.

### Showing Data

1.  Click the **"Open Image"** button and select the image containing the hidden data (e.g., `hidden.png`).
2.  Click the **"Show Data"** button.
3.  The hidden message will appear in the text area on the right.

## 🛠️ Project Structure :

```
.
├── Data Hider.py           # The main Python script with the GUI and logic
├── logo.jpg                # Icon file used for the application window (Placeholder)
├── logo.png                # Logo image used inside the GUI (Placeholder)
├── hidden.png              # Output file when saving a hidden image
└── README.md               # This file
```

*(Note: You will need to provide `logo.jpg` and `logo.png` files or remove the lines related to them in the Python script if you don't use them.)*

-----

## 📜 Dependencies :

  * [**Tkinter**](https://docs.python.org/3/library/tkinter.html)
  * [**Pillow (PIL)**](https://pypi.org/project/Pillow/)
  * [**Stegano**](https://pypi.org/project/stegano/)

-----

## 🤝 Contributing :

Feel free to fork the repository, make improvements, and submit pull requests. Any suggestions for improving the code or GUI are welcome\!

-----

## 🛑 Disclaimer :

This tool is created for **educational purposes** only to demonstrate the concept of steganography. Use it responsibly and ethically.

## 🧑‍💻 Author

**Rushikesh Powar**
