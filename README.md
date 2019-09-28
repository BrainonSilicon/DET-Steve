# DET-Steve
Code base for DET Project 1

## Introduction 
Steve is a Robotic server for a Starbucks that helps you decide what drink to order

## Logic 
There are 3 orders of logic in Steve's codebase
  - The individual functions which define (1) the actions and interactions of Steve and his arms and (2) the LCD print out
  - The driver which calls and orders the functions 
  - main () which allows us to complete the logic from driver several times with different LCD input

## Version 
There are many versions of Steve's code detailed here:

testing_steve_arms was working based on 9.23

steve_movement_functions was written on wednesday 9.25 and edited a little thursday 2.26 but has not seen any debugging based on the errors from the pi 

welove_Bryan was a non logically sound version of the code as of 9.26 and "could" be used as a regression but would need updating and checking by a later branch 

steve_movement_functions "may" have been the one that was the least of the broken code but am not certain

GoogleVisionCode is where I was testing if the vision api code worked 

Steve_functions_are_separated_out is where are started to pull out the code into the separate pieces of logic 

steve_with_LCD was the first try at integrating the LCD code before the pin numbers have been updated 
      -> would suggested checking the pin numbers based on ananyan's master or by steve_friday 

will_new_LCD_code is the new pin numbers for the LCD screen 

steve-motor-lcd I think is one of the better versions but was not debugged -> it's probably the most safe version to regress to

Steve_friday is the most debugged code based on the errors on 9.27 
  - each version indicates a "major" error being resolved 
  
 
 
## Plan 

to check group's master against most updated steve-friday 
to check that against steve-motor-lcd for logic 

continue debugging 
  - each major debug will be placed in a new file with the v1 etc next to it and the day it was worked on 
  
  
## Why Does It Need To Be This Complicated 
because I can't debug well on the pi (it's almost 300 lines of code) 
because git and the pi make things a little difficult so the work flow looks like this 
  1) run a verson on the pi 
  2) look at the errors 
  3) try to debug the errors in pi first and then vs code
  4) update the file in vs code 
  5) save that code as a new file 
  6) put that file on the usb 
  7) upload the file to the pi via usb 
  8) run it 
  9) debug some more 
