from random import choice


def get_allowed(size, prev_queens, current_line):
    positions = [True] * size
    for i in range(size):
        if i in prev_queens:
            positions[i] = False
            continue
        for j in range(len(prev_queens)):
            if abs(i - prev_queens[j]) == current_line - j:
                positions[i] = False
                break
    return [i for i in range(len(positions)) if positions[i]]
     


def recurse(question_size, line=0, back=False):
    while line < question_size:
        if back:  # The next line has no solution
            stack[line].remove(queen.pop())  # Recent cause no solution
        else:  # New line
            stack[line] = get_allowed(question_size, queen, line)
        if stack[line]:  # If current line has solution
            queen.append(choice(stack[line]))
            return recurse(question_size, line + 1)
        else:  # If not
            return recurse(question_size, line - 1, back=True)
    return queen


def print_chestboard(board):
    for i in range(8):
        line = [' |_| '] * 8
        line[board[i]] = ' |Q| '
        print(''.join(line)+'\n')


queen = []
stack = [[]] * 8
recurse(8)
print_chestboard(queen)
