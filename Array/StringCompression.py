"""
Given a string in the form 'AAAABBBBCCCCCDDEEEE' 
compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings 
single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' e
ven though this technically takes more space.

The function should also be case sensitive, 
so that a string 'AAAaaa' returns 'A3a3'.
"""

def compress(text):
    count = 1
    result = prev = text[0]

    for char in text[1:]:
        if char == prev:
            count += 1
        else:
            result += str(count) + char
            count = 1
        prev = char
    
    result += str(count)
    return result

compress('AAAaaa')
