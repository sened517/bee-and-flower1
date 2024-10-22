import pgzrun
import random
import time 

WIDTH= 700
HEIGHT= 500

bee = Actor("bee")
flower = Actor("flower")

bee.x = 100
bee.y = 150
msg = "use arow keys to move the bee and touch the flower. " 
score = 0
gameover = False
def draw():
    screen.blit("grass1",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text(msg, (100,100))
    screen.draw.text(f"score:{score}",(100,50))
    if gameover:
        screen.fill("dark blue")
        screen.draw.text("You have ran out of time.",(200,200))
        screen.draw.text(f" final score:{score}",(100,50))


def update():
    global score 
    if keyboard.right:
        bee.x+=2
    if keyboard.left:
        bee.x-=2
    if keyboard.down:
        bee.y+=2
    if keyboard.up:
        bee.y-=2
    if bee.colliderect(flower):
        flower.x=random.randint(0,700)
        flower.y=random.randint(0,500)
        score=score+1

def exit():
    global gameover
    gameover=True

clock.schedule(exit,20)







pgzrun.go()