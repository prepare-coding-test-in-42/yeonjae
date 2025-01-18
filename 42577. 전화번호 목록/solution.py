def solution(phone_book):    
    phone_book.sort()
    
    for idx in range(0, len(phone_book) - 1):
        if phone_book[idx + 1].startswith(phone_book[idx]):
            return False
        
    return True
