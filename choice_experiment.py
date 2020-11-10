#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on November 10, 2020, at 10:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'choice_experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\zisvfs12\\Home\\mathieu.pinger\\Documents\\GitHub\\Learning_Psychopy\\choice_experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
immediate_choice = visual.TextStim(win=win, name='immediate_choice',
    text='default text',
    font='Arial',
    pos=(-0.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
delayed_choice = visual.TextStim(win=win, name='delayed_choice',
    text='default text',
    font='Arial',
    pos=(0.2, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
choice = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choice_experiment_options.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    immediate_choice.setText(immediate)
    delayed_choice.setText(delayed
)
    choice.keys = []
    choice.rt = []
    _choice_allKeys = []
    # keep track of which components have finished
    TrialComponents = [immediate_choice, delayed_choice, choice]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *immediate_choice* updates
        if immediate_choice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            immediate_choice.frameNStart = frameN  # exact frame index
            immediate_choice.tStart = t  # local t and not account for scr refresh
            immediate_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(immediate_choice, 'tStartRefresh')  # time at next scr refresh
            immediate_choice.setAutoDraw(True)
        if immediate_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > immediate_choice.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                immediate_choice.tStop = t  # not accounting for scr refresh
                immediate_choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(immediate_choice, 'tStopRefresh')  # time at next scr refresh
                immediate_choice.setAutoDraw(False)
        
        # *delayed_choice* updates
        if delayed_choice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            delayed_choice.frameNStart = frameN  # exact frame index
            delayed_choice.tStart = t  # local t and not account for scr refresh
            delayed_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(delayed_choice, 'tStartRefresh')  # time at next scr refresh
            delayed_choice.setAutoDraw(True)
        if delayed_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > delayed_choice.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                delayed_choice.tStop = t  # not accounting for scr refresh
                delayed_choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(delayed_choice, 'tStopRefresh')  # time at next scr refresh
                delayed_choice.setAutoDraw(False)
        
        # *choice* updates
        if choice.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            choice.frameNStart = frameN  # exact frame index
            choice.tStart = t  # local t and not account for scr refresh
            choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
            choice.status = STARTED
            # keyboard checking is just starting
            choice.clock.reset()  # now t=0
            choice.clearEvents(eventType='keyboard')
        if choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                choice.tStop = t  # not accounting for scr refresh
                choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice, 'tStopRefresh')  # time at next scr refresh
                choice.status = FINISHED
        if choice.status == STARTED:
            theseKeys = choice.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _choice_allKeys.extend(theseKeys)
            if len(_choice_allKeys):
                choice.keys = _choice_allKeys[-1].name  # just the last key pressed
                choice.rt = _choice_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('immediate_choice.started', immediate_choice.tStartRefresh)
    trials.addData('immediate_choice.stopped', immediate_choice.tStopRefresh)
    trials.addData('delayed_choice.started', delayed_choice.tStartRefresh)
    trials.addData('delayed_choice.stopped', delayed_choice.tStopRefresh)
    # check responses
    if choice.keys in ['', [], None]:  # No response was made
        choice.keys = None
    trials.addData('choice.keys',choice.keys)
    if choice.keys != None:  # we had a response
        trials.addData('choice.rt', choice.rt)
    trials.addData('choice.started', choice.tStart)
    trials.addData('choice.stopped', choice.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
