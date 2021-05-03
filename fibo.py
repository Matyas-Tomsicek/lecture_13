def recursive_nth_fibo(n):
    if n < 0:
        message = "Invalid input"
        return message
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = recursive_nth_fibo(n-1)
        b = recursive_nth_fibo(n-2)
        # fibo = recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)
        fibo = a + b
        return fibo

def main():
    n = int(input("Zadej kolik prvků fibonacciho posloupnosti chceš: "))
    # nth = recursive_nth_fibo(n=n)
    fibo = []
    for i in range(n):
        fibo.append(recursive_nth_fibo(n=i))
    print(fibo)
    pass

if __name__ == '__main__':
    main()
