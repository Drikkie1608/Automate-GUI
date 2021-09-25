# Automate GUI
 A smart system that can automate tasks by simulating the computer mouse and keyboard.

 Terraria module contains methods solemnly for the game Terraria
 - Fishing
 - Inventory
 - Journey mode
 - Transportation

 Toolkit module contains methods that can be used for other software
 - calibration
 - image detection
 - essentials
 - flow
 - steam

## Main
 The program consists of 3 seperate threads (programs) running simultaniously:
 - execute the flow (more about this later)
 - toggle a global variable RUNNING on/off when a trigger key is pressed, e.g. when v is pressed the flow is put on hold
 - an user-friendly interface that can be used to add an action to the flow

 ## Flow
 The flow is a literally a list of tasks the system has to execute.
 A very specific example to explain this rather complicated process, we look at 2 very simple methods: autofish and autodrink.

 In terraria, you can fish. Click once, wait +- 5 seconds, click to reel back in and click to throw the line back in the water.
 This process is one itteration of the 'autofish' loop.

 After a preditermined time you have to drink a potion, e.g. 3 minutes. One itteration of this function would be: select the drink, click, return to the previous selected item.

 When these 2 functions are combined, the ods of them coliding and the system breaking is high. So in order to avoid this, we use the 'flow'.

 Via our interface (thread 3), we add both the actions to our flow. Every 3 minutes, the drinking method will be added at the back of the list.
 At the same time, at the end of every itteration of the autofishing method, it will also be added back to the list.

 When the toggle button is activated (thread 2 is constantly listening for this trigger button), no further methods will be added to the flow and all timers will be stopped.

 Thread 1 will constantly keep executing the first function in the list and afterwards delete it from the list, so it executes all the elements of the flow one by one.

 With this rather complex system, it's not only possible to execute functions at the same time but also plan ahead and put future tasks one by one in the flow.

## Calibration
The current calibration system saves important positions of the screen in a json file. In this repository, you can see the specifics for my 2 monitors.
I wrote some handy functions that make the calibration process really straight forward.
After calibration, locations can be specified in your code by e.g. typing *c["research_menu"]. 
This will automatically convert the correct json file into a dictionary, take the correct location and fill in the coördinates.

### Function 1: calibrate
Given a screen, a trigger key and a list of locations, it will go over these locations one by one asking you to hover with your mouse over them.
When you hover over the right spot and press the trigger key, the coordinates will be saved to the correct json file.
You'll have to do this for all locations mentioned in the list.

E.g. :
tk.calibrate_grid('screen1', ["dup_menu", "research_menu", "time_menu", "weather_menu", "pp_menu", "infection_toggle","enemy_difficulty_slider"], 'v')
Hover over duplication menu and press 'v', hover over research menu and press 'v', ...

### Function 2: calibrate_grid
This function can only be used if all the locations listed are evenly spaced from each other. e.g. the hotbar from a video game, all n slots are in a perfect grid.
Given a screen, a trigger key and a list of locations, it will ask you to only calibrate the two outmost locations on the list. It fills in the other locations based on the assumption these are evenly spread.

E.g. :
tk.calibrate_grid('screen1', ["dup_menu", "research_menu", "time_menu", "weather_menu", "pp_menu", "infection_toggle","enemy_difficulty_slider"], 'v')
Hover over duplication menu and press 'v', hover over enemy_difficulty_slider and press 'v', calibration COMPLETE

### Future releases
I want to combine this system with the image recognition, instead of having to calibrate everything manually, let the program search for text or specific images.

