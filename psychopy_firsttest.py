# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:19:18 2020

@author: mathieu.pinger
"""

from psychopy import visual, core, event

# open window
win = visual.Window([400,300], monitor="testMonitor")

# create stimulus
message = visual.TextStim(win, text="Hello World!")

# Draw the stimulus to the window.
message.draw()
 
# Flip backside of the window.
win.flip()
 
# Pause 5 s, so you get a chance to see it!
core.wait(5.0)

# This block is needed in spyder to close window!
win.close()
core.quit()


# Psychopy online example

win = visual.Window(fullscr=True)
message = visual.TextStim(win, text='hello')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'world'  # Change properties of existing stim
win.flip()
core.wait(2.0)
win.close()
core.quit()

# two-choice stimuli

win = visual.Window(fullscr=True)
choice_1 = visual.TextStim(win, text = "1€ sofort", pos = [-0.5,0])
choice_2 = visual.TextStim(win, text = "2€ in 2 Wochen", pos = [0.5,0])
choice_1.draw()
choice_2.draw()
win.flip()
 
# Pause 5 s, so you get a chance to see it!
core.wait(2.0)


win.close()
core.quit()