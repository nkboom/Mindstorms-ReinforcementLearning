#SARSA Learning - Mindstorms
import random
from random import choice
from random import sample
import argparse
import GitSARSA

#Read in Command-Line Arguments via argparse - MindSARSA.py --Iter <#> --HappyStart <#> --Rand <0 or 1> --TargetLocation <#>
parser = argparse.ArgumentParser()
parser.add_argument("--Iter", type=int, default = None)
parser.add_argument("--Rand", type=int, default = None)
parser.add_argument("--HappyStart", type=int, default=None)
parser.add_argument("--TargetLocation", type=int, default=None)
args = parser.parse_args()

#Defining What Code to Execute with each Argument via argparse
if args.Iter is not None:
    Iter = args.Iter

if args.Rand == 1:
    HappyStart = random.choice([10,11,12,13,14,15,18,19,20,21,22,23,26,27,28,29,30,31,34,35,36,37,38,39])
    print
    print "Random Conditions:"
    print "HappyStart: " + str(HappyStart)
    
    TargetLocation = random.choice([10,11,12,13,14,15,18,19,20,21,22,23,26,27,28,29,30,31,34,35,36,37,38,39])
    while TargetLocation == HappyStart:
        TargetLocation = random.choice([10,11,12,13,14,15,18,19,20,21,22,23,26,27,28,29,30,31,34,35,36,37,38,39])
    Goal = [TargetLocation]
    print "TargetLocation: " + str(TargetLocation)
          
    Cliff1 = [1,2,3,4,5,6,7,8,9,16,17,24,25,32,33,40,41,42,43,44,45,46,47,48,49]
    TopRow = [34,35,36,37,38,39]
    Cliff2 = random.sample([10,11,12,13,14,15,18,19,20,21,22,23,26,27,28,29,30,31,34,35,36,37,38,39], 4)
    for number in Cliff2:
        while number == HappyStart or number == TargetLocation:
            Cliff2 = random.sample([10,11,12,13,14,15,18,19,20,21,22,23,26,27,28,29,30,31,34,35,36,37,38,39], 4)
    print Cliff2

if args.Rand == 0:
    Cliff1 = [1,2,3,4,5,6,7,8,9,16,17,24,25,32,33,40,41,42,43,44,45,46,47,48,49]
    Cliff2 = [11,12,13,14]
    TopRow = [34,35,36,37,38,39]
if args.HappyStart is not None:
    HappyStart = args.HappyStart
if args.TargetLocation is not None:
    Goal = [args.TargetLocation]

#Mindstorms Specific ev3dev commands and action execution
from time import sleep
from ev3dev import *

directions = [-1,1,-8,8]

lmotor = large_motor(OUTPUT_B); assert lmotor.connected
rmotor = large_motor(OUTPUT_C); assert rmotor.connected
irsens = infrared_sensor();     assert irsens.connected
ts     = touch_sensor()
irsens.mode = 'IR-PROX'
lmotor.speed_regulation_enabled = 'on'
rmotor.speed_regulation_enabled = 'on'
motors = [lmotor, rmotor]
distance = irsens.value()
    
def goInDirection(mindmove):
    if mindmove == 8:
        lmotor.run_forever(speed_sp=400)
        rmotor.run_forever(speed_sp=400)
        sleep(1.38)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=0)
        rmotor.run_forever(speed_sp=0)
        sleep(0.7)
    elif mindmove == -8:
        lmotor.run_forever(speed_sp=-400)
        rmotor.run_forever(speed_sp=-400)
        sleep(1.38)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=0)
        rmotor.run_forever(speed_sp=0)
        sleep(0.7)
    elif mindmove == 1:
        lmotor.run_forever(speed_sp=400)
        rmotor.run_forever(speed_sp=-400)
        sleep(0.94)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=400)
        rmotor.run_forever(speed_sp=400)
        sleep(1.47)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=-400)
        rmotor.run_forever(speed_sp=400)
        sleep(0.99)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=0)
        rmotor.run_forever(speed_sp=0)
        sleep(0.7)
    elif mindmove == -1:
        rmotor.run_forever(speed_sp=400)
        lmotor.run_forever(speed_sp=-400)
        sleep(0.94)
        lmotor.stop
        rmotor.stop
        rmotor.run_forever(speed_sp=400)
        lmotor.run_forever(speed_sp=400)
        sleep(1.47)
        lmotor.stop
        rmotor.stop
        rmotor.run_forever(speed_sp=-400)
        lmotor.run_forever(speed_sp=400)
        sleep(0.99)
        lmotor.stop
        rmotor.stop
        lmotor.run_forever(speed_sp=0)
        rmotor.run_forever(speed_sp=0)
        sleep(0.7)
    else:
        print "BAD VALUE!"

def goBacktoStart(mindmoveback):
    if mindmoveback == 1:
        goInDirection(1)
        goInDirection(8)
    elif mindmoveback == 2:
        goInDirection(8)
    elif mindmoveback == 3:
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 4:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 5:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 6:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 7:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 8:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 9:
        goInDirection(1)
    elif mindmoveback == 11:
        goInDirection(-1)
    elif mindmoveback == 12:
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 13:
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 14:
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 15:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
    elif mindmoveback == 16:
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 17:
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 24:
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 25:
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 32:
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 33:
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 40:
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(8)
    elif mindmoveback == 41:
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 42:
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 43:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 44:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 45:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 46:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    elif mindmoveback == 47:
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-1)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(-8)
        goInDirection(1)
    else:
        print "Didn't Work!"


#Call class SARSA from file GitSARSA.py
AI = GitSARSA.Sarsa(actions=directions, epsilon=0.1, alpha=0.2, gamma=0.9)

#Sets up State Space and Layout of Grid Mindstorms will be moving on and learning from (using SARSA learning algorithm)
HappyLastAction = None
for number in range(2000000):
    if number < Iter + 1: 
        if HappyLastAction is None:
            HappyLastState = HappyStart
            print "START: HappyFace - " + str(HappyLastState)
            HappyLastAction = AI.chooseAction(HappyLastState)
            goInDirection(HappyLastAction)
            HappyCurrentState = HappyLastState + HappyLastAction
            HappyCurrentAction = AI.chooseAction(HappyCurrentState)

            if HappyLastAction == -HappyCurrentAction:
                reward = -50
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                HappyLastState = HappyCurrentState
                HappyLastAction = HappyCurrentAction
                goInDirection(HappyLastAction)
                HappyCurrentState = HappyCurrentState + HappyLastAction
                HappyCurrentAction = AI.chooseAction(HappyCurrentState)
                print "HappyFace RETRACED steps"
            if HappyCurrentState in Cliff1 or HappyCurrentState in Cliff2:
                reward = -100
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                print "END: (Cliff Fall): " + str(HappyCurrentState) + ". REWARD: " + str(reward) + "."
                goBacktoStart(HappyCurrentState)
                HappyLastAction = None
            else:
                reward = -1
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                print "HappyFace: " + str(HappyCurrentState) + ". REWARD: " + str(reward) + "."
                HappyLastState = HappyCurrentState
                HappyLastAction = HappyCurrentAction
                goInDirection(HappyLastAction)
                HappyCurrentState = HappyCurrentState + HappyLastAction
                HappyCurrentAction = AI.chooseAction(HappyCurrentState)
                            
        if HappyLastAction is not None:
        
            if HappyLastAction == -HappyCurrentAction:
                reward = -50
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                HappyLastState = HappyCurrentState
                HappyLastAction = HappyCurrentAction
                goInDirection(HappyLastAction)
                HappyCurrentState = HappyCurrentState + HappyLastAction
                HappyCurrentAction = AI.chooseAction(HappyCurrentState)
                print "HappyFace RETRACED steps"
            if HappyCurrentState in Cliff1 or HappyCurrentState in Cliff2:
                reward = -100
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                print "END: (Cliff Fall): " + str(HappyCurrentState) + ". REWARD: " + str(reward) + "."
                goBacktoStart(HappyCurrentState)
                HappyLastAction = None
            elif HappyCurrentState in Goal:
                reward = 10
                print "END: (Goal): " + str(HappyCurrentState) + ". REWARD: " + str(reward) + "."
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                goBacktoStart(HappyCurrentState)
                HappyLastAction = None
            else:     
                reward = -1
                AI.learn(HappyLastState, HappyLastAction, reward, HappyCurrentState, HappyCurrentAction)
                print "HappyFace: " + str(HappyCurrentState) + ". REWARD: " + str(reward) + "."
                HappyLastState = HappyCurrentState
                HappyLastAction = HappyCurrentAction
                goInDirection(HappyLastAction)
                HappyCurrentState = HappyLastState + HappyLastAction
                HappyCurrentAction = AI.chooseAction(HappyCurrentState)
        
