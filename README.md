# Notepad

## Table of Contents
1. [Description](#Description)
2. [Technical](#Technical)
2. [Structure](#Structure)


## Description
A simple Notepad coded in Python to create, read, update and delete notes. All notes will be saved in a database coded in SQLite.

## Technical
* Python3 for frontend and backend development
* SQLite for a light and serverless database
* CustomTkinter for GUI in python


## Structure
* backend.py: This modul will handle the backend logic and will comunicate with the database to add, read, update and delete notes.

* frontend.py: This modul will handle the GUI for the Note app.

* app.py: This script will combine evrything. It initializes both the backend and frontend modules to create a working app.