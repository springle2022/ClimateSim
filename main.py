from library_files import gui, frames
import multiprocessing
import random

interface = gui.interface() #gets interface object

root = interface.root #returns the root, needed for other calculations
home_frame = interface.home_frame #returns the home frame, or the first frame

#Global Monitering Frame
GM_Frame = frames.global_monitering().create(root)

def reset():
    GM_Frame.lift()
    #print("you pressed global monitering!")
    doReset = interface.confirm(text="RESET?")
    #print(doReset)
    if doReset == True:
        frames.global_monitering().start(GM_Frame)

#Empty Frame
#interface.new_frame(root,0,1,sticky="NEWS") #This is to hide the other frames

#Interface buttons
#interface.new_button(home_frame,"Global Monitering",pressed_global_monitering,4,0,"NEWS")
frames.global_monitering().start(GM_Frame)
# reset button
reset_frame = interface.new_frame(GM_Frame,3,4,"NEWS")
interface.new_button(reset_frame,"RESET",reset,4,10,"NEWS")

'''interface.new_button(home_frame,"Ocean Acidification",pressed_ocean_acidification,2,0,"NEWS")
interface.new_button(home_frame,"Rising Sea Level",pressed_rising_sea_level,3,0,"NEWS")'''

interface.root.mainloop() #prevents the program from ending early
