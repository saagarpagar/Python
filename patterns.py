# some basic python patterns
# i just made different functions so its easy to try

def square(n):
    for i in range(n):
        print("* " * n)

def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)



def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def floyd(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    n = 5   # change size here

    print("Square:")
    square(n)

    print("\nRight Triangle:")
    right_triangle(n)

    print("\nInverted Triangle:")
    inverted_triangle(n)

    print("\nPyramid:")
    pyramid(n)

    print("\nDiamond:")
    diamond(n)

    print("\nNumber Triangle:")
    number_triangle(n)

    print("\nFloyd’s Triangle:")
    floyd(n)
    
    print("\nHollow Square:")
    hollow_square(n)
