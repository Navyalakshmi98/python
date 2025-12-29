s="1235"
def check_digit(s):
    for char in s:
        if not(48<=ord(char)<=57):
            return False
    return True
print(check_digit(s))
        