from turtle import Turtle, Screen
import time 

window =Screen()
window.setup(700,700)
window.bgcolor('black')
window.title("BING BONG")

class Paddle (Turtle):
  def __init__(self, position):
    super().__init__() 
    self.shape("square")
    self.penup()
    self.color("white")
    self.goto(position)
    self.shapesize(9,1)
    
  def move_up(self):
    if self.ycor()< 190:
      self.goto(self.xcor(),self.ycor()+80)
    
  def move_down(self):
    if self.ycor() >-190:
      self.goto(self.xcor(),self.ycor()-80)
 
#check the move of paddles       
def move_paddle(x,y):
    
    if y>0:
      if x>0:
        l_paddle.move_up()
      else:
        r_paddle.move_up()
    else:
      if x>0:
        l_paddle.move_down()
      else:
        r_paddle.move_down() 
    
          
class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("white")
    self.x_move=10
    self.y_move=10

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()  
    self.score=0
    self.timer=60
    #self.goto(200,200)
    

  def display_score(self):
    self.clear()
    self.write(f"{self.score}")  
    
  def score_timer(self):
    self.clear()
    self.write(f"00:{round(self.timer)}")
    self.timer-=0.04
  
  #def end_time(self):
#    if self.timer==0:
      
window.tracer(0)
r_paddle =Paddle ((-650,0))
r_paddle.color("red")

l_paddle=Paddle((650,0))
l_paddle.color("blue")

ball=Ball()

l_score=Scoreboard()
l_score.goto(300,200)
l_score.display_score()
r_score=Scoreboard()
r_score.goto(-400,200)
r_score.display_score()

timer=Scoreboard()
sleep=0.04
timer.score_timer()
timer.goto(-70,200)
result=Scoreboard()
result.goto(-250,0)
game_on=True

while game_on:
   window.update()
   timer.score_timer()
   ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
   time.sleep(abs(sleep))
   if ball.ycor() >280 or ball.ycor() <-280:
     ball.y_move*=-1
     
   if ( ball.xcor()>620 and ball.distance(l_paddle)<90) or (ball.xcor()<-620 and ball.distance(r_paddle)<90):
     ball.x_move*=-1
     sleep-=0.008
    
  
   if ball.xcor()>=740 or ball.xcor()<-740:
     ball.x_move*=-1     
     ball.goto(0,0) 
     sleep=0.04
    
          
   if ball.xcor()>=730 :
      r_score.score+=1
      r_score.display_score()
      
   if ball.xcor()<-730:
      l_score.score+=1
      l_score.display_score()
      
   if timer.timer== 0 or timer.timer <= 0:
     game_on=False 
     if l_score.score > r_score.score:
       result.write("        GAME OVER\n blue player is a winner")
     elif r_score.score> l_score.score:
       result.write("        GAME OVER\n red player is a winner ")
     else:
       result.write("        GAME OVER \n draw with two players ")
   window.onscreenclick(move_paddle)   
   
    
window.exitonclick()
