def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def sum(n):
    partSum = 0
    while n != 0:
        partSum += n % 10
        n //= 10
    return partSum


def calcFactSum(n):
    factNum = fact(n)
    return sum(factNum)


find_sum_fact = 100
print(calcFactSum(find_sum_fact))
