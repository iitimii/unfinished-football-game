import pygame as p

p.init()

win = p.display.set_mode((1200,700))
p.display.set_caption('Football!')
icon = p.image.load('ball32.png')
p.display.set_icon(icon)

background = p.image.load('field1.jpg')

ballimg = p.image.load('ball64.png')
bx = 568
by = 318
bdx = 0
bdy = 0

p1img = p.image.load('player1.png')
p1x = 306
p1y = 288
p1dx = 0
p1dy = 0

p2img = p.image.load('player2.png')
p2x = 766
p2y = 288
p2dx = 0
p2dy = 0


def ball(x,y):
    win.blit(ballimg, (x,y))

def p1(x,y):
    win.blit(p1img, (x,y))

def p2(x,y):
    win.blit(p2img, (x,y))


running = True
while running:

    win.blit(background, (0,0))

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_a:  
                p1dx = -1
            if event.key == p.K_d:  
                p1dx = 1
            if event.key == p.K_w:  
                p1dy = -1
            if event.key == p.K_s:  
                p1dy = 1
            if event.key == p.K_LEFT:  
                p2dx = -1
            if event.key == p.K_RIGHT:  
                p2dx = 1
            if event.key == p.K_UP:  
                p2dy = -1
            if event.key == p.K_DOWN:  
                p2dy = 1
            
        if event.type == p.KEYUP:
            if event.key == p.K_a or event.key == p.K_d or event.key == p.K_w or event.key == p.K_s:
                p1dx = 0
                p1dy = 0
            if event.key == p.K_LEFT or event.key == p.K_RIGHT or event.key == p.K_UP or event.key == p.K_DOWN:
                p2dx = 0
                p2dy = 0
            
        
    p1x += p1dx
    p1y += p1dy

    p2x += p2dx
    p2y += p2dy

    bx += bdx
    by += bdy
    

    if p1x < 0:
        p1x = 0
    if p1x > 1072:
        p1x = 1072
    if p1y < 0:
        p1y = 0
    if p1y > 572:
        p1y = 572
    
    if p2x < 0:
        p2x = 0
    if p2x > 1072:
        p2x = 1072
    if p2y < 0:
        p2y = 0
    if p2y > 572:
        p2y = 572

    if p1x - bx > -128 and p1x - bx < -64 and p1y - by > -127 and p1y - by < 63:
        bx = p1x + 128
        bdx = 0.5
    
    if p1x - bx < 64 and p1x - bx > 0 and p1y - by > -127 and p1y - by < 63:
        bx = p1x - 64
        bdx = -0.5

    if p1y - by > -128 and p1y - by < -64 and p1x - bx > -127 and p1x - bx < 63:
        by = p1y + 128
        bdy = 0.5
       

    if p1y - by < 64 and p1y - by > 0 and p1x - bx > -127 and p1x - bx < 63:
        by = p1y - 64
        bdy = -0.5

    
    if p2x - bx > -128 and p2x - bx < -64 and p2y - by > -127 and p2y - by < 63:
        bx = p2x + 128
        bdx = 0.5
    
    if p2x - bx < 64 and p2x - bx > 0 and p2y - by > -127 and p2y - by < 63:
        bx = p2x - 64
        bdx = -0.5

    if p2y - by > -128 and p2y - by < -64 and p2x - bx > -127 and p2x - bx < 63:
        by = p2y + 128
        bdy = 0.5
       

    if p2y - by < 64 and p2y - by > 0 and p2x - bx > -127 and p2x - bx < 63:
        by = p2y - 64
        bdy = -0.5


    if p1x - p2x > -128:
        p1dx = 0
        p2dx = 0
        

    if bx <0:
        bx = 0
        bdx *= -1
    if bx > 1136:
        bx = 1136
        bdx *= -1
    if by < 0:
        by = 0
        bdy *= -1
    if by > 636:
        by = 636
        bdy *= -1




    ball(bx,by)
    p1(p1x,p1y)
    p2(p2x,p2y)

    
    
    p.display.update()