import numpy

def chess_pattern(n):
    result = numpy.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    result[i][j] = -1
                else:
                    result[i][j] = 1
            else:
                if(j % 2 == 0):
                    result[i][j] = 1
                else:
                    result[i][j] = -1
    return result

def main():
    print(chess_pattern(8))

if __name__ == '__main__':
    main()
