import copy

# Kiem tra ma tran dung
def check(state):
    if state == [[1,2,3],[8,0,4],[7,6,5]]:
        return True
    return False


# Tao cac trang thai moi khi di chuyen qua 1 o
def generateState(state, moves):
    next = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for move in moves:
                    nextI = i+move[0]
                    nextJ = j+move[1]
                    if 0<= nextI <3 and 0<= nextJ <3:
                        tmp = copy.deepcopy(state)
                        tmp[i][j] = tmp[nextI][nextJ]
                        tmp[nextI][nextJ] = 0
                        next.append(tmp)
    return next


# BFS de tim duong di toi trang thai dung
def BFS(input):
    frontier = [[input]]
    visited = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while frontier:
        node = frontier.pop(0)
        visited.append(node[-1])
        next = generateState(node[-1], moves)
        for state in next:
            if state not in visited:
                frontier.append(node + [state])
                if check(state):
                    return frontier[-1]
    return []


# Test voi ma tran dau vao
input = [[2,0,3],[1,8,4],[7,6,5]]
result = BFS(input)
for state in result:
    print('=========')
    for row in state:
        print(row)
    print('=========')

print(f'Total step: {len(result)}')