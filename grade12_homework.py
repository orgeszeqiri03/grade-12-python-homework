# Grade 12 Python Homework – mBot2

import cyberpi

# Display personal information on the CyberPi screen
cyberpi.console.println("Name: Orges")
cyberpi.console.println("Surname: Zeqiri")
cyberpi.console.println("Favorite Color: Green")

cyberpi.console.println("")
cyberpi.console.println("Favorite Subjects:")
cyberpi.console.println("1. PE")
cyberpi.console.println("2. Mathematics")
cyberpi.console.println("3. ICT")

# Set the mBot2 RGB LED lights to red
cyberpi.led.on(255, 0, 0)
