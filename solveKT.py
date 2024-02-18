def solveKT(n): 
    ''' 
        This function solves the Knight Tour problem using  
        Backtracking. This function mainly uses solveKTUtil()  
        to solve the problem. It returns false if no complete  
        tour is possible, otherwise return true and prints the  
        tour.  
        Please note that there may be more than one solutions,  
        this function prints one of the feasible solutions. 
    '''
  
    # Initialization of Board matrix 
    board = [[-1 for i in range(n)]for i in range(n)] 
  
    # move_x and move_y define next move of Knight. 
    # move_x is for next value of x coordinate 
    # move_y is for next value of y coordinate 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
  
    # Since the Knight is initially at the first block 
    board[0][0] = 0
  
    # Step counter for knight's position 
    pos = 1
  
    # Checking if solution exists or not 
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)): 
        print("Solution does not exist") 
    else: 
        printSolution(n, board) 