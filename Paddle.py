from tkinter import*
import random
import time
counter=0
counter1=0
start=5
life=0
life1=0
tk =Tk()
tk.title("crazykesari!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas1 = Canvas(tk,height=50,width=1000,bd=0,bg="pink",highlightthickness = 0)
canvas1.pack()
canvas = Canvas(tk,height=700,width=1000,bd=0,bg="black",highlightthickness = 0)
canvas.pack()

canvas1.create_line(500,0,500,50,fill = "white")
canvas.create_line(500,0,500,1000,fill = "white")
canvas1.create_text(570,30,text="Player2",font=("bold",25))
canvas1.create_text(70,30,text="Player1",font=("Bold",25))
canvas1.create_text(320,30,text="Score:",font=20)
canvas1.create_text(850,30,text="Score:",font=20)

canvas1.create_text(365,30,text=counter,font=20)

canvas1.create_text(895,30,text=counter1,font=20)
tk.update()
class Ball:
  def __init__(self,canvas,paddle,paddle1,color):
    self.canvas = canvas
    self.paddle = paddle
    self.paddle1 =paddle1
    self.id = canvas.create_oval(10,10,35,35,fill =color )
    self.canvas.move(self.id,480,400)
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    start=[-3,-2,-1,1,2,3]
    random.shuffle(start)
    self.x = start[0]
    self.y = -3
    self.hit_leftcorner =False
    self.hit_rightcorner =False
    
	
  def hit_paddle(self,pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if pos[1]>= paddle_pos[1] and pos[1]<= paddle_pos[3] :
     if pos[0]>= paddle_pos[0] and pos[0] <= paddle_pos[2] :
       return True
     return False
 	
   
  def hit_paddle1(self,pos):
    paddle1_pos = self.canvas.coords(self.paddle1.id)
    if pos[1]>= paddle1_pos[1] and pos[1]<= paddle1_pos[3] :
     if pos[2]>= paddle1_pos[0] and pos[2] <= paddle1_pos[2] :
       return True
     return False
      
  def draw(self) :
    self.canvas.move(self.id,self.x,self.y)
    pos = self.canvas.coords(self.id)
    if pos[0]<=0:
     self.hit_leftcorner=True
    if pos[2]>= self.canvas_width :
     self.hit_rightcorner=True
    if pos[1]<=0 :
     self.y=3
    if pos[3] >= self.canvas_height :
      self.y =-3
    if self.hit_paddle(pos) == True:
      self.x=3
      self.score1(True)
      
    if self.hit_paddle1(pos) ==True :
      self.x=-3
      self.score2(True)
      
  def score1(self,val):
     global counter

     if val==True :
      a = canvas1.create_text(365,30,text=counter,font=1,fill="pink")
      counter = counter + 5
      a = canvas1.create_text(365,30,text=counter,font=20)
     
         
  def score2(self,val1) :
     global counter1
     if val1 == True :
      a= canvas1.create_text(895,30,text=counter1,font=20,fill="pink")
      counter1 = counter1 + 5
      a= canvas1.create_text(895,30,text=counter1,font=20)

class Paddle :
   def __init__(self,canvas,color) :
      self.canvas = canvas
      self.id = canvas.create_rectangle(10,10,33,200,fill = color)
      self.canvas_height=self.canvas.winfo_height()
      self.canvas.move(self.id,0,300)
      self.y =0
      self.canvas.bind_all("<KeyPress-Left>",self.turn_up)  
      

      self.canvas.bind_all("<KeyPress-Down>",self.turn_down)
   def draw(self) :
    pos = self.canvas.coords(self.id)
    self.canvas.move(self.id,0,self.y)
    if pos[1]<=0 :
     self.y=0.5
    if pos[3]>= self.canvas_height :
     self.y=-0.5
    
   def turn_up(self,evt):
    self.y=-5
   
   def turn_down(self,evt):
    self.y=5
	

class Paddle1 :
   def __init__(self,canvas,color) :
      self.canvas = canvas
      self.id = canvas.create_rectangle(10,10,33,200,fill = color)
      self.canvas_height=self.canvas.winfo_height()
      self.canvas.move(self.id,965,300)
      self.y =0
      self.canvas.bind_all("<KeyPress-Up>",self.turn_left)  
      self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
   def draw(self) :
    pos = self.canvas.coords(self.id)
    self.canvas.move(self.id,0,self.y)
    if pos[1]<=0 :
     self.y=0.5
    if pos[3]>= self.canvas_height :
     self.y=-0.5
    
   
   def turn_left(self,evt):
    self.y=-5
   
   def turn_right(self,evt):
    self.y=5
paddle = Paddle(canvas,"blue")	 
paddle1 = Paddle1(canvas,"green")
	  
ball = Ball(canvas,paddle,paddle1,"yellow")	

if ball.hit_leftcorner == False :
    ball.draw()
    paddle.draw()
    paddle1.draw()
   

if ball.hit_rightcorner == False :
    ball.draw()
    paddle.draw()
    paddle1.draw()
   
tk.update()
time.sleep(5)

while 1 :
    
  
   if ball.hit_leftcorner == False :
    ball.draw()
    paddle.draw()
    paddle1.draw() 
	
   if ball.hit_leftcorner == True :
       if counter > counter1:
         canvas.create_text(450,320,text="Player1 win the Game!",font=("bold",30),fill="red")
                  #time.sleep(10)
       elif counter == counter1 :
         canvas.create_text(450,300,text="No Player Win!",font=("bold",30),fill="red")
       else :
        canvas.create_text(450,400,text="Player2 win the Game",font=("bold",30),fill="red")
        #time.sleep(10)
        #break
   if ball.hit_rightcorner == False :
    ball.draw()
    paddle.draw()
    paddle1.draw() 
	
   if ball.hit_rightcorner == True :
       if counter > counter1:
          canvas.create_text(450,400,text="Player1 win the Game!",font=("bold",30),fill="red")
       elif counter == counter1 :
         canvas.create_text(450,300,text="No Player Win!",font=("bold",30),fill="red")
	
         #time.sleep(10)
      
       else :
         canvas.create_text(450,400,text="Player2 win the Game",font=("bold",30),fill="red")
	     #time.sleep(10)
         #break 	
   
   tk.update_idletasks()
   tk.update()
   time.sleep(0.001)