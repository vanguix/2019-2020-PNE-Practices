def fibosum(n):
    index1 = 0
    index2 = 1
    sumn = 0
    for number in range(0, n+1):
        if number == 0:
            sumn = 0
        elif number == 1:
            sumn = 1
        else:
            number = index1 + index2
            index1 = index2
            index2 = number
            sumn += number
    return sumn

print("Sum of the First 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the First 10 terms of the Fibonacci series:", fibosum(10))
