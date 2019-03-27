"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    short_len = 0
    if len(line1) < len(line2):
        short_len = len(line1)
        for itr in range(short_len):
            if line1[itr] != line2[itr]:
                return itr
        return short_len

    elif len(line2) < len(line1):
        short_len = len(line2)
        for itr in range(short_len):
            if line2[itr] != line1[itr]:
                return itr
        return short_len

    else:
        for itr in range(len(line1)):
            if line1[itr] != line2[itr]:
                return itr

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    singlen = line1.find('\n')
    singler = line1.find('\r')
    singlenn = line2.find('\n')
    singlerr = line2.find('\n')

    if singlen != -1 or singler != -1 or singlenn != -1 or singlerr != -1:
        return ""
    elif idx == -1:
        return ""
    else:
        ret =""
        for itr  in range(idx):
            ret += "="
            itr +=1
            itr -=1
        ret += "^"
        return line1 + "\n" + ret + "\n" + line2+ "\n"


    return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    count_l=0
    for line1, line2 in zip(lines1, lines2):
        idx = singleline_diff(line1, line2)
        if idx == IDENTICAL:
            count_l += 1
        else:
            ret = (count_l, idx)
            return ret
    if len(lines2) < (len(lines1)):
        return (len(lines2),0)
    elif len(lines1) < len(lines2):
        return (len(lines1),0)

    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    open_file = open(filename, "rt")
    lines =[]
    for line in open_file.readlines():
        if line[-1] == "\n" or line[-1] =="\r":
            line = line[0:-1]
        lines.append(line)
    open_file.close()
    return lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines_one = get_file_lines(filename1)
    lines_two = get_file_lines(filename2)
    multiline_ret    = multiline_diff(lines_one, lines_two)
    ret = ""
    if multiline_ret[0] == IDENTICAL:
        return ("No differences\n")
    else:
        ret += ("Line " + str(multiline_ret[0]) + ":\n")
        ret += (singleline_diff_format(lines_one[multiline_ret[0]], lines_two[multiline_ret[0]], multiline_ret[1]))



    return ret



# print("Testing singlieline_diff")
# print("\nTest 1.1\n")
#
# line1 = "I love you"
# line2 = "I love you"
# out = singleline_diff(line1, line2)
# print(out == -1)
#
# print("\nTest 1.2\n")
# line1 = "I l0ve you"
# line2 = "I love you"
# out = singleline_diff(line1, line2)
# print(out == 3)
#
# print("\nTest 1.3\n")
# line1 = "I love you"
# line2 = "I love y"
# out = singleline_diff(line1, line2)
# print(out ==8)
#
# print("\nTest 1.4\n")
# line1 = "I love u"
# line2 = "I love you"
# out = singleline_diff(line1, line2)
# print(out == 7)
#
# print("===========================")
# print(("Testing singleline_diff_format"))
# print(" ")
# print(("test 2.1\n"))
#
# line1 = "I love u"
# line2 = "I love you"
# out = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, out)+ "\n")
# print(" ")
# print("test 2.2\n")
# line1 = "I love you"
# line2 = "I love u"
# out = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, out) + "\n")
#
# print("===========================")
# print(("Testing multiline_diff"))
# print(" ")
# print(("test 3.1\n"))
# lines1 = ["i love you", "70b 3omry"]
# lines2 = ["i love you", "70b 30mry"]
# print(multiline_diff(lines1, lines2))

# print("===========================")
# print(("Testing get lines"))
# print(" ")
# print(("test 4.1\n"))
#
# print("===========================")
# print(("Testing file_diff_format"))
# print(" ")
# print(("test 4.1\n"))
#
