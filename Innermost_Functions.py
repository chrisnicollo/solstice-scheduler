import time


# Checks if a value is divisible by 5
def isDivisibleByFive(number):
    val = 0
    while number > val:
        val = val + 5
    if number == val:
        is_divisible = True
    elif number != val:
        is_divisible = False
    return is_divisible


# Allows the user to input the description and amount of time for a "work" task
def getWork():
    task = input("What is the next task you want to do today?")
    time.sleep(1)

    time_block_input = False
    while time_block_input == False:
        time_block = input("How many minutes do you want to spend on this task? "
                           "Please input an integer greater than 0")
        try:
            time_block_number = int(time_block)
            if time_block_number > 0:
                time_block_input = True
            else:
                print("Please enter an integer greater than 0.")
                time.sleep(1)
        except ValueError:
            print("I do not understand that input.")
            time.sleep(1)
    return task, time_block_number


# Allows the user to set the amount of time for a break
def getBreak():
    task = "take a break"
    mins_without_break = 0
    time_block_input = False
    while time_block_input == False:
        time_block = input("How many minutes do you want to spend taking a break?")
        try:
            time_block_number = int(time_block)
            if time_block_number > 0:
                time_block_input = True
            else:
                print("Please enter an integer greater than 0.")
                time.sleep(1)
        except ValueError:
            print("I do not understand that input.")
            time.sleep(1)
    return task, time_block_number, mins_without_break


# Reminds the user that they plan to work for a long period of time without a break
# Asks the user if they wish to add a break to their schedule
def needBreak(mins_without_break):

    valid_break_input = False
    while valid_break_input == False:
        break_input = input(
        "You plan to work for " + str(mins_without_break) + " minutes straight. "
        "Do you want to take a break after this task? Please enter 'y' or 'n'").lower()
        need_break = False
        if break_input == "y":
            valid_break_input = True
            need_break = True
        elif break_input == "n":
            valid_break_input = True
        else:
            print("I do not understand that input")
            time.sleep(1)

    time.sleep(1)
    return need_break
