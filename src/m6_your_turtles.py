"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joe Krisciunas.
"""
###############################################################################
# Done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
import rosegraphics as rg
window = rg.TurtleWindow()
freddy = rg.SimpleTurtle()
jeffrey = rg.SimpleTurtle()
freddy.pen = rg.Pen('orange',3)
jeffrey.pen = rg.Pen('black',3)
freddy.speed = 200
jeffrey.speed = 5000
size = 500
for k in range(30):
    freddy.draw_circle(150)
    freddy.pen_up()
    freddy.forward(10)
    freddy.pen_down()
    size = size - 5

    jeffrey.draw_circle(149)
    jeffrey.pen_up()
    jeffrey.forward(11)
    jeffrey.pen_down()
    size= size-4

window.close_on_mouse_click()




#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################



