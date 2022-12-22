# user string ('XX_O____O) to list of numbers [10, 10, 0, 1, 0, 0, 0, 0, 1]
def s2n(ss):
    nn = [c for c in ss]
    for i in range(9):
        if nn[i] == 'X':
            nn[i] = 10
        elif nn[i] == 'O':
            nn[i] = 1
        else:
            nn[i] = 0
    return nn


# list of numbers [10, 10, 0, 1, 0, 0, 0, 0, 1] to user string ('XX_O____O)
def n2s(nn):
    ss = ''
    for i in range(9):
        if nn[i] == 10:
            ss = ss + 'X'
        elif nn[i] == 1:
            ss = ss + 'O'
        else:
            ss = ss + ' '
    return ss


# print user string
def print_s(ss):
    print('---------')
    print('| ' + ss[0] + ' ' + ss[1] + ' ' + ss[2] + ' |')
    print('| ' + ss[3] + ' ' + ss[4] + ' ' + ss[5] + ' |')
    print('| ' + ss[6] + ' ' + ss[7] + ' ' + ss[8] + ' |')
    print('---------')


# get cell in row=i, col=j
def m(i, j):
    return n[(i - 1) * 3 + (j - 1)]


# set cell in row=i, col=j by value=v
def set_m(i, j, v):
    n[(i - 1) * 3 + (j - 1)] = v


def n2d():
    d1 = m(1, 1) + m(1, 2) + m(1, 3)
    d2 = m(2, 1) + m(2, 2) + m(2, 3)
    d3 = m(3, 1) + m(3, 2) + m(3, 3)
    d4 = m(1, 1) + m(2, 1) + m(3, 1)
    d5 = m(1, 2) + m(2, 2) + m(3, 2)
    d6 = m(1, 3) + m(2, 3) + m(3, 3)
    d7 = m(1, 1) + m(2, 2) + m(3, 3)
    d8 = m(1, 3) + m(2, 2) + m(3, 1)
    return [d1, d2, d3, d4, d5, d6, d7, d8]


def print_result(d):
    if 30 not in d and 3 not in d and 0 not in n:
        print('Draw')
        return False
    elif 30 in d and 3 not in d:
        print('X wins')
        return False
    elif 30 not in d and 3 in d:
        print('O wins')
        return False
    return True

def step(gamer):
    c = input('> ').split(' ')
    try:
        x = int(c[0])
        y = int(c[1])
        if m(x, y) > 0:
            print('This cell is occupied! Choose another one!')
        else:
            set_m(x, y, gamer)
            s = n2s(n)
            d = n2d()
            print_s(s)
            return print_result(d)
    except ValueError:
        print('You should enter numbers!')
    except IndexError:
        print('Coordinates should be from 1 to 3!')
    return True


s = '         '
n = s2n(s)
d = n2d()
print_s(s)

while step(10) and step(1):
    pass





