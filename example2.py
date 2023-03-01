# Python DATA CONVERTER PROGRAM
# Completed date 28/06/2022
# Author: Đoàn Quang Minh
# Convention: snake_case

# ***

# Import library with
# Tkinter: Main GUI library
# Tkinter with filedialog: Work with file name and directory path
# Pandas: Dataframe and CSV support

import tkinter as tk
from tkinter import filedialog
import pandas as pd


#
#
# CONVERT FUNCTION ----------------------------------------------
# Include Convert from: [convert + <type>]


# Kilometre to Miles <Km_miles>
def convertKm_miles(data: float) -> float:
    '''
    1 Km = 0.6213711922 miles
    '''
    return data*0.6213711922


# Celsius to Fahrenheit <C_F>
def convertC_F(data: float) -> float:
    '''
    1C = 33.8F; 2C = 35.6F
    '''
    return 32+data*1.8


# Gallon to Litre <Gal_L>
def convertGal_L(data: float) -> float:
    '''
    1Gal = 3.78541178L
    '''
    return data*3.78541178


# GMT+7 to GMT+9 <GMT7_9>
def convertGMT7_9(data: float) -> float:
    '''
    GMT+7 + 2 = GMT+9\n
    If Hour is over 24, minus for 24
    '''
    result = data + 2
    if result > 24:
        result -= 24
    return result


#
#
# BUTTON HANDLER -------------------------------------------------


# Delete input: Delete all of a list of <tk.Entry> contents
def detele_input(*targets: tk.Entry) -> None:
    '''
    Loop through targets and call tk.Entry.delete function from 0 to END
    '''
    for target in targets:
        target.delete(0, tk.END)


# Converter: Convert input to float, then check for type, finally push to output with error announcement
#       Dependencies: float_converter, get_hour, Data Convert Function
def converter(input_target: tk.Entry, output_target: tk.Entry, type: str) -> None:
    '''
    [input Entry, output Entry, type]\n
    The type can be:\n
    - km-miles: (number) convert to miles\n
    - c-f: (number) convert to fahrenheit\n
    - gal-l: (number) convert to litre\n
    - gmt7-9: (hh:mm:ss) convert to gmt+9
    '''
    data = float_converter(input_target.get())
    output = ''
    if type == 'gmt7-9':
        data = get_hour(input_target)
    if data == 'error detected':
        output = 'Bạn đã nhập sai'
    elif data == 'empty string':
        output = 'Vui lòng nhập số'
    elif type == 'km-miles':
        output = str(convertKm_miles(data))
    elif type == 'c-f':
        output = str(convertC_F(data))
    elif type == 'gal-l':
        output = str(convertGal_L(data))
    elif type == 'gmt7-9':
        output = f'{convertGMT7_9(int(data))}{input_target.get()[2:]}'
    output_target.delete(0, tk.END)
    output_target.insert(0, output)


# Close window: Exit program
def close_window() -> None:
    '''
    Exit program
    '''
    window.destroy()


# Get Hour: Get an hour in a time format [hh:mm:ss] with error handler
#       Dependencies: floar_converter
def float_converter(data: float) -> ...:
    '''
    Try convert and return float number\n
    If error is detected, return 'error detected'\n
    If there are empty input, return 'empty string'
    '''
    try:
        return float(data)
    except:
        if data == '':
            return 'empty string'
        return 'error detected'


# Float converter: Convert string to float with error handler
def get_hour(time: tk.Entry) -> ...:
    '''
    Get and return hour (float) from time format (hh:mm:ss)\n
    If error is detected, return 'error detected'\n
    If there are empty input, return 'empty string'
    '''
    timestamp = time.get()
    if len(timestamp) == 8 and timestamp[2] == ':' and timestamp[5] == ':':
        return float_converter(timestamp[0:2])
    else:
        if timestamp == '':
            return 'empty string'
        return 'error detected'


#
#
# WORK WITH CSV ------------------------------------------------
# Include import csv file, export csv file


# Uncomplete function
def select_directory():
    pass


# Create dataframe format and return a data dictionary
def make_dataframe(values: tuple[tk.Entry]) -> dict[str, list[str]]:
    '''
    Make dataframe for pandas from a tuple of Entry by return a dictionary of data
    '''

    # Insert blank value in title row for reading on excel
    def insert_gutter(space: list, lists: tuple) -> list[str]:
        '''
        Insert blank space for dataframe and return a new list with gutter
        '''
        _list = list(lists)
        for i in space:
            _list.insert(i, '')
        return _list

    def get_value(value: tk.Entry) -> str:
        '''
        Get value for tk.Entry\n
        Insert 0 if Entry is empty
        '''
        if value == '':
            return ''
        val = value.get()
        if val == '':
            return '0'
        else:
            return val

    data = {
        'Data Converter': ['Km to Miles', 'Km', 'Miles', 'C to F', 'C', 'F', 'Gallon to Litre', 'Gal', 'L', 'GMT+7 to GMT+9', 'GMT+7', 'GMT+9'],
        '': list(map(get_value, insert_gutter([0, 3, 6, 9], values)))
    }
    return data


# Export to CSV with specific directory
def export_to_csv(directory: tk.Entry, name: tk.Entry, *values: tk.Entry) -> None:
    '''
    Export to CSV with directory and file name\n
    Get directory, file name, and list of tk.Entry as arguments
    '''

    def make_file(path: str) -> None:
        '''
        Call export function from pandas and print state
        '''
        try:
            df.to_csv(f'{path}.csv', index=False, header=True)
            print("Saved successfully!")
        except:
            print("Something error!")

    # Create dataframe
    df = pd.DataFrame(make_dataframe(values))

    # Check for directory
    # If directory is empty, as for new directory and file name
    # If directory and file name is filled, save to existing file
    if directory.get() == '':
        file_path = filedialog.asksaveasfilename()
        if file_path == '':
            return
        file_dir = file_path[:file_path.rfind('/')+1]
        file_name = file_path[file_path.rfind('/')+1:]
        directory.insert(0, file_dir)
        name.insert(0, file_name)
        make_file(file_path)
    else:
        if name.get() == '':
            make_file(f'{directory.get()}untitled')
            name.insert(0, 'untitled')
        make_file(f'{directory.get()}{name.get()}')


def load_csv(path: str) -> list[str]:
    '''
    Read CSV file from path and return a list of data
    '''

    if not path.endswith('.csv'):
        return []
    df = pd.read_csv(path)
    lists = df['Unnamed: 1'].dropna().to_list()
    return lists


def load_data(directory: tk.Entry, name: tk.Entry, *targets: list[tk.Entry]) -> None:
    '''
    Open file and insert to directory and file name Entry
    '''

    file_path = filedialog.askopenfilename()
    file_dir = file_path[:file_path.rfind('/')+1]
    file_name = file_path[file_path.rfind('/')+1:]
    if file_path != '':
        directory.delete(0, tk.END)
        name.delete(0, tk.END)
    directory.insert(0, file_dir)
    name.insert(0, file_name.removesuffix('.csv'))
    lists = load_csv(file_path)
    if len(lists) == 0:
        return
    for i in range(len(targets)):
        targets[i].delete(0, tk.END)
        targets[i].insert(0, lists[i])


#
#
# TKINTER GUI ---------------------------------------------------


window = tk.Tk()
window.title('DATA CONVERTER')
window.geometry('570x360')

title = tk.Label(text='Chương trình chuyển đổi đơn vị',
                 padx=10, pady=5, bg='#cccccc', font=('Arial', 20))
title.grid(row=0, column=0, columnspan=5)

directory = tk.Entry(width=90)
directory.grid(row=1, column=0, columnspan=5)

file_name = tk.Entry(width=90)
file_name.grid(row=2, column=0, columnspan=5)

# Km Converter
km = tk.Label(text='Nhập Km', padx=5, pady=2)
km_input = tk.Entry(width=20)
km_unit = tk.Label(text='Km', padx=5, pady=2)
km_btn = tk.Button(text='Xoá', width=10,
                   command=lambda: detele_input(km_input))
km_cv = tk.Label(text='Chuyển đổi', padx=5, pady=2)
km_input_cv = tk.Entry(width=20)
km_unit_cv = tk.Label(text='miles', padx=5, pady=2)
km_btn_cv = tk.Button(text='Chuyển đổi', width=10, command=lambda: converter(
    km_input, km_input_cv, 'km-miles'))

km.grid(row=3, column=0)
km_input.grid(row=3, column=1)
km_unit.grid(row=3, column=2)
km_btn.grid(row=3, column=3)
km_cv.grid(row=4, column=0)
km_input_cv.grid(row=4, column=1)
km_unit_cv.grid(row=4, column=2)
km_btn_cv.grid(row=4, column=3)

# C Converter
c = tk.Label(text='Nhập độ C', padx=5, pady=2)
c_input = tk.Entry(width=20)
c_unit = tk.Label(text='C', padx=5, pady=2)
c_btn = tk.Button(text='Xoá', width=10, command=lambda: detele_input(c_input))
c_cv = tk.Label(text='Chuyển đổi', padx=5, pady=2)
c_input_cv = tk.Entry(width=20)
c_unit_cv = tk.Label(text='F', padx=5, pady=2)
c_btn_cv = tk.Button(text='Chuyển đổi', width=10,
                     command=lambda: converter(c_input, c_input_cv, 'c-f'))

c.grid(row=5, column=0)
c_input.grid(row=5, column=1)
c_unit.grid(row=5, column=2)
c_btn.grid(row=5, column=3)
c_cv.grid(row=6, column=0)
c_input_cv.grid(row=6, column=1)
c_unit_cv.grid(row=6, column=2)
c_btn_cv.grid(row=6, column=3)

# Gallon Converter
g = tk.Label(text='Nhập gallon', padx=5, pady=2)
g_input = tk.Entry(width=20)
g_unit = tk.Label(text='Gal', padx=5, pady=2)
g_btn = tk.Button(text='Xoá', width=10, command=lambda: detele_input(g_input))
g_cv = tk.Label(text='Chuyển đổi', padx=5, pady=2)
g_input_cv = tk.Entry(width=20)
g_unit_cv = tk.Label(text='L', padx=5, pady=2)
g_btn_cv = tk.Button(text='Chuyển đổi', width=10,
                     command=lambda: converter(g_input, g_input_cv, 'gal-l'))

g.grid(row=7, column=0)
g_input.grid(row=7, column=1)
g_unit.grid(row=7, column=2)
g_btn.grid(row=7, column=3)
g_cv.grid(row=8, column=0)
g_input_cv.grid(row=8, column=1)
g_unit_cv.grid(row=8, column=2)
g_btn_cv.grid(row=8, column=3)

# Time Converter
t = tk.Label(text='Giờ GMT+7', padx=5, pady=2)
t_input = tk.Entry(width=20)
t_unit = tk.Label(text='AM', padx=5, pady=2)
t_btn = tk.Button(text='Xoá', width=10, command=lambda: detele_input(t_input))
t_cv = tk.Label(text='Chuyển đổi', padx=5, pady=2)
t_input_cv = tk.Entry(width=20)
t_unit_cv = tk.Label(text='AM', padx=5, pady=2)
t_btn_cv = tk.Button(text='Chuyển đổi', width=10,
                     command=lambda: converter(t_input, t_input_cv, 'gmt7-9'))

t.grid(row=9, column=0)
t_input.grid(row=9, column=1)
t_unit.grid(row=9, column=2)
t_btn.grid(row=9, column=3)
t_cv.grid(row=10, column=0)
t_input_cv.grid(row=10, column=1)
t_unit_cv.grid(row=10, column=2)
t_btn_cv.grid(row=10, column=3)

# Notation
km_mile = tk.Label(text='Chuyển đổi Km --> miles', padx=5, pady=20)
km_mile.grid(row=3, column=4, rowspan=2)

c_f = tk.Label(text='Chuyển đổi C --> F', padx=5, pady=20)
c_f.grid(row=5, column=4, rowspan=2)

gal_l = tk.Label(text='Chuyển đổi Gallon --> Litter', padx=5, pady=20)
gal_l.grid(row=7, column=4, rowspan=2)

gmt7_9 = tk.Label(text='Chuyển đổi GMT+7 --> GMT+9', padx=5, pady=20)
gmt7_9.grid(row=9, column=4, rowspan=2)

# Navigation
delete = tk.Button(text='Xoá', padx=5, pady=5, width=10,
                   command=lambda: detele_input(km_input, c_input, g_input, t_input, km_input_cv, c_input_cv, g_input_cv, t_input_cv))
delete.grid(row=11, column=0)

open = tk.Button(text='File mới', padx=5, pady=5,
                 width=10, command=lambda: detele_input(directory, file_name, km_input, km_input_cv, c_input, c_input_cv, g_input, g_input_cv, t_input, t_input_cv))
open.grid(row=11, column=1)

open = tk.Button(text='Mở File', padx=5, pady=5,
                 width=10, command=lambda: load_data(directory, file_name, km_input, km_input_cv, c_input, c_input_cv, g_input, g_input_cv, t_input, t_input_cv))
open.grid(row=11, column=2)

saved = tk.Button(text='Lưu File', padx=5, pady=5,
                  width=10, command=lambda: export_to_csv(directory, file_name, km_input, km_input_cv, c_input, c_input_cv, g_input, g_input_cv, t_input, t_input_cv))
saved.grid(row=11, column=3)

exit = tk.Button(text='Thoát', padx=5, pady=5, width=10,
                 command=lambda: close_window())
exit.grid(row=11, column=4)
window.resizable(False, False)

window.mainloop()
