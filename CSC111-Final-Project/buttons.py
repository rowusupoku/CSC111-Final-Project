from graphics import *

class Buttons: 
  def __init__ (self, win, position1, position2):
    
    self.__next= None
    self.__back= None 
    self.construct(position1, position2)
    self.__win = win
  
  def construct(self, position1, position2):
    
    self.p1=Point(position1.getX(), position1.getY())
    self.p2=Point(position2.getX(), position2.getY())
    self.__next = Rectangle(self.p1, self.p2) 
    self.__next.setFill("Chocolate")
    
  def draw(self, win):
    self.__next.draw(win)

  def undraw(self):
    self.__next.undraw()
  
  def inside(self, win, position, rectangle):
    """ Is point inside rectangle? """
    print(self.p1, self.p2,  position)
    WIDTH, HEIGHT = 1080, 600
    
    centerPoint = Point(WIDTH / 2, HEIGHT / 2)
    text = Text(centerPoint, "")
    text.draw(win)
    
    return self.p1.getX() < position.getX() < self.p2.getX() and self.p1.getY() < position.getY() < self.p2.getY() 
