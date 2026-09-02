#1)
def check_valid_tr_number(number):
    
    if not isinstance(number, (int, str)):
        return False
        
    s = str(number)
    
    
    if len(s) != 11 or not s.isdigit() or s[0] == '0':
        return False
        
    
    digits = [int(d) for d in s]
    
    
    odd_sum = 0
    for i in range(0, 9, 2):
        odd_sum += digits[i]
        
    
    even_sum = 0
    for i in range(1, 8, 2):
        even_sum += digits[i]
        
   
    check_10 = (odd_sum * 7 - even_sum) % 10
    if check_10 != digits[9]:
        return False
        
   
    total_10_sum = 0
    for i in range(10):
        total_10_sum += digits[i]
        
    if total_10_sum % 10 != digits[10]:
        return False
        
    return True