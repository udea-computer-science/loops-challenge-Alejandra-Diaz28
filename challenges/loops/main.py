if __name__ == "__main__":
    n = int(input())
    print(f"el número ingresado es: {n}")
    x = []
    if 1 <= n and n <= 20:
        for i in range(0, n):
            x.append(i)
        print(f"los números no negativos menores a {n} son: {x}")
        print("el cuadrado de cada número es:")
        for i in range(0, n):
            print(i**2)
    else:
        print("el número debe estar entre 1 y 20")
