def Dijkstra(Graph, _s, _d): 
    row = len(Graph) 
    col = len(Graph[0]) 
    dist = [float("Inf")] * row 
    Blackened =[0] * row 
    pathlength =[0] * row 
    parent = [-1] * row 
    dist[_s]= 0
    for count in range(row-1): 
        u = MinDistance(dist, Blackened) 
        if u == float("Inf"): 
            break
        else: 
            Blackened[u]= 1 
        for v in range(row): 
            if Blackened[v]== 0 and Graph[u][v] and dist[u]+Graph[u][v]<dist[v]: 
                parent[v]= u 
                pathlength[v]= pathlength[parent[v]]+1
                dist[v]= dist[u]+Graph[u][v] 
            elif Blackened[v]== 0 and Graph[u][v] and dist[u]+Graph[u][v]== dist[v] and pathlength[u]+1<pathlength[v]: 
                parent[v]= u 
                pathlength[v] = pathlength[u] + 1
    if dist[_d]!= float("Inf"): 

        PrintPath(parent, _d) 
    else: 
        print("There is no path between vertex ", _s, "to vertex ", _d)
  

def PrintPath(parent, _d): 
    if parent[_d]==-1: 
        print(_d), 
        return
    PrintPath(parent, parent[_d]) 
    print("->", _d) 
def MinDistance(dist, Blackened): 
    min = float("Inf") 
    for v in range(len(dist)): 
        if not Blackened[v] and dist[v]<min: 
            min = dist[v] 
            Min_index = v 
    return float("Inf") if min == float("Inf") else Min_index 
  

Graph =[[0, 1, float("Inf"), float("Inf"), 10], 
       [1, 0, 4, float("Inf"), float("Inf")], 
       [float("Inf"), 4, 0, 7, float("Inf")], 
       [float("Inf"), float("Inf"), 7, 0, 2], 
       [10, float("Inf"), float("Inf"), 2, 0]] 
Dijkstra(Graph, 0, 3) 