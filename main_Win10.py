from Inner_Functions_Win10 import *

def main():

    # Creating variables and lists to be used throughout the program
    mins_without_break = 0
    task_list = []
    time_block_list = []

    start = input("Press enter when you would like to begin creating your schedule for today")
    time.sleep(1)

    # Allowing user to input how long they would like to work before taking a break
    break_time_input = False
    while break_time_input == False:
        break_time = input("First, enter after how many minutes of work you would like to take breaks. "
                           "Please input a positive integer value.")
        time.sleep(1)
        try:
            break_time_int = int(break_time)
            if break_time_int > 0:
                print("I will suggest that you take breaks after " + break_time + " minutes of working.")
                break_time_input = True
            else:
                print("Please enter a number greater than 0")
                time.sleep(1)
        except ValueError:
            print("I do not understand that input")

    time.sleep(1)

    # Starting a loop to allow the user to continually add tasks to their schedule
    new_task = True
    while new_task == True:
        task, time_block_number, break_task, work_task, mins_without_break = getNewTask(mins_without_break)
        task_list.append(task)
        # print(task_list)
        time_block_list.append(time_block_number)
        # print(time_block_list)
        time.sleep(1)

        # Suggesting the user takes a break if they create a schedule that makes them work for a long time
        if mins_without_break >= break_time_int:
            need_break = needBreak(mins_without_break)
            if need_break == True:
                task, time_block_number, mins_without_break = getBreak()
                task_list.append(task)
                # print(task_list)
                time_block_list.append(time_block_number)
                # print(time_block_list)
                time.sleep(1)

        # Asking the user if they would like to continue the loop of adding tasks to their schedule
        valid_task_input = False
        while valid_task_input == False:
            new_task_input = input("Would you like to add another task to your schedule? Enter 'y' or 'n'").lower()
            if new_task_input == "y":
                valid_task_input = True
            elif new_task_input == "n":
                valid_task_input = True
                new_task = False
            else:
                print("I do not understand that input")
                time.sleep(1)
        time.sleep(1)

    # Checking if the user likes the final list they created
    # And giving them the opportunity to edit it if they do not
    task_list, time_block_list, schedule_is_okay = isScheduleOkay(task_list, time_block_list)

    time.sleep(1)

    # If the user made any changes to the schedule through the previous function,
    # Checking once again to see if the schedule has any spots where the user may want a break
    # And recommending to the user that they add a break
    if schedule_is_okay == False:
        task_list, time_block_list, break_added = checkForBreaks(task_list, time_block_list, break_time_int)
        time.sleep(1)

    # If the user added a break, they get asked once again to confirm their final schedule
    # And are given the option to edit it if they so wish
        if break_added == True:
            task_list, time_block_list, schedule_is_okay = isFinalScheduleOkay(task_list, time_block_list)
            if schedule_is_okay == False:
                task_list, time_block_list, schedule_is_okay = isScheduleOkay(task_list, time_block_list)

    # Calls a function that creates a timer for each of the tasks for the user to do
    timeTasks(task_list, time_block_list)

if __name__ == '__main__':
    main()