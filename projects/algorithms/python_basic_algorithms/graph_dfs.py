import numpy as np

def graph_dfs(cur,dis): #Current City Code, Distance walked, Adjacency Matrix, the Shortest Path
    global min1
    global visited
    global e
    if dis > min1:
        return 
    if cur == n: #Check if it arrives the target city in map
        if dis < min1:
            min1 = dis #Update the shortest distance
            return 
    for j in range(1, n +1): #Trying from city 1 to city n
        #Check if j city contains path, and if it is visited
        if e[cur][j] !=99999999 and visited[j] == 0:
            visited[j] = 1 #Label city in
            graph_dfs(j,dis+e[cur][j])
            visited[j] = 0 
    return 
    
if __name__ == "__main__":
    ###### Graph Initiation by Adjacency Matrix and Starting Index from 1
    min1 = 99999999 #Represent infinity in map and initial shortest path
    map_size = 6 #Map_size  = number of city + 1
    visited = np.zeros(map_size,dtype=np.int64) #1D array for visited node
    e = np.zeros((map_size,map_size),dtype=np.int64) #The max size of whole map 
    # n,m = map(int,input().split(' ')) #n=> target place , m=> no. of path
    n = 5 #Destination city => n*n map
    weighted_path = [[1,2,2],[1,5,10],[2,3,3],[2,5,7],[3,4,4],[3,1,4],[4,5,5],[5,3,3]] #Graph Weighted Edge: [vertex1,vertex2,weight]
    for i in range(1,n+1): #Row
        for j in range(1,n+1):
            if i==j:
                e[i][j] = 0
            else:
                e[i][j] = 99999999
    for i in range(len(weighted_path)):
        #a, b, c = map(int, input().split(' '))
        a,b,c = weighted_path[i][0],weighted_path[i][1],weighted_path[i][2]
        e[a][b] = c #Unidirectional edge
        #e[b][a] = c #****Enable this line for Bi-directional edge in graph 
    print("The Adjacency Matrix of Graph:\n{0}".format(e)) 
    visited[1] = 1 #Set the initial first city to be invaild for visiting
    graph_dfs(1,0) 
    print("The shortest path to city {0} is {1}.".format(map_size - 1,min1)) #The shortest path for traversal of graph
        
        
    
