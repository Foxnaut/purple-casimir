# purple-casimir
Aiden, Josh, Kavin, Aathii

Made for: Kurius Hacks: Christmas Edition
Made from: 4:30 PM EST on 28/12/2020 to 4:00 PM EST on 30/12/2020

Our githubs:
- Aiden - https://github.com/Foxnaut/  
- Josh - https://github.com/iWolf22
- Kavin - https://github.com/KavinSatheeskumar/ 
- Aathii - https://github.com/Aathii 

Project components:
- HTML and CSS frontend (primarily written by Aiden and Aathii)
- game design and mechanics (done by Josh)
- web backend for score retention and presentation (Kavin did this component)

Goals:
- have fun
- learn more of the respective languages we used 
- make a game that children might actually find fun
- format a good looking product in the end (which as the frontend guy is my job :/ - Aiden)

# HOW TO USE:

(note, this is a windows only series of commands, if you don't have windows, the video runs through the main steps on windows and only steps 2 and 3 are different)
(note two, this will require a machine that can run python and has pip install,
pip does come with python 3 by deafult)

Step one: extract the zip file

Step two: Change the directory into the extracted zip file
>cd C:\Users\[...]\Purpe-Casmier

Step three: Activate the virtual environment
>venv\Scripts\activate.bat

Step four: Install the nesscicary dependencies
>pip install flask

>pip install pygame

>pip install pyyaml

Step five: set environment variables
>set FLASK_APP=purple
-If you would like to see error messages when things go wrong, you can run
>set FLASK_ENV=development

Step six: run
>flask run

Step seven: open
open your favourite browser and open
localhost:5000
