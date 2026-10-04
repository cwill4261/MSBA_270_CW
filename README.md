# Python Trivia Night

## Project Overview

Python Trivia Night is an interactive command-line trivia game developed to practice foundational Python programming concepts. Players enter their name, select a trivia category, answer a question, and receive immediate feedback while the program tracks their score.

The project was developed as part of my Python programming coursework and demonstrates how several fundamental programming concepts can be combined to create an interactive application.

## Features

- Interactive command-line interface
- Multiple trivia categories
- Category-based question filtering
- Case-insensitive answer checking
- Input validation
- Error handling for missing input
- Running score tracking
- Option to continue selecting additional trivia categories

## Python Skills Demonstrated

This project demonstrates my use of:

- Lists
- Dictionaries and key-value pairs
- Functions
- Function parameters and return values
- Boolean logic
- `if` / `else` conditional statements
- `for` loops
- `while` loops
- `break`
- User input with `input()`
- String manipulation using `.strip()` and `.lower()`
- Exception handling with `try` / `except`
- Data filtering
- Running totals and score tracking
- Python indentation and program flow

## How the Program Works

Trivia questions are stored as dictionaries inside a Python list. Each dictionary contains:

- A question
- The correct answer
- A category

The program asks the player to select a category and filters the question list to identify matching questions.

The `ask_question()` function displays the selected question, collects the player's response, validates the input, and returns either `True` or `False` depending on whether the answer is correct.

The main program uses this Boolean result to update the player's score.

## Example

```text
=== Welcome to Trivia Night ===

Choose a category:
Geography
Literature
Science
History
Space

Enter your name: Cole

Enter a category: Science

[Science] What is the chemical symbol for gold?
Your answer: Au
Correct!
Cole, your score is 1.

Would you like another category? yes
