# Working with Data - Lab 1

## 🔍 Overview

The lab is designed to be self-guided, providing solutions for each exercise to check your work and assist if you get stuck. However, it is important to first attempt to solve the problem on your own as this is the best way to learn. If you become stuck, don't give up and seek help from the instructor, peers, or even a search engine like Google. Be mindful that not all answers from a search engine may be correct, so use your judgement to determine the validity of the information. Remember, the best way to learn is to try solving the problem yourself first.

### Emojis Legend

Throughout the assignment instructions, you'll find some emojis that will help you navigate the instructions. Here's what they mean:

- 👨🏻‍💻 - Instructions; Tells you about something specific you need to do.
- 🦉 - Tips; Will tell you about some hints, tips and best practices
- 📜 - Documentations; provides links to documentations
- 🚩 - Checkpoint; marks a good spot for you to commit your code to git
- 🕵️ - Tester; Don't modify code blocks starting with this emoji

This is inspired by `@kentcdodds` workshops.

## 🎯 Objectives

This lab will introduce you to the basics of working with data in Python. You will learn:

- how to read and write data from and to a file
- how to use the `pandas` library to work with data in a `DataFrame`
- how to read data from CSV file (local and remote)
- how to read data from SQL Database

---

## 📝 Instructions

### 0.Setup

- Accept the assignment on GitHub Classroom. (looks like you've already done that)
  - This repository is private; only you and the instructors can see it. Please don't change the visibility of the repository in the settings.
- Clone the repository to your computer.
  - You can use GitHub Desktop, the command line, or VSCode to do that.
  - You can view the ["Cloning a Repository - GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui) for more information.
- Open the assignment root folder in VSCode.
  - If you get a notification asking you to install the recommended extensions, go ahead and do that.
- using the terminal, install the dependencies for this project:
  - if you're using `poetry`, run `poetry install`.
  - If you're using `pipenv`, run `pipenv install`
  - if you're using `pip`, run `pip install -r requirements.txt`
- Open the `python-exercises.ipynb` Notebook in VSCode
- Make sure you have the right kernel selected for the notebook. Use this [guide](https://it4063c.github.io/guides/FAQ/vscode-jupyter) if you need help.

### 1. Complete the exercises

The notebook itself will guide you through the exercises. You'll find instructions regarding each exercise in the notebook.
You'll also find some tips and links to documentations that will help you complete the exercises.

- Make sure you commit often, you'll find this emoji 🚩, signifying suggested spots where you can make a commit of your code.
- Don't forget to push your code to GitHub when you're done.
- If you're doing this assignment, over multiple sessions, make sure you always push your code to GitHub before you close your computer to avoid losing your work.

### 2. Finalize and Submit your Work

- **Once you've completed all the exercises, come back to this file** and complete the reflection section and the self-evaluation section at the end of this file.
- Submit your work by submitting a link to your repository on Canvas.

---

---

## 💭 Reflection and Self Assessment

**I learned:** (repeat as needed)

- How to read and write text files in Python using `open()` and the `with` statement.
- How to loop with `range()` and write formatted lines to a file using f-strings.
- How to load data into pandas using `read_table()` and `read_csv()`, including reading a CSV from a URL.
- How to save a DataFrame to a CSV file with `to_csv()`.
- How to connect to a SQLite database with SQLAlchemy and query it with `pd.read_sql()`.
- How to use SQL `JOIN`, `LIKE`, and `DISTINCT` to answer questions about the Chinook database.
- How to add a row with `pd.concat()` and write a DataFrame back to a database with `to_sql()`.

**I struggled with:** (repeat as needed)

- Downloading the Chinook database, which gave an HTTP 403 error until I added a User-Agent header.
- Missing packages (`sqlalchemy` and `nbconvert`), which I had to install with `%pip install`.
- Understanding when to use `replace` versus `append` with `to_sql()`.

**I need the instructor to help me with:** (repeat as needed)

- Understanding SQL joins across multiple tables more deeply.
- Best practices for managing database connections (committing and closing them).

**How long did it take you to complete this assignment? and reflect on that**

- 3 hours. I think I spend good amount of time.

**How often did you have to check the solution to the problem? How do you feel about that?**
I checked the provided solutions several times, mostly for the SQL join exercises. I had to write dwon in paper to make sure I am getting what is expected.

**If I were to do this assignment again, I would:** (repeat as needed)

- Install the required packages before starting.
- Commit and push after each exercise to catch Git problems early.

**💯 Self Grade:** For this assignment, based on my work and my reflections I should get 19 out of 20.

---

## 📚 References and Citations

**I used the following links, books, and other resources in my work:** (repeat as needed)

- pandas documentation: https://pandas.pydata.org/docs/
- SQLite Tutorial (Chinook sample database): https://www.sqlitetutorial.net/sqlite-sample-database/
- SQLAlchemy documentation: https://docs.sqlalchemy.org/
- Google with error messages, and Git troubleshooting

**I received help from the following people:** (repeat as needed)

- None

---

## Copyrights and License

IT4063C Data Technologies Analytics by [Yahya Gilany](https://yahyagilany.io). is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
