#
# Number of icecream
# use DFS
# Size: n * m
#

# input map
#n, m = map(int, input("map: ").split())
n, m = 3, 3
# map list
graph = [[0,0,1],[0,1,0],[1,0,1]]
#for i in range(n):
#    graph.append(list(map(int, input())))

# DFS check
def dfs(x, y):
    if n <= x or x <= -1 or m <= y or y <= -1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# Filling the beverge
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)

