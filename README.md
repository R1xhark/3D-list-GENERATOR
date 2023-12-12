# 3D List Generator

This Python script generates two 3D lists filled with random integers and then multiplies corresponding elements to produce a new 3D list. The flattened version of the input lists and the result is printed for better visualization.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Logging](#logging)
- [Exiting the Program](#exiting-the-program)

## Requirements
- Python 3.x

## Usage
1. Clone the repository:

    ```bash
    git clone https://github.com/R1xhark/3D-list-GENERATOR.git
    cd 3D-list-GENERATOR
    ```

2. Run the script:

    ```bash
    python 3d_list_run.py
    ```

3. Follow the on-screen instructions to input values for A, B, and rows. Press 'k' at any point to exit the program.

4. If any of the inputs (A, B, or rows) is left empty, the script will prompt you to re-enter the empty values.

5. The flattened versions of the input lists and the resulting 3D list multiplication will be printed.

## Logging
- Logs are stored in the `/Users/macbook/terminal_hell/` directory.
- Log files are named in the format `3d_list_runX.log` where `X` is a unique number.

## Exiting the Program
- To exit the program at any time, press 'k' when prompted for input.

### Example
```bash
Press 'k' to exit:
Enter A: 2
Enter B: 3
Enter rows: 4

{'list 1:': (1, 7, 3, 6, 9, 3)}
{'list 2:': (5, 10, 4, 5, 1, 5)}
'Multiplication of two lists:[[[5, 70, 12], [30, 9, 15], [16, 35, 15], [5, 1, 25]]]'

