#! /usr/bin/env python

# Simple string program. Writes and updates strings.


# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel
# Backlight: Enhanced by TOMDENKT - backlight control (on/off)
# Backlight: lcd_backlight(1) = ON, lcd_backlight(0) = OFF
# Backlight: Usage, if lcddriver is set to "display" (like example below)
# Backlight: display.lcd_backlight(0) # Turn backlight off
# Backlight: display.lcd_backlight(1) # Turn backlight on

import setups.lcd.settings as drivers
from time import sleep

display = drivers.Lcd()

def Base():
    # Main body of code
    try:
        while True:
            # Remember that your sentences can only be 16 characters long!
            print("Writing to display")
            display.lcd_display_string("Greetings Human!", 1)  # Write line of text to first line of display
            display.lcd_display_string("Demo Pi Guy code", 2)  # Write line of text to second line of display
            sleep(2)                                           # Give time for the message to be read
            display.lcd_display_string("I am a display!", 1)   # Refresh the first line of display with a different message
            sleep(2)                                           # Give time for the message to be read
            display.lcd_clear()                                # Clear the display of any data
            sleep(2)                                           # Give time for the message to be read
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()

def Scroll():
    # Main body of code
    try:
        print("Press CTRL + C to stop this script!")

        def long_string(display, text='', num_line=1, num_cols=20):
            """ 
            Parameters: (driver, string to print, number of line to print, number of columns of your display)
            Return: This function send to display your scrolling string.
            """
            if len(text) > num_cols:
                display.lcd_display_string(text[:num_cols], num_line)
                sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i+num_cols]
                    display.lcd_display_string(text_to_print, num_line)
                    sleep(0.2)
                sleep(1)
            else:
                display.lcd_display_string(text, num_line)


        # Example of short string
        long_string(display, "Hello World!", 1)
        sleep(1)

        # Example of long string
        long_string(display, "Hello again. This is a long text.", 2)
        display.lcd_clear()
        sleep(1)

        while True:
            # An example of infinite scrolling text
            long_string(display, "Hello friend! This is a long text!", 2)
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()

def Backlight():
    # Main body of code
    try:
        print("Press CTRL + C to quit program")
        while True:
            # Remember that your sentences can only be 16 characters long!
            print("Loop: Writing to display and toggle backlight...")
            display.lcd_backlight(1)                          # Make sure backlight is on / turn on
            sleep(0.5)                                        # Waiting for backlight toggle
            display.lcd_backlight(0)                          # Turn backlight off
            sleep(0.5)                                        # Waiting for turning backlight on again
            display.lcd_backlight(1)                          # Turn backlight on again
            sleep(1)                                          # Waiting for text
            display.lcd_display_string("Demo Backlight", 1)   # Write line of text to first line of display
            display.lcd_display_string("Control ON/OFF", 2)   # Write line of text to second line of display
            sleep(2)                                          # Waiting for backlight toggle
            display.lcd_backlight(0)                          # Turn backlight off
            sleep(0.5)                                        # Waiting for turning backlight on again
            display.lcd_backlight(1)                          # Turn backlight on again
            sleep(0.5)                                        # Waiting for turning backlight off again
            display.lcd_backlight(0)                          # Turn backlight off
            sleep(0.5)                                        # Waiting for turning backlight on again
            display.lcd_backlight(1)                          # Turn backlight on again
            sleep(2)                                          # Give time for the message to be read
            display.lcd_display_string("I am a display! ", 1) # Refresh the first line of display with a different message
            display.lcd_display_string("Demo Backlight", 2)   # Refresh the second line of display with a different message
            sleep(2)                                          # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            sleep(1)                                          # Give time for the message to be read
            display.lcd_backlight(0)                          # Turn backlight off
            sleep(1.5)                                        # Waiting until restart
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press CTRL + C), exit the program and cleanup
        print("Exit and cleaning up!")
        display.lcd_clear()
        # Make sure backlight is on / turn on by leaving
        display.lcd_backlight(1)
