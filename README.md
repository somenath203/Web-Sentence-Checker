# Web Sentence Checker App

This is a basic website created using bootstrap and flask. Here, you have to enter your username(which can be anything) which should satisfy three conditions i.e. your username must contain at least one upper-case letter, one lower-case letter and the username must end with a number. If your username misses out on any of these conditions, then, that ***missed out condition*** will be displayed in front of the user for eg. if the user name is **hello**, then, the message that will be displayed on submitting the user-name will be **'Your username does not contain any upper-case letter.'** and **'Your username does not end with any number.'** respectively.

## Requirements

Python version 3.9.1+

## Installation

### Step 1

In order to use this app in your system, we need to install **Flask**. To install **Flask**, open any independent or any IDE-based terminal and write 
```
pip install flask
```
### Step 2
After this, navigate to that directory where the ***Web-Sentence-Checker-App*** folder is present using the command
```
cd file_location
```
### Step 3
After getting to the location where ***Web-Sentence-Checker-App*** folder is present, get inside the folder using the command
```
cd Web-Sentence-Checker-App
```
### Step 4
After you are inside the folder, type the command to start the server
```
python app.py
```
This will start the server. 
Now, we will get an URL link on that terminal where the server is running for eg. http://127.0.0.1:5000/. Just copy the link and paste it on any browser and then, press ENTER to open the application.
