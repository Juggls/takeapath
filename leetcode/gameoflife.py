
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # cheating
        board_copy = [row[:] for row in board]

        for i in range(len(board)):
            for j in range(len(board[0])):
                new_state = self.get_new_state(board_copy, (i, j))
                board[i][j] = new_state

    def get_new_state(self, board, pos):
        n_set = self.get_neighbours(board, pos)
        count = 0

        for n in n_set:
            if board[n[0]][n[1]] == 1:
                count += 1

        if board[pos[0]][pos[1]] == 1:
            if count < 2 or count > 3:
                return 0
            return 1
        else:
            if count == 3:
                return 1
            return 0

    def get_neighbours(self, board, pos):
        n = []
        for x in range(pos[0] - 1, pos[0] + 2):
            for y in range(pos[1] - 1, pos[1] + 2):
                if (x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and not (x == pos[0] and y == pos[1])):
                    n.append((x, y))

        return n
