def solution(board, moves):
    new_board = []
    fake_board = []
    basket = []
    answer = 0
    
    for s_board in range(0, len(board)):
        for t_board in range(len(board)-1, -1, -1):
            fake_board.append(board[t_board][s_board])
        new_board.append(fake_board)
        fake_board = []
        
    for i in range(0, len(new_board)):
        while (new_board[i][-1] == 0):
            new_board[i].pop()
    
    for draw in moves:
        count = draw-1
        son_board = new_board[count]
        
        if len(son_board) == 0:
            continue
        
        if len(basket) != 0 and basket[-1] == son_board[-1]:
            basket.pop()
            son_board.pop()
            answer += 2
        else:
            basket.append(son_board[-1])
            son_board.pop()
        
    return answer