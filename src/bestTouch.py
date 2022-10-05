# CSCI 1100 Gateway to Computer Science
#
# This program displays an NxN grid of randomly colored squares.
# Click to place a square.
#
# run: python3 bestTouch.py N

from animate import *
from enum import Enum
import sys

# Splash page
backing = Image.rectangle(WIDTH, HEIGHT, Color.DarkGray)
instruction = Image.text("Click", Color.White, 80)
_x, _y = HEIGHT // 2 - 100, WIDTH // 2 - 40
splash = Image.placeImage(instruction, (_x, _y), backing)

# The program is either ready or running. Clicking changes the
# state from ready to running. This version is an improvement over
# betterTouch.py in that it uses an enumeration rather than global
# constants.
#
class State(Enum):
    Ready   = 0
    Running = 1

# toggle : state -> state
def toggle(state):
    if state == State.Ready:
        return State.Running
    else:
        return State.Ready

# Define a record type with model.n, model.image and model.state
#
class Model():
    def __init__(self, n, image, state):
        self.n = n
        self.image = image
        self.state = state

# view : model -> image
def view(model):
    return model.image
        
# touchUpdate : model * (int * int) * event -> model
def touchUpdate(model, xy, event):
    if event == Touch.Down:
        return model
    # event is Touch.Up
    if model.state == State.Ready:
        newState = toggle(model.state)
        return Model(model.n, backing, newState)
    # event is Touch.Up and model.state is State.Running
    side = WIDTH // model.n
    square = Image.rectangle(side, side, Color.random())
    (arrowX, arrowY) = xy
    (col, row) = (arrowX // side, arrowY // side)
    (x, y) = (col * side, row * side)
    image = Image.placeImage(square, (x, y), model.image)
    return Model(model.n, image, model.state)

# finished : model -> boolean
def finished(model):
    return False

# go : unit -> unit
def go():
    n = 0
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print("run: python3 bestTouch.py N")
        sys.exit()

    initialModel = Model(n, splash, State.Ready)

    Animate.start(model=initialModel,
                  view=view,                 # model -> image
                  touchUpdate=touchUpdate,   # model * xy * event -> model
                  stopWhen=finished)         # model -> boolean

go()
