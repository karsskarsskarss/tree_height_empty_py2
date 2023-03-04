# python3

import sys
import threading
import numpy as np

#pārbaudeGithubam
def compute_height(n, parents):
    # Write this function
    def _compute_height(node):
        if node in cache:
            return cache[node]
        elif parents[node] == -1:
            cache[node] = 1
        else:
            cache[node] = 1 + _compute_height(parents[node])
        return cache[node]
    max_height = 0
    # Your code here
    cache = {}
    for node in range(n):
        height = _compute_height(node)
        if height > max_height:
            max_height = height
    return max_height


def main():
    n = int(np.array(input().split(), dtype=int)[0])
    parents = np.array(input().split(), dtype=int)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    max_height = compute_height(n, parents)
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    print(max_height)
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))