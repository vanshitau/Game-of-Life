'''
This module provides functions for the 1-dimensional Game of Life.

The 1-dimensional Game of Life occurs on a list of cells where each
cell is either alive or dead. The population of cells evolves from
one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 4
living neighbours in its 2-neighborhood.
2. Any dead cell becomes alive in the next generation if it has 2 or 3
living neighbours in its 2-neighborhood.
3. All other live cells die and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 2-neighborhood of a cell consists of the cell itself and its
two neighbors to the left and two neighbors to the right of the cell
(if those neighbors exist).
'''


def make_cells(n, val):
    '''
    Return a list filled with a specified value.

    Parameters
    ----------
    n : int
        The number of elements in the returned list.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list of `n` copies of `val`

    Raises
    ------
    ValueError
        If `n` is less than zero.
    '''
    
    if n < 0:
        raise ValueError('make_cells() number of elements less than zero, n = ' + str(n))
    a = [val] * n
    return a

def print_cells(cells):
    '''
    Prints a list named cells which have either the element True or False. 

    Parameters
    ----------
    cells : a list
        A list of bool

    Returns
    -------
    prints "#" or "-" depending on the bool in the list 

    Raises
    ------
    None
    '''

    for element in cells:
        if element == True:
            print("#", end='')
        else:
            print("-", end='')
    print()

def neighborhood(cells,index):
    '''
    Returns a list displaying the 2-neighborhood of each element. 

    Parameters
    ----------
    cells : a list
            A list of bool 
            
    index : position of the element
        

    Returns
    -------
    A list with the 2-neighborhood of the cell[index]

    Raises
    ------
    ValueError
       If index is less than 0 
    '''

    if index < 0:
        raise ValueError("The index is less than 0")
    else:
        left_neighbor = max(0,index - 2)
        
        right_neighbor = min(len(cells), index + 3)
    

    return cells[left_neighbor : right_neighbor]


def evolve(cells):
    '''
    Applies the rules of 1D cells and moves each cell to the next generation

    Parameters
    ----------
    cells : a list
        A list of bool

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

        length=len(cells)

        #Create a copy of the cell
        cells_copy = cells.copy()
        
        for i in range(0,length):  
            
            neighbor = neighborhood(cells_copy,i)
            

            #Determines if the cell is alive or dead 
            current_cell = cells_copy[i] 
            
            #Count the number of times the cell is alive
            count = neighbor.count(True)
                    
        
            check = False
        
            if current_cell == True:
                if count == 3 or count == 5:
                    check = True
                    
            elif current_cell == False:
                if count == 2 or count == 3:
                    check = True
            
            
            cells[i] = check

        
    return cells


def blinker(cells,index):
    '''
    Adds a blinker pattern to cells starting at cells[index]

    Parameters
    ----------
    cells : a list
        A list of bool
    index : the positon of each element 

    Returns
    -------
    Cells executing a blinker pattern 

    Raises
    ------
    ValueError:
       If the index is less than 0
       If the blinker pattern does not fit into the cells
    '''
    
    values = [False, False, True, True, False, False]
    length = len(values)

    if index < 0: 
        raise ValueError("The index is less than zero")
    
    elif index > len(cells)-5:    
        raise ValueError("The index is does not fit in the cells")
    
    else:

        for i in range(len(values)):
            cells[index] = values[i]
            index +=1

    return cells
    
