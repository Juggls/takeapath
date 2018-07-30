class Solution:
    def check_array(self, arr):
        seen = {}

        for i in arr:
            if i in seen:
                return False

            if i < 1 or i > 9:
                return False

            seen[i] = True

        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board:
            int_row = [int(x) for x in row if x != "."]
            if self.check_array(int_row) == False:
                return False

        for y in range(9):
            col = [board[x][y] for x in range(9)]
            int_col = [int(x) for x in col if x != "."]

            if self.check_array(int_col) == False:
                return False

        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                flattened_tile = []
                for i in range(x, x + 3):
                    for j in range(y, y+3):
                        flattened_tile.append(board[i][j])

                flattened_tile = [int(x) for x in flattened_tile if x != "."]
                if self.check_array(flattened_tile) == False:
                    print("swag")
                    print(flattened_tile)
                    return False

        return True
