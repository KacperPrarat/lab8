def sum_rec(n):
    if n == 1:
        return n
    else:
        return sum_rec(n-1)+n

print(sum_rec(3))