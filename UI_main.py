from tkinter import *
import threading

import main
import config 
from Sudoku_database import *

N = config.N

Name = "Sudoku Solver"
MenuList = ["Easy", "Medium", "Hard"]

def SetupUI():
    global Frame3

    #button functions
    def Randomize_grid():
        currOption = Option.get()
        if (currOption == "Easy"):
            tempGrid = getGrid(0)
        elif (currOption == "Medium"):
            tempGrid = getGrid(1)
        elif (currOption == "Hard"):
            tempGrid = getGrid(2)
        else:
            return
            
        for i in range(N):
            config.grid[i] = tempGrid[i]

        temp = [[[i + 1 for i in range(N)] for i in range(N)] for i in range(N)]
        for i in range(N):
            config.options[i] = temp[i]

        Make_GridUI()

    def Make_GridUI():
        for i in range(N):
            for j in range(N):
                if(config.grid[i][j] == 0):
                    text = ""
                else:
                    text = f"{config.grid[i][j]}"

                Cell = Label(Frame3, text=text, font=("Arial", 18),
                highlightbackground=config.button, highlightthickness=1,
                width = 2, height= 1,bg = config.dark_gray,fg = config.white,)
                Cell.grid(row= i, column=j)

    def Solve_Grid():
        main.sudokuSolve()
        return

    def initThreading():
        t1 = threading.Thread(target=Solve_Grid)
        t1.start()
        return 

    #-----User Interface-----

    #---main root---
    root = Tk()
    root.title(Name)
    root.configure(background=config.light_gray)
    root.iconbitmap("UI_Elements\icon.ico")
    root.geometry("610x800+800+0")

    Main_frame = Frame(root,bg = config.dark_gray)

    #frame1
    image = PhotoImage(file= "UI_Elements\logo.gif")
    Title = Label(Main_frame, image=image,bg = config.dark_gray)

    #frame2
    Frame2 = Frame(Main_frame,bg = config.dark_gray)
    Option = StringVar(Main_frame)
    Option.set("Difficulty")
    Diff_menu = OptionMenu(Frame2, Option, *MenuList)
    Diff_menu.config(width= 12, font=("Arial", 16),relief=GROOVE,bg = config.button,fg = config.white,
                    highlightbackground=config.dark_gray, highlightthickness=1,
                    activebackground=config.dark_gray, activeforeground= config.white)
    Diff_menu["menu"].config(borderwidth = 10, font=("Arial", 14),relief=GROOVE,bg = config.button,fg = config.white,
                            activebackground=config.dark_gray, activeforeground=config.white)
    diffOption = Option.get()
    Randomise_Btn = Button(Frame2, text= "Randomize", font=("Arial", 14), width= 15, height= 1,
                            relief=GROOVE, command= Randomize_grid, bg = config.button,fg = config.white,
                            activebackground=config.dark_gray, activeforeground=config.white,highlightbackground=config.white)

    #frame3
    Frame3 = Frame(Main_frame, border=2, highlightbackground=config.button, highlightthickness=1, bg = config.light_gray)
    Make_GridUI()

    #frame4 
    global delayCheck 
    global Frame4
    global runTime 
    Frame4 = Frame(Main_frame,bg = config.dark_gray)
    delayCheck = IntVar(Frame4)
    realTime_checkbox = Checkbutton(Frame4, text= "Run slower",font=("Arial", 10), highlightthickness=0,justify="left",
                                    bg = config.dark_gray,fg = config.white,activebackground=config.dark_gray, 
                                    activeforeground=config.white,highlightbackground=config.dark_gray, selectcolor = config.dark_gray,
                                    variable= delayCheck, onvalue=1, offvalue=0, offrelief= FLAT) 
    
    RunTimeText = "Run Time: " + "      "
    runTime = Label(Frame4, text = RunTimeText, font=("Arial", 10), justify="right",
                    bg = config.dark_gray,fg = config.white,activebackground=config.dark_gray, 
                    activeforeground=config.white,highlightbackground=config.white)

    #frame5
    Frame5 = Frame(Main_frame,bg = config.dark_gray)
    Solve_Btn = Button(Frame5, text="Solve", font=("Arial", 20), width= 10, relief=GROOVE, command=initThreading,
                        bg = config.button,fg = config.white, activebackground=config.dark_gray, 
                        activeforeground=config.white,highlightbackground=config.white)
    Exit_Btn = Button(Frame5, text="Exit", font=("Arial", 12), width= 10, relief=GROOVE, command=root.quit,
                        bg = config.button,fg = config.white, activebackground=config.dark_gray, 
                        activeforeground=config.white,highlightbackground=config.white)

    #---placing in grids---
    Main_frame.grid(row= 0, column= 0,padx= 50, pady= 20, sticky="N")
    #frame1
    Title.grid(row=0, column= 0, sticky="N",pady= 20)

    #frame2
    Frame2.grid(row= 1, column=0, pady= 10, sticky="N")
    Diff_menu.grid(row= 0, column = 0,padx= 20, sticky="N")
    Randomise_Btn.grid(row= 0, column= 1, padx= 20, sticky="N")

    #frame3
    Frame3.grid(row= 2, column= 0, sticky="N")

    #frame4
    Frame4.grid(row=3, column= 0, sticky= "N",pady=5)
    realTime_checkbox.grid(row=0, column=0, sticky= "W", padx=50)
    runTime.grid(row= 0, column= 2, sticky="E", padx= 50)

    #frame5
    Frame5.grid(row=4, column= 0,pady=10)
    Solve_Btn.grid(row=0, column=0, padx= 150)
    Exit_Btn.grid(row= 1, column= 0, pady= 10, sticky="E")


    root.mainloop()

def update_cellUI(row, clm, number):
    text = f"{number}"
    UpdatedCell = Label(Frame3, text=text, font=("Arial", 18),
                highlightbackground=config.button, highlightthickness=1, bg= config.dark_gray, fg= config.Red,
                width = 2, height= 1)
    UpdatedCell.grid(row= row, column=clm)
    return

def get_delay_time():
    if(delayCheck.get() == 1):
        return config.DelayTime
    return 0

def displayTime(isSolved, RunTime):
    RunTime = round(RunTime, 2)
    if isSolved:
        LabelText = "Run Time: " + f"{RunTime}"
    else:
        LabelText = "Run Time: " + "--.--"

    runTime.config(text= LabelText)    
