# Problem Statement

In today's digital environment, efficient keyboard typing is a fundamental skill that directly impacts productivity. Many individuals, especially students, professionals, and programmers, seek simple, readily available tools to accurately measure their current typing speed (WPM - Words Per Minute) and identify areas for improvement. The need is for a straightforward, command-line utility that provides quick, quantitative, and precise feedback without the overhead of a graphical interface.

# Scope of the Project

The project is a Command-Line Interface (CLI) application developed in Python.

* In Scope:

  * Core Functionality: Presenting a randomly selected phrase to the user for transcription.

  * Performance Metrics: Accurate measurement of the time taken to type the phrase.

  * Calculation: Computation of the WPM based on the time taken and the length of the target text (using the standard 5 characters per word calculation).

  * Feedback: Providing pass/fail status and detailed error reporting upon completion.

* Out of Scope:

  * Graphical User Interface (GUI).

* User accounts, saving historical test data, or leaderboards.

  * Advanced statistical analysis (e.g., character-level accuracy).

  * Integration with external text sources or databases.

# Target Users

The primary users for this application are:

  * Students and Learners: Individuals practicing their typing skills or preparing for assessments.

  * Casual Users: Anyone wanting a quick, no-frills method to check their current typing speed.

  * Programmers and Developers: Users who prefer or require a tool that runs directly in their terminal/console environment.

  * Educators: Teachers needing a simple utility to administer basic typing tests.

# High-Level Features

The Typing Speed Test includes the following high-level features:

  *  Randomized Text Prompts - Selects a random sentence from an internal list for each test run to ensure variety and minimize memorization.

  * Real-time Performance Tracking - Utilizes the time module to record the start and end time of the typing session, calculating the elapsed time in seconds.

  * Words Per Minute (WPM) Calculation - Computes the WPM using the industry standard formula: (Total Characters / 5) / Time Taken in Minutes.

  * Input Validation and Accuracy Check - Compares the user's input against the target text, ignoring leading/trailing whitespace, to determine if the test was completed successfully.

  * Detailed Error Reporting - If the input is incorrect, the application reports word-by-word mismatches, indicating the expected word versus the word the user typed (or 'No character' if the input was shorter).

  * User-Friendly CLI Output - Provides clear, formatted output for instructions, the target phrase, and the final results (WPM and Time Taken).
