#Artūrs Jānis Karss 211REC029
import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    for x in range(n):
       height = 0
       id = x
       while id != -1:
            height += 1
            id = parents[id]
       max_height = max(max_height, height)
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    
    print(compute_height(n, parents))

#2.versija runo un paskaties main pec tam!!!!!
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()