def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos): 
    ''' 
        A recursive utility function to solve Knight Tour  
        problem 
    '''
  
    if(pos == n**2): 
        return True
  
    # Try all next moves from the current coordinate x, y 
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(isSafe(new_x, new_y, board)): 
            board[new_x][new_y] = pos 
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)): 
                return True
  
            # Backtracking 
            board[new_x][new_y] = -1
    return False