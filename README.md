# Time-Based Greeting Script

A simple Python script that prints the current time and displays a context-appropriate greeting (e.g., "Good Morning", "Good Night") based on your system time.

---

## 📑 Table of Contents

- [📜 Description](#-description)  
- [✨ Features](#-features)  
- [🛠️ Requirements](#-requirements)  
- [🚀 How to Run](#-how-to-run)  
- [🔍 Example Output](#-example-output)  
- [🧠 Code Logic Breakdown](#-code-logic-breakdown)  
- [🔧 Built With](#-built-with)  
- [📌 Notes](#-notes)  
- [📝 Final Note](#-final-note)

---

## 📜 Description

This script uses Python’s built-in `time` module to determine the current time and print a greeting appropriate for the time of day. It's designed to be lightweight, beginner-friendly, and easy to integrate into larger systems.

---

## ✨ Features

- 📅 Displays current system time in `HH:MM:SS` format  
- 🕒 Provides appropriate greeting based on time  
- 🔁 Automatically updates every time it is run  
- 💡 Requires no external libraries  

---

## 🛠️ Requirements

- Python 3.x  
- OS with system time support (Windows/Linux/macOS)

---

## 🚀 How to Run

1. Save the script in a file named `greeting.py`
2. Open a terminal/command prompt in the same directory
3. Run the following command:

```bash
python greeting.py
```

---

## 🔍 Example Output

```
14:30:15  
Good Afternoon
```

---

## 🧠 Code Logic Breakdown

```python
import time
```
- Imports the `time` module to access system time.

```python
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
```
- Gets the current time in `HH:MM:SS` format and prints it.

```python
if '05:00:00' <= timestamp < '12:00:00':
    print("Good Morning")
elif '12:00:00' <= timestamp < '17:00:00':
    print("Good Afternoon")
elif '17:00:00' <= timestamp < '21:00:00':
    print("Good Evening")
else:
    print("Good Night")
```
- Compares the time using string comparison (works correctly for zero-padded `HH:MM:SS`)  
- Prints an appropriate greeting depending on the range the current time falls into

---

## 🔧 Built With

- [Python Standard Library](https://docs.python.org/3/library/) – for system time functionality using `time`

---

## 📌 Notes

- This script relies on your system’s local time—ensure your clock is accurate.  
- It’s a good example of using conditionals and time handling for beginners.  
- Future enhancements could include support for different time zones or a GUI version.

---

## 📝 Final Note

This project may be small in size, but it’s built with care.  
I'm currently learning Python, and this script—though simple—is a part of my hands-on journey to grasp the basics. Every line of code helps me grow a little more confident and curious about what's next.

Thanks for checking it out! 🎉  
Feel free to improve, remix, or extend it further.

– Shuvo Ahmed
```
