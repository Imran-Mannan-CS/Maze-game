import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):  
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(0)
            self.gold = 0
        
        def go_up(self):
            
            move_to_x = player.xcor()
            move_to_y = player.ycor() + 24
            
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            
        def go_down(self):
            
            move_to_x = player.xcor()
            move_to_y = player.ycor() - 24
            
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            
        def go_left(self):
            
            move_to_x = player.xcor() - 24
            move_to_y = player.ycor()
            
            
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y) 
            
        def go_right(self):
            
            move_to_x = player.xcor() + 24
            move_to_y = player.ycor()
            
          
            
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
        
        def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2) )
            
            if distance < 5:
                return True
            else:
                return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
   
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("circle")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("circle")
        else:
            dx = 0
            dy = 0
        
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
        
        
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
            
        turtle.ontimer(self.move, t=random.randint(100, 300))
    
    def is_close(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )
        
        if distance < 75:
            return True
        else:
            return False
          
   
    
 
#create level list
levels = [""]

#define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X           XXXXXX  XXXXX",
"X  XXXXXXX E        XXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X            E          X",
"XXXXXXX  XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX                  X",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                       X",
"XXXXX   EXXXXXXXXXT   XXX",
"X        XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                       X",
"XXXXXX   XXXXE  XXXXXXXXX",
"XXXXXX   XXXX   XXXXXXXXX",
"XXXXX    XXXX           X",
"X               X       X",
"XXXXXXX  EXXXXXXXXXXXXXXX",
"XXXXXX    XXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

treasures = []

enemies = []

levels.append(level_1)

def setup_maze(level):

    for y in range(len(level)):
        for x in range(len(level[y])):

            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)
            
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
                
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
                

#class instances
pen = Pen()
player = Player()
 
#wall cordinate list
walls = []

#Set up the level
setup_maze(levels[1])

#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

#main game loop
while True:
    
    for treasure in treasures:
        if player.is_collision(treasure):
            
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            
            treasure.destroy()
            
            treasures.remove(treasure)
   
    for enemy in enemies:
        if player.is_collision(enemy):
            print ("Player dies!")
            
    wn.update()
    