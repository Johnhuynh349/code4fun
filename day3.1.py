#check if the number is pronic (product of 2 consecutive number)
def is_pronic(n):
    for i in range(0, n):
        if i*(i+1) == n:
            return True
        else:
            continue
    return False
            
list_n = [6, 2, 12, 13, 14, 17, 20, 30, 24, 42, 56, 45, 24]

print(list(map(is_pronic, list_n)))