from tkinter import *# importing tkinter module to create GUI window
import random # importing random module to generate random values
import tkinter.messagebox as tmsg # importing messagebox module to show specific messages to the user.
start=Tk() # Tk() class instance
def gamerules(): # Game rules window 
    rule=Toplevel(start) # Toplevel() function copies the instance of Tk() from start
    rule.title("Game Rules") # title
    rule.iconbitmap("c:\\Users\\user\\Downloads\\swg.ico")# icon
    rule.geometry("515x690")# geometry size
    rule.maxsize(515,690)# fixing max size
    rule.minsize(515,690)# fixing min size
    ruleupper=Frame(rule,bg="springgreen4")# frame 1
    ruleupper.pack(fill=BOTH)
    rf=Label(ruleupper,text=" ",bg="springgreen4")# show label to create space
    rf.grid(row=1,column=1)
    # show label to create space
    rf1=Label(ruleupper,text="      ",bg="springgreen4",font=("times of roman",40,"bold"))
    rf1.grid(row=2,column=1)
    # Heading
    ruleheading=Label(ruleupper,text="Game Rules",bg="springgreen4",fg="palegreen1",font=("times of roman",40,"bold","underline"))
    ruleheading.grid(row=2,column=2)
    # show label to create space
    rf2=Label(ruleupper,text="      ",bg="springgreen4",font=("times of roman",30,"bold"))
    rf2.grid(row=3,column=1)
    rulelower=Frame(rule,bg="palegreen1")# frame 2
    rulelower.pack(fill=BOTH)
    # show label to create space
    rf3=Label(rulelower,text="",bg="palegreen1",font=("times of roman",30,"bold"))
    rf3.grid(row=1,column=1)
    # game rules
    rule1=Label(rulelower,text="  1.  User should select among these three option:              \n       ( Snake / Water / Gun ).\n",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule1.grid(row=2,column=1)
    rule2=Label(rulelower,text="   2.  If your choice and opponent's choice matches              \n        then game will be draw, and there will be no            \n        change in score.\n",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule2.grid(row=3,column=1)
    rule3=Label(rulelower,text="  3.  Each user will get 10 lifes and for each game               \n       life will be reduced by 1.\n",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule3.grid(row=4,column=1)
    rule4=Label(rulelower,text="  4.  If a player get 100 points, then he/she will get              \n       a shoutout.",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule4.grid(row=5,column=1)
    rule5=Label(rulelower,text="\n  5.  If you win a game, you will get 10 points.                      ",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule5.grid(row=6,column=1)
    rule4=Label(rulelower,text="\n  6.  If you lost a game, 10 points will be reduced but           \n       if the point is 0 then there will be no change.           \n",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    rule4.grid(row=7,column=1)
    # show label to create space
    rf4=Label(rulelower,text="",bg="palegreen1",font=("times of roman",30,"bold"))
    rf4.grid(row=8,column=1)
    rule.mainloop()# declaring mainloop() to execute the window in the screen
    
def playgame():# gameplay window
    def gamelogic(): # game play logic defined here
        global s # global variable s for score
        global l # global variable l for health
        opponent_choice.delete("1.0",END) # deleting opponent choice in the text screen
        result.delete("1.0",END) # deleting result in the text screen
        n = nameentry.get() # getting the user name here
        c = var1.get() # getting the user choice
        game=["SNAKE", "WATER", "GUN"] # list for opponent choice
        cval = random.choice(game) # random.choice() function chooses random values from game[] list
        opponent_choice.insert(END,f"{cval}") # inserting the opponent choice at text screen
        if (c!="Nothing"): # if user chooses any option 
            # condition for if user chooses snake and opponent's choice gun
            if (c == "SNAKE" and cval == "GUN"): 
                # this message will be shown in the result text screen
                result.insert(END,f"\t\tOh no! {cval} kills the {c} 😔\n\n\t\t{n}, you loosed the game😔😓😭")
                s-=10 # decreasing one point
                l-=1 # decreasing one health point
                if (l<=0): # checking if health is 0 or not
                    # if health is 0 then this message will be shown
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0 # score will be reset into 0
                    l=10 # health will be reset into 10 again
                    nameentry.delete(0,END) # deleting the name entry
                    opponent_choice.delete("1.0",END) # clearing opponent choice
                    result.delete("1.0",END) # clearing the result 
                    var1.set("Nothing") # deselcting the radio buttons
                    # health showing
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # score showing
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # health changing
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                if(s<=0): # checking the score is less than equal to 0 
                    s=0 # if yes then it will be set as 0
                    # showing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)   
                else:
                    # if greater than 0 then printing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5) 
            # condition for if user chooses gun and opponent's choice snake          
            elif (c == "GUN" and cval == "SNAKE"):
                # this message will be shown in the result text screen
                result.insert(END,f"\t\tYes! {c} kills the {cval} 🤩\n\n  Congratulations!🎉🎊 {n}, you won the game🥳🎉🎊")
                s+=10 # adding 10 points
                l-=1 # decreasing the health
                if (l<=0): # checking if health is 0 
                    # if health is 0 then showing this message
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0 # reseting the score
                    l=10 # reseting the health
                    nameentry.delete(0,END)# clearing the name entry
                    opponent_choice.delete("1.0",END)# clearing opponent choice
                    result.delete("1.0",END)# clearing the result
                    var1.set("Nothing")# deselecting the radiobutton options
                    # showing the updated health
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # showing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # showing the updated health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                # showing the updated score
                score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                score.grid(row=1, column=5)
                if(s==100):# checking if score is 100 
                    # showing the congratulations message
                    tmsg.showinfo("Congratulations!",f"Congratulions!🤩 {n} you achieved 100 score🎉🎊")
            # condition for if user chooses gun and opponent's choice is water
            elif (c == "GUN" and cval == "WATER"):
                # showing the result
                result.insert(END,f"\t\tOh no! {cval} damages the {c} 😔\n\n\t\t{n}, you loosed the game😔😓😭")
                s-=10 # decreasing the point
                l-=1 # decresing the health
                if (l<=0):# checking the health is 0 or not
                    # showing this message
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0# setting the score 0 again 
                    l=10# setting the health 10 again
                    nameentry.delete(0,END)# resets name entry
                    opponent_choice.delete("1.0",END)# resets opponent's choice
                    result.delete("1.0",END)# clearing the result
                    var1.set("Nothing")# setting choice as nothing
                    # showing health
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # showing score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # showing updated health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                if(s<=0):# checking the score 0 or not
                    s=0 # setting the score to 0
                    # showing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)   
                else:
                    # showing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5) 
             # condition for if user chooses water and opponent's choice is gun
            elif (c == "WATER" and cval == "GUN"):
                # showing the result
                result.insert(END,f"\t\tYes! {c} damages the {cval} 🤩\n\n  Congratulations!🎉🎊 {n}, you won the game🥳🎉🎊")
                s+=10 # increasing the score
                l-=1 # decreasing the health
                if (l<=0):# checking if health is 0 or not
                    # showing the gameover message
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0# reseting the score
                    l=10# reseting the health
                    nameentry.delete(0,END)# deleting name entry
                    opponent_choice.delete("1.0",END)# deleting opponent choice
                    result.delete("1.0",END)# deleting result
                    var1.set("Nothing")# setting option as nothing
                    # showing new health
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # showing new score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # showing updated health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                # showing updated score
                score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                score.grid(row=1, column=5)    
                if(s==100):# checking if score is 100 or not
                    # showing congratulations message
                    tmsg.showinfo("Congratulations!",f"Congratulions!🤩 {n} you achieved 100 score🎉🎊")
            # condition for if user chooses water and opponent's choice is snake
            elif (c == "WATER" and cval == "SNAKE"):
                # showing the result 
                result.insert(END,f"\t\tOh no! {cval} can float in the {c} 😔\n\n\t\t{n}, you loosed the game😔😓😭")
                s-=10# decreasing score
                l-=1# decreasing health
                if (l<=0):# checking health is 0 or not
                    # showing game over message
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0 # reseting the score
                    l=10 # reseting the health
                    nameentry.delete(0,END)# deleting nameentry
                    opponent_choice.delete("1.0",END)# deleting opponent choice
                    result.delete("1.0",END)# deleting result
                    var1.set("Nothing")# setting option as nothing
                    # showing the health
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # showing the score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # showing updated health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                # checking if score is 0 or not
                if(s<=0):
                    s=0# setting the score as 0
                    # showing the score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)   
                else:
                    # showing the updated score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
            # condition for if user chooses snake and opponent's choice is water
            elif (c == "SNAKE" and cval == "WATER"):
                # showing the result
                result.insert(END,f"\t\tYes! {c} can float in the {cval} 🤩\n\n  Congratulations!🎉🎊 {n}, you won the game🥳🎉🎊")
                s+=10 # increasing the score
                l-=1 # decreasing the health
                if (l<=0):# checking the health is 0 or not
                    # showing game over message
                    tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                    s=0# resets the score
                    l=10# resets the health
                    nameentry.delete(0,END)# deleting name entry
                    opponent_choice.delete("1.0",END)# deleting opponent choice
                    result.delete("1.0",END)# deleting result
                    var1.set("Nothing")# setting the option as nothing
                    # showing new health
                    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                    life.grid(row=1,column=2)
                    # showing the new score
                    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                    score.grid(row=1, column=5)
                # showing the updated health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                # showing the updated score
                score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                score.grid(row=1, column=5)
                # checking the score is 100 or not
                if(s==100):
                    # showing congratulations message
                    tmsg.showinfo("Congratulations!",f"Congratulions!🤩 {n} you achieved 100 score🎉🎊")
            # condition for if both choice matches
            else:
                # showing result
                result.insert(END,f"\t\tWhat!😳 you both chooses {c} 😑\n\n\t\t{n}, the game is drawn😑😶")
                l-=1 # decreasing health
            # checking the health is 0 or not
            if (l<=0):
                # showing the game over message
                tmsg.showinfo("Game Over!",f"Game over!\n{n}, you got total {s} points!")
                s=0# reseting the score
                l=10# reseting the health
                nameentry.delete(0,END)# deleting the name entry
                opponent_choice.delete("1.0",END)# deleting opponent choice
                result.delete("1.0",END)# clearing the result
                var1.set("Nothing")# deselcting the option as nothing
                # showing the new health
                life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
                life.grid(row=1,column=2)
                # showing the new score
                score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
                score.grid(row=1, column=5)
            # showing the updated health
            life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
            life.grid(row=1,column=2)
        # if no choice is selected
        else:
            # showing the message
            result.insert(END,f"\t\tYou did not make any choice!!!!")
    play = Toplevel(start)# copying the Tk() class instance from start
    play.title("Play Game")# title
    play.iconbitmap("c:\\Users\\user\\Downloads\\swg.ico")# icon
    play.geometry("1000x900")# geometry
    play.maxsize(1000,900)# max size
    play.minsize(1000,900)# minsize
    upperplay=Frame(play, bg="springgreen4")# frame 1
    upperplay.pack(fill=BOTH)
    # show label to create space
    gf = Label(upperplay, text=" ", bg="springgreen4", fg="springgreen4", font=("times of roman", 40, "bold", "underline"))
    gf.grid(row=1, column=1)
    # show label to create space
    gf1 = Label(upperplay, text="      ", bg="springgreen4", fg="springgreen4", font=("times of roman", 40, "bold", "underline"))
    gf1.grid(row=2, column=1)
    # heading
    playheading = Label(upperplay, text="\tPlay The Game", bg="springgreen4", fg="palegreen1", font=("times of roman", 40, "bold", "underline"))
    playheading.grid(row=2,  column=2)
    # show label to create space
    gf2 = Label(upperplay, text="      ", bg="springgreen4", fg="springgreen4", font=("times of roman", 40, "bold", "underline"))
    gf2.grid(row=3, column=1)
    lowerplay = Frame(play, bg="palegreen1")
    lowerplay.pack(fill=BOTH) 
    global s # global variable for score
    s = 0 # setting score at 0
    global l# global variable for health
    l=10 # setting health at 10
    # show label to create space
    gf3 = Label(lowerplay, text="", bg="palegreen1", fg="palegreen1", font=("times of roman", 40, "bold", "underline"))
    gf3.grid(row=1, column=1)
    # showing health
    life = Label(lowerplay, text=f"     💗:{l}  ", bg="palegreen1", fg="deep pink", font=("times of roman", 20, "bold"))
    life.grid(row=1,column=2)
    # showing score
    score = Label(lowerplay, text=f"     Score: {s}  ", bg="palegreen1", fg="red", font=("times of roman", 20, "bold"))
    score.grid(row=1, column=5)
    # label
    name = Label(lowerplay, text="Enter your name:", bg="palegreen1", fg="black", font=("times of roman", 20, "bold"))
    name.grid(row=2, column=1)
    nment = StringVar() # nment is a string type variable
    nameentry = Entry(lowerplay, textvariable=nment, width=20, font=("times of roman", 25, "bold"))# user name entry
    nameentry.grid(row=2, column=2)
    gf7 = Label(lowerplay, text="", bg="palegreen1", fg="palegreen1", font=("times of roman", 40, "bold", "underline"))
    gf7.grid(row=3, column=1)
    # label for choose option
    optionlabel = Label(lowerplay, text="   Choose your choice below:", bg="palegreen1", fg="black", font=("poppins", 20, "bold"))
    optionlabel.grid(row=4, column=1)
    lowerplay1 = Frame(play, bg="palegreen1")# frame 2
    lowerplay1.pack(fill=BOTH) 
    # show label to create space
    gf6 = Label(lowerplay1, text="      ", bg="palegreen1", fg="palegreen1", font=("times of roman", 10, "bold", "underline"))
    gf6.grid(row=1, column=1)
    var1 = StringVar()# var1 is a string type variable
    var1.set("Nothing")# setting var1 as nothing
    # radio button for snake option
    snake = Radiobutton(lowerplay1, text="Snake🐍", variable=var1, value="SNAKE", font=("poppins", 20, "bold"), bg="palegreen1", fg="darkgreen")
    snake.grid(row=2, column=3)
    # show label to create space
    gf8 = Label(lowerplay1, text="\t", bg="palegreen1", fg="palegreen1", font=("times of roman", 40, "bold", "underline"))
    gf8.grid(row=2, column=4)
    # radio button for water option
    water = Radiobutton(lowerplay1, text="Water💧", variable=var1, value="WATER", font=("poppins", 20, "bold"), bg="palegreen1", fg="deepskyblue3")
    water.grid(row=2, column=5)
    # show label to create space
    gf9 = Label(lowerplay1, text="\t", bg="palegreen1", fg="palegreen1", font=("times of roman", 40, "bold", "underline"))
    gf9.grid(row=2, column=6)
    # radio button for gun option
    gun = Radiobutton(lowerplay1, text="Gun🔫", variable=var1, value="GUN", font=("poppins", 20, "bold"), bg="palegreen1", fg="black")
    gun.grid(row=2, column=7)
    # submit button
    submit = Button(lowerplay1, text="Submit", bg="brown1", fg="white", font=("poppins", 14, "bold"), padx=15, pady=8, command=gamelogic)
    submit.grid(row=3, column=5)
    # show label to create space
    gf10 = Label(lowerplay1, text="        ", bg="palegreen1", fg="palegreen1", font=("times of roman", 20, "bold", "underline"))
    gf10.grid(row=4, column=3)
    lowerplay2 = Frame(play, bg="palegreen1")# frame 3
    lowerplay2.pack(fill=BOTH)
    # label for opponent's choice
    opponent = Label(lowerplay2, text="         Opponent's choice:   ", bg="palegreen1", fg="black", font=("poppins", 20, "bold"))
    opponent.grid(row=1, column=1)
    # text box to show opponent choice
    opponent_choice = Text(lowerplay2, width=25, height=1, font=("poppins", 20, "bold"))
    opponent_choice.grid(row=1, column=2)
    # show label to create space
    gf11 = Label(lowerplay2, text="", bg="palegreen1", fg="palegreen1", font=("times of roman", 20, "bold", "underline"))
    gf11.grid(row=2, column=1)
    lowerplay3 = Frame(play, bg="palegreen1")# frame 4
    lowerplay3.pack(fill=BOTH) 
    # show label to create space
    gf12 = Label(lowerplay3, text="  ", bg="palegreen1", fg="palegreen1", font=("times of roman", 20, "bold", "underline"))
    gf12.grid(row=1, column=1)   
    # text box to show the result
    result = Text(lowerplay3, width=63, height=6,fg="blue",font=("poppins", 20, "bold"))
    result.grid(row=1, column=2)
    # show label to create space
    gf13 = Label(lowerplay3, text="  ", bg="palegreen1", fg="palegreen1", font=("times of roman", 20, "bold", "underline"))
    gf13.grid(row=2, column=1)  
    play.mainloop() # declaring mainloop() to show the window in the screen
# need help window
def needhelp():
    nhelp=Toplevel(start)# copying the Tk() class instance from start
    nhelp.title("Game Help")# title
    nhelp.iconbitmap("c:\\Users\\user\\Downloads\\swg.ico")# icon
    nhelp.geometry("425x340")# geometry size
    nhelp.maxsize(425,340)# maxsize
    nhelp.minsize(425,340)# minsize
    helpupper=Frame(nhelp,bg="springgreen4")# frame 1
    helpupper.pack(fill=BOTH)
    hf=Label(helpupper,text="",bg="springgreen4")# show label to create space
    hf.grid(row=1,column=1)
    hf1=Label(helpupper,text="",bg="springgreen4",font=("times of roman",40,"bold"))# show label to create space
    hf1.grid(row=2,column=1)
    # heading
    helpheading=Label(helpupper,text="Game Help",bg="springgreen4",fg="palegreen1",font=("times of roman",40,"bold","underline"))
    helpheading.grid(row=2,column=2)
    # show label to create space
    hf2=Label(helpupper,text="      ",bg="springgreen4",font=("times of roman",30,"bold"))
    hf2.grid(row=3,column=1)
    helplower=Frame(nhelp,bg="palegreen1")# frame 2
    helplower.pack(fill=BOTH)
    # help quotes 
    help1=Label(helplower,text="\n\t1.  Snake can float in water.            ",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    help1.grid(row=2,column=1)
    help2=Label(helplower,text="\n\t2.  Gun can kill a snake.                  ",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    help2.grid(row=3,column=1)
    help3=Label(helplower,text="\n\t3.  Water can damage the gun.       ",bg="palegreen1",fg="black",font=("times of roman",15,"bold"),justify=LEFT)
    help3.grid(row=4,column=1)
    # show label to create space
    hf3=Label(helplower,text="      ",bg="palegreen1",fg="palegreen1",font=("times of roman",30,"bold"))
    hf3.grid(row=5,column=1)
    nhelp.mainloop() # declaring mainloop() to show the window in the screen 
# message to show after rating
def rmessage():
    tmsg.showinfo("Thank You!","Thank You! for your rating :)")# showing this message after rating
def about_us():
    tmsg.showinfo("About Us","This Game is developed by Soumyajeet Das.\nIt is created using tkinter module in Python.\nDate: 09/07/2024")
# rate us window
def rate_us():
    rate_window=Toplevel(start)# copying the Tk() class instance from start 
    rate_window.title("Rate Us")# title
    rate_window.iconbitmap("c:\\Users\\user\\Downloads\\swg.ico")# icon
    rate_window.geometry("300x275")# geometry size
    rate_window.maxsize(300,275)# maxsize
    rate_window.minsize(300,275)# minsize
    uframe=Frame(rate_window,bg="seagreen4",pady=20,borderwidth=4,relief="groove")# frame 1
    uframe.pack(fill=X)
    # heading
    title=Label(uframe,text="Rate us here please",font=("poppins",15,"bold"),bg="springgreen4",fg="palegreen1")
    title.pack()
    lframe=Frame(rate_window,bg="palegreen1",pady=20,borderwidth=4,relief="groove")# frame 2
    lframe.pack(fill=X)
    # rate scale to rate
    rate_scale=Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,sliderrelief="sunken",tickinterval=50,bg="palegreen1",borderwidth=2,relief="solid",font=("poppins",10,"bold"))
    rate_scale.set(50)# setting the rate scale at 50
    rate_scale.pack()
    f_label=Label(lframe,text="\n",bg='palegreen1')# frame 3
    f_label.pack()
    # submit button
    s_button=Button(lframe,text="Submit",borderwidth=2,relief="solid",font=("poppins",10,"bold"),padx=10,pady=10,bg="brown1",fg="white",command=rmessage)
    s_button.pack()
    rate_window.mainloop() # declaring mainloop() to show the window in the screen
start.title("Snake-Water-Gun Game")# title
start.iconbitmap("c:\\Users\\user\\Downloads\\swg.ico")# icon
start.geometry("1000x580")# geometry size
start.maxsize(1000,580)# fixing max size
start.minsize(1000,580)# fixing min size
helpmenu=Menu(start)# help menu
hmenu=Menu(helpmenu,tearoff=0)# submenu of help menu
# help menu options
hmenu.add_command(label="Rate Us!",command=rate_us)
hmenu.add_command(label="About Us",command=about_us)
start.config(menu=helpmenu)# configging the help menu here
helpmenu.add_cascade(label="Help",menu=hmenu)# add_cascade the help menu here to add submenu
upper=Frame(start,bg="springgreen4")# frame 1
upper.pack(fill=BOTH)
f=Label(upper,text=" ",bg="springgreen4")# show label to create space
f.grid(row=1,column=1)
# heading
heading=Label(upper,text="\n\tSnake-Water-Gun Game\n",bg="springgreen4",fg="palegreen1",font=("times of roman",40,"bold","underline"))
heading.grid(row=1,column=2)
lower=Frame(start,bg="palegreen1")# frame 2
lower.pack(fill=BOTH)
# show label to create space
f1=Label(lower,text=" ",bg="palegreen1",font=("poppins",20,"bold"))
f1.grid(row=1,column=1)
# show label to create space
f2=Label(lower,text=" ",bg="palegreen1",font=("poppins",20,"bold"))
f2.grid(row=2,column=1)
# show label to create space
f3=Label(lower,text=" ",bg="palegreen1",font=("poppins",20,"bold"))
f3.grid(row=3,column=1)
# show label to create space
f4=Label(lower,text="\t\t\t",bg="palegreen1",font=("poppins",20,"bold"))
f4.grid(row=4,column=2)
# game rules option
rules=Button(lower,text="  1.  Game Rules",bg="palegreen1",fg="black",font=("poppins",20,"bold"),borderwidth=1,relief="flat",justify="left",anchor="w",pady=10,command=gamerules)
rules.grid(row=4,column=3)
# play game options
play=Button(lower,text="2.  Play Game",bg="palegreen1",fg="black",font=("poppins",20,"bold"),borderwidth=1,relief="flat",justify="left",anchor="w",pady=10,command=playgame)
play.grid(row=5,column=3)
# need help options
ghelp=Button(lower,text="3.  Need Help",bg="palegreen1",fg="black",font=("poppins",20,"bold"),borderwidth=1,relief="flat",justify="left",anchor="nw",pady=10,command=needhelp)
ghelp.grid(row=6,column=3)
# show label to create space
f5=Label(lower,text="\n\n\n",bg="palegreen1",font=("poppins",20,"bold"))
f5.grid(row=7,column=2)
start.mainloop()# declaring mainloop() to show the window in the screen