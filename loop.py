s = "Emma is a data scientist who knows Python. Emma works at Google."
A = 0

for i in range(len(s)):
    if s[i:i + 4] == "Emma":
        A += 1
        if A == 2:
            print("The position of Emma is ", i)
            break
