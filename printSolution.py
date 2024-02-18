def printSolution(n, board): 
    ''' 
        A utility function to print Chessboard matrix 
    '''
    for i in range(n): 
        for j in range(n): 
            print(board[i][j], end=' ') 
        print() 