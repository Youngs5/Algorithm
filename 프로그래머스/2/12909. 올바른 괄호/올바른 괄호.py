def solution(s):
    count = 0
    
    for i in s:
        count = count + 1 if i == "(" else count - 1

        if count == -1:
            return False
        
    if count > 0:
        return False
    else:
        return True