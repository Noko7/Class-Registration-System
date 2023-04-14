# Class-Registration-System
Final Class Project for Intro to Python Course


This program simulates a course registration system for students. Students can log in, add and drop courses, list their courses, and view their billing information.

## Features

- Login verification
- Add and drop courses
- List courses
- Calculate and display billing information

## Getting Started

1. Clone the repository
2. Run `python course_registration.py` in the terminal
3. Follow the prompts to log in, select an option, and manage your courses.

## Usage

When you run the program, you will be prompted to enter your student ID and PIN to log in. Once you are logged in, you will be presented with a menu of options:

- Add Course: Enter the name of the course you want to add to your schedule. If the course is not full, you will be added to the roster. Otherwise, you will be added to the waitlist.
- Drop Course: Enter the name of the course you want to drop from your schedule. If there are students on the waitlist, the first student will be added to the roster in your place.
- List Courses: View a list of the courses you are currently enrolled in.
- Show Bill: Calculate and display your credit hours and billing information.

## Requirements

- Python 3.5+
- `student` module
- `billing` module


## License

This project is licensed under the MIT License - see the LICENSE file for details.
