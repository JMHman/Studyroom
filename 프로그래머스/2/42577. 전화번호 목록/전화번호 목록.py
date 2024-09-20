def solution(phone_book):
    pb = {}
    
    for phone in phone_book:
        pb[phone] = 1
    
    for phone in phone_book:
        temp = ''
        for num in phone:
            temp += num
            if temp in pb and temp != phone:
                return False
    
    return True
