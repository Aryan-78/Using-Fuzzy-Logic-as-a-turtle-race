import turtle
#import time

win_length = 500
win_height = 500

turtles = 8

turtle.screensize(win_length, win_height)


class racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self,a):
        
        self.pos = (self.pos[0], self.pos[1] + a)
        self.turt.pendown()
        self.turt.forward(a)
        
    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()







while True:
    print('-----------------------------------')
    start = input('Would you like to play again ')
    
    Dict={}
    x=0
    while x < 8 :
        a=input("write the input fuzzy value for the turtle ") 
        t=float(a)
        Dict[x]=10*t
        x=x+1
        
    
    print('\n') 
    Area_med={}
    x=0
    while x<7:
        w=Dict[x]
        j=0
        a=Dict[x+1]
        t=1/2*(w+a)
        if a>0:
            if a>w:
                j=x+1+((2*a-w)/(a+w))*0.3
            else:
                j=x+1+((2*w-a)/(a+w))*0.33
        elif w>0:
            if a>w:
                j=x+1+((2*a-w)/(a+w))*0.33
            else:
                j=x+1+((2*w-a)/(a+w))*0.33
        else:
                j=0
            
        
        z=t*j
        Area_med[x]=z
        Area_med[x+9]=t
        x=x+1
    
    Area_med[7]=1/3*int(Dict[0])
    Area_med[8]=1/2*int(Dict[0])
    
    
    mediancrisp=(int(Area_med[0])+int(Area_med[1])+int(Area_med[2])+int(Area_med[3])+int(Area_med[4])+int(Area_med[5])+int(Area_med[6])+int(Area_med[7]))/(int(Area_med[8])+int(Area_med[9])+int(Area_med[10])+int(Area_med[11])+int(Area_med[12])+int(Area_med[13])+int(Area_med[14])+int(Area_med[15]))
    print("The actual crisp value for the given fuzzy set: ")
    print(mediancrisp)
    print('\n')
    
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
    start = -(win_length/2) + 20
    for t in range(turtles):
        newPosX = start + t*(win_length)//turtles
        tList.append(racer(colors[t],(newPosX, -230)))
        tList[t].turt.showturtle()

    
       
    run = True
    while run:
        x=0
        a=0
        while x<8:
            
            tList[x].move(int(Dict[a]))
            x=x+1
            a=a+1

        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color)

        if len(maxColor) > 0:
            run = False
            print('The winner is: ')
            for win in maxColor:
                print(win)
    break

    oldScore = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])

    file.close()
    
    file = open('scores.txt', 'w')

    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')


    file.close()
    
     

   
    