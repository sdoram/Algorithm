def infinite_str():
    s = input()
    t = input()
    return 1 if s*len(t) == t*len(s) else 0
        
print(infinite_str())