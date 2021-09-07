import math

def floyd(graph):
    def get_path(P, u, v):
        path = [u]
        while u != v:
            u = P[u][v]
            path.append(u)
    
        return path
    
    
    #V = [[0, 2, 0, 3, 1, 0, 0, 10],
     #    [2, 0, 4, 0, 0, 0, 0, 0],
      #   [0, 4, 0, 0, 0, 0, 0, 3],
       #  [3, 0, 0, 0, 0, 0, 0, 8],
        # [1, 0, 0, 0, 0, 2, 0, 0],
         #[0, 0, 0, 0, 2, 0, 3, 0],
         #[0, 0, 0, 0, 0, 3, 0, 1],
         #[10, 0, 3, 8, 0, 0, 1, 0],]
    V = graph
    
    N = len(V) # число вершин в графе
    P = [[v for v in range(N)] for u in range(N)] # начальный список предыдущих вершин для поиска кратчайших маршрутов
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                if V[i][j] > d:
                    V[i][j] = d
                    P[i][j] = k     # номер промежуточной вершины при движении от i к j
    
    # нумерацця вершин начинается с нуля
    start = 0
    end = len(V)-1
    return get_path(P, end, start)