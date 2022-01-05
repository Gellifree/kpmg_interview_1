def count_number_of_attacks(n, r_q, c_q, obstacles):
    sum = 0
    for i in range(n, 0, -1):
        for j in range(1,n+1):
            if(i == r_q and j == c_q):
                print("[Q] ", end="")
            elif(j == c_q and i > r_q):
                print("[T] ", end="")
                sum += 1
            elif(j == c_q and i < r_q):
                print("[B] ", end="")
                sum += 1
            elif(i == r_q and j > c_q):
                print("[R] ", end="")
                sum += 1
            elif(i == r_q and j < c_q):
                print("[L] ", end="")
                sum += 1
            elif(r_q + c_q == i + j):
                print("[h] ", end="")
                sum += 1
            elif(r_q - c_q == i - j):
                print("[H] ", end="")
                sum += 1
            else:
                print("[ ] ", end="")
        print()
    return sum

def main():
    n = 8
    r_q = 4
    c_q = 4
    obstacles = [
        [3,5]
    ]
    sum = count_number_of_attacks(n, r_q, c_q, obstacles)
    print(f"\nSum of the squares: {sum}")

if __name__ == '__main__':
    main()
