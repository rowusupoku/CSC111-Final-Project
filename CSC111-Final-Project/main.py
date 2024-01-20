# ------------------------------------------------------
#    Team Name:RNR
# Team Members:Rachel, Natali, Renee
#        Peers:
#   References:
# ------------------------------------------------------

## Basic Function to demonstrate test suite.
from graphics import *
from buttons import *

#The dimensions of our screen
WIDTH = 1080
HEIGHT = 600

# Our Avatar Alexis
avatar1 = Image(Point(545, 320), "images/avatar/AlexisTexas.png")

#the questions we ask the user
question = Text(Point(190, 200), "Do you like the outfit? \n Pick: yes or no")

text = Text(Point(524, 250),
            "Hey! Where you going? Pick: school, gym, or party")
text.setFace("courier")
text.setStyle("bold")
text.setTextColor("Chocolate")
text.setSize(15)

# Introducing Alexis our avatar
intro = Text(Point(800, 250), "Hi! I'm Alexis")

# The text explaining how to layer the outfit
text2 = Text(
    Point(800, 300),
    "Adjust the layers \n to desired look \n\n For best result: \n Choose shoes first \n accessories last"
)
text2.setFace("courier")
text2.setStyle("bold")
text2.setTextColor("Chocolate")
text2.setSize(12)

#Invalid input warning message
invalid = Text(Point(524, 250),
               "Invalid input, please click the run button to restart")
invalid.setFace("courier")
invalid.setSize(10)
invalid.setStyle("bold")
invalid.setTextColor("Chocolate")

# Creating the background and first screen
win = GraphWin("Smithie Dress Up Game", WIDTH, HEIGHT)
background = Image(Point(575, 300), "images/Dress Up Desktop.png")
background.draw(win)

#The list of oufits in the game
tops = [
    Image(Point(545, 320), "images/tops/btop1.png"),
    Image(Point(545, 320), "images/tops/gtop1.png"),
    Image(Point(545, 320), "images/tops/ptop1.png"),
    Image(Point(545, 320), "images/tops/otop2.png")
]

bottoms = [
    Image(Point(545, 320), "images/bottoms/bbottom1.png"),
    Image(Point(545, 320), "images/bottoms/gbottom1.png"),
    Image(Point(545, 320), "images/bottoms/pbottom1.png"),
    Image(Point(545, 320), "images/bottoms/obottom1.png"),
    Image(Point(545, 320), "images/bottoms/gbottom2.png")
]

shoes = [
    Image(Point(545, 320), "images/shoes/bshoes1.png"),
    Image(Point(545, 320), "images/shoes/gshoes1.png"),
    Image(Point(545, 320), "images/shoes/pshoes1.png")
]

accessories = [
    Image(Point(545, 320), "images/accessories/baccess1.png"),
    Image(Point(545, 320), "images/accessories/gaccess1.png"),
    Image(Point(545, 320), "images/accessories/paccess1.png"),
    Image(Point(545, 320), "images/accessories/oaccess1.png"),
    Image(Point(545, 320), "images/accessories/oaccess2.png"),
    Image(Point(545, 320), "images/accessories/oaccess3.png")
]

#The Buttons that iterate through clothes list
abutton1 = Buttons(win, Point(350, 150), Point(375, 165))
tbutton1 = Buttons(win, Point(350, 235), Point(375, 250))
bbutton1 = Buttons(win, Point(350, 350), Point(375, 365))
sbutton1 = Buttons(win, Point(350, 475), Point(375, 490))

#The done button that closes game
donebutton = Buttons(win, Point(70, 460), Point(150, 500))
doneW = Text(Point(110, 480), "DONE")

#Entry Boxs
input_box = Entry(Point(524, 350), 15)
otherinput_box = Entry(Point(190, 300), 10)


def myTestedFunction(val: bool) -> str:
    if val:
        return "Happy"
    else:
        return "Sad"


def aestheticChoice(choice: str) -> str:
    """ 
    Constructs and prints the outfit the user selects based on their event/asthetic choice.
  
    param choice: (str) The choice the user makes/selects
    return: (str) The name of the outfit is printed to the console and the graphics for the outfit displayed on the window based on the user's selection
    """
    if choice == "school":
        preppyb = bottoms[2]
        preppyb.draw(win)

        preppyt = tops[2]
        preppyt.draw(win)

        preppys = shoes[2]
        preppys.draw(win)

        preppya = accessories[2]
        preppya.draw(win)

        return ("school outfit is printed to window")

    elif choice == "gym":
        gyms = shoes[1]
        gyms.draw(win)

        gymb = bottoms[1]
        gymb.draw(win)

        gymt = tops[1]
        gymt.draw(win)

        gyma = accessories[1]
        gyma.draw(win)

        return ("gym outfit is printed to window")

    elif choice == "party":
        bbls = shoes[0]
        bbls.draw(win)

        bblb = bottoms[0]
        bblb.draw(win)

        bblt = tops[0]
        bblt.draw(win)

        bbla = accessories[0]
        bbla.draw(win)

        return ("party outfit is printed to window")


def undrawChoice(choice: str):
    """
  Undraws the outfits and creates the  buttons that allows the user to make their own decisions about what the avatar wears. The buttons appear only if they decide they don't like the outfit that was constructed. 

  param choice: (str) The answer for the question that asks the user if you like they like the oufit or not.
  return: No return
  
  """
    if choice.lower() == 'yes':
        preppyb = bottoms[2]
        preppyb.undraw()

        preppyt = tops[2]
        preppyt.undraw()

        preppys = shoes[2]
        preppys.undraw()

        preppya = accessories[2]
        preppya.undraw()

        gyms = shoes[1]
        gyms.undraw()

        gymb = bottoms[1]
        gymb.undraw()

        gymt = tops[1]
        gymt.undraw()

        gyma = accessories[1]
        gyma.undraw()

        bbls = shoes[0]
        bbls.undraw()

        bblb = bottoms[0]
        bblb.undraw()

        bblt = tops[0]
        bblt.undraw()

        bbla = accessories[0]
        bbla.undraw()

        avatar1.undraw()
        question.undraw()
        text2.undraw()
        text2.undraw()

        end = Text(Point(524, 250), "Thank you for playing! :)")
        end.setFace("courier")
        end.setStyle("bold")
        end.setTextColor("Chocolate")
        end.setSize(15)
        end.draw(win)
        intro.undraw()

    elif choice.lower() == 'no':
        preppyb = bottoms[2]
        preppyb.undraw()

        preppyt = tops[2]
        preppyt.undraw()

        preppys = shoes[2]
        preppys.undraw()

        preppya = accessories[2]
        preppya.undraw()

        gyms = shoes[1]
        gyms.undraw()

        gymb = bottoms[1]
        gymb.undraw()

        gymt = tops[1]
        gymt.undraw()

        gyma = accessories[1]
        gyma.undraw()

        bbls = shoes[0]
        bbls.undraw()

        bblb = bottoms[0]
        bblb.undraw()

        bblt = tops[0]
        bblt.undraw()

        bbla = accessories[0]
        bbla.undraw()

        question.undraw()
        intro.undraw()
        abutton1.draw(win)
        tbutton1.draw(win)
        bbutton1.draw(win)
        sbutton1.draw(win)
        donebutton.draw(win)
        text2.draw(win)
        doneW.setSize(10)
        doneW.setTextColor("White")
        doneW.draw(win)

    else:
        preppyb = bottoms[2]
        preppyb.undraw()

        preppyt = tops[2]
        preppyt.undraw()

        preppys = shoes[2]
        preppys.undraw()

        preppya = accessories[2]
        preppya.undraw()

        gyms = shoes[1]
        gyms.undraw()

        gymb = bottoms[1]
        gymb.undraw()

        gymt = tops[1]
        gymt.undraw()

        gyma = accessories[1]
        gyma.undraw()

        bbls = shoes[0]
        bbls.undraw()

        bblb = bottoms[0]
        bblb.undraw()

        bblt = tops[0]
        bblt.undraw()

        bbla = accessories[0]
        bbla.undraw()

        avatar1.undraw()
        question.undraw()
        invalid.draw(win)
        intro.undraw()

        while True:
            clickPoint = win.getMouse()
            if clickPoint is None:
                text.setText("")
            else:
                win.close()
                exit()
                return


def userInput():
    """
    Checks the occasion choice that the user makes 
    """
    choice = input_box.getText()
    if choice.lower() == "school" or choice == "party" or choice == "gym":

        #Draws the users avatar and adds clothes
        avatar1.draw(win)
        print(aestheticChoice(choice))

        #Ask the user if they like the outfit
        question.setFace("courier")
        question.setSize(10)
        question.setStyle("bold")
        question.setTextColor("Chocolate")
        question.draw(win)

        # Introduces Alexis
        intro.draw(win)
        intro.setFace("courier")
        intro.setStyle("bold")
        intro.setTextColor("Chocolate")
        intro.setSize(15)

    else:
        invalid.draw(win)
        while True:
            clickPoint = win.getMouse()
            if clickPoint is None:
                text.setText("")
            else:
                win.close()
                exit()
                return


def main():
    print("Program Starts")
    print(myTestedFunction(True))

    #Ask the user where they're going
    text.draw(win)
    input_box.draw(win)

    while True:
        #User inputs a choice to the input box
        u = win.checkKey()
        if u == 'Return':
            text.undraw()
            input_box.undraw()
            userInput()
            otherinput_box.draw(win)
            break

        # Instructs the program how to layer the clothes. The code that makes the buttons work
    while True:
        y = win.checkKey()
        if y == 'Return':
            choice2 = otherinput_box.getText()
            otherinput_box.undraw()
            undrawChoice(choice2)
            acounter = -1
            bcounter = -1
            tcounter = -1
            scounter = -1

            while True:
                clickPoint = win.getMouse()
                if clickPoint is None:
                    text.setText("")
                elif abutton1.inside(win, clickPoint, next):
                    # for a in range(len(accessories)):
                    accessories[acounter].undraw()
                    acounter = (acounter + 1) % 6
                    accessories[acounter].draw(win)
                    clickPoint = win.getMouse()
                elif bbutton1.inside(win, clickPoint, next):
                    bottoms[bcounter].undraw()
                    bcounter = (bcounter + 1) % 5
                    bottoms[bcounter].draw(win)
                    clickPoint = win.getMouse()
                elif tbutton1.inside(win, clickPoint, next):
                    tops[tcounter].undraw()
                    tcounter = (tcounter + 1) % 4
                    tops[tcounter].draw(win)
                    clickPoint = win.getMouse()
                elif sbutton1.inside(win, clickPoint, next):
                    shoes[scounter].undraw()
                    scounter = (scounter + 1) % 3
                    shoes[scounter].draw(win)
                    clickPoint = win.getMouse()
                elif donebutton.inside(win, clickPoint, next):
                    close = Text(Point(524, 250), "Thank you for playing! :)")
                    close.setFace("courier")
                    close.setSize(25)
                    close.setStyle("bold")
                    close.setTextColor("Chocolate")
                    close.draw(win)

                    avatar1.undraw()
                    intro.undraw()
                    accessories[acounter].undraw()
                    bottoms[bcounter].undraw()
                    tops[tcounter].undraw()
                    shoes[scounter].undraw()
                    text2.undraw()
                    question.undraw()
                    abutton1.undraw()
                    bbutton1.undraw()
                    tbutton1.undraw()
                    sbutton1.undraw()
                    donebutton.undraw()
                    doneW.undraw()


if __name__ == "__main__":
    main()
