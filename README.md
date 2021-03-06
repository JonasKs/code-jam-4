# Code Jam IV: This app hates you!

The theme for this code jam will be **This app hates you!**. You will be creating an application using a GUI library of your choice in Python. The application must serve a real purpose, but must also fit the theme.

You can use any GUI library that you wish to use, but you have to make _a desktop app_. For example, you may use frameworks like PySide, PyQt, tkinter, or wxPython. You can even use stuff like Kivy or PyGame, although we do not recommend that you do. You may not, however, use webframeworks like Django or Flask, and you may not use anything that turns HTML and CSS into a desktop app that runs as a browser. 

Here are a couple of examples of what we mean by an application that "serves a real purpose but also fits the theme":
* A calculator app that calculates the right answers, but represents the answer in a way that's completely impractical.
* An image resizer where you have to specify which part of the image to resize, specify how much force to apply to the resize operation in newtons, and then manually resize the image by turning a crank.
* An alarm clock app that plays a very loud sound effect every 5 minutes reminding you that your alarm will ring in 6 hours. The closer it gets to the 6 hour mark, the lower the volume of the sound effect. When the time is up, the sound effect is virtually inaudible.

Remember that teamwork is not optional for our code jams - You must find a way to work together. For this jam, we've assigned a leader for each team based on their responses to the application form. Remember to listen to your leader, and communicate with the rest of your team! 

**Remember to provide instructions on how to set up and run your app at the bottom of this README**.

# Tips

* Please lint your code, and listen to the linter. We recommend **flake8**, and you can use `pipenv run lint` to run it. We will be evaluating your style, and unlinted code will lead to point deductions.
* Remember to work closely with the rest of your team. We will deduct points for poor teamwork.
* Don't overcomplicate this. It's better to write a relatively simple app that is 100% feature complete than failing to finish a more ambitious project.
* For information on how the Code Jam will be judged, please see [this document](https://wiki.pythondiscord.com/wiki/jams/judging).

# Setting Up

You should be using [Pipenv](https://pipenv.readthedocs.io/en/latest/). Take a look 
[at the documentation](https://pipenv.readthedocs.io/en/latest/) if you've never used it before. In short:

* Setting up for development: `pipenv install --dev`
* Running the application (assuming you use our project layout): `pipenv run start`

# Project Information

This project is our solution to the 4th code jam, created by the Python Discord. 
Our team name is **Wild Whispers** and consists of the following users:
*  Supalien#8434 (frontend master)
*  TheRealZeljko#2692 (backend master)
*  Hotfix#6638 (team leader)


## Description

This app does a few things:
*  Location has a 50% chance to change into something similar, but not match your exact search. 
(So if you search for `Oslo` with the intention to get `Oslo, Norway`, you could get `Olot, Spain`.)
*  Images changes according to the weather, so if its a clear sky, you'll see a clear sky in the background. 
*  Todays weather is swapped with tomorrows weather (The intention was to have todays weather be the weather for today, last year, but some API paywall restrictions stopped us)
*  Its completely random if you see the weather in `celsius`, `fahrenheit` or `kelvin`
*  An annoying, useless settings button, try to hover it.

## Setup & Installation

Make sure you have installed `git` and `python` (>=3.7) and `pipenv`
```shell
git clone https://github.com/JonasKs/code-jam-4 
cd code-jam-4
pipenv --python 3.7
pipenv install
pipenv run setup  # make sure you have an internet connection
pipenv run start
```
 

## How do I use this thing?
After you've got the app running, type a place and click `enter`. Maybe even click enter a few times, see where it takes you. Try to click the settings icon too? 


