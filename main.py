import time

import UI_main
import config

N = config.N 

temp_Grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#main solve fucntion
def sudokuSolve():
    start_time = time.time()

    #modifying all cells for possibilities
    while (not grid_verify()):
        modified = False
        for i in range(N):
            for j in range(N):
                if (config.grid[i][j] == 0 and modify_cell_options(i,j)):
                    modified = True
        
        #cell wise solving
        cell_changed = cell_solve()
        if cell_changed:
            continue
        
        #row wise solving
        row_changed = row_solve()
        if row_changed:
            continue

        #column wise solving
        clm_changed = clm_solve()
        if clm_changed:
            continue
        
        #3x3 Zone wise solving
        zone_changed = zone_solve()
        if zone_changed:
            continue

        #final backtrack solving
        if(modified):
            continue
        backtrack_changed = backtrack_init()

        #non solvable case
        if(not grid_verify()):
            end_time = time.time()
            print_grid(config.grid)
            UI_main.displayTime(False, end_time - start_time)

            print("Couldnt solve the sudoku")
            return False
    
    #solved case
    end_time = time.time()
    print_grid(config.grid)
    UI_main.displayTime(True, end_time - start_time)

    print("Sudoku solved")
    return True
        
#cell solve functions
def cell_solve():
    cell_modified = False

    row, clm = 0,0
    while (row < N):
        #finding empty cells with 1 possibility
        if(config.grid[row][clm] == 0):
            if (len(config.options[row][clm]) == 1):
                update_cell(row,clm,config.options[row][clm][0])

                print("updated:",row,clm,config.options[row][clm][0])
                cell_modified = True

                row, clm = 0, 0
                continue
        else:
            #for already assigned cells 
            config.options[row][clm] = [config.grid[row][clm]]

        if(clm >= 8):
            clm = 0
            row += 1
        else:
            clm += 1
    
    return cell_modified

def modify_cell_options(row,clm):
    ismodified = False

    #removing cell possibilities in
    #row 
    for i in range(N):
        if(config.grid[row][i] in config.options[row][clm]):
            config.options[row][clm].remove(config.grid[row][i])
            ismodified = True
    #clm
    for i in range(N):
        if (config.grid[i][clm] in config.options[row][clm]):
            config.options[row][clm].remove(config.grid[i][clm])
            ismodified = True

    #3x3 zone
    if N == 16:
        div  = 4
    else:
        div = 3
    rnew, cnew = row - row % div, clm - clm % div;
    for i in range(rnew,rnew + 3):
        for j in range(cnew, cnew + 3):
            if (config.grid[i][j] in config.options[row][clm]):
                config.options[row][clm].remove(config.grid[i][j])
                ismodified = True


    return ismodified

#row, clm, zone  solve functions
def row_solve():
    i = 0
    while (i < N):
        #for every row
        poss = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for j in range(N):
            if config.grid[i][j] != 0:
                continue
            for k in config.options[i][j]:
                poss[k - 1] += 1;

        if (1 in poss):
            num = poss.index(1) + 1
            
            #checking which cell had the options
            for j in range(N):
                if config.grid[i][j] != 0:
                    continue
                if num in config.options[i][j]:
                    update_cell(i, j, num)
                    print("row updated:", i, j, num)
                        
                    return True

        i += 1          
        
    return False

def clm_solve():
    i = 0
    while (i < N):
        #for every colum
        poss = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for j in range(N):
            if config.grid[j][i] != 0:
                continue
            for k in config.options[j][i]:
                poss[k - 1] += 1;

        if (1 in poss):
            num = poss.index(1) + 1
            
            #checking which cell had the options
            for j in range(N):
                if config.grid[j][i] != 0:
                    continue
                if num in config.options[j][i]:
                    update_cell(j, i, num)
                    print("clm updated:", j, i, num)
                        
                    return True
                        
        i += 1

    return False

def zone_solve():
    i = 0
    j = 0
    if N == 16:
        div = 4
    else:
        div = 3
    while (i < N):
        #for each zone
        poss = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for k in range(i,i+div):
            for l in range(j, j+div):
                #for each cell
                if config.grid[k][l] != 0:
                    continue
                for m in config.options[k][l]:
                    poss[m - 1] += 1

        if (1 in poss):
            num = poss.index(1) + 1

            for k in range(i,i+3):
                for l in range(j, j+3):
                    #for each cell
                    if config.grid[k][l] != 0:
                        continue
                    if num in config.options[k][l]:
                        update_cell(k, l, num)
                        print(f"zone {i},{j} updated:", k, l, num)

                        return True

        if(j >= N - div):
            j = 0
            i += div
        else:
            j += div

    return False

#backtrack solve functions
def backtrack_init():
    global temp_Grid

    for i in range(N):
        for j in range(N):
            temp_Grid[i][j] = config.grid[i][j]
    
    print("Recursing....")

    if backtrack_solve(0,0):
        for i in range(N):
            for j in range(N):
                if config.grid[i][j] != 0:
                    continue
                update_cell(i, j, temp_Grid[i][j])
        return True
    
    return False

def backtrack_solve(row, clm):
    #next step
    if clm == N:
        if row == N - 1:
            return True
        row += 1
        clm = 0
    
    if temp_Grid[row][clm] != 0:
        return backtrack_solve(row, clm + 1)
    
    #main recursion
    for num in config.options[row][clm]:

        if isValid(row, clm, num):

            temp_Grid[row][clm] = num

            if backtrack_solve(row, clm + 1):
                return True

        #backing out of recursion
        temp_Grid[row][clm] = 0
    
    return False

def isValid(row, clm, number):

    #checking if a number is valid in cell
    if N == 16:
        div = 4
    else:
        div = 3
    for i in range(N):
        if temp_Grid[row][i] == number:
            return False
    
    for i in range(N):
        if temp_Grid[i][clm] == number:
            return False

    rnew, cnew = row - row %div, clm - clm % div
    for i in range(rnew, rnew + div):
        for j in range(cnew, cnew + div):
            if temp_Grid[i][j] == number:
                return False

    return True
        
#general functions
def update_cell(row,clm, number):
    #updates cell
    config.grid[row][clm] = number
    config.options[row][clm] = [number]

    UI_main.Frame3.after(UI_main.get_delay_time(), UI_main.update_cellUI(row, clm, number))

def grid_verify():
    #row verify
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += config.grid[i][j]
        
        if (sum != 136):
            return False
    
    #clm verify
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += config.grid[j][i]
        
        if (sum != 136):
            return False
    
    #3x3 zone verify
    for i in range(0, N, N//3):
        for j in range(0, N, N//3):
            #checking each zone
            sum = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    sum += config.grid[k][l]
            
            if (sum != 136):
                return False

    return True

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                print("_",end="  ")
            else:
                print(grid[i][j], end= "  ")
        print()
    print()

def setup_grid(difficulty):
    tempGrid = getGrid(difficulty)
    for i in range(N):
        config.grid[i] = tempGrid[i]

#difficulty
def findDiff():
    for i in range(N):
        options = 0
        for j in range(N):
            config.grid[i][j]


if (__name__ == '__main__'):
    #setup_grid(0) 
    UI_main.SetupUI()
    sudokuSolve()
    


