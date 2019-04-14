
import math
nk = input()
n = int(list(nk.split())[0])
k = int(list(nk.split())[1])

ans =0

def log(n):
    t = 0
    while n > 0:
        n = n/2
        t += 1
    return t

if k > log(n):
    ans = log(n) + 2
else:
    for i in range(k):
        if n%2 == 0:
            n = n/2
        else:
            n = int(n/2) + 1
        
    if n > 1:
        ans = k + int(n)
    else:
        ans = k + int(n) + 1
# arr.append(n)

# def already(arr):
#     for x in arr:
#         if x > 2:
#             return False
#     return True

# def division(arr):
#     for x in arr:
#         if x == 2:
#             pass
#         else:
#             if x%2 == 0:
#                 arr.append(x/2)
#                 arr.append(x/2)
#             else:
#                 arr.append(x/2)
#                 arr.append(x/2+1)
#     return arr

# for i in range(k):
#     if already(arr):
#         pass
#     else:
#         arr = division(arr)
#         ans += 1
    
# ans += 2

print(ans)