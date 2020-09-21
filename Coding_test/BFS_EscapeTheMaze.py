#
# Escape The Maze
#
# map size : n * m
# start : 1, 1
# exit : n, m
# monstar : 0
#
from collections import deque

# map
#n, m = map(int, input("map size: ").split())
n, m = 4, 4
maps =[[1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1]]
#for i in range(n):
#    maps.append(list(map(int, input().split())))

# Direction of Movement
dx= [-1, 1, 0 ,0]
dy= [0, 0, -1, 1]

# BFS
def bfs(x, y):
    # use Queue(deque)
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # Checking Direction
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # Exception 1
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            # Exception 2
            if maps[nx][ny] == 0:
                continue
            # Distance record
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    # last location
    return maps[n-1][m-1]

for i in maps:
    print(i)
print(bfs(0,0))
