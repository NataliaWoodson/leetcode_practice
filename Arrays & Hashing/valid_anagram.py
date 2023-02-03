def isAnagram(s, t):
    if len(s) != len(t):
        return False

    char_counts = {}

    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    for char in t:
        if char in char_counts:
            char_counts[char] -= 1
        else:
            return False
    
    for count in char_counts.values():
        if count != 0:
            return False

    return True
