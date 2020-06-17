#installing Libraries
from tkinter import *
import random
root = Tk()
Msg=Message(root,text='Move Mouse or ckick the screen to Generate number.')

#declaring global variable
finNumMove = 0
redValue=0
greenValue=0
def callback(event):
    print ("clicked at", event.x, event.y)
    rNum = random.randint(1,9999)
    finNumClick = (rNum*event.x)%event.y
    
    print('Random Number', finNumClick)
    Msg['text']='random Number by mouse position is: ' + str(finNumClick)
def mouseMotion(event):
    rNum = random.randint(1,9999)
    finNumMove = ((rNum*event.x)*event.y)/rNum
   
   #converting random generated number
    redValue = int(str(finNumMove)[:3])
    print('redval:',redValue)
    greenValue = int(str(finNumMove)[3:6])
    print('green val:',greenValue)
    Msg['text']='random Number by mouse position is: ' + str(finNumMove)

# RGBredValue,greenValue,150)
# cannot figure out how to make this work (just yet)
# def generateColor(event):
#     mouseMotion()
#     return finNumMove
#     r=[]
#     r.append(finNumMove)
#     redValue = r[0:3]
#     greenValue = r[3:6]
#     print(redValue)
#     print(greenValue)
    

frame = Frame(root, width=1000, height=1000)
root.configure(background='red')
frame.bind("<Button-1>", callback)
frame.bind('<Motion>', mouseMotion)



Msg.bind("click", callback)
Msg.pack()
frame.pack()
root.mainloop()
