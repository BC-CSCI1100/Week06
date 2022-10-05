# CSCI 1100 Gateway to Computer Science
#
# This program displays an NxN grid of randomly colored squares.
# Click to place a square.
#
# run: python3 betterTouch.py N

from animate import *
import sys

# Splash page
backing = Image.rectangle(WIDTH, HEIGHT, Color.DarkGray)
instruction = Image.text("Click", Color.White, 80)
_x, _y = HEIGHT // 2 - 100, WIDTH // 2 - 40
splash = Image.placeImage(instruction, (_x, _y), backing)

# The program is either ready or running. Clicking changes the state
# from ready to running. We'll use a global symbolic constant Ready
# to represent the ready state and a global constant Running to 
# represent the running state.
#
Ready   = 0       # These symbols are defined at the top-level so they
Running = 1       # are "global" constants, i.e., available everywhere.

# toggle : state -> state
def toggle(state):
    if state == Ready:
        return Running
    else:
        return Ready

# Define a record type Model with n, image and state fields. If
# model is a variable of this type, the fields are accessed as in
# model.n, model.image and model.state.
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
    if model.state == Ready:
        newState = toggle(model.state)
        return Model(model.n, backing, newState)
    # event is Touch.Up and model.state is running
    side = WIDTH // model.n
    square = Image.rectangle(side, side, Color.random())
    (x0, y0) = xy
    (col, row) = (x0 // side, y0 // side)
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
        print("run: python3 betterTouch.py N")
        sys.exit()

    initialModel = Model(n, splash, Ready)

    Animate.start(model=initialModel,
                  view=view,                 # model -> image
                  touchUpdate=touchUpdate,   # model * xy * event -> model
                  stopWhen=finished)         # model -> boolean

go()
