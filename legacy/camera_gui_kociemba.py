from threading import Thread, Lock
import threading
import cv2
import numpy as np
import queue
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import kociemba
import serial





import time
salir=True
q = queue.Queue()
#timerrr = time.clock()
run_once = 0
root = tk.Tk()
guardarvar=0
face=""
cubecolors= []
def off():
    global salir
    salir =False
    root.destroy()
def Guardar():
    global face,stringfront,stringright,stringdown,stringup,stringback,stringleft,positionfrontfinal,positiondownfinal,positionleftfinal,positionupfinal,arduino
    global timerrr,positionbackfinal,positionrightfinal,cubecolors
    global reset
    global guardarvar,stringcubecolors
    
    ''' elapsed = (time.clock() - timerrr)
        reset=reset+1
        timerrr = time.clock()'''

    guardarvar=guardarvar+1
    
    if (guardarvar==1):
        stringfront=canvas.create_text(1000, 140, fill="WHITE", font="THelvetica -21", text=positionfront)
        face="Right"
        positionfrontfinal=positionfront
        cubecolors=positionfront
        
        arduino = serial.Serial('COM5', 9600)
        while True:
            arduino.write('S'.encode('utf-8'))
            print arduino.readline()
            if (arduino.in_waiting):
                break  
        



    elif (guardarvar==2):
        stringright=canvas.create_text(1000, 165, fill="WHITE", font="THelvetica -21", text=positionright)
        face="Down"
        positionrightfinal=positionright
        cubecolors=positionfrontfinal+positionright

            
        
    elif (guardarvar==3):
        stringdown=canvas.create_text(1000, 190, fill="WHITE", font="THelvetica -21", text=positiondown)
        face="Up"
        positiondownfinal=positiondown
        cubecolors=positionfrontfinal+positionrightfinal+positiondown

    elif(guardarvar==4):
        stringup=canvas.create_text(1000, 215, fill="WHITE", font="THelvetica -21", text=positionup)
        face="Left"
        positionupfinal=positionup
        cubecolors=positionfrontfinal+positionrightfinal+positiondownfinal+positionup

    elif(guardarvar==5):
        stringback=canvas.create_text(1000, 240, fill="WHITE", font="THelvetica -21", text=positionleft)
        face="Back"
        positionleftfinal=positionleft
        cubecolors=positionfrontfinal+positionrightfinal+positiondownfinal+positionupfinal+positionleft

    
    else:
        postionback=positionback[::-1]
        stringleft=canvas.create_text(1000, 265, fill="WHITE", font="THelvetica -21", text=positionback)
        cubecolors=positionupfinal+positionrightfinal+positionfrontfinal+positiondownfinal+positionleftfinal+positionback

    
   

    
def Reinciar():
    global guardarvar,t,t1,t2,t3,t4,t5,face
    guardarvar=guardarvar-1
    if (guardarvar==0):
        canvas.delete(stringfront)
        face="Front"
        t=0
    elif (guardarvar==1):
        canvas.delete(stringright)
        face="Right"
        t1=0
    elif (guardarvar==2):
        canvas.delete(stringdown)
        face="Down"
        t2=0
    elif (guardarvar==3):
        canvas.delete(stringup)
        face="Up"
        t3=0
    elif (guardarvar==4):
        canvas.delete(stringback)
        face="Left"
        t4=0    
    elif (guardarvar==5):
        canvas.delete(stringleft)
        face="Back"
        t5=0



def Resolver():
    global cubecolors
    s=kociemba.solve(cubecolors)
    stringcubecolors=canvas.create_text(400, 600, fill="BLACK", font="THelvetica -22", text="Solution = "+str(solve))  
    print s
    i = 0
    s += ' '
    while(i < len(s)):
          print arduino.readline() 
          if ( s[i+1] == ' '):
                arduino.write(s[i].encode('utf-8'))
                i+=2
          elif (s[i+1] == "'"):
                arduino.write((s[i].lower()).encode('utf-8'))    
                i+=3
          elif (s[i+1] == "2"):
                if   (s[i] == 'F'):   arduino.write(b'1')
                elif (s[i] == 'B'):   arduino.write(b'2')
                elif (s[i] == 'U'):   arduino.write(b'3')
                elif (s[i] == 'D'):   arduino.write(b'4')
                elif (s[i] == 'L'):   arduino.write(b'5')
                elif (s[i] == 'R'):   arduino.write(b'6')
                i+=3
    

def gui():
    global canvas



    # CREACION FONDO Y DEFINICION DE COLORES Y PROPIEDADES #

    
    canvas = tk.Canvas(root, width=1280, height=1024, background="FireBrick4")
    canvas.update_idletasks()
    canvas.pack(side="bottom", fill="both", expand=True)
    canvas.pack(side="bottom", fill="both", expand=True)
    root.overrideredirect(True) #Fullscreen
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) #FullSreen

    # CREACION DE LAS CARAS DEL CUBO Y ASIGNACION DE SUS VARIABLES #

    canvas.create_rectangle(250, 500, 300, 450, fill="gold", width=0)
    canvas.create_text(275, 475, fill="black", font="THelvetica -18", text="D")

    #  ROJO

    canvas.create_rectangle(250, 325, 300, 275, fill="red", width=0)
    canvas.create_text(275, 300, fill="BLACK", font="THelvetica -18", text="F")

    #  BLANCO

    canvas.create_rectangle(250, 100, 300, 150, fill="white", width=0)
    canvas.create_text(275, 125, fill="BLACK", font="THelvetica -18", text="U")

    #  VERDE

    canvas.create_rectangle(75, 325, 125, 275, fill="green", width=0)
    canvas.create_text(100, 300, fill="BLACK", font="THelvetica -18", text="L")

    #  AZUL

    canvas.create_rectangle(425, 325, 475, 275, fill="blue", width=0)
    canvas.create_text(450, 300, fill="BLACK", font="THelvetica -18", text="R")

    #  NARANJA

    canvas.create_rectangle(600, 325, 650, 275, fill="DarkOrange3", width=0)
    canvas.create_text(625, 300, fill="BLACK", font="THelvetica -18", text="B")

    canvas.create_line(15,40,765,40, fill="BLACK",width=5)

    mainFrame = Frame(canvas)
    mainFrame.place(x=800, y=300)                

    #Capture video frames
    lmain = tk.Label(mainFrame)
    lmain.grid(row=0, column=0)    
    # Botones - Textos
    canvas.create_text(390, 20, fill="BLACK", font="Verdana -28", text="RUBIK SOLVER  CONTURSO - ROCCASALVO - SMARA")
    button = tk.Button( text="Salir",command= lambda: off() ,height = 3,width = 20)
    buttonGuardar = tk.Button( text="Guardar Cara",command= lambda: Guardar() ,height = 3,width = 20)
    buttonReiniciar = tk.Button( text="Reiniciar",command= lambda: Reinciar() ,height = 3,width = 20)
    buttonResolver = tk.Button( text="Resolver",command= lambda: Resolver() ,height = 3,width = 20)
    button.place(x=610,y=680)
    buttonReiniciar.place(x=230,y=680)
    buttonResolver.place(x=420,y=680)
    buttonGuardar.place(x=40,y=680)


        
    global textdetect
    global textface1

    textdetect = canvas.create_text(540, 120, fill="black", font="THelvetica -25", text="Detecting:")

    textface = canvas.create_text(595, 150, fill="black", font="THelvetica -25", text="Face:")
    textface1 = canvas.create_text(660, 150, fill="black", font="THelvetica -25", text="Front")
    canvas.create_text(870, 140, fill="BLACK", font="THelvetica -22", text="Front Face:")
    canvas.create_text(870, 165, fill="BLACK", font="THelvetica -22", text="Right Face:")
    canvas.create_text(870, 190, fill="BLACK", font="THelvetica -22", text="Down Face:")
    canvas.create_text(870, 215, fill="BLACK", font="THelvetica -22", text="Up Face:")
    canvas.create_text(870, 240, fill="BLACK", font="THelvetica -22", text="Back Face:")
    canvas.create_text(870, 265, fill="BLACK", font="THelvetica -22", text="Left Face:")


    " LOGO Y LETRAS DE LA INTERFAZ "
    image1 = Image.open('logo.png')
    image1 = image1.resize((550,100))
    gif1 = ImageTk.PhotoImage(image1)
    
    
    canvas.create_image((800,8), image=gif1, anchor='nw')
    global texttimer

    global reset

    global timerrr
    reset = 2
    #texttimer = canvas.create_text(700, 120, fill="BLACK", font="THelvetica -25", text=5)

   
        
    def guiu():
        global positionfront,positionright,positionup,positiondown,positionleft,positionback,t,t1, positionfrontfinal,positionrightfinal
        global reset,positiondownfinal,positionupfinal,positionbackfinal,positionleftfinal,t2,t3,t4,t5
        global texttimer,timerrr,textdetection,textdetect,guardarvar,textface1,face


        positionfront='F' #red
        positionright='R' #blue
        positiondown='D' #blue
        positionup='U' #blue
        positionback='B' #blue
        positionleft='L' #blue

        if (guardarvar==0):
            face="Front"

        try:
            #cv2.imshow('blue ',blue)
            #cv2.imshow('red ',red)
            wat = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img   = Image.fromarray(wat)
            imgtk = ImageTk.PhotoImage(image = img)

            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
        except NameError:
            pass
        

        ''' elapsed = (time.clock() - timerrr)
            if elapsed >= 5:
                timerrr = time.clock()
                reset = reset + 1'''
        '''f1="FireBrick4"
        f2="FireBrick4"
        f3="FireBrick4"
        f4="FireBrick4"
        f6="FireBrick4"
        f7="FireBrick4"
        f8="FireBrick4"
        f9="FireBrick4"'''

        if reset % 2 == 0:

            status = "green"
            textdetection = "Detecting:"
            try:
                q.get(f1)
                q.get(f2)
                q.get(f3)
                q.get(f4)
                q.get(f5)
                q.get(f6)
                q.get(f7)
                q.get(f8)
                q.get(f9)

                colorsquare = [f4,f3,f2,f1,f6,f7,f8,f9]
                    
                if guardarvar==0:
                    canvas.create_rectangle(200, 275, 250, 225, fill=f1, width=0)
                    canvas.create_rectangle(250, 275, 300, 225, fill=f2, width=0)
                    canvas.create_rectangle(300, 275, 350, 225, fill=f3, width=0)
                    canvas.create_rectangle(200, 325, 250, 275, fill=f4, width=0)
                    canvas.create_rectangle(300, 325, 350, 275, fill=f6, width=0)
                    canvas.create_rectangle(200, 375, 250, 325, fill=f7, width=0)
                    canvas.create_rectangle(250, 375, 300, 325, fill=f8, width=0)
                    canvas.create_rectangle(300, 375, 350, 325, fill=f9, width=0)
                    
                    for i in colorsquare: #red

                            
                        if (i=="red"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'F' #F = red = front
                            else:
                                positionfront='F'+positionfront
                            
                        elif (i=="blue"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'R'
                            else:   

                                positionfront='R'+positionfront
                            
                        elif (i=="white"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'U'
                            else:
                                positionfront='U'+positionfront 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'D'
                            else:
                                positionfront='D'+positionfront
                                                                                                            

                        elif (i=="green"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'L'
                            else:
                                positionfront='L'+positionfront
                            
                        elif (i=="DarkOrange3"):
                            if len(positionfront)>=5:
                                positionfront=positionfront+'B'
                            else:
                                positionfront='B'+positionfront 
                        
                        
                                
                        
                                
            except queue.Empty:
                pass
            except NameError:
                pass
            try:

                if guardarvar==1:
                    
                    canvas.create_rectangle(375, 275, 425, 225, fill=f1, width=0)
                    canvas.create_rectangle(425, 275, 475, 225, fill=f2, width=0)
                    canvas.create_rectangle(475, 275, 525, 225, fill=f3, width=0)
                    canvas.create_rectangle(375, 375, 425, 325, fill=f7, width=0)
                    canvas.create_rectangle(425, 375, 475, 325, fill=f8, width=0)
                    canvas.create_rectangle(475, 375, 525, 325, fill=f9, width=0)
                    canvas.create_rectangle(375, 325, 425, 275, fill=f4, width=0)
                    canvas.create_rectangle(475, 325, 525, 275, fill=f6, width=0)

                    for i in colorsquare: #red
                        if (i=="red"):
                            if len(positionright)>=5:
                                positionright=positionright+'F'
                            else:
                                positionright='F'+positionright
                            
                        elif (i=="blue"):
                            if len(positionright)>=5:
                                positionright=positionright+'R'
                            else:   

                                positionright='R'+positionright
                            
                        elif (i=="white"):
                            if len(positionright)>=5:
                                positionright=positionright+'U'
                            else:
                                positionright='U'+positionright 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positionright)>=5:
                                positionright=positionright+'D'
                            else:
                                positionright='D'+positionright
                                                                                                            

                        elif (i=="green"):
                            if len(positionright)>=5:
                                positionright=positionright+'L'
                            else:
                                positionright='L'+positionright
                            
                        elif (i=="DarkOrange3"):
                            if len(positionright)>=5:
                                positionright=positionright+'B'
                            else:
                                positionright='B'+positionright 
                        
                                                                   

                        
                        
                           
            except queue.Empty:
                pass
            except NameError:
                pass
            try:

                if guardarvar==2:
                    canvas.create_rectangle(200, 450, 250, 400, fill=f1, width=0)
                    canvas.create_rectangle(250, 450, 300, 400, fill=f2, width=0)
                    canvas.create_rectangle(300, 450, 350, 400, fill=f3, width=0)
                    canvas.create_rectangle(200, 550, 250, 500, fill=f7, width=0)
                    canvas.create_rectangle(250, 550, 300, 500, fill=f8, width=0)
                    canvas.create_rectangle(300, 550, 350, 500, fill=f9, width=0)
                    canvas.create_rectangle(200, 500, 250, 450, fill=f4, width=0)
                    canvas.create_rectangle(300, 500, 350, 450, fill=f6, width=0)
                    for i in colorsquare: #red
                        if (i=="red"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'F'
                            else:
                                positiondown='F'+positiondown
                            
                        elif (i=="blue"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'R'
                            else:   

                                positiondown='R'+positiondown
                            
                        elif (i=="white"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'U'
                            else:
                                positiondown='U'+positiondown 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'D'
                            else:
                                positiondown='D'+positiondown
                                                                                                            

                        elif (i=="green"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'L'
                            else:
                                positiondown='L'+positiondown
                            
                        elif (i=="DarkOrange3"):
                            if len(positiondown)>=5:
                                positiondown=positiondown+'B'
                            else:
                                positiondown='B'+positiondown 
                        
                                
                                                    
            except queue.Empty:
                pass
            except NameError:
                pass
            try:

                if guardarvar==3:
                    canvas.create_rectangle(200, 50, 250, 100, fill=f1, width=0)
                    canvas.create_rectangle(250, 50, 300, 100, fill=f2, width=0)
                    canvas.create_rectangle(300, 50, 350, 100, fill=f3, width=0)
                    canvas.create_rectangle(200, 150, 250, 200, fill=f7, width=0)
                    canvas.create_rectangle(250, 150, 300, 200, fill=f8, width=0)
                    canvas.create_rectangle(300, 150, 350, 200, fill=f9, width=0)
                    canvas.create_rectangle(200, 100, 250, 150, fill=f4, width=0)
                    canvas.create_rectangle(300, 100, 350, 150, fill=f6, width=0)
                    for i in colorsquare: #red
                        if (i=="red"):
                            if len(positionup)>=5:
                                positionup=positionup+'F'
                            else:
                                positionup='F'+positionup
                            
                        elif (i=="blue"):
                            if len(positionup)>=5:
                                positionup=positionup+'R'
                            else:   

                                positionup='R'+positionup
                            
                        elif (i=="white"):
                            if len(positionup)>=5:
                                positionup=positionup+'U'
                            else:
                                positionup='U'+positionup 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positionup)>=5:
                                positionup=positionup+'D'
                            else:
                                positionup='D'+positionup
                                                                                                            

                        elif (i=="green"):
                            if len(positionup)>=5:
                                positionup=positionup+'L'
                            else:
                                positionup='L'+positionup
                            
                        elif (i=="DarkOrange3"):
                            if len(positionup)>=5:
                                positionup=positionup+'B'
                            else:
                                positionup='B'+positionup 
                        
            except queue.Empty:
                pass
            except NameError:
                pass
            try:


                if guardarvar==4:
                    canvas.create_rectangle(25, 275, 75, 225, fill=f1, width=0)
                    canvas.create_rectangle(75, 275, 125, 225, fill=f2, width=0)
                    canvas.create_rectangle(125, 275, 175, 225, fill=f3, width=0)
                    canvas.create_rectangle(25, 325, 75, 275, fill=f4, width=0)
                    canvas.create_rectangle(125, 325, 175, 275, fill=f6, width=0)
                    canvas.create_rectangle(25, 375, 75, 325, fill=f7, width=0)
                    canvas.create_rectangle(75, 375, 125, 325, fill=f8, width=0)
                    canvas.create_rectangle(125, 375, 175, 325, fill=f9, width=0)
                    for i in colorsquare: #red
                        if (i=="red"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'F'
                            else:
                                positionleft='F'+positionleft
                            
                        elif (i=="blue"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'R'
                            else:   

                                positionleft='R'+positionleft
                            
                        elif (i=="white"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'U'
                            else:
                                positionleft='U'+positionleft 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'D'
                            else:
                                positionleft='D'+positionleft
                                                                                                            

                        elif (i=="green"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'L'
                            else:
                                positionleft='L'+positionleft
                            
                        elif (i=="DarkOrange3"):
                            if len(positionleft)>=5:
                                positionleft=positionleft+'B'
                            else:
                                positionleft='B'+positionleft
                                                               
            except queue.Empty:
                pass
            except NameError:
                pass
            try:


                if guardarvar==5:
                    canvas.create_rectangle(550, 275, 600, 225, fill=f1, width=0)
                    canvas.create_rectangle(600, 275, 650, 225, fill=f2, width=0)
                    canvas.create_rectangle(650, 275, 700, 225, fill=f3, width=0)
                    canvas.create_rectangle(550, 375, 600, 325, fill=f7, width=0)
                    canvas.create_rectangle(650, 325, 700, 275, fill=f6, width=0)
                    canvas.create_rectangle(600, 375, 650, 325, fill=f8, width=0)
                    canvas.create_rectangle(650, 375, 700, 325, fill=f9, width=0)
                    canvas.create_rectangle(550, 325, 600, 275, fill=f4, width=0)
                    for i in colorsquare: #red
                        if (i=="red"):
                            if len(positionback)>=5:
                                positionback=positionback+'F'
                            else:
                                positionback='F'+positionback
                            
                        elif (i=="blue"):
                            if len(positionback)>=5:
                                positionback=positionback+'R'
                            else:   

                                positionback='R'+positionback
                            
                        elif (i=="white"):
                            if len(positionback)>=5:
                                positionback=positionback+'U'
                            else:
                                positionback='U'+positionback 
                                                                                                            
                        elif (i=="yellow"):
                            if len(positionback)>=5:
                                positionback=positionback+'D'
                            else:
                                positionback='D'+positionback
                                                                                                            

                        elif (i=="green"):
                            if len(positionback)>=5:
                                positionback=positionback+'L'
                            else:
                                positionback='L'+positionback
                            
                        elif (i=="DarkOrange3"):
                            if len(positionback)>=5:
                                positionback=positionback+'B'
                            else:
                                positionback='B'+positionback 
                                                               
            except queue.Empty:
                pass
            except NameError:
                pass

        else:
            status = "red"
            textdetection = "No Detecting:"
        #print(face)
        canvas.delete(textdetect)
        #canvas.delete(texttimer)
        canvas.delete(textface1)
        textface1 = canvas.create_text(660, 150, fill="black", font="THelvetica -25", text=face)
        textdetect = canvas.create_text(540, 120, fill="BLACK", font="THelvetica -25", text=textdetection)
        #texttimer = canvas.create_text(670, 120, fill="BLACK", font="THelvetica -25", text=int(5 - elapsed))
        #canvas.create_text(695, 120, fill="BLACK", font="THelvetica -25", text="s")
        canvas.create_rectangle(630, 110, 650, 130, fill=status, width=0)

        
        canvas.after(100, guiu)


    guiu()
    # start the thread
    root.mainloop()  # Run your UI


###############

cap= cv2.VideoCapture(0)

if run_once == 0:
    global t,t1,t2,t3,t4,t5
    t=0
    t1=0
    t2=0
    t3=0
    t4=0
    t5=0
    areaf1=0
    th = threading.Thread(target=gui)  # initialise the thread
    th.setDaemon(True)
    th.start()  # start the thread
    run_once = 1

  

#cap.set(11,11) #Contrast #12
#cap.set(13,30) #Hue #30
#cap.set(12, 80) #Saturation #60

                            
if __name__ == "__main__" :

    while salir==True :
        
        ret , frame = cap.read()
        
        #print(cap.get(13))




        # Capturar frames
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Transformar imagen a gris para mejor visualizacion de contornos

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #        COLORES      #
        ORANGE_MIN = np.array([50, 50, 111], np.uint8)
        ORANGE_MAX = np.array([100, 200, 239], np.uint8)
        GREEN_MIN = np.array([55, 137, 131], np.uint8)
        GREEN_MAX = np.array([77, 255, 255], np.uint8)
        RED_MIN = np.array([0, 183, 93], np.uint8)
        RED_MAX = np.array([59, 255, 255], np.uint8)
        BLUE_MIN = np.array([80, 131, 0], np.uint8)
        BLUE_MAX = np.array([112, 255, 255], np.uint8)
        YELLOW_MIN = np.array([8, 43, 0], np.uint8)
        YELLOW_MAX = np.array([56, 255, 255], np.uint8)
        WHITE_MIN = np.array([11, 0, 95], np.uint8)
        WHITE_MAX = np.array([153, 43, 255], np.uint8)

        red = cv2.inRange(hsv, RED_MIN, RED_MAX)
        white = cv2.inRange(hsv, WHITE_MIN, WHITE_MAX)
        orange = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
        green = cv2.inRange(hsv, GREEN_MIN, GREEN_MAX)
        blue = cv2.inRange(hsv, BLUE_MIN, BLUE_MAX)
        yellow = cv2.inRange(hsv, YELLOW_MIN, YELLOW_MAX)

        # Aplicar filtros para mejorar los contornos
        gaussian = cv2.GaussianBlur(gray, (7, 7), 0)
        # Mas filtros
        laplacian = cv2.Laplacian(frame, cv2.CV_8U)

        # Dilatar los bordes obtenidos para que se noten mejor

        mat = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
        # Aplicar threshold para invertir los bordes y que queden de otro color
        im = cv2.adaptiveThreshold(gaussian, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)

        dilation = cv2.dilate(im, mat, 20)
        # 1
        im2 = cv2.adaptiveThreshold(dilation, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        # Encontrar contornos y dejarlos lo mas rectos posible
        _,cnts, hierarchy = cv2.findContours(im2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        cv2.rectangle(frame, (160, 133), (480, 460), (150, 150, 150), 1)
        cv2.line(frame, (265, 133), (265, 460), (150, 150, 150), 1)
        cv2.line(frame, (370, 133), (370, 460), (150, 150, 150), 1)
        cv2.line(frame, (160, 350), (478, 350), (150, 150, 150), 1)
        cv2.line(frame, (160, 240), (478, 240), (150, 150, 150), 1)

        # X1 Y1 X2 Y2

        # Mostrar todos los contornos encontrados

        #    Dibujar solo contornos que sean rectangulos











#############










        #        COLORES      #

        position = {}

        # def extract(face):
        global f1
        global f2
        global f3
        global f4
        global f5
        global f6
        global f7
        global f8
        global f9

        gaussian1 = cv2.GaussianBlur(red, (7, 7), 0)
        kernel = np.ones((20, 20), np.uint8)
        imred = cv2.adaptiveThreshold(gaussian1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)
        red1 = cv2.dilate(imred, kernel)
        red2 = cv2.adaptiveThreshold(red, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
        res = cv2.bitwise_and(frame, frame, mask=red)
        _,red1, hierarchy = cv2.findContours(red2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        ##    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)
        #cv2.rectangle(frame,(380,360),(470,450),(0,0,255),3)

        for c in red1:
            M = cv2.moments(c)
            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0
            rect = cv2.boundingRect(c)
            area = cv2.contourArea(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(red)
            #areared = moments['m00']
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect


            area = cv2.contourArea(c)
            if 10000 > area > 4000:
                if 170 < cX < 255:
                    if 140 < cY < 230:
                        if area>areaf1:
                            areaf1=area
                            f1 = 'red'
                            q.put(f1)

                # Mostramos sus coordenadas por pantalla

                #            cv2.rectangle(frame,(150,300),(00,80),(0,0,255),3)
                #            cv2.circle(frame,(cX,cY), 5, (0,0,255), -1)

                if 275 < cX < 360:
                    if 255 < cY < 335:
                        #   position[face+'5'] = 'red'

                        
                        f5 = 'red'
                        q.put(f5)


                            
                        #print(area+" f1")
                        
                
                        
                if 275 < cX < 360:
                    if 140 < cY < 230:
                        #  position[face+'2'] = 'red'
                        
                        f2 = 'red'
                       # print(str(area)+" f2")
                        q.put(f2)


                if 380 < cX < 470:
                    if 140 < cY < 230:
                        

                        #print(str(area)+" f3")
                        #  position[face+'3'] = 'red'
                        
                        
                        f3 = 'red'
                        q.put(f3)
                if 170 < cX < 255:
                    if 255 < cY < 335:
                        # position[face+'4'] = 'red'
                        
                        f4 = 'red'
                        q.put(f4)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                        #  position[face+'6'] = 'red'
                        #print(str(area)+" f6")
                        f6 = 'red'
                        q.put(f6)

                if 170 < cX < 255:
                    if 360 < cY < 450:
                        
                        #  position[face+'7'] = 'red'
                        
                        f7 = 'red'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        
                        # position[face+'8'] = 'red'
                        
                        f8 = 'red'
                        q.put(f8)

                if 380 < cX < 470:
                    if 360 < cY < 450:
                        
                        #  position[face+'9'] = 'red'
                        
                        f9 = 'red'
                        q.put(f9)

        # YELLOWWW
        yellow = cv2.inRange(hsv, YELLOW_MIN, YELLOW_MAX)

        gaussian2 = cv2.GaussianBlur(yellow, (7, 7), 0)
        kernel = np.ones((20, 20), np.uint8)
        imyellow = cv2.adaptiveThreshold(gaussian2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)

        yellow2 = cv2.adaptiveThreshold(imyellow, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        res = cv2.bitwise_and(frame, frame, mask=yellow)
        _,imyellow, hierarchy = cv2.findContours(yellow2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)

        for c in imyellow:
            M = cv2.moments(c)
            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0

            rect = cv2.boundingRect(c)
            areayellow = cv2.contourArea(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(yellow)
            #areayellow = moments['m00']
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect
            
            if 9000> areayellow >6000:
                #print (areayellow)

                if 170 < cX < 255:
                    if 140 < cY < 230:
                        
                        if areayellow>areaf1:
                            areaf1=areayellow
                            f1 = 'yellow'
                            q.put(f1)

                if 275 < cX < 360:
                    if 140 < cY < 230:
                            
                        #  position[face+'2'] = 'yellow'
                        f2 = 'yellow'
                        q.put(f2)

                if 380 < cX < 470:
                    if 140 < cY < 230:
                        
                        #  position[face+'3'] = 'yellow'
                        f3 = 'yellow'
                        q.put(f3)
                if 170 < cX < 255:
                    if 255 < cY < 335:
                        
                        # position[face+'4'] = 'yellow'
                        f4 = 'yellow'
                        
                        q.put(f4)
                if 275 < cX < 360:
                    if 255 < cY < 335:
                        
                        #  position[face+'5'] = 'yellow'
                        f5 = 'yellow'

                        q.put(f5)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                       
                        # position[face+'6'] = 'yellow'

                        f6 = 'yellow'
                        q.put(f6)
                if 170 < cX < 255:
                    if 360 < cY < 450:
                        
                        #  position[face+'7'] = 'yellow'
                        f7 = 'yellow'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        
                        #  position[face+'8'] = 'yellow'
                        f8 = 'yellow'
                        q.put(f8)
                if 380 < cX < 470:
                    if 360 < cY < 450:
                       
                        # position[face+'9'] = 'yellow'
                        f9 = 'yellow'
                        q.put(f9)
        # Mostramos sus coordenadas por pantalla

        #            cv2.rectangle(frame,(150,300),(00,80),(0,0,255),3)
        #            cv2.circle(frame,(cX,cY), 5, (0,0,255), -1)

        # WHITEEE
        white = cv2.inRange(hsv, WHITE_MIN, WHITE_MAX)
        gaussian6 = cv2.GaussianBlur(white, (7, 7), 0)
        kernel6 = np.ones((20, 20), np.uint8)
        imwhite = cv2.adaptiveThreshold(gaussian6, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)

        white1 = cv2.adaptiveThreshold(imwhite, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        resw = cv2.bitwise_and(frame, frame, mask=white)
        _,imwhite, hierarchy = cv2.findContours(white1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)

        for c in imwhite:
            #print (areawhite)   
            
            M = cv2.moments(c)

            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0

            rect = cv2.boundingRect(c)
            areawhite = cv2.contourArea(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(white)
            #areawhite = moments['m00']
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect

            
            
            if 8000 > areawhite > 6000:
                #print(areawhite)


                if 170 < cX < 255:
                    if 140 < cY < 230:
                        
                        if areawhite>areaf1:
                            areaf1=areawhite
                            f1 = 'white'
                            q.put(f1)
                        

                if 275 < cX < 360:
                    if 140 < cY < 230:
                        
                        
                        #  position[face+'2'] = 'white'
                        f2 = 'white'
                        q.put(f2)

                if 380 < cX < 470:
                    if 140 < cY < 230:
                        
                        #  position[face+'3'] = 'white'
                        f3 = 'white'
                        q.put(f3)

                if 170 < cX < 255:
                    if 255 < cY < 335:
                        
                        # position[face+'4'] = 'white'
                        f4 = 'white'
                        q.put(f4)
                if 275 < cX < 360:
                    if 255 < cY < 335:
                        
                        # position[face+'5'] = 'white'
                        f5 = 'white'

                        q.put(f5)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                        
                        #  position[face+'6'] = 'white'
                        f6 = 'white'
                        q.put(f6)

                if 170 < cX < 255:
                    if 360 < cY < 450:
                        # position[face+'7'] = 'white'
                        f7 = 'white'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        # position[face+'8'] = 'white'
                        f8 = 'white'
                        q.put(f8)

                if 380 < cX < 470:
                    if 360 < cY < 450:
                        #print(str(areawhite)+" f9")
                        # position[face+'9'] = 'white'
                        f9 = 'white'
                        q.put(f9)

        # BLUE

        blue = cv2.inRange(hsv, BLUE_MIN, BLUE_MAX)
        gaussian4 = cv2.GaussianBlur(blue, (7, 7), 0)
        kernel4 = np.ones((20, 20), np.uint8)
        imblue = cv2.adaptiveThreshold(gaussian4, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)
        blue1 = cv2.adaptiveThreshold(imblue, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        res = cv2.bitwise_and(frame, frame, mask=blue)
        _,imblue, hierarchy = cv2.findContours(blue1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)

        for c in imblue:
            
        
            M = cv2.moments(c)

            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0

            rect = cv2.boundingRect(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(white)
            areablue = cv2.contourArea(c)
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect
            
            if 10500 > areablue > 4000:
                if 275 < cX < 360:
                    if 255 < cY < 335:
                        #  position[face+'5'] = 'blue'
                        
                        f5 = 'blue'
                        q.put(f5)

                if 170 < cX < 255:
                    if 140 < cY < 230:
                        
                        if areablue>areaf1:
                            areaf1=areablue
                            f1 = 'blue'
                            q.put(f1)

                if 275 < cX < 360:
                    if 140 < cY < 230:
                        # position[face+'2'] = 'blue'
                        f2 = 'blue'
                        q.put(f2)
                if 380 < cX < 470:
                    if 140 < cY < 230:
                        # position[face+'3'] = 'blue'
                        f3 = 'blue'
                        q.put(f3)
                if 170 < cX < 255:
                    if 255 < cY < 335:
                        # position[face+'4'] = 'blue'
                        f4 = 'blue'
                        q.put(f4)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                        # position[face+'6'] = 'blue'
                        f6 = 'blue'
                        q.put(f6)
                if 170 < cX < 255:
                    if 360 < cY < 450:
                        #  position[face+'7'] = 'blue'
                        f7 = 'blue'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        #  position[face+'8'] = 'blue'
                        f8 = 'blue'
                        q.put(f8)
                if 380 < cX < 470:
                    if 360 < cY < 450:
                        # position[face+'9'] = 'blue'
                        f9 = 'blue'
                        q.put(f9)
            # Mostramos sus coordenadas por pantalla

        #           cv2.rectangle(frame,(150,300),(00,80),(0,0,255),3)
        #           cv2.circle(frame,(cX,cY), 5, (0,0,255), -1)

        # GREEN

        green = cv2.inRange(hsv, GREEN_MIN, GREEN_MAX)
        gaussian5 = cv2.GaussianBlur(green, (7, 7), 0)
        kernel = np.ones((20, 20), np.uint8)
        imgreen = cv2.adaptiveThreshold(gaussian5, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)
        green1 = cv2.dilate(imgreen, kernel)
        green2 = cv2.adaptiveThreshold(green1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        res = cv2.bitwise_and(frame, frame, mask=green)
        _,green2, hierarchy = cv2.findContours(green, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)

        for c in green2:
            areagreen = cv2.contourArea(c)

            M = cv2.moments(c)

            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0

            rect = cv2.boundingRect(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(white)
            areagreen1 = moments['m00']
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect
            #   print(areagreen)
            if 17500 > areagreen > 4000:

                if 170 < cX < 255:
                    if 140 < cY < 230:
                        if areagreen>areaf1:
                            areaf1=areagreen
                            f1 = 'green'
                            q.put(f1)

                if 275 < cX < 360:
                    if 140 < cY < 230:
                        # position[face+'2'] = 'green'
                        f2 = 'green'
                        q.put(f2)
                if 380 < cX < 470:
                    if 140 < cY < 230:
                        #  position[face+'3'] = 'green'
                        f3 = 'green'
                        q.put(f3)
                if 170 < cX < 255:
                    if 255 < cY < 335:
                        # position[face+'4'] = 'green'
                        f4 = 'green'
                        q.put(f4)
                if 275 < cX < 360:
                    if 255 < cY < 335:
                        # position[face+'5'] = 'green'
                        f5 = 'green'

                        q.put(f5)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                        # position[face+'6'] = 'green'
                        f6 = 'green'
                        q.put(f6)

                if 170 < cX < 255:
                    if 360 < cY < 450:
                        # position[face+'7'] = 'green'
                        f7 = 'green'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        #  position[face+'8'] = 'green'
                        f8 = 'green'

                        q.put(f8)
                if 380 < cX < 470:
                    if 360 < cY < 450:
                        # position[face+'9'] = 'green'
                        f9 = 'green'
                        q.put(f9)
            # Mostramos sus coordenadas por pantalla

        #            cv2.rectangle(frame,(150,300),(00,80),(0,0,255),3)
        #            cv2.circle(frame,(cX,cY), 5, (0,0,255), -1)

        # ORANGEEE

        orange = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
        gaussian6 = cv2.GaussianBlur(orange, (7, 7), 0)
        kernel = np.ones((20, 20), np.uint8)
        imorange = cv2.adaptiveThreshold(gaussian6, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)
        orange1 = cv2.dilate(imorange, kernel)
        orange = cv2.adaptiveThreshold(orange, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 4)
        res = cv2.bitwise_and(frame, frame, mask=orange)
        _,orange1, hierarchy = cv2.findContours(orange, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #    cv2.drawContours(frame, red1, -1, (0, 0, 255), 2,)

        for c in orange1:
            areaorange = cv2.contourArea(c)

            M = cv2.moments(c)

            if M["m00"] != 0:

                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

            else:
                cX, cY = 0, 0

            rect = cv2.boundingRect(c)
            peri = cv2.arcLength(c, True)
            moments = cv2.moments(orange)
            areaorange1 = moments['m00']
            aprox = cv2.approxPolyDP(c, 0.09 * peri, True)
            x, y, w, h = rect
            # print(areaorange)
            if 11000 > areaorange > 4000:

                if 170 < cX < 255:
                    if 140 < cY < 230:
                        #  position[face+'1'] = 'orange'
                        

                        if areaorange>areaf1:
                            areaf1=areaorange
                            f1 = 'DarkOrange3'
                            print areaorange
                            q.put(f1)
                    # print(f1)
                if 275 < cX < 360:
                    if 140 < cY < 230:
                        #  position[face+'2'] = 'orange'
                        
                        f2 = 'DarkOrange3'
                        q.put(f2)
                if 380 < cX < 470:
                    if 140 < cY < 230:
                        # position[face+'3'] = 'orange'
                        f3 = 'DarkOrange3'
                        q.put(f3)
                if 170 < cX < 255:
                    if 255 < cY < 335:
                        # position[face+'4'] = 'orange'
                        f4 = 'DarkOrange3'
                        q.put(f4)

                if 275 < cX < 360:
                    if 255 < cY < 335:
                        # position[face+'5'] = 'orange'
                        f5 = 'DarkOrange3'
                        q.put(f5)

                if 380 < cX < 470:
                    if 255 < cY < 335:
                        # position[face+'6'] = 'orange'
                        f6 = 'DarkOrange3'
                        q.put(f6)
                if 170 < cX < 255:
                    if 360 < cY < 450:
                        # position[face+'7'] = 'orange'
                        f7 = 'DarkOrange3'
                        q.put(f7)
                if 275 < cX < 360:
                    if 360 < cY < 450:
                        #  position[face+'8'] = 'orange'


                        f8 = 'DarkOrange3'
                        q.put(f8)
                if 380 < cX < 470:
                    if 360 < cY < 450:
                        #  position[face+'9'] = 'orange'
                        f9 = 'DarkOrange3'
                        #print(str(areaorange)+" f9")
                        q.put(f9)




        #    print (squares)


        # def main():
        #  front= extract(face='f')
        #  position = dict()

        # main()

        
        

       
    cv2.destroyAllWindows()
    
