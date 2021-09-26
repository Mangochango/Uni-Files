import random
import numpy as np
import matplotlib.pyplot
import sys
sys.setrecursionlimit(10**6)

def greedy_descent(initial_state, neighbours, cost):
    
    """Iteratively improves the state until a local minimum
    is reached 
    
    Returns the list of states"""
    
    min_found = False
    current_state = initial_state
    states = [initial_state]
    while min_found is False:
        neighbours_list = neighbours(current_state)
        current_min  = current_state
        for neighbour in neighbours_list:
            if cost(neighbour) < cost(current_min):
                current_min = neighbour
        if cost(current_min) < cost(current_state):
            current_state = current_min
            states.append(current_state)
        else:
            min_found = True
    return states
        
def greedy_descent_with_random_restart(random_state, neighbours, cost, repetitions=0, chessboard=[]):
    
    """Restarts by calling random state once min has been found"""
    
    current_state = random_state()
    if len(chessboard) == 0:
        n = len(current_state)
        chessboard= np.zeros((n, n))
    for state in greedy_descent(current_state, neighbours, cost):
        #print(state)
        min_state = state
    if cost(min_state) == 0:
        
        for row, column in enumerate(state):
            chessboard[row, column-1] += 1
        repetitions += 1
       # print(str(repetitions) + " solutions found so far.")
        if repetitions <= 400:
            greedy_descent_with_random_restart(random_state, neighbours, cost, repetitions, chessboard)
        else:
            print(chessboard)
            matplotlib.pyplot.imshow(chessboard, cmap='hot')
            
    else:
       # print("RESTART")
        greedy_descent_with_random_restart(random_state, neighbours, cost, repetitions, chessboard)
            
def n_queens_neighbours(state):
    """ Returns a sorted list of states that are neighbors of the current assignment.
    
    A neighbor is otained by swapping the position of two numbers in the given permutation """
    
    n = len(state)
    results = []
    for i in range(n):
        for j in range(n):
            list1 = list(state)
            if j > i:
                list1[i],list1[j] = list1[j],list1[i]
                results.append(tuple(list1))

    return sorted(results)

def n_queens_cost(state):
    """ Returns the number of conflicts for the given state.
    
    Which is the number of unordered pairs of queens that threaten eachother.
    
    """
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if j > i:
                dx =i-j
                dy = state[i] -state[j]
                if abs(dx) == abs(dy):
                    conflicts += 1
    
    return conflicts
def draw_chessboard(state):
    n = len(state)
    topline = "+" +"-" * n*3 + "+"
    rows = ["|" + " "*n*3 + "|"for i in range(0,n)]
   
    for row, column in enumerate(state):
        rows[row] = rows[row][0:column*3] +'X' + rows[row][column*3 + 1:]
    
    print(topline)
    for row in rows:
        print(row)
    print(topline)
            
        
            
def chessboard_plot(state):
    n = len(state)
    chessboard = np.zeros((n,n))
    chessboard[1::2, 0::2] = 1
    chessboard[0::2, 1::2] = 1
    
    for row, column in enumerate(state):
        chessboard[row, column-1] = 2
    print(chessboard[0][1])
    print(chessboard)
    
    matplotlib.pyplot.imshow(chessboard, cmap='hot')





N = 6
#random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))  

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)