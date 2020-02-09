from statistics import mean

print("Hello from Iceland! Hello from Greenland!")

scrm = open("scrambles.txt", "r")
mo3 = open("Mo3.txt", "a")

attempts = 0
disp_count = 1
solves = 0
disp_list = []
solve_list = []
lower = ""
last_solve = []
flt_list = []

class MySolve:
    def __init__(self, num=1, time=0, isdnf=False, scramble=""):
        self.num = num
        self.time = time
        self.isdnf = isdnf
        self.scramble = scramble

    def write_out(self):
        print(self.time, self.isdnf, self.scramble)

    def solve_ip(self, num):
        self.time, self.isdnf = input("Enter Time then If is dnf").split()
        self.num = MySolve(self.time, self.isdnf, self.scramble)


'''s1 = MySolve()
s1.write_out()
s1.solve_ip(1)
s1.write_out()'''


# Determines if input is a float?


def is_float(s):
    result = False
    if s.count(".") == 1:
        if s.replace(".", "").isdigit():
            result = True
    return result


def ip_num(string):
    if is_float(string) or string.isdecimal():
        last = float(str_solve)
        print("this maybe gets run")
        return last


def is_num(string):
    if is_float(string) or string.isdecimal():
        return bool


def ip_str(is_str):
    if isinstance(is_str, str):
        lower_case = is_str.lower()
        return lower_case


def append_float(num):
    solve_list.append(num)
    disp_list.append(num)


def while_ip(str_slv, low, dsp_cnt):
    while not is_num(str_slv) and not low == "dnf":
        str_slv = input(f"Enter solve {dsp_cnt}:")
        low = ip_str(str_slv)
        print("print me")
    # Returns a decimal, float or "dnf"
    return str_slv


def confirm():
    return True


def print_ave(slv):
    '''Prints the average of a list.'''
    flt = [float(i) for i in slv]
    print(f'Average: {mean(flt)} for {attempts} solves yay')


while attempts < 6:
    print(scrm.readline())
    str_solve = input(f"Enter solve {disp_count}:")

    lower = ip_str(str_solve)

    # Prompts until user ip that Returns a decimal, float or "dnf"
    var = while_ip(str_solve, lower, disp_count)

    if is_float(str_solve):
        last_solve = float(str_solve)

    print("ok")
    attempts += 1
    solves += 1
    disp_count += 1

    if lower != "dnf":
        print("This code gets run")
        disp_list.append(var)
        solve_list.append(var)
        print(disp_list)
        print(solve_list)
    elif lower == "dnf":
        disp_list.append("DNF")
        print(disp_list)

    if attempts % 3 == 0:
        flt_list = [float(i) for i in solve_list]
        dnf_list = disp_list[-3:]
        print(disp_list)
        if not dnf_list.count("DNF"):
            print("Last mean of 3: " + str(mean(flt_list[-3:])) + "\n")
            str2 = str1 = ', '.join(str(e) for e in dnf_list)
            mo3.write(str2)
            mo3.write(" Last mean of 3: " + str(mean(flt_list[-3:])) + "\n")

        else:
            print("Last mean of 3: DNF \n")
            str2 = str1 = ', '.join(str(e) for e in dnf_list)
            mo3.write(str2)
            mo3.write(" Last mean of 3: DNF \n")


# End of loop
mo3.close()

save = open("solves.txt", "a")
str1 = ', '.join(str(e) for e in disp_list)

print("Solves saved to text file.")

dnf_input = disp_list.count("DNF")
dnf_num_confirm = disp_list.count("dnf")
total_dnfs = dnf_num_confirm + dnf_input
try:
    disp_list.remove("DNF")
except ValueError:
    print("You got no DNFs!")

print(solve_list)
print_ave(solve_list)
# Trying to calculate accuracy
# print(solves)
print("Accuracy:")
print(1 - (total_dnfs / attempts))
flt_list = [float(i) for i in solve_list]
str2 = str(mean(flt_list))
save.write(str1 + " Ave: " + str2 + "\n")
save.close()

# TODO Built in stats?
# TODO data collect / store
# TODO compute data
# TODO change last item
# TODO compute accuracy
# TODO print data
# TODO saves / prints data to external .txt file
# TODO prints scrambles before timer input
# TODO how to deal with dnfs
# TODO fix counting logic for input and checks
# TODO disp list and solve list fix
