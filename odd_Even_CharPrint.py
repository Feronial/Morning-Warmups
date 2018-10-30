N = int(input())

for i in range(0, N):

    string = input()

    for k in range(0, len(string)):
        if k % 2 == 0:
            print(string[k], end='')

    print(" ", end='')

    for m in range(0, len(string)):
        if m % 2 != 0:
            print(string[m], end='')

    print("")
