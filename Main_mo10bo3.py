from statistics import mean
solve_count = 0
solve_list = []
while solve_count < 6:
    solve_count += 1
    last_solve = float(input(f"Solve number {str(solve_count)} Time: "))
    confirm = input("Are You sure?").lower()
    if confirm == "no":
        last_solve = float(input("Solve Time: "))
    solve_list.append(last_solve)
    print("")
    if solve_count // 3:
        print(solve_list)
        print("Last mean of 3: " + str(mean(solve_list[-3:])) + "\n")

'''save = open("solves.txt", "a")
save.write(solve_list)
save.close()
'''

def print_ave():
    print(f'Average: {mean(solve_list)} for {solve_count} solves yay')
print_ave()


