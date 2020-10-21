# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:19:18 2020

@author: mathieu.pinger
"""

from psychopy import visual, core

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