from turtle import *

def draw_s():
    """Draws the letter 'S'."""
    penup()
    goto(-80, 0)  # Position for 'S'
    pendown()
    pensize(10)
    seth(-45)
    circle(30, 225)  # Draw upper half circle
    fd(30)
    seth(135)
    circle(-30, 135)  # Draw lower half circle
    fd(30)

def draw_o():
    """Draws the letter 'O'."""
    penup()
    goto(50, 0)  # Position for 'O'
    pendown()
    pensize(10)
    seth(0)
    circle(30)  # Draw a full circle to form 'O'

def draw_so():
    """Draws the letters 'SO' in a coordinated manner."""
    speed(5)
    bgcolor("lightyellow")
    color("blue")
    draw_s()  # Draw letter 'S'
    draw_o()  # Draw letter 'O'
    done()

# Draw the letters "SO"
draw_so()
