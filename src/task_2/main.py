# Description:
# Given the queen's position and the locations of all the obstacles, find and
# print the number of squares the queen can attack from her position at  (𝑟𝑞,𝑐𝑞).
# In the board above, there are 24 such squares.
# There are obstacles on the chessboard, each preventing the queen from
# attacking any square beyond it on that path.


# Check a given position for obstacle
def is_there_an_obstacle(i,j,obstacles):
    for obstacle in obstacles:
        if(i == obstacle[0]-1 and j == obstacle[1]-1):
            #print(f"obstacle in: {obstacle[0]} and {obstacle[1]}")
            return True
    return False

# Draw the map out in the 'right' order
def draw_map(map, obstacles):
    print()
    for i in range(len(map)-1, -1, -1):
        print(f"{i+1}   ", end="")
        for j in range(len(map)):
            if(is_there_an_obstacle(i,j,obstacles)):
                print("[X]", end=" ")
            elif(map[j][i] == 0):
                print("[ ]", end=" ")
            else:
                print(f"[{map[j][i]}]", end=" ")
        print()
    print("\n     ", end="")
    for i in range(1,9):
        print(f"{i}   ", end="")

# Generating the map with possible squares
def generate_map(n, r_q, c_q, obstacles):
    sum = 0
    result = []
    # Matrix filled with zeroes
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(0)


    ## Generating the different 'paths' of the queen

    # Right path
    for i in range(c_q, n+1):
        if(is_there_an_obstacle(r_q-1,i, obstacles) == True):
            result[i-1][r_q-1] = '1'
            break;
        else:
            result[i-1][r_q-1] = '1'

    # Left path
    for i in range(c_q, 0, -1):
        if(is_there_an_obstacle(r_q-1,i - 1, obstacles) == True):
            break;
        else:
            result[i-1][r_q-1] = '1'

    # Top
    for i in range(r_q, n + 1):
        if(is_there_an_obstacle(i-1,c_q-1, obstacles) == True):
            #print('obstacle!')
            break;
        else:
            result[c_q-1][i-1] = '1'

    # Bottom
    for i in range(r_q, 0, -1):
        if(is_there_an_obstacle(i-1,c_q-1, obstacles) == True):
            break;
        else:
            result[c_q-1][i-1] = '1'

    # top right diagonal
    j = r_q
    for i in range(c_q, n + 1):
        if(is_there_an_obstacle(j-1,i-1,obstacles) == True):
            break;
        else:
            result[i-1][j-1] = '1'
        j += 1
        if(j > n):
            break


    # top left diagonal
    i = c_q
    for j in range(r_q, n+1):
        if(is_there_an_obstacle(j-1,i-1,obstacles) == True):
            break;
        else:
            result[i-1][j-1] = '1'
        i -= 1
        if(i <= 0):
            break



    # bottom right diagonal
    i = c_q
    for j in range(r_q, 0, -1):
        #print(f"{j},{i}")

        if(is_there_an_obstacle(j-1,i-1,obstacles) == True):
            break;
        else:
            result[i-1][j-1] = '1'
        i += 1
        if(i > n):
            break


    # bottom left diagonal
    j = r_q
    for i in range(c_q, 0, -1):
        if(is_there_an_obstacle(j-1,i-1,obstacles) == True):
            break;
        else:
            result[i-1][j-1] = '1'

        j -= 1
        if(j <= 0):
            break

    # 'Put' the Queen in the right position
    result[c_q-1][r_q-1] = 'Q'
    draw_map(result, obstacles)
    return result

# Sum the amount of 'ones', which represent the attackable squares
def count_attackable_squares(map):
    result = 0
    for i in range(len(map)):
        for j in range(len(map)):
            if(map[i][j] == '1'):
                result += 1
    return result

def main():
    n = 8
    r_q = 4
    c_q = 4
    obstacles = [
        [3,5]
    ]
    map = generate_map(n, r_q, c_q, obstacles)
    result = count_attackable_squares(map)
    print(f"\n\nThe Queen can attack {result} squares.")

if __name__ == '__main__':
    main()
