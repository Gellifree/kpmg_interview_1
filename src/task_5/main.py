# Description:
# Create a function which expects any number of square matrices and outputs
# a block-matrix which contains the input matrices in its main diagonal, and
# contains 0 in every other place.
# Input is a list, containing the matrices.


def arrange_in_diagonal(list_of_matrices):
    result = []

    for i in range(len(list_of_matrices)):
        result.append([])
        for j in range(len(list_of_matrices)):
            if(i == j):
                result[i].append(list_of_matrices[i])
            else:
                result[i].append(0)
    return result

def main():
    list_of_matrices = [
        [
            [1,2,3],
            [1,2,3],
            [1,2,3]
        ],
        [
            [1,2],
            [1,2]
        ],
        [
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4]
        ],
        [
            [1,2,3],
            [1,2,3],
            [1,2,3]
        ]
    ]
    result = arrange_in_diagonal(list_of_matrices)
    print(f'The output without any formatting: \n {result}')

if __name__ == '__main__':
    main()
