from statistics import mean

attempts = 0
disp_count = 1
solves = 0
disp_list = []
solve_list = []

for var in range(1, 30):
    print(f"30/{var} with a {30 % var} remainder")


# Determines if input is a float?
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def print_ave():
    print(f'Average: {mean(solve_list)} for {attempts} solves yay')


while attempts < 6:
    str_last_solve = input(f"Solve number {str(disp_count)} Time: ");
    print("hello")
    attempts += 1
    disp_count += 1
    # eval str_last_solve for str as bool
    '''res = isinstance(str_last_solve, str)
    res = isfloat(res)
    print(res)
    print(str_last_solve)'''
    print(attempts)
    if str_last_solve != "dnf":
        last_solve = float(str_last_solve)
        confirm = input("Are You sure?").lower()

        if confirm == "no":
            last_solve = float(input("Solve Time: "))
        solve_list.append(last_solve)
        disp_list.append(last_solve)
    elif str_last_solve == "dnf":
        confirm = input("Are You sure?").lower()

        if confirm == "no":
            last_solve = float(input("Solve Time: "))
        disp_list.append("DNF")
        count_dnf = disp_list.count("DNF")
        print(str(count_dnf) + "here i am")

    #   solves -= 1
    if attempts % 3 == 0:
        print(attempts)
        print(disp_list)
        print("Last mean of 3: " + str(mean(solve_list[-3:])) + "\n")
# End of loop

#
'''save = open("solves.txt", "a")
save.write(solve_list)
save.close()
'''

print_ave()
# Trying to calculate accuracy
# print(solves)

# TODO
'''
Built in stats?
data collect/store
compute data
change last item
compute accuracy
print data
saves/prints data to external .txt file


how to deal with dnfs'''
