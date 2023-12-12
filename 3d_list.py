import pprint
import random
import sys
import logging
import os

log_folder_location = '/Users/macbook/terminal_hell/'
log_base_name = "3d_list_run"
i = 1
existing_logs = [f for f in os.listdir(log_folder_location) if f.startswith(log_base_name)]
if existing_logs:
    existing_numbers = [int(log.split('.')[1]) for log in existing_logs]
    i = max(existing_numbers) + 1
else:
    i = 1

log_name = f"{log_base_name}{i}.log"

log_location = os.path.join(log_folder_location,log_name)

logging.basicConfig(filename=log_location,level=logging.DEBUG)

def flatten(lst):
    try:
        logging.info('Running flatten.py')
        logging.warning('Reformatting lists for printing')
        flat_list = []

        for sublist in lst:
            for item in sublist:
                flat_list.append(item)
        return tuple(flat_list)  # Return as a tuple instead of a string

    except (RuntimeError, TypeError, NameError) as err:
        logging.critical(f'Error occurred in def.flatten.py:{err}')

def ThreeD(a, b, c):
    try:
        list1 = [[[random.randint(1, 10) for col in range(a)] for col in range(b)] for row in range(c)]
        list2 = [[[random.randint(1, 10) for col in range(a)] for col in range(b)] for row in range(c)]
        result = []  # Initialize the result list

        pprint.pprint({"list 1:": flatten(list1)})
        pprint.pprint({"list 2:": flatten(list2)})

        for i in range(c):
            temp_list = []
            for j in range(b):
                temp_row = [list1[i][j][k] * list2[i][j][k] for k in range(a)]
                temp_list.append(temp_row)
            result.append(temp_list)

        return f"Multiplication of two lists:{result}"

    except (RuntimeError, TypeError, NameError) as err:
        logging.critical(f'Error occurred:{err}')

def exit_program():
    logging.info('Exit by user initiated')
    print("Exiting the program")
    sys.exit(0)

if __name__ == "__main__":
    try:
        while True:
            print("Press 'k' to exit:")

            a = input("Enter A:")
            if a == 'k':
                exit_program()
            b = input("Enter B:")
            if b == 'k':
                exit_program()
            c = input("Enter rows:")
            if c == 'k':
                exit_program()

            # Check for empty inputs
            if a == '' or b == '' or c == '':
                print("Empty input")
                while a == '':
                    try:
                        logging.warning('Value A was empty')
                        print("Rerunning A as it was an empty string")
                        a = input("Enter A:")
                        logging.info(f'Input rerun with value:{a}')
                    except TypeError as err:
                        print(f"Error recorded{err}")
                        logging.critical(f'TypeError recorded {err}')
                while b == '':
                    try:
                        logging.warning('Value B was empty')
                        print("Rerunning B as it was an empty string")
                        b = input("Enter B:")
                        logging.info(f'Input rerun with value:{b}')
                    except TypeError as err:
                        print(f"Error recorded{err}")
                        logging.critical(f'TypeError recorded {err}')
                while c == '':
                    try:
                        logging.warning('Value C was empty')
                        print("Rerunning C as it was an empty string")
                        c = input("Enter C:")
                        logging.info(f'Input rerun with value:{c}')
                    except TypeError as err:
                        print(f"Error recorded{err}")
                        logging.critical(f'TypeError recorded{err}')
                pprint.pprint(ThreeD(int(a), int(b), int(c)))

            else:
                pprint.pprint(ThreeD(int(a), int(b), int(c)))

    except ValueError as err:
        logging.error(err)
        logging.critical("Critical error occured! exiting..")
        print("Invalid input. Please enter integers for A, B, and rows.")
