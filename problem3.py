# problem link - https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())

    if (n % 2 == 0):
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")