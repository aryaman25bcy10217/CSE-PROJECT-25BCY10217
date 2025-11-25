# CSE-PROJECT-25BCY10217
Test Utility for Command-Line Typing 
A straightforward, lightweight, and precise Python command-line tool to gauge a user's typing accuracy and speed in words per minute (WPM).
This project was created as a submission for a Computer Science and Engineering (CSE) project. 

# Features
• Randomized Text Selection: For every test session, the program chooses a sentence at random from a predetermined list. 
• Accurate Timing: Accurate start and end time tracking is achieved by utilizing the integrated time module. 
• WPM Calculation: Uses the industry-standard formula (5 characters per word) to calculate WPM. 
• Accuracy Feedback: If the user's input differs from the target text, it offers a thorough word-by-word error analysis to help pinpoint specific errors. 
• No External Dependencies: Just the standard Python 3 libraries (random and time) are needed.
Prerequisites You only need to have Python 3 installed in order to use this application.
# Check the version of Python you are using.
Python --version# or Python 3 --version
# Setup and Installation
There is very little setup because there is only one file in the project.
1. Download the file or clone the repository:
2. CD typing test
3. Find the Script: Cseprojectaraman.py is the primary application file.
# Utilization
Use Python 3 to run the script straight from your terminal: python cseprojectaraman.py # or python3 cseprojectaraman.py
# Workflow
1. The target phrase and the welcome message will appear.
2. As soon as the input prompt appears, the timer begins.
3. Enter the text exactly as it appears, then hit Enter.
4. The application shows your WPM and total time spent after the test is over.
5. In the event that you made a mistake, the program will display an Error Analysis that highlights the mismatched words.
# Formula for WPM Calculation
The following formula, which approximates a word as five characters, is used by the application to determine the Words Per Minute (WPM):
((Total Character / 5)/Time Taken In Seconds)*60
# Writer
  * The developer of this project is Aryaman Singh Chauhan.
  * Registration number is 25BCY10217.
# Contributing
Although this project report submission is finished, comments and recommendations are still welcome! Please feel free to create a pull request or open an issue for features like: 
• Expanding the text bank with additional sentences.
• Putting in place long-term high-score storage (e.g., using a local JSON file). 
• Increasing degrees of difficulty.


