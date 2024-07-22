import csv
import random

import config

N = config.N

def openGrid(difficulty):
    #0 for easy
    #1 for medium
    #2 for hard
    fileName = ""
    if(difficulty ==0):
        fileName = "database\Easy.csv"
    elif (difficulty == 1):
        fileName = "database\Medium.csv"
    elif (difficulty == 2):
        fileName = "database\Hard.csv"
    else:
        return

    with open(fileName, "r") as File:
        r = random.randint(0,99999)
        reader = csv.reader(File)

        for i in range(r):
            next(reader)
        sudoku = next(reader)
        File.close()
    
    return sudoku

def getGrid(difficulty):
    Grid =[0,0,0,0,0,0,0,0,0]
    tempGrid = openGrid(difficulty)
    index = 0

    for i in range(N):
        Grid[i] = tempGrid[index:index+9]
        index += 9

    for i in range(N):
        for j in range(N):
            if Grid[i][j] == ".":
                Grid[i][j] = 0
            else:
                Grid[i][j] = int(Grid[i][j])
    
    return Grid
