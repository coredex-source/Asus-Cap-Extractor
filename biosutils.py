from biosutilscore.core import caputils
import os
from tkinter import Tk, filedialog
import sys

title = """
--------------------------------------
|       BiosUtils-Core Beta v2       |
--------------------------------------
"""

# Function to clear console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to pop up an output directory selection menu.
def select_output_directory():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    root.destroy()
    return output_directory

# Function to remove "" to make it function well with the library.
def format_input_file(input_file):
    if input_file[0] == "\"":
        input_file = input_file.split("\"",1)
        input_file = input_file[1]
        input_file = input_file.rsplit("\"",1)
        input_file = input_file[0]
        return input_file
    elif input_file[0] == "\'":
        input_file = input_file.split("\'",1)
        input_file = input_file[1]
        input_file = input_file.rsplit("\'",1)
        input_file = input_file[0]
        return input_file

# Function to display a menu for using caputils.
def display_caputils():
    print(title)
    input_file = input("Enter the path to your .cap file or drag the file in this window: ")
    input_file = format_input_file(input_file)
    output_directory = select_output_directory()
    if output_directory:
        print(f"Output will be saved in: {output_directory}")
        output_directory = output_directory + "/output.bin"
        caputils(input_file,output_directory)
        input("Press any key to exit...")
        sys.exit()
    else:
        print("No output directory selected. Exiting.")
        sys.exit()

# Function to display a main menu.
def display_menu():
    while True:
        print(title)
        print("Available tools:")
        print("\t1. Cap Utilities\n")
        tool_choice = int(input("Select the tool number of the tool that you want to use: "))

        if tool_choice == 1:
            clear_screen()
            display_caputils()
        else:
            print("Invalid choice.")
            input("Press any key to continue.")
            clear_screen()

# Code initialization function call.
display_menu()