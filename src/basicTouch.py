# CSCI 1100 Gateway to Computer Science
#
# This program displays an NxN grid of randomly colored squares.
# Click to place a square.
#
# run: python3 basicTouch.py N

from animate import *
import sys

# Splash page
backing = Image.rectangle(WIDTH, HEIGHT, Color.DarkGray)
instruction = Image.text("Click", Color.White, 80)
_x, _y = HEIGHT // 2 - 100, WIDTH // 2 - 40
splash = Image.placeImage(instruction, (_x, _y), backing)

# The program is either ready or running. Clicking changes the
# state from ready to running. 
# 
# Attention: We'll use 0 for the ready state and 1 for the running state.

# toggle : state -> state
def toggle(state):
    if state == 0:
        return 1
    else:
        return 0

# Attention: We'll use a 3-tuple (n, image, state) to represent the overall
# state of our application, i.e., the model.

# view : model -> image
def view(model):
    (_, image, _) = model
    return image

# touchUpdate : model * (int * int) * event -> model
def touchUpdate(model, xy, event):
    (n, image, state) = model
    if event == Touch.Down:
        return model
    # event is Touch.Up
    if state == 0:
        newState = toggle(state)
        return (n, backing, newState)
    # event is Touch.Up and model state is running
    side = WIDTH // n
    square = Image.rectangle(side, side, Color.random())
    (arrowX, arrowY) = xy
    (col, row) = (arrowX // side, arrowY // side)  # NB effect of int div //
    (x, y) = (col * side, row * side)
    image = Image.placeImage(square, (x, y), image)
    return (n, image, state)

# finished : model -> boolean
def finished(model):
    return False

# go : unit -> unit
def go():
    n = 0
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print("run: python3 basicTouch.py N")
        sys.exit()

    initialModel = (n, splash, 0)

    Animate.start(model=initialModel,
                  view=view,               # model -> image
                  touchUpdate=touchUpdate, # model * xy * event -> model
                  stopWhen=finished)       # model -> boolean

go()
