"""Find the mean, median and mode of a list of random numbers."""

# ============================= Import modules ==============================
import math
import dataset_loader as d
import matplotlib.pyplot as plot
# ===========================================================================


# ================================= Options =================================
output_list_info = True
output_list_contents = False
generate_new_data = False
plot_x = d.income_raw
plot_y = d.education_raw
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
    import dataset_generator as dg
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
plot.scatter(plot_x, plot_y)
plot.show()
# ===========================================================================
