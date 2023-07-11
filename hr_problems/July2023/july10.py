# NumPy - Numeric Python package 

import numpy 

def arrays(arr):
    arr = numpy.array(arr, float)
    # result = []
    # for element in range(len(par_result)):
    #     result.append(par_result[(len(par_result - 1) - i])
    # return numpy.aray(result, float)
    arr = arr[::-1]
    return arr


def main():
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

if __name__ == '__main__':
    main()