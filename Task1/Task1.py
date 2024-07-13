import sys

def my_path(n, m):
    path = []
    circ_array = m * list(range(1, n + 1))

    while True:
        path.append(circ_array[0])
        if circ_array[(m-1)] == 1: # конец == 1 стоп
            break
        circ_array[:] = circ_array[(m-1):] + circ_array[:(m-1)] # смещаю массив влево на m - 1

    return path

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    my_path = my_path(n, m)
    print(''.join(map(str, my_path)))


