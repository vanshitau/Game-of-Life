'''
This module provides functions for the 2-dimensional Game of Life.

The 2-dimensional Game of Life occurs on an n-by-n array of
cells where each cell is either alive or dead. The population of cells
evolves from one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 3
living neighbours in its 1-neighborhood (the cell itself does not
count towards the number of living neighbors).
2. Any dead cell becomes alive in the next generation if it has 3
living neighbours in its 1-neighborhood.
3. All other live cells die, and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 1-neighborhood of a cell consists of the cell itself and its
eight neighbours, which are the cells that are horizontally, vertically,
or diagonally adjacent (if those neighbors exist).
'''

import math
import sys
import copy

def test_indexes(cells, row, col, func_name):
    '''
    Test if row and column indexes are valid for a square array.

    This function tests if `row` and `col` are both in the
    range 0 to (n - 1), inclusive, where n is equal to
    len(cells). Raises a ValueError if an index is out of
    range.

    Parameters
    ----------
    cells : list-of-list of bool
        The n-by-n cells of a 2D Game of Life.
    row : int
        A row index for cells.
    col : int
        A column index for cells.
    func_name : str
        The name of the function that called test_indexes

    Raises
    ------
    ValueError
        If `row` or `col` is out of range.
    '''
    n = len(cells)
    if row < 0:
        raise ValueError(func_name, 'number of rows < 0, row = ', row)
    elif row >= n:
        raise ValueError(func_name, 'number of rows >= len(cells), row = ', row)
    if col < 0:
        raise ValueError(func_name, 'number of cols less than zero, col = ', col)
    elif col >= n:
        raise ValueError(func_name, 'number of cols >= len(cells), col = ', col)


def make_cells(rows, cols, val):
    '''
    Return an array filled with a specified value.

    Parameters
    ----------
    rows : int
        The number of rows in the array.
    cols : int
        The number of columns in the array.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list-of-lists of `rows`-by-`cols` copies of `val`

    Raises
    ------
    ValueError
        If `rows` or `cols` is less than zero.
    '''
    
    if rows < 0:
        raise ValueError('make_cells() size less than zero, rows = ', rows)
    if cols < 0:
        raise ValueError('make_cells() size less than zero, cols = ', cols)
    a = []
    for i in range(0, rows):
        row = [val] * cols
        a.append(row)
    return a


def print_cells(cells):
    '''
    Prints a list-of-lists named cells which have either the element True or False

    Parameters
    ----------
    cells: a list-of-lists of bool
    
    Returns
    -------
    Prints '#' for True and '-' for False

    Raises
    ------
    None
    '''
    
    for element in cells:  
        for j in element:  
            if j == True:  
                print("#", end='')
            else:           
                print("-", end='')
        print()
    return cells



def neighborhood(cells, row, col):
    '''
    Returns a list-of-lists displaying the 1-neighborbood for the cell[row][col]

    Parameters
    ----------
    cells : list-of-lists of bool
    
    row : int
        The location of the list in cells
        
    col : int
        The location of the element in rows.

    Returns
    -------
    list
        A list-of-lists containting the 1-neighborhood for the cell[row][col]

    Raises
    ------
    ValueError
        If row or col is less than zero.
    '''
    
    if row < 0:
        raise ValueError()
    elif col < 0:
        raise ValueError()
    else:
        nrow = len(cells)
        final_cells = []
        
     
        if row == 0:
            #row == 0 
            left_neighbor = max(0, col-1)
            right_neighbor = min(len(cells[0]), col + 2)
            temp_cells= cells[0][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)

            #row == 1
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[1]), col +2)
            temp_cells= cells[1][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)
            
        elif row == nrow-1:

            #row == nrow-2
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[nrow-2]), col +2)
            temp_cells= cells[nrow-2][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)

            #row == nrow-1
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[nrow-1]), col +2)
            temp_cells= cells[nrow-1][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)
            

        else:
            #row == row-1
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[row - 1]), col + 2)
            temp_cells= cells[row-1][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)

            #row == row
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[row]), col + 2)
            temp_cells= cells[row][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)

            #row == row + 1
            left_neighbor = max(0,col-1)
            right_neighbor = min(len(cells[row+1]), col + 2)
            temp_cells= cells[row+1][left_neighbor: right_neighbor]
            final_cells.append(temp_cells)


        cells = final_cells
            
        return cells
            

def evolve(cells):
    '''
    Applies the rules of the Game of Life for 2D list and moves each cell to the next generation

    Parameters
    ----------
    cells : list-of-lists of bool
    
    Returns
    -------
    A new generation of cells 

    Raises
    ------
    ValueError
        If cells is empty 
    '''
    
    if cells == []:
        raise ValueError("The cells/list is empty")
    else:
        length1=len(cells)  
        length2=len(cells[0])  

        #Create a copy of cells
        finalized_output = copy.deepcopy(cells)

        
        for i in range(0, length1):
            for j in range(0, length2):
                
                temp_list = neighborhood(finalized_output, i, j)
                
                current_cell = finalized_output[i][j]

                #Creates a 1D list with True and False 
                boolean_list=[]
                for row in temp_list:
                    for col in row:
                        boolean_list.append(col)
                count = boolean_list.count(True)
                

                check = False
                
                if current_cell == True:
                    if count == 3 or count == 4:
                        check = True
                elif current_cell == False:
                    if count == 3:
                        check = True
                        
                cells[i][j]=check
                

    return cells
        
                   
def glider(cells, top_row, left_col):
    '''
    Displays the glider pattern on the cells starting on cells[top_row][left_col]

    Parameters
    ----------
    cells : a list-of-lists of bool
        
    top_row : The first row of cells
    
    left_col : The first column of cells
    
    Returns
    -------
    list-of-lists
    Cells executing a glider pattern 

    Raises
    ------
    ValueError
        If top_row or left_col is less that 0
        If the glider pattern does not fit 
    '''
    
    if top_row < 0:
        raise ValueError("The top_row is less than 0")
    elif left_col < 0:
        raise ValueError("The left_col is less than 0")
    elif len(cells)-top_row < 4 or len(cells[0])-left_col < 4:
        raise ValueError("The pattern does not fit")
    else:
        
        copy_cells=cells

        #Set everything to False
        for i in range(5):
            for j in range(5):
                copy_cells[top_row+i][left_col+i] = False

        #Second Row
        copy_cells[top_row + 1][left_col + 1] = True
        

        #Third Row
        copy_cells[top_row + 2][left_col + 2] = True
        copy_cells[top_row + 2][left_col + 3] = True

        #Forth Row
        copy_cells[top_row + 3][left_col + 1] = True
        copy_cells[top_row + 3][left_col + 2] = True

        cells = copy_cells

    return cells
                       
                

