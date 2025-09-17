
def main(board,showboard=False):
    board_list = [list(row) for row in board.splitlines()]
    for row in range(len(board_list)):
        for cell in range(len(board_list[row])):
            if "R" in board_list[row][cell]:
                for dr, dc in [(-1, 0), (1, 0), (0 ,-1), (0, 1)]:
                    r, c = row + dr, cell + dc
                    while 0 <= r < len(board_list) and 0 <= c < len(board_list[row]):
                        if board_list[r][c] == ".":
                            board_list[r][c] = "X"
                        elif board_list[r][c] not in ("B", "R", "P"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                        if board_list[r][c] in ("B", "R", "P"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                            break
                        r += dr
                        c += dc

            elif "P" in board_list[row][cell]:
                if row != 0:
                    if cell != 0 and cell != len(board_list[row])-1:
                        board_list[row-1][cell-1] = "X" if board_list[row-1][cell-1] == "." else board_list[row-1][cell-1].replace("X","")+"X"
                        board_list[row-1][cell+1] = "X" if board_list[row-1][cell+1] == "." else board_list[row-1][cell+1].replace("X","")+"X"
                    elif cell == 0 :
                        board_list[row-1][cell+1] = "X" if board_list[row-1][cell+1] == "." else board_list[row-1][cell+1].replace("X","")+"X"
                    
                    elif cell == len(board_list[row])-1 :
                        board_list[row-1][cell-1] = "X" if board_list[row-1][cell-1] == "." else board_list[row-1][cell-1].replace("X","")+"X"
                    
            elif "B" in board_list[row][cell]:
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    r, c = row + dr, cell + dc
                    while 0 <= r < len(board_list) and 0 <= c < len(board_list[row]):
                        if board_list[r][c] == ".":
                            board_list[r][c] = "X"
                        elif board_list[r][c] not in ("B", "R", "P"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                        if board_list[r][c] in ("B", "R", "P"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                            break
                        r += dr
                        c += dc

            elif "Q" in board_list[row][cell]:
                for dr, dc in [(-1, 0), (1, 0), (0 ,-1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    r, c = row + dr, cell + dc
                    while 0 <= r < len(board_list) and 0 <= c < len(board_list[row]):
                        if board_list[r][c] == ".":
                            board_list[r][c] = "X"
                        elif board_list[r][c] not in ("B", "R", "P", "Q"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                        if board_list[r][c] in ("B", "R", "P", "Q"):
                            board_list[r][c] = board_list[r][c].replace("X", "") + "X"
                            break
                        r += dr
                        c += dc 
    if showboard:
        for row in board_list:
            for cell in row:
                print(cell+"  " if len(cell) == 1 else cell+" ", end="")
            print()

    for row in range(len(board_list)):
        for cell in range(len(board_list[row])):
            if "KX" in board_list[row][cell]:
                for dr, dc in [(-1, -1),  (-1 ,0), (-1, 1)
                              , (0, -1)          , (0, -1)
                              , (1, -1),  (1, 0), (1, 1)]:
                    r, c = row + dr, cell + dc
                    r = max(0, min(r, len(board_list)-1))
                    c = max(0, min(c, len(board_list[row])-1))
                    if not "X" in board_list[r][c]:
                        return "Fail" 
                return "Success"
                      

def checkmate(board):
    print(main(board))
