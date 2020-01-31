from statistics import mean
disp_solve_count = 0
solves = 1
solve_list = []
while disp_solve_count < 6:
    str_last_solve = input(f"Solve number {str(solves)} Time: ")
    if str_last_solve != "dnf":
        last_solve = float(str_last_solve)
        confirm = input("Are You sure?").lower()
        solves += 1
        disp_solve_count += 1
        if confirm == "no":
            last_solve = float(input("Solve Time: "))
        solve_list.append(last_solve)
        print("")
    else: solves -= 1
    if disp_solve_count // 3:
        print(solve_list)
        print("Last mean of 3: " + str(mean(solve_list[-3:])) + "\n")

'''save = open("solves.txt", "a")
save.write(solve_list)
save.close()
'''

def print_ave():
    print(f'Average: {mean(solve_list)} for {solves} solves yay')
print_ave()


