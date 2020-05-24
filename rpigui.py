#!/usr/bin/env python3

import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

red = 22
green = 27
blue = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 320, 250)
    win.setWindowTitle("5-2C")

    redButton = QtWidgets.QRadioButton("Red", win)
    redButton.move(20, 80)
    redButton.toggled.connect(lambda:toggle("red"))

    grnButton = QtWidgets.QRadioButton("Green", win)
    grnButton.move(120, 80)
    grnButton.toggled.connect(lambda:toggle("green"))

    bluButton = QtWidgets.QRadioButton("Blue", win)
    bluButton.move(220, 80)
    bluButton.toggled.connect(lambda:toggle("blue"))

    win.show()
    sys.exit(app.exec_())

def toggle(colour):
    GPIO.output(red,   GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue,  GPIO.LOW)

    if (colour == "red"):
        GPIO.output(red, GPIO.HIGH)
    elif (colour == "green"):
        GPIO.output(green, GPIO.HIGH)
    elif (colour == "blue"):
        GPIO.output(blue, GPIO.HIGH)

window()
