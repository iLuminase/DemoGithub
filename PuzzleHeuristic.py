import heapq
class State:
    def __init__(self, board, g=0, h=0, parent=None):
        self.board = board  # Ma trận 3x3
        self.g = g          # Chi phí từ trạng thái bắt đầu đến trạng thái hiện tại
        self.h = h          # Heuristic: chi phí ước lượng đến đích
        self.f = g + h      # Tổng chi phí (f = g + h)
        self.parent = parent  # Để theo dõi đường đi
        self.blank_pos = self.find_blank()  # Vị trí của ô trống

    # Tìm vị trí ô trống
    def find_blank(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)

    # Puzzle Đích
    def is_goal(self):
        return self.board == [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    # So sánh các giá trị của 2 bảng có bằng nhau k?
    def __eq__(self, other):
        return self.board == other.board

    # So sánh chi phí ước lượng (f) trong hàng đợi
    def __lt__(self, other):
        return self.f < other.f

    # bảng băm
    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def generate_children(self):
        # Sinh ra các trạng thái con dựa trên việc di chuyển ô trống
        children = []
        x, y = self.blank_pos
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # xuống, lên, phải, trái

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                child = State(new_board, self.g + 1, parent=self)
                children.append(child)

        return children
# Xác định đường đi 
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0:
                target_x = (state.board[i][j] - 1) // 3
                target_y = (state.board[i][j] - 1) % 3
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# DeQueue


def a_star(initial_state):
    open_list = []
    closed_set = set()

    # Khởi tạo heuristic cho trạng thái ban đầu
    initial_state.h = manhattan_distance(initial_state)
    initial_state.f = initial_state.g + initial_state.h

    # Đưa trạng thái đầu vào hàng đợi ưu tiên
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state  # Trạng thái đích đã tìm thấy

        closed_set.add(hash(current_state))

        for child in current_state.generate_children():
            if hash(child) in closed_set:
                continue

            child.h = manhattan_distance(child)
            child.f = child.g + child.h

            heapq.heappush(open_list, child)

    return None  # Không tìm thấy lời giải

def solve_8_puzzle(initial_board):
    initial_state = State(initial_board)
    result = a_star(initial_state)

    if result:
        print("Found solution:")
        state_path = []
        while result:
            state_path.append(result.board)
            result = result.parent
        for board in reversed(state_path):
            for row in board:
                print(row)
            print()
    else:
        print("No solution found.")


initial_board = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]  # Trạng thái khởi đầu
solve_8_puzzle(initial_board)

