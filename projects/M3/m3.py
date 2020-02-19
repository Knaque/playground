"""Find the mean, median and mode of a list of random numbers."""

# ============================= Import modules ==============================
from sys import argv
import math
import dataset_loader as d
import matplotlib.pyplot as plot
# ===========================================================================


# ================================== Args ===================================
if "-h" in argv:
    print("Available arguments are:")
    print("""
    -i
        Prints additional info about the list.

    -c
        Prints the raw contents of the list.

    -g
        Generates a new dataset on run.

    -p <plot_x> <plot_y>
        Shows a MatPlotLib chart for the two specified lists.

    -h
        Prints this help message.""")
    quit()

output_list_info = True if "-i" in argv else False
output_list_contents = True if "-c" in argv else False
generate_new_data = True if "-g" in argv else False
generate_matplotlib = True if "-p" in argv else False

plot_x = None
plot_y = None
if generate_matplotlib is True:
    for set in range(1, 3):
        try:
            if argv[argv.index("-p")+set] in ["gender", "age", "income",
                                              "education"]:
                if argv[argv.index("-p")+set] == "gender":
                    if set == 1:
                        plot_x = d.gender_raw
                    else:
                        plot_y = d.gender_raw
                elif argv[argv.index("-p")+set] == "age":
                    if set == 1:
                        plot_x = d.age_raw
                    else:
                        plot_y = d.age_raw
                elif argv[argv.index("-p")+set] == "income":
                    if set == 1:
                        plot_x = d.income_raw
                    else:
                        plot_y = d.income_raw
                elif argv[argv.index("-p")+set] == "education":
                    if set == 1:
                        plot_x = d.education_raw
                    else:
                        plot_y = d.education_raw
                else:
                    print("Something went wrong... Ctrl+F: 7fb7f")
            else:
                print(f"'{argv[argv.index('-p')+set]}' is not a valid",
                      f"argument for '{'plot_x' if set == 1 else 'plot_y'}'")
                quit()
        except IndexError:
            print("Missing required argument",
                  f"'{'plot_x' if set == 1 else 'plot_y'}'")
            quit()
# ===========================================================================


# ============================= Define function =============================
def main(list):
    """Contains all the math and IO for float values."""
    # ===== Perform calculations =====
    # Find lowest value in list
    lowest_value = list[0]
    # Find highest value in list
    highest_value = list[len(list)-1]

    # Calculate mean
    mean = 0
    for i in list:
        mean = mean + i
    mean = round(mean / len(list), 2)

    # Calculate median
    median = 0
    if (len(list) % 2) == 0:
        median = round((list[int(len(list)/2-1)]+list[int(len(list)/2)])/2, 2)
    else:
        median = round(list[int(len(list)/2-0.5)], 2)

    # Calculate mode
    all_numbers = []
    for item in list:
        if item not in all_numbers:
            all_numbers.append(item)
    occurences = []
    for item in all_numbers:
        occurences.append(0)
    for number in all_numbers:
        position = 0
        for item in list:
            if number == item:
                occurences[position] += 1
    most_occurences = 0
    for i in occurences:
        if i > most_occurences:
            most_occurences = i
    mode = ""
    counter = 0
    for i in occurences:
        if i == most_occurences and mode == "":
            mode = str(all_numbers[counter])
        elif i == most_occurences:
            mode = mode + ", " + str(all_numbers[counter])
        counter += 1

    # Calculate standard deviation
    variance = sum(pow(x-mean, 2) for x in list) / len(list)
    std_dev = math.sqrt(variance)

    # ===== Output results =====
    if output_list_info is True:
        print("Dataset size: " + str(len(list)))
        print("Lowest value: " + str(lowest_value))
        print("Highest value: " + str(highest_value))
        print("")

    if output_list_contents is True:
        print("Contents of list:")
        print(list)
        print("")

    print("Mean: " + str(mean))
    print("Median: " + str(median))
    print("Mode: " + mode)
    print("Variance: " + str(variance))
    print("Std. Dev.: " + str(std_dev))
# ===========================================================================


# ===================== Generate new data if applicable =====================
if generate_new_data is True:
    try:
        import dataset_generator as dg
    except ModuleNotFoundError:
        print("dataset_generator.py is missing, aborting.")
        quit()
    dg.lint_check()
# ===========================================================================


# ===================== Call functions & print headers ======================
print("")

print("====================== Gender =====================")
main(d.gender)

print("")
print("")

print("======================= Age =======================")
main(d.age)

print("")
print("")

print("===================== Income ======================")
main(d.income)

print("")
print("")

print("==================== Education ====================")
main(d.education)

print("")
# ===========================================================================


# ======================== Generate and display plot ========================
if generate_matplotlib is True:
    plot.scatter(plot_x, plot_y)
    plot.show()
# ===========================================================================
