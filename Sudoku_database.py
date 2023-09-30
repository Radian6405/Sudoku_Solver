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

def openNewDB():
    sudoku = [[0, 5, 0, 0, 0, 4, 0, 8, 0, 6, 0, 0, 0, 0, 9, 16],
         [1, 0, 0, 0, 0, 0, 0, 13, 4, 0, 0, 7, 15, 0, 8, 0],
         [13, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 9, 5, 10, 0, 0],
         [0, 11, 12, 15, 10, 0, 0, 0, 0, 0, 5, 0, 3, 4, 0, 13],
         [15, 0, 1, 3, 0, 0, 7, 2, 0, 0, 0, 0, 0, 5, 0, 0],
         [0, 0, 0, 12, 0, 3, 0, 5, 0, 11, 0, 14, 0, 0, 0, 9],
         [4, 7, 0, 0, 0, 0, 0, 0, 12, 0, 15, 16, 0, 0, 0, 0],
         [0, 0, 0, 0, 14, 0, 15, 0, 6, 9, 0, 0, 0, 0, 12, 0],
         [3, 0, 15, 4, 0, 13, 14, 0, 0, 0, 0, 1, 0, 0, 7, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 0, 0, 0, 0],
         [11, 0, 16, 10, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3, 5, 0],
         [0, 0, 13, 0, 0, 0, 0, 0, 14, 0, 15, 16, 0, 9, 0, 1],
         [9, 0, 2, 0, 0, 14, 0, 4, 8, 0, 0, 0, 0, 0, 0, 0],
         [0, 14, 0, 0, 0, 0, 0, 10, 9, 0, 3, 0, 0, 0, 1, 7],
         [8, 0, 0, 0, 16, 0, 0, 1, 2, 14, 11, 4, 0, 0, 0, 3],
         [0, 0, 0, 1, 0, 0, 5, 0, 0, 16, 0, 6, 0, 12, 0, 0]]
    return sudoku

def getGrid(difficulty):
    if(N == 16):
        sudoku = openNewDB()
        return sudoku

    Grid =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    tempGrid = openGrid(difficulty)
    index = 0

    for i in range(N):
        Grid[i] = tempGrid[index:index+N]
        index += N

    for i in range(N):
        for j in range(N):
            if Grid[i][j] == ".":
                Grid[i][j] = 0
            else:
                Grid[i][j] = int(Grid[i][j])
    
    return Grid
