"""Graph shortest path solved with DFS on a weighted adjacency matrix."""

import numpy as np


def graph_dfs(cur, dis):  # Current city code, distance walked
    global min1
    global visited
    global e
    if dis > min1:
        return
    if cur == n:  # Check if we arrived at the target city
        if dis < min1:
            min1 = dis  # Update the shortest distance
            return
    for j in range(1, n + 1):  # Try every city from 1 to n
        # Check if city j has a path from cur and has not been visited
        if e[cur][j] != 99999999 and visited[j] == 0:
            visited[j] = 1  # Mark city as visited
            graph_dfs(j, dis + e[cur][j])
            visited[j] = 0
    return


if __name__ == "__main__":
    ### Graph initiation by adjacency matrix, indices start from 1 ###
    min1 = 99999999  # Infinity, also the initial shortest-path value
    map_size = 6  # map_size = number of cities + 1
    visited = np.zeros(map_size, dtype=np.int64)  # 1-D array of visited nodes
    e = np.zeros((map_size, map_size), dtype=np.int64)  # Max size of the map
    # n, m = map(int, input().split(' '))  # n => target city, m => no. of paths
    n = 5  # Destination city => n * n map
    # Graph weighted edge: [vertex1, vertex2, weight]
    weighted_path = [[1, 2, 2], [1, 5, 10], [2, 3, 3], [2, 5, 7], [3, 4, 4], [3, 1, 4], [4, 5, 5], [5, 3, 3]]
    for i in range(1, n + 1):  # Row
        for j in range(1, n + 1):
            if i == j:
                e[i][j] = 0
            else:
                e[i][j] = 99999999
    for i in range(len(weighted_path)):
        # a, b, c = map(int, input().split(' '))
        a, b, c = weighted_path[i][0], weighted_path[i][1], weighted_path[i][2]
        e[a][b] = c  # Unidirectional edge
        # e[b][a] = c  # Enable this line for a bi-directional edge in graph
    print("The Adjacency Matrix of Graph:\n{0}".format(e))
    visited[1] = 1  # Mark the starting city as visited
    graph_dfs(1, 0)
    # The shortest path for traversal of the graph
    print("The shortest path to city {0} is {1}.".format(map_size - 1, min1))
