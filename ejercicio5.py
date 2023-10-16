
def mult(a,b):
    acc=0
    max_num=max(a,b)
    min_num=min(a,b)
    for _ in range(min_num):
        acc+=max_num
    return acc

def mult_rec(a,b):
    if b==1:
        return a
    return a+mult_rec(a,b-1)

print(mult(4,5000000000000))
print(mult_rec(-4,10))
