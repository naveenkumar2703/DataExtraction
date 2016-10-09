# -*- coding: utf-8 -*-
"""
This file reads data by taking the absolute path and returns array of arrays with each row representing an array. 
"""

"""
Input:
   fileName - absolute path of the file
   hasHeader - does the file has header. If True first line will be returned as header_data otherwise None.

Output:
   file_data - array of array. One array for each line.
   header_data - array of header string
"""


def read_data(file_name, has_header):
    file_data = None
    header_data = None
    if file_name is None:
        return file_data, header_data
    if not file_name:  # checking if string is empty
        return file_data, header_data
    try:
        with open(str(file_name), 'r', encoding='utf-8') as file:
            header_handled = False

            if not has_header:
                header_handled = True
            file_data = []
            for line in file:
                if not header_handled:
                    header_data = []
                    headerLine = line.rstrip('\n').split(',')
                    for item in headerLine:
                        header_data.append(item)
                    header_handled = True
                    continue
                line_data = line.rstrip('\n').split(',')
                line_data_formatted = []
                for item in line_data:
                    line_data_formatted.append(item)
                file_data.append(line_data_formatted)


    except Exception as e:
        print('Unable to read file - ' + str(file_name) + ' due to error - ' + e.strerror)

    return file_data, header_data
