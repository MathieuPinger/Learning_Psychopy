/************************** 
 * Choice_Experiment Test *
 **************************/

import { PsychoJS } from 'https://lib.pavlovia.org/lib/core-2020.2.js';
import * as core from 'https://lib.pavlovia.org/lib/core-2020.2.js';
import { TrialHandler } from 'https://lib.pavlovia.org/lib/data-2020.2.js';
import { Scheduler } from 'https://lib.pavlovia.org/lib/util-2020.2.js';
import * as visual from 'https://lib.pavlovia.org/lib/visual-2020.2.js';
import * as sound from 'https://lib.pavlovia.org/lib/sound-2020.2.js';
import * as util from 'https://lib.pavlovia.org/lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'choice_experiment';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'choice_experiment_options.xlsx', 'path': 'choice_experiment_options.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var TrialClock;
var immediate_choice;
var delayed_choice;
var choice;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Trial"
  TrialClock = new util.Clock();
  immediate_choice = new visual.TextStim({
    win: psychoJS.window,
    name: 'immediate_choice',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  delayed_choice = new visual.TextStim({
    win: psychoJS.window,
    name: 'delayed_choice',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  choice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'choice_experiment_options.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(TrialRoutineBegin(snapshot));
    trialsLoopScheduler.add(TrialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(TrialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _choice_allKeys;
var TrialComponents;
function TrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Trial'-------
    t = 0;
    TrialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    immediate_choice.setText(immediate);
    delayed_choice.setText(delayed);
    choice.keys = undefined;
    choice.rt = undefined;
    _choice_allKeys = [];
    // keep track of which components have finished
    TrialComponents = [];
    TrialComponents.push(immediate_choice);
    TrialComponents.push(delayed_choice);
    TrialComponents.push(choice);
    
    for (const thisComponent of TrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
var continueRoutine;
function TrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *immediate_choice* updates
    if (t >= 0.5 && immediate_choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      immediate_choice.tStart = t;  // (not accounting for frame time here)
      immediate_choice.frameNStart = frameN;  // exact frame index
      
      immediate_choice.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (immediate_choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      immediate_choice.setAutoDraw(false);
    }
    
    // *delayed_choice* updates
    if (t >= 0.5 && delayed_choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      delayed_choice.tStart = t;  // (not accounting for frame time here)
      delayed_choice.frameNStart = frameN;  // exact frame index
      
      delayed_choice.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (delayed_choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      delayed_choice.setAutoDraw(false);
    }
    
    // *choice* updates
    if (t >= 0.5 && choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice.tStart = t;  // (not accounting for frame time here)
      choice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      choice.clock.reset();
      choice.start();
      choice.clearEvents();
    }

    frameRemains = 0.5 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice.status = PsychoJS.Status.FINISHED;
  }

    if (choice.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _choice_allKeys = _choice_allKeys.concat(theseKeys);
      if (_choice_allKeys.length > 0) {
        choice.keys = _choice_allKeys[_choice_allKeys.length - 1].name;  // just the last key pressed
        choice.rt = _choice_allKeys[_choice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Trial'-------
    for (const thisComponent of TrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('choice.keys', choice.keys);
    if (typeof choice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice.rt', choice.rt);
        routineTimer.reset();
        }
    
    choice.stop();
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
