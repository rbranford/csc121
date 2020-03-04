def print_10_stars():
    for _ in range(10):
        print('*', end=' ')
    print()

def print_5_stars():
    for _ in range(5):
        print('*', end=' ')
    print()

def print_20_stars():
    for _ in range(20):
        print('*', end=' ')
    print()


def problem_2():
    print_10_stars()
    print_5_stars()
    print_20_stars()


def problem_3():
    for _ in range(10):
        for _ in range(10):
            print('*', end=' ')
        print()


def problem_4():
    for _ in range(10):
        for _ in range(5):
            print('*', end=' ')
        print()


def problem_5():
    for _ in range(5):
        for _ in range(20):
            print('*', end=' ')
        print()

def problem_6():
    for _ in range(10):
            for i in range(10):
                print(i, end=' ')
            print()

    
def problem_7():
    for i in range(10):
        for _ in range(10):
            print(i, end=' ')
        print()


def problem_8():
    for i in range(10):
        for j in range(i+1):
            print(j, end=' ')
        print()


def problem_9():
    for i in range(10):
        for j in range(i):
            print(' ', end=' ')
        for j in range(10-i):
            print(j, end=' ')
        print()


def problem_10():
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j < 10:
                print(' ', end=' ')
            print(i*j, end=' ')
        print()
        

def problem_11():
    for i in range (10):
        for j in range(10-i):
            print (' ', end=' ')
        for j in range(1, i+1):
            print(j, end=' ')
        for j in range(i-1, 0, -1):
            print(j, end=' ')
        print()


def problem_12():
    for i in range(10):
        for j in range(10-i):
            print (' ', end=' ')
        for j in range(1,i+1):
            print (j, end=' ')
        for j in range(i-1,0,-1):
            print (j, end=' ')
        print()
    for i in range(10):
        for j in range(i+2):
            print (' ', end=' ')
        for j in range(1,9-i):
            print (j, end=' ')
        print()


def problem_13():
    for i in range(10):
        for j in range(10-i):
            print (' ', end=' ')
        for j in range(1, i+1):
            print (j, end=' ')
        for j in range(i-1,0,-1):
            print (j, end=' ')
        print()
    for i in range(10):
        for j in range(i+2):
            print (' ', end=' ')
        for j in range(1, 9-i):
            print (j, end=' ')
        for j in range(7-i, 0, -1):
            print (j, end=' ')
        print()



