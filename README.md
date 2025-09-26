# Dynamic_Quiz_and_Achievement_Tracker

A command-line quiz application that tests your knowledge across various topics with personalized user statistics and progress tracking.

---

## Overview
**QuizMaster** is a Python-based interactive quiz game that fetches questions from the **Open Trivia Database API**.  
It features user authentication, topic selection, score tracking, and detailed performance statistics.

---

##  Features

### Quiz Functionality
- **Multiple Topics**: Choose from 5 different quiz categories  
- **Real-time Question Fetching**: Dynamic API integration for fresh questions  
- **Randomized Options**: Multiple-choice answers with randomized order  
- **Instant Feedback**: Immediate correct/incorrect feedback with explanations  

### User Management
- **Personalized Accounts**: User-specific progress tracking  
- **Persistent Data**: JSON-based user database with score history  
- **Statistics Tracking**: Comprehensive performance metrics including:  
  - Highest score achieved  
  - Total questions attempted  
  - Correct answers count  
  - Overall accuracy percentage  

### User Experience
- **Color-coded Output**: Visual feedback with ANSI color codes  
- **Input Validation**: Robust error handling for user inputs  
- **Smooth Navigation**: Intuitive menu system  

---

## Technologies Used
- **Python 3** – Main application logic  
- **Node.js** – API fetching utility  
- **Open Trivia Database API** – Question source  
- **JSON** – Data persistence  
- **ANSI Escape Codes** – Terminal coloring  

---

### Taking the Quiz
- Each quiz consists of 5 medium-difficulty questions

- Multiple-choice format (a, b, c, d)

- Enter the letter corresponding to your answer

- Receive immediate feedback with correct answers

### Viewing Statistics
- After completing a quiz, view performance statistics:

- Highest score achieved

- Total questions attempted

- Correct answers count

- Overall accuracy percentage

### Available Quiz Topics
#### Topic
- 1	General Knowledge
- 2	Science & Nature
- 3	Science: Computers
- 4	Science: Mathematics
- 5	Entertainment: Cartoon & Animations

## Technical Details

### API Integration
- Uses **[Open Trivia Database API](https://opentdb.com)**
- Questions encoded in **URL3986** format
- Handles API failures gracefully
- Medium difficulty, multiple-choice format

---

### Data Management
- Individual **JSON files** created for each user
- Automatic database creation for new users
- Real-time statistics updating after each quiz
- Persistent score tracking across sessions

---

### Color Coding System
- **Red** (`\033[31m`) → Errors & incorrect answers  
- **Green** (`\033[32m`) → Success messages & usernames  
- **Yellow** (`\033[33m`) → Statistics & scores  
- **Blue** (`\033[34m`) → Section headers  
- **Magenta** (`\033[35m`) → Special achievements  
- **Cyan** (`\033[36m`) → Information messages  

---

## Troubleshooting

### Common Issues
1. **API Connection Errors**
   - Check internet connection  
   - Verify API endpoint accessibility  

2. **Node.js Execution Issues**
   - Ensure Node.js is properly installed  
   - Verify `script.js` is in the same directory  

3. **File Permission Errors**
   - Ensure write permissions in the current directory  
   - Check if user JSON files can be created/modified  

---

### Error Messages
- **`Please enter a number!`** → Input validation for numeric choices  
- **`An error occurred while fetching data!`** → API connection issues  
- Automatic creation of new user databases for first-time users  
