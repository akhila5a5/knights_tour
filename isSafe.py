def isSafe(x, y, board): 
    ''' 
        A utility function to check if i,j are valid indexes  
        for N*N chessboard 
    '''
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
        return True
    return False