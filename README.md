# 🧪 Selenium Web Automation - DemoQA Web Tables

This project demonstrates basic **CRUD operations (Create, Read, Update, Delete)** using **Selenium WebDriver** on the [DemoQA Web Tables](https://demoqa.com/webtables) page.

As part of my learning journey in automation testing, I developed this script to interact with web elements dynamically using waits, JavaScript execution, and exception handling.

---

## 🚀 Features

- ✅ Add a new record (`Karthik G`)
- ✏️ Edit the record (change name to `Karthii G`)
- ❌ Delete the record
- 📜 Uses `Explicit Waits` for stability
- 🔄 Handles `StaleElementReferenceException` gracefully
- 💻 JavaScript execution for scrolling and hiding ad iframe

---

## 🧰 Technologies Used

- Python 🐍
- Selenium WebDriver 🌐
- ChromeDriver
- WebDriverWait + Expected Conditions

---

## ⚙️ How to Run

### Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver installed and added to PATH
- Selenium library (`pip install selenium`)

### Running the Script

```bash
python crud.py
```

## 📸 Sample Output

- Adding a new record...
- Record added: Karthik G
- Editing the record...
- Record updated: Karthii G
- Deleting the record...
- Record deleted successfully
- All CRUD operations completed successfully.
