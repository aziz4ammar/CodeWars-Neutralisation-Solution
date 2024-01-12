def neutralise(s1, s2):
    result = ''
    
    for char1, char2 in zip(s1, s2):
        if char1 == char2:
            result += char1
        else:
            result += '0'
    
    return result