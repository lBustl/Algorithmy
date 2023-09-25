def create_empty_board(n):
    return [['O' for _ in range(n)] for _ in range(n)]

def is_safe(board, row, col):

    n = len(board)

    for i in range(n):
        if board[row][i] == 'X':
            return False
        
    for j in range(n):
        if board[j][col] == 'X':
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'X':
            return False

    return True

def display(board,n):
    print (5*n*'*')
    for row in range(n):
        print (board [row])


def main(n):
    board=create_empty_board(n)
    display(board,n)
    for i in range(n):
        for j in range(n):
            check=is_safe(board, i, j)
            if check== True:
                board[i][j]='X'
                display(board,n)

from collections import deque

def read_maze(file_name):
    with open(file_name, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def write_maze(file_name, maze):
    with open(file_name, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

def is_valid_move(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == ' '

def find_shortest_path(maze):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left

    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (row, col), path = queue.popleft()
        if (row, col) == end:
            return path
        visited.add((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(maze, new_row, new_col) and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))

    return None

def solve_maze(input_file, output_file):
    maze = read_maze(input_file)
    shortest_path = find_shortest_path(maze)

    if shortest_path:
        for row, col in shortest_path:
            maze[row][col] = 'X'
        write_maze(output_file, maze)
        print("Maze solved and saved to", output_file)
    else:
        print("No solution found for the maze.")

if __name__ == "__main__":
    input_file = "maze.mz"
    output_file = "maze-out.mz"
    solve_maze(input_file, output_file)


