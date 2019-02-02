def det_2x2(m):
    det = m[0][0]*m[1][1] - m[1][0]*m[0][1]
    return det


def det_1x1(m):
    return m[0][0]


def parity(i):
    if i % 2 == 0:
        return -1
    else:
        return 1


def submatrix(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[i+1:]+m[:i])]


def matrix_final_form(m):
    for row in m:
        return ' '.join(map(str, row))



def det_nxn(m):
    if len(m) == 1:
        return det_1x1(m)
    elif len(m) == 2:
        return det_2x2(m)
    else:
        determinant = 0
        for i in range(len(m)):
            determinant += parity(i)*m[0][i]*det_nxn(submatrix(m,0,i))
        return determinant


def start(filename):
    input = open(filename).read().split('=')
    for data in input:
        lst = [item.split() for item in data.split('\n')[:-1:]]
        new_lst =[]
        for i in lst:
            if i != []:
                new_lst.append(i)
        matrices = [[int(x) for x in row] for row in new_lst]
        print 'The discriminant of the matrix\n%s\nis\n%.2f' % (matrix_final_form(matrices), det_nxn(matrices))

a = [[1,2,3],[4,5,6]]

print matrix_final_form(a)