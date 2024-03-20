def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i -1)

def fatorial(item):
    if item == 1:
        return 1
    else:
        return item * fatorial(item-1)


print(regressiva(5))
print(fatorial(5))