from Innermost_Functions import *


# Allows the user to add a task of their choosing (either work or break) to their schedule
# Allows them to choose how long they want to plan for that task to continue for
# Increments the variable that measures how long the user plans to work without a break
def getNewTask(mins_without_break):

    break_task = False
    work_task = False

    # The user chooses if they want to add a "work" task or a break to their schedule
    task_type_input = False
    while task_type_input == False:
        task_type = input("Would you like to add a work task or a break to your schedule? "
                          "Enter 'w' for work task and 'b' for break").lower()
        if task_type == "w":
            work_task = True
            task_type_input = True
        elif task_type == "b":
            break_task = True
            task_type_input = True
        else:
            print("I do not understand that input")
            time.sleep(1)
    time.sleep(1)

    # The name of the task is chosen depending on whether it is work or a break
    if break_task == True:
        task, time_block_number, mins_without_break = getBreak()
    elif work_task == True:
        task, time_block_number = getWork()

        # If the task is a work task,
        # the variable expressing how long the user plans to work without a break is incremented

        mins_without_break = mins_without_break + time_block_number

    return task, time_block_number, break_task, work_task, mins_without_break
    # time_left = time_block
    # time_without_break = time_without_break + time_block


# Allows the user to add a new task. Similar to the getNewTask() function,
# but does not require for the mins_without_break variable to be passed through it.
# Also has different dialogue to reflect that the task is not necessarily
# being added to the end of the schedule
def addNewTask():
    break_task = False
    work_task = False

    # The user chooses if they want to add a "work" task or a break to their schedule
    task_type_input = False
    while task_type_input == False:
        task_type = input("Would you like to add a work task or a break to your schedule? "
        "Enter 'w' for work task and 'b' for break").lower()
        if task_type == "w":
            work_task = True
            task_type_input = True
        elif task_type == "b":
            break_task = True
            task_type_input = True
        else:
            print("I do not understand that input")
            time.sleep(1)
    time.sleep(1)

    # The name of the task is chosen depending on whether it is work or a break
    if break_task == True:
        task, time_block_number, mins_without_break = getBreak()
    elif work_task == True:
        task, time_block_number = getWork()

    return task, time_block_number


# Allows the user to add, delete, or edit tasks in the schedule
def editTaskList(task_list, time_block_list):
    task_list_length = len(task_list)

    edit_input = False
    add_task = False
    delete_task = False
    edit_task = False

    #First, the user is asked to choose whether they would like to add, delete, or edit a task
    while edit_input == False:
        edit = input("Enter 'add' to add a task, 'delete' to delete a task, or 'edit' to edit a task. "
                     "Enter 'no' if you no longer wish to make a change.").lower()
        if edit == "add":
            edit_input = True
            add_task = True
        elif edit == "delete":
            edit_input = True
            delete_task = True
        elif edit == "edit":
            edit_input = True
            edit_task = True
        elif edit == "no":
            edit_input = True
        else:
            print("I do not understand that input")
            time.sleep(1)

    time.sleep(1)

    # This allows the user to add a task wherever in the schedule they choose
    if add_task == True:
        task_index_input = False

        # First, the user decides where they want to add the new task
        while task_index_input == False:
            task_index = input("What position in the list do you want the new task to have? " 
                               "Please enter an integer value.")
            try:
                real_task_index = int(task_index) - 1
                if real_task_index > task_list_length or real_task_index < 0:
                    print("That value is not valid. "
                          "Please enter a value for a position within the list or just after the end of the list.")
                    time.sleep(1)
                else:
                    task_index_input = True
            except ValueError:
                print("That wasn't a number.")
                time.sleep(1)
        time.sleep(1)

        # Then a function is called for the user to add a new task
        task, time_block_number = addNewTask()
        task_list.insert(real_task_index, task)
        time_block_list.insert(real_task_index, time_block_number)

    # This allows the user to delete one of the tasks they previously added
    if delete_task == True:
        task_index_input = False
        while task_index_input == False:
            task_index = input("What position in the list does the task that you want to delete have? " 
                               "Please enter an integer value.")
            try:
                real_task_index = int(task_index) - 1
                if real_task_index >= task_list_length or real_task_index < 0:
                    print("That value is not valid. "
                          "Please enter the value for a position within the list.")
                    time.sleep(1)
                else:
                    task_index_input = True
            except ValueError:
                print("That wasn't a number.")
                time.sleep(1)
        del task_list[real_task_index]
        del time_block_list[real_task_index]

    # This allows the user to edit one of the tasks they previously added
    if edit_task == True:
        task_index_input = False

        # First, the user must select which task they wish to edit
        while task_index_input == False:
            task_index = input(
                "What position in the list does the task that you want to edit have? Please enter an integer value.")
            time.sleep(1)
            try:
                real_task_index = int(task_index) - 1
                if real_task_index >= task_list_length or real_task_index < 0:
                    print("That value is not valid. "
                          "Please enter the value for a position within the list.")
                    time.sleep(1)
                else:
                    task_index_input = True
            except ValueError:
                print("That wasn't a number.")
                time.sleep(1)

        # Then, the user is asked whether they would like to edit the task description
        edit_task_input = False
        edit_time_input = False
        while edit_task_input == False:
            edit_task_answer = input("Would you like to edit the description for the following task: "
                                     + task_list[real_task_index] + "? "
                                     "Please enter 'y' or 'n'").lower()
            time.sleep(1)
            if edit_task_answer == "y":
                edit_task_input = True
                task_type_input = False
                while task_type_input == False:
                    task_type = input(
                        "Would you like to make this task a work task or a break? "
                        "Enter 'w' for work task and 'b' for break").lower()
                    time.sleep(1)
                    if task_type == "w":
                        task = input("What do you want to rename the task?")
                        task_list[real_task_index] = task
                        task_type_input = True
                        time.sleep(1)
                    elif task_type == "b":
                        task = "take a break"
                        task_list[real_task_index] = task
                        task_type_input = True
                    else:
                        print("I do not understand that input")
                        time.sleep(1)
                time.sleep(1)
            elif edit_task_answer == "n":
                edit_task_input = True
            else:
                print("I do not understand that input")
                time.sleep(1)

        # The user is asked whether they would like to change the length of time the task will take
        while edit_time_input == False:
            edit_time_answer = input("Would you like to edit the number of minutes of time allotted to this task? "
                                     "Please enter 'y' or 'n'").lower()
            time.sleep(1)
            if edit_time_answer == "y":
                edit_time_input = True
                time_block_input = False
                while time_block_input == False:
                    time_block = input("How many minutes do you want to spend doing the task?")
                    try:
                        time_block_number = int(time_block)
                        if time_block_number > 0:
                            time_block_list[real_task_index] = time_block
                            time_block_input = True
                        else:
                            print("Please enter an integer greater than 0.")
                            time.sleep(1)
                    except ValueError:
                        print("I do not understand that input.")
                        time.sleep(1)
            elif edit_time_answer == "n":
                edit_time_input = True
            else:
                print("I do not understand that input")
                time.sleep(1)

    time.sleep(1)

    return task_list, time_block_list


# This asks the user if they are okay with the schedule they have made
def isScheduleOkay(task_list, time_block_list):
    schedule_okay_input = False
    schedule_is_okay = True

    # This prints the schedule for the user
    while schedule_okay_input == False:
        print("Here is your schedule:")
        time.sleep(1)
        val = 0
        num = 1
        task_list_length = len(task_list)
        while val <= task_list_length - 1:
            print(str(num) + ". " + task_list[val] + " for " + str(time_block_list[val]) + " minutes.")
            val = val + 1
            num = num + 1
            time.sleep(1)

        # The user is asked if they are okay with the schedule
        schedule_okay = input("Are you okay with this schedule? Please enter 'y' or 'n'")
        if schedule_okay == "y":
            schedule_okay_input = True

        # If the user is not okay with the schedule, a function is called that allows them to edit it
        elif schedule_okay == "n":
            time.sleep(1)
            task_list, time_block_list = editTaskList(task_list, time_block_list)
            schedule_is_okay = False
        else:
            print("I do not understand that input")
            time.sleep(1)

    return task_list, time_block_list, schedule_is_okay


# This asks the user if they are okay with the schedule they have made
# This is similar to the isScheduleOkay() function,
# But it does not print out the schedule for the user.],
# And some of the other text is slightly modified
def isFinalScheduleOkay(task_list, time_block_list):
    schedule_okay_input = False
    schedule_is_okay = True
    while schedule_okay_input == False:
        schedule_okay = input("Are you okay with this as your final schedule? Please enter 'y' or 'n'")
        time.sleep(1)
        if schedule_okay == "y":
            schedule_okay_input = True
        elif schedule_okay == "n":
            schedule_okay_input = True
            schedule_is_okay = False
            task_list, time_block_list = editTaskList(task_list, time_block_list)
        else:
            print("I do not understand that input")

    return task_list, time_block_list, schedule_is_okay


# This function checks if the user planned to work for long blocks of time
# And recommends that they add breaks into their schedule if needed
def checkForBreaks(task_list, time_block_list, break_time_int):
    break_added = False
    mins_without_break = 0
    value = 0
    number = 1
    task_list_length = len(task_list)

    # This checks how long the user will go without a break
    # By incrementing the mins_without_break variablr
    while number <= task_list_length:
        task = task_list[value]
        if task == "take a break":
            mins_without_break = 0
        else:
            mins_without_break = mins_without_break + int(time_block_list[value])

        # If the user goes a certain time without a break
        # Without planning to have a break right after,
        # The program will let them know and recommend they add a break in their schedule
        if mins_without_break >= break_time_int:
            if number <= task_list_length:
                if task_list[value] != "take a break":
                    valid_break_input = False
                    while valid_break_input == False:
                        print("You plan to work for " + str(mins_without_break) + " minutes straight "
                        "without a break afterwards.")
                        time.sleep(1)

                        # Asks the user if they want to add a break
                        break_input = input("Do you want to add a break after your task '" + str(number) + ". " + task_list[
                            value] + " for " + str(time_block_list[value]) + " minutes'? "
                                                                             "Please enter 'y' or 'n'").lower()
                        need_break = False
                        if break_input == "y":
                            valid_break_input = True
                            need_break = True
                            break_added = True
                            time.sleep(1)
                        elif break_input == "n":
                            valid_break_input = True
                        else:
                            print("I do not understand that input")
                            time.sleep(1)

                    value = value + 1
                    number = number + 1

                    # If the user chose to add a break in their schedule,
                    # A function is called that asks them how long they want it to be,
                    # And the break is added
                    if need_break == True:

                        task, time_block_number, mins_without_break = getBreak()
                        task_list.insert(value, task)
                        time_block_list.insert(value, time_block_number)

                        time.sleep(1)

                        # The schedule is printed
                        print("Here is your updated schedule:")
                        time.sleep(1)
                        val = 0
                        num = 1
                        task_list_length = len(task_list)
                        while val <= task_list_length - 1:
                            print(str(num) + ". " + task_list[val] + " for " + str(time_block_list[val]) + " minutes.")
                            val = val + 1
                            num = num + 1
                            time.sleep(1)
        else:
            value = value + 1
            number = number + 1

    return task_list, time_block_list, break_added


# This counts down the number of minutes left for a certain task
def countDown(val, tasks_left, time_block_list):
    minutes_left = time_block_list[val]
    while minutes_left > 0:
        # In real applications, this would be time.sleep(60) so that the program would pause for one minute
        time.sleep(1)
        minutes_left = minutes_left - 1
        is_divisible = isDivisibleByFive(minutes_left)
        # The program gives the user a message when the task is done
        # The message is different depending on if there are any more tasks left or not
        if minutes_left == 0:
            if tasks_left == 1:
                print("You have completed all of your tasks that you have planned!")
            else:
                print("You can now stop doing this task and move on to the next task")

        # If the number of minutes left is a multiple of 5,
        # A message is printed letting the user know how many minutes are left for that task
        elif is_divisible == True:
            print("You have " + str(minutes_left) + " minutes remaining for this task")

    val = val + 1
    tasks_left = tasks_left - 1
    time.sleep(1)
    return val, tasks_left


# This organizes the countDown() function so that it only runs for each task
# After a message has been printed and the user presses the enter key
def timeTasks(task_list, time_block_list):
    task_list_length = len(task_list)
    # print("There are " + str(task_list_length) + " items in the list")

    tasks_left = task_list_length
    val = 0
    print("Your first task is to " + task_list[val] + " for " + str(time_block_list[val]) + " minutes.")
    time.sleep(1)
    next = input("Please press enter when you would like to start your timer for this task")
    val, tasks_left = countDown(val, tasks_left, time_block_list)

    while tasks_left > 0:
        print("Your next task is to " + task_list[val] + " for " + str(time_block_list[val]) + " minutes.")
        time.sleep(1)
        next = input("Please press enter when you would like to start your timer for this task")
        minutes_left = time_block_list[val]
        val, tasks_left = countDown(val, tasks_left, time_block_list)