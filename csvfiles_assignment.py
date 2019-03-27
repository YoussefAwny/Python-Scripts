"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote = csv.QUOTE_MINIMAL):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, newline='') as csv_file:  # don't need to explicitly close the file now
        field_name = []
        csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar = quote)
        field_name = csv_reader.fieldnames
    return field_name


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """

    table = list(dict())
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar = quote)
        field_name = read_csv_fieldnames(filename, separator, quote)
        for row in csvreader:
            table.append(row)
    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar = quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        #for i in range(len(table)):
         #   writer.writerow(table[i])
        writer.writerows(table)

    pass


# print("Testing \" read_csv_fieldnames\" \n")
# print("Test 1.1")
# field_names = read_csv_fieldnames("hightemp.csv", ",", csv.QUOTE_ALL)
# print(field_names)
#
# print("\n-------------------\n")
# print("Testing \" read_csv_as_list_dict\" \n")
# print("Test 2.1")
# data = read_csv_as_list_dict("hightemp.csv", ",", csv.QUOTE_ALL)
# print(data[2]["Jan"])
#
# print("\n-------------------\n")
# print("Testing \" read_csv_as_nested_dict\" \n")
# print("Test 3.1")
# data = read_csv_as_nested_dict("hightemp.csv", "City",",", csv.QUOTE_ALL)
# print(data["Moscow"]["Jan"])
#
# print("\n-------------------\n")
# print("Testing \" write_csv_from_list_dict\" \n")
# print("Test 4.1")