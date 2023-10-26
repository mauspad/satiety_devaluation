#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on October 26, 2023, at 09:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'sat_deval_part2'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Silver\\Box\\psychopy_git_masters\\satiety_deval\\part2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='cm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'cm'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "choose_salt" ---
    choose_salt_text = visual.TextStim(win=win, name='choose_salt_text',
        text="Choose your favorite salty reward again (same as before): \n(button '1', '2', or '3')",
        font='Open Sans',
        pos=(0, 7), height=1.0, wrapWidth=40.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    salt_1 = visual.TextStim(win=win, name='salt_1',
        text='1',
        font='Open Sans',
        pos=(-9, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    salt_2 = visual.TextStim(win=win, name='salt_2',
        text='2',
        font='Open Sans',
        pos=(0, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    salt_3 = visual.TextStim(win=win, name='salt_3',
        text='3',
        font='Open Sans',
        pos=(9, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    salt_selection = keyboard.Keyboard()
    # Run 'Begin Experiment' code from choose_salt_code
    ##start and hide mouse
    mouse = event.Mouse(visible=False)
    
    #create and hide some other shit
    leftcount = 0
    rightcount = 0
    chexmix = visual.ImageStim(
        win=win,
        name='chexmix', 
        image='images/salty_chexmix.png', mask=None, anchor='center',
        ori=0.0, pos=(-9, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    doritos = visual.ImageStim(
        win=win,
        name='doritos', 
        image='images/salty_doritos.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    ritz = visual.ImageStim(
        win=win,
        name='ritz', 
        image='images/salty_ritz.png', mask=None, anchor='center',
        ori=0.0, pos=(9, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    
    # --- Initialize components for Routine "salt_confirm" ---
    salt_confirm_image = visual.ImageStim(
        win=win,
        name='salt_confirm_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "choose_sweet" ---
    choose_sweet_text = visual.TextStim(win=win, name='choose_sweet_text',
        text="Choose your favorite sweet reward again (same as before): \n(button '1', '2', or '3')",
        font='Open Sans',
        pos=(0, 7), height=1.0, wrapWidth=40.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sweet_1 = visual.TextStim(win=win, name='sweet_1',
        text='1',
        font='Open Sans',
        pos=(-9, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    sweet_2 = visual.TextStim(win=win, name='sweet_2',
        text='2',
        font='Open Sans',
        pos=(0, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sweet_3 = visual.TextStim(win=win, name='sweet_3',
        text='3',
        font='Open Sans',
        pos=(9, -5), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    sweet_selection = keyboard.Keyboard()
    minioreo = visual.ImageStim(
        win=win,
        name='minioreo', 
        image='images/sweet_minioreo.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-9, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    minipbcups = visual.ImageStim(
        win=win,
        name='minipbcups', 
        image='images/sweet_minipbcups', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    skittles = visual.ImageStim(
        win=win,
        name='skittles', 
        image='images/sweet_skittles.png', mask=None, anchor='center',
        ori=0.0, pos=(9, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    
    # --- Initialize components for Routine "sweet_confirm" ---
    sweet_confirm_image = visual.ImageStim(
        win=win,
        name='sweet_confirm_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(7.5, 7.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='In this part of the experiment, you can earn the same sweet and salty rewards as before.\n\nHowever, this time you will not be able to see how much you earned until the end of the experiment.\n\n[press spacebar to continue]',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    instructions_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "start" ---
    start_text = visual.TextStim(win=win, name='start_text',
        text='Attention! \n\nThe experiment continues now',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "fixation" ---
    asterisk = visual.TextStim(win=win, name='asterisk',
        text='*',
        font='Open Sans',
        pos=(0, 0), height=3.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "choose" ---
    choose_text = visual.TextStim(win=win, name='choose_text',
        text='choose a button',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=1.0, wrapWidth=20.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "choose_salt" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('choose_salt.started', globalClock.getTime())
    salt_selection.keys = []
    salt_selection.rt = []
    _salt_selection_allKeys = []
    # Run 'Begin Routine' code from choose_salt_code
    #no really, hide the mouse
    win.mouseVisible = False
    # keep track of which components have finished
    choose_saltComponents = [choose_salt_text, salt_1, salt_2, salt_3, salt_selection, chexmix, doritos, ritz]
    for thisComponent in choose_saltComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choose_salt" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choose_salt_text* updates
        
        # if choose_salt_text is starting this frame...
        if choose_salt_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choose_salt_text.frameNStart = frameN  # exact frame index
            choose_salt_text.tStart = t  # local t and not account for scr refresh
            choose_salt_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choose_salt_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            choose_salt_text.status = STARTED
            choose_salt_text.setAutoDraw(True)
        
        # if choose_salt_text is active this frame...
        if choose_salt_text.status == STARTED:
            # update params
            pass
        
        # *salt_1* updates
        
        # if salt_1 is starting this frame...
        if salt_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salt_1.frameNStart = frameN  # exact frame index
            salt_1.tStart = t  # local t and not account for scr refresh
            salt_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salt_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            salt_1.status = STARTED
            salt_1.setAutoDraw(True)
        
        # if salt_1 is active this frame...
        if salt_1.status == STARTED:
            # update params
            pass
        
        # *salt_2* updates
        
        # if salt_2 is starting this frame...
        if salt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salt_2.frameNStart = frameN  # exact frame index
            salt_2.tStart = t  # local t and not account for scr refresh
            salt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salt_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            salt_2.status = STARTED
            salt_2.setAutoDraw(True)
        
        # if salt_2 is active this frame...
        if salt_2.status == STARTED:
            # update params
            pass
        
        # *salt_3* updates
        
        # if salt_3 is starting this frame...
        if salt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salt_3.frameNStart = frameN  # exact frame index
            salt_3.tStart = t  # local t and not account for scr refresh
            salt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salt_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            salt_3.status = STARTED
            salt_3.setAutoDraw(True)
        
        # if salt_3 is active this frame...
        if salt_3.status == STARTED:
            # update params
            pass
        
        # *salt_selection* updates
        waitOnFlip = False
        
        # if salt_selection is starting this frame...
        if salt_selection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salt_selection.frameNStart = frameN  # exact frame index
            salt_selection.tStart = t  # local t and not account for scr refresh
            salt_selection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salt_selection, 'tStartRefresh')  # time at next scr refresh
            # update status
            salt_selection.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(salt_selection.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(salt_selection.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if salt_selection.status == STARTED and not waitOnFlip:
            theseKeys = salt_selection.getKeys(keyList=['1','2','3'], ignoreKeys=["escape"], waitRelease=False)
            _salt_selection_allKeys.extend(theseKeys)
            if len(_salt_selection_allKeys):
                salt_selection.keys = _salt_selection_allKeys[-1].name  # just the last key pressed
                salt_selection.rt = _salt_selection_allKeys[-1].rt
                salt_selection.duration = _salt_selection_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from choose_salt_code
        #set salt reward selection
        if salt_selection.keys == '1':
            salt_reward = 'images/salty_chexmix.png'
        elif salt_selection.keys == '2':
            salt_reward = 'images/salty_doritos.jpg'
        elif salt_selection.keys == '3':
            salt_reward = 'images/salty_ritz.png'
        
        # *chexmix* updates
        
        # if chexmix is starting this frame...
        if chexmix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            chexmix.frameNStart = frameN  # exact frame index
            chexmix.tStart = t  # local t and not account for scr refresh
            chexmix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(chexmix, 'tStartRefresh')  # time at next scr refresh
            # update status
            chexmix.status = STARTED
            chexmix.setAutoDraw(True)
        
        # if chexmix is active this frame...
        if chexmix.status == STARTED:
            # update params
            pass
        
        # *doritos* updates
        
        # if doritos is starting this frame...
        if doritos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            doritos.frameNStart = frameN  # exact frame index
            doritos.tStart = t  # local t and not account for scr refresh
            doritos.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(doritos, 'tStartRefresh')  # time at next scr refresh
            # update status
            doritos.status = STARTED
            doritos.setAutoDraw(True)
        
        # if doritos is active this frame...
        if doritos.status == STARTED:
            # update params
            pass
        
        # *ritz* updates
        
        # if ritz is starting this frame...
        if ritz.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ritz.frameNStart = frameN  # exact frame index
            ritz.tStart = t  # local t and not account for scr refresh
            ritz.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ritz, 'tStartRefresh')  # time at next scr refresh
            # update status
            ritz.status = STARTED
            ritz.setAutoDraw(True)
        
        # if ritz is active this frame...
        if ritz.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choose_saltComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choose_salt" ---
    for thisComponent in choose_saltComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('choose_salt.stopped', globalClock.getTime())
    # check responses
    if salt_selection.keys in ['', [], None]:  # No response was made
        salt_selection.keys = None
    thisExp.addData('salt_selection.keys',salt_selection.keys)
    if salt_selection.keys != None:  # we had a response
        thisExp.addData('salt_selection.rt', salt_selection.rt)
        thisExp.addData('salt_selection.duration', salt_selection.duration)
    thisExp.nextEntry()
    # the Routine "choose_salt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "salt_confirm" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('salt_confirm.started', globalClock.getTime())
    salt_confirm_image.setImage(salt_reward)
    # keep track of which components have finished
    salt_confirmComponents = [salt_confirm_image]
    for thisComponent in salt_confirmComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "salt_confirm" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *salt_confirm_image* updates
        
        # if salt_confirm_image is starting this frame...
        if salt_confirm_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salt_confirm_image.frameNStart = frameN  # exact frame index
            salt_confirm_image.tStart = t  # local t and not account for scr refresh
            salt_confirm_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salt_confirm_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            salt_confirm_image.status = STARTED
            salt_confirm_image.setAutoDraw(True)
        
        # if salt_confirm_image is active this frame...
        if salt_confirm_image.status == STARTED:
            # update params
            pass
        
        # if salt_confirm_image is stopping this frame...
        if salt_confirm_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > salt_confirm_image.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                salt_confirm_image.tStop = t  # not accounting for scr refresh
                salt_confirm_image.frameNStop = frameN  # exact frame index
                # update status
                salt_confirm_image.status = FINISHED
                salt_confirm_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in salt_confirmComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "salt_confirm" ---
    for thisComponent in salt_confirmComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('salt_confirm.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "choose_sweet" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('choose_sweet.started', globalClock.getTime())
    sweet_selection.keys = []
    sweet_selection.rt = []
    _sweet_selection_allKeys = []
    # keep track of which components have finished
    choose_sweetComponents = [choose_sweet_text, sweet_1, sweet_2, sweet_3, sweet_selection, minioreo, minipbcups, skittles]
    for thisComponent in choose_sweetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choose_sweet" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choose_sweet_text* updates
        
        # if choose_sweet_text is starting this frame...
        if choose_sweet_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choose_sweet_text.frameNStart = frameN  # exact frame index
            choose_sweet_text.tStart = t  # local t and not account for scr refresh
            choose_sweet_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choose_sweet_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            choose_sweet_text.status = STARTED
            choose_sweet_text.setAutoDraw(True)
        
        # if choose_sweet_text is active this frame...
        if choose_sweet_text.status == STARTED:
            # update params
            pass
        
        # *sweet_1* updates
        
        # if sweet_1 is starting this frame...
        if sweet_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sweet_1.frameNStart = frameN  # exact frame index
            sweet_1.tStart = t  # local t and not account for scr refresh
            sweet_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sweet_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            sweet_1.status = STARTED
            sweet_1.setAutoDraw(True)
        
        # if sweet_1 is active this frame...
        if sweet_1.status == STARTED:
            # update params
            pass
        
        # *sweet_2* updates
        
        # if sweet_2 is starting this frame...
        if sweet_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sweet_2.frameNStart = frameN  # exact frame index
            sweet_2.tStart = t  # local t and not account for scr refresh
            sweet_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sweet_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            sweet_2.status = STARTED
            sweet_2.setAutoDraw(True)
        
        # if sweet_2 is active this frame...
        if sweet_2.status == STARTED:
            # update params
            pass
        
        # *sweet_3* updates
        
        # if sweet_3 is starting this frame...
        if sweet_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sweet_3.frameNStart = frameN  # exact frame index
            sweet_3.tStart = t  # local t and not account for scr refresh
            sweet_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sweet_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            sweet_3.status = STARTED
            sweet_3.setAutoDraw(True)
        
        # if sweet_3 is active this frame...
        if sweet_3.status == STARTED:
            # update params
            pass
        
        # *sweet_selection* updates
        waitOnFlip = False
        
        # if sweet_selection is starting this frame...
        if sweet_selection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sweet_selection.frameNStart = frameN  # exact frame index
            sweet_selection.tStart = t  # local t and not account for scr refresh
            sweet_selection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sweet_selection, 'tStartRefresh')  # time at next scr refresh
            # update status
            sweet_selection.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sweet_selection.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sweet_selection.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sweet_selection.status == STARTED and not waitOnFlip:
            theseKeys = sweet_selection.getKeys(keyList=['1','2','3'], ignoreKeys=["escape"], waitRelease=False)
            _sweet_selection_allKeys.extend(theseKeys)
            if len(_sweet_selection_allKeys):
                sweet_selection.keys = _sweet_selection_allKeys[-1].name  # just the last key pressed
                sweet_selection.rt = _sweet_selection_allKeys[-1].rt
                sweet_selection.duration = _sweet_selection_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from choose_sweet_code
        #set sweet reward selection
        if sweet_selection.keys == '1':
            sweet_reward = 'images/sweet_minioreo.jpg'
        elif sweet_selection.keys == '2':
            sweet_reward = 'images/sweet_minipbcups.png'
        elif sweet_selection.keys == '3':
            sweet_reward = 'images/sweet_skittles.png'
        
        # *minioreo* updates
        
        # if minioreo is starting this frame...
        if minioreo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            minioreo.frameNStart = frameN  # exact frame index
            minioreo.tStart = t  # local t and not account for scr refresh
            minioreo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(minioreo, 'tStartRefresh')  # time at next scr refresh
            # update status
            minioreo.status = STARTED
            minioreo.setAutoDraw(True)
        
        # if minioreo is active this frame...
        if minioreo.status == STARTED:
            # update params
            pass
        
        # *minipbcups* updates
        
        # if minipbcups is starting this frame...
        if minipbcups.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            minipbcups.frameNStart = frameN  # exact frame index
            minipbcups.tStart = t  # local t and not account for scr refresh
            minipbcups.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(minipbcups, 'tStartRefresh')  # time at next scr refresh
            # update status
            minipbcups.status = STARTED
            minipbcups.setAutoDraw(True)
        
        # if minipbcups is active this frame...
        if minipbcups.status == STARTED:
            # update params
            pass
        
        # *skittles* updates
        
        # if skittles is starting this frame...
        if skittles.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            skittles.frameNStart = frameN  # exact frame index
            skittles.tStart = t  # local t and not account for scr refresh
            skittles.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(skittles, 'tStartRefresh')  # time at next scr refresh
            # update status
            skittles.status = STARTED
            skittles.setAutoDraw(True)
        
        # if skittles is active this frame...
        if skittles.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choose_sweetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choose_sweet" ---
    for thisComponent in choose_sweetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('choose_sweet.stopped', globalClock.getTime())
    # check responses
    if sweet_selection.keys in ['', [], None]:  # No response was made
        sweet_selection.keys = None
    thisExp.addData('sweet_selection.keys',sweet_selection.keys)
    if sweet_selection.keys != None:  # we had a response
        thisExp.addData('sweet_selection.rt', sweet_selection.rt)
        thisExp.addData('sweet_selection.duration', sweet_selection.duration)
    thisExp.nextEntry()
    # the Routine "choose_sweet" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sweet_confirm" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('sweet_confirm.started', globalClock.getTime())
    sweet_confirm_image.setImage(sweet_reward)
    # keep track of which components have finished
    sweet_confirmComponents = [sweet_confirm_image]
    for thisComponent in sweet_confirmComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sweet_confirm" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sweet_confirm_image* updates
        
        # if sweet_confirm_image is starting this frame...
        if sweet_confirm_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sweet_confirm_image.frameNStart = frameN  # exact frame index
            sweet_confirm_image.tStart = t  # local t and not account for scr refresh
            sweet_confirm_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sweet_confirm_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            sweet_confirm_image.status = STARTED
            sweet_confirm_image.setAutoDraw(True)
        
        # if sweet_confirm_image is active this frame...
        if sweet_confirm_image.status == STARTED:
            # update params
            pass
        
        # if sweet_confirm_image is stopping this frame...
        if sweet_confirm_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sweet_confirm_image.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sweet_confirm_image.tStop = t  # not accounting for scr refresh
                sweet_confirm_image.frameNStop = frameN  # exact frame index
                # update status
                sweet_confirm_image.status = FINISHED
                sweet_confirm_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sweet_confirmComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sweet_confirm" ---
    for thisComponent in sweet_confirmComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('sweet_confirm.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    instructions_resp.keys = []
    instructions_resp.rt = []
    _instructions_resp_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [instructions_text, instructions_resp]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        
        # if instructions_text is starting this frame...
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions_text.status = STARTED
            instructions_text.setAutoDraw(True)
        
        # if instructions_text is active this frame...
        if instructions_text.status == STARTED:
            # update params
            pass
        
        # *instructions_resp* updates
        waitOnFlip = False
        
        # if instructions_resp is starting this frame...
        if instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_resp.frameNStart = frameN  # exact frame index
            instructions_resp.tStart = t  # local t and not account for scr refresh
            instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instructions_resp.status == STARTED and not waitOnFlip:
            theseKeys = instructions_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instructions_resp_allKeys.extend(theseKeys)
            if len(_instructions_resp_allKeys):
                instructions_resp.keys = _instructions_resp_allKeys[-1].name  # just the last key pressed
                instructions_resp.rt = _instructions_resp_allKeys[-1].rt
                instructions_resp.duration = _instructions_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.stopped', globalClock.getTime())
    # check responses
    if instructions_resp.keys in ['', [], None]:  # No response was made
        instructions_resp.keys = None
    thisExp.addData('instructions_resp.keys',instructions_resp.keys)
    if instructions_resp.keys != None:  # we had a response
        thisExp.addData('instructions_resp.rt', instructions_resp.rt)
        thisExp.addData('instructions_resp.duration', instructions_resp.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "start" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('start.started', globalClock.getTime())
    # keep track of which components have finished
    startComponents = [start_text]
    for thisComponent in startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_text* updates
        
        # if start_text is starting this frame...
        if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_text.frameNStart = frameN  # exact frame index
            start_text.tStart = t  # local t and not account for scr refresh
            start_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            start_text.status = STARTED
            start_text.setAutoDraw(True)
        
        # if start_text is active this frame...
        if start_text.status == STARTED:
            # update params
            pass
        
        # if start_text is stopping this frame...
        if start_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_text.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                start_text.tStop = t  # not accounting for scr refresh
                start_text.frameNStop = frameN  # exact frame index
                # update status
                start_text.status = FINISHED
                start_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('start.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/trials_part2.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation.started', globalClock.getTime())
        # Run 'Begin Routine' code from jitter_code
        #set jitter between 1 and 2.5s
        jitter = 1 + random() * 1.5
        jitter = (round(jitter, 1))
        
        # keep track of which components have finished
        fixationComponents = [asterisk]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *asterisk* updates
            
            # if asterisk is starting this frame...
            if asterisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                asterisk.frameNStart = frameN  # exact frame index
                asterisk.tStart = t  # local t and not account for scr refresh
                asterisk.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(asterisk, 'tStartRefresh')  # time at next scr refresh
                # update status
                asterisk.status = STARTED
                asterisk.setAutoDraw(True)
            
            # if asterisk is active this frame...
            if asterisk.status == STARTED:
                # update params
                pass
            
            # if asterisk is stopping this frame...
            if asterisk.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > asterisk.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    asterisk.tStop = t  # not accounting for scr refresh
                    asterisk.frameNStop = frameN  # exact frame index
                    # update status
                    asterisk.status = FINISHED
                    asterisk.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation.stopped', globalClock.getTime())
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "choose" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('choose.started', globalClock.getTime())
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from outcome_code
        #counterbalance left and right
        if (int(float(expInfo['participant'])) % 2) == 0:
            leftstim = salt_reward
            rightstim = sweet_reward
        else:
            leftstim = sweet_reward
            rightstim = salt_reward
        # keep track of which components have finished
        chooseComponents = [choose_text, key_resp]
        for thisComponent in chooseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "choose" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *choose_text* updates
            
            # if choose_text is starting this frame...
            if choose_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choose_text.frameNStart = frameN  # exact frame index
                choose_text.tStart = t  # local t and not account for scr refresh
                choose_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choose_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                choose_text.status = STARTED
                choose_text.setAutoDraw(True)
            
            # if choose_text is active this frame...
            if choose_text.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in chooseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "choose" ---
        for thisComponent in chooseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('choose.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from outcome_code
        #response coding
        if key_resp.keys == 'left':
            thisExp.addData('choice', leftstim)
            if left_ref == 0:
                thisExp.addData('outcome', '0')
            elif left_ref == 1:
                thisExp.addData('outcome', '1')
                leftcount += 1
        elif key_resp.keys == 'right':
            thisExp.addData('choice', rightstim)
            if left_ref == 1:
                thisExp.addData('outcome', '0')
            elif left_ref == 0:
                thisExp.addData('outcome', '1')
                rightcount += 1
        # the Routine "choose" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    # Run 'Begin Routine' code from end_code
    #rebind left/right to salt/sweet
    if (int(float(expInfo['participant'])) % 2) == 0:
        saltcount = leftcount
        sweetcount = rightcount
    else:
        sweetcount = leftcount
        saltcount = rightcount
    
    feedback = "End of experiment!" + '\n' + '\n' + 'Total reward:' + '\n' + str(sweetcount) + " sweet" + '\n' + str(saltcount) + " salty"
    end_text.setText(feedback)
    # keep track of which components have finished
    endComponents = [end_text]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # if end_text is stopping this frame...
        if end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_text.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.frameNStop = frameN  # exact frame index
                # update status
                end_text.status = FINISHED
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
