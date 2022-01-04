# Description:
# In this problem, your input is a list of integers, which represents the
# layout of a 3D structure, cubes arranged into towers in a row. The first
# number is the height of the first tower, the second is the height of the
# second and so on. The function has to calculate the surface area of the
# structure (we suppose the surface area of a single cube is 6 unit). If
# the input starts as [2, 1], then the first tower connects with the second
# one in 1 level, which means the surface area is 14 units.

# Printing the map for debugging
def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            print(map[i][j], end="")
        print()

# Generating a matrix containing a 'map' based on the numbers of the input list
# For example:
# [2,1,3]
#
# [ [1,1,0],
#   [1,0,0],
#   [1,1,1] ]
def generate_map(list):
    max_height = max(list)
    result = []
    for i in range(len(list)):
        result.append([])
        for j in range(max_height):
            result[i].append(0)

    for i in range(len(list)):
        for j in range(list[i]):
            result[i][j] = 1
    return result

# generating the 'valid neighbours'
def valid_neighbours(map, pos_x, pos_y):
    result = []

    possibble_neighbours = [
        [pos_x - 1, pos_y],
        [pos_x, pos_y - 1],
        [pos_x, pos_y + 1],
        [pos_x + 1, pos_y]
    ]

    # If the neighbour is out of border
    for neighbour in possibble_neighbours:
        if(not(neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(map) or neighbour[1] >= len(map[0]))):
            result.append(neighbour)
    return result

# Counting the neighbours containing a box
def count_neighbour_boxes(map, neighbour_list):
    result = 0
    for neighbour in neighbour_list:
        if(map[neighbour[0]][neighbour[1]] == 1):
            result += 1
    return result

# generating a neighbour matrix, and calculate the sum of the individual surfaces
def calculate_surface_area(map):
    result = 0
    neighbour_matrix = []
    for i in range(len(map)):
        neighbour_matrix.append([])
        for j in range(len(map[i])):
            if(map[i][j] == 1):
                counter = 6 - count_neighbour_boxes(map, valid_neighbours(map, i,j))
                neighbour_matrix[i].append(counter)
            else:
                neighbour_matrix[i].append(0)
    result = sum_matrix(neighbour_matrix)
    return result

def sum_matrix(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result += matrix[i][j]
    return result


# TODO: test it with a list of data
def main():
    example_list = [2,1]
    map = generate_map(example_list)
    surface_area = calculate_surface_area(map)
    print(f"The surface area of the structure is {surface_area} unit.")

if __name__ == '__main__':
    main()
