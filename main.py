'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
'''drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0)
drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0)
drawCircle(myturtle=None, radius=0)
isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0)
setupDartboard'''

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
    # using draw line to draw a square or using forward and left
    top_right_x = top_left_x+width
    top_right_y = top_left_y
    bottom_right_x = top_right_x
    bottom_right_y = top_left_y-width
    bottom_left_x = top_left_x
    bottom_left_y = top_left_y-width
    drawLine(myturtle, top_left_x, top_left_y, top_right_x, top_right_y)
    drawLine(myturtle, top_right_x, top_right_y, bottom_right_x, bottom_right_y)
    drawLine(myturtle, bottom_right_x, bottom_right_y, bottom_left_x, bottom_left_y)
    drawLine(myturtle, bottom_left_x, bottom_left_y, top_left_x, top_left_y)


def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
    # set turtle to starting point
    myturtle.hideturtle()
    myturtle.goto(x_start, y_start)
    myturtle.showturtle()
    myturtle.goto(x_end, y_end)

def drawCircle(myturtle=None, radius=0):
    myturtle.circle(radius)


def setUpDartboard(myscreen=None, myturtle=None):
    myscreen.setworldcoordinates(-4, -4, 4, 4)
    # set tutle to top left corner of squre and start
    # drawing in couter-clock direction
    myturtle.penup()
    myturtle.goto(-1, 1)
    myturtle.pendown()
    drawSquare(myturtle, 2, -1, 1)

    # set turtle to 0,0 and then draw turtle
    myturtle.penup()
    myturtle.goto(0, -1)
    myturtle.pendown()
    drawCircle(myturtle, 1)

    # draw x-axis
    myturtle.penup()
    myturtle.goto(-1, 0)
    myturtle.pendown()
    drawLine(myturtle, -1, 0, 1, 0)

    # draw y-axis
    myturtle.penup()
    myturtle.goto(0, -1)
    myturtle.pendown()
    drawLine(myturtle, 0, -1, 0, 1)
    pass


def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
    # current turtle position from last drawing position (dart landing/drawing point)
    # to axis center
    return myturtle.distance(circle_center_x, circle_center_y) < radius


def throwDart(myturtle=None):
    # using random to get uniformly distributed value for x-cord and y-cord
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # set position to where dart will land and draw a blue dot
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.dot(5, 'blue')


def playDarts(myturtle=None):
    # Asks how many turns you want the two players to play
    turns = int(input('How many turns do you want to play'))
    player_a_score = 0
    player_b_score = 0
    for i in range(turns):
        throwDart(myturtle)
        if isInCircle(myturtle=myturtle, radius=1):
            print("Player A hit the dartboard!")
            myturtle.dot(5, 'red')
            player_a_score += 1
    for i in range(turns):
        throwDart(myturtle)
        if isInCircle(myturtle=myturtle, radius=1):
            print("Player B hit the dartboard!")
            myturtle.dot(5, 'red')
            player_b_score += 1
    print('Player A scored: ', player_a_score, ' Player B scored: ', player_b_score)


def montePi(myturtle=None, num_darts=0):
    # Asks how many times you want to run the simulation
    inside_count = 0
    for i in range(num_darts):
        throwDart(myturtle)
        if isInCircle(myturtle=myturtle, radius=1):
            print("You hit the dartboard!")
            myturtle.dot(5, 'red')
            inside_count += 1
    return 4 * (inside_count/num_darts)
    


#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
        if isInCircle(myturtle=darty, radius=1):
          print("You hit the dartboard!")
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    playDarts(myturtle=darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(myturtle=darty, num_darts=number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
