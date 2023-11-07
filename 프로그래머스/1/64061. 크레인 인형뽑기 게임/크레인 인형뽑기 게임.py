def solution(board, moves):
    basket = []
    answer = 0
    
    for move in moves:
        index = 0
        while index < len(board) and board[index][move - 1] == 0:
            index += 1

        if index < len(board):
            if len(basket) > 0 and basket[-1] == board[index][move-1]:
                basket.pop()
                answer += 2
            else:
                basket.append(board[index][move-1])
            board[index][move-1] = 0
            
    return answer