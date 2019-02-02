a = [[1,2,3],[4,5,6]]


def matrix_final_form (m):
    for row in m:
        print ' '.join(map(str, row))

matrix_final_form(a)