import numpy as np

def tree_height(n, parents):
    # Convert the parent array to a matrix for easier indexing
    matrix = np.zeros((n, n), dtype=bool)
    for i, p in enumerate(parents):
        if p >= 0:
            matrix[p][i] = True

    # Find the depth of each node by counting the number of ancestors
    depths = np.zeros(n, dtype=int)
    for i in range(n):
        j = i
        while j >= 0:
            depths[i] += 1
            j = parents[j]

    # The height of the tree is the maximum depth
    return np.max(depths)

def main():
    # Read input data
    try:
        n = int(input())
        parents = list(map(int, input().split()))
        assert len(parents) == n
    except ValueError:
        print("Invalid input: please enter integers only.")
        return
    except AssertionError:
        print("Invalid input: the number of nodes doesn't match the length of the parent array.")
        return

    # Calculate tree height and print result
    print(tree_height(n, parents))

if __name__ == '__main__':
    main()
