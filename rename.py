import os

os.chdir('D:\\Philosophy Crash Course')

#print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    name = file_name.split('-',3)
    name[0] = name[0].strip()               # to remove any extra spaces from the start or end of string
    name[1] = name[1].strip()               # to remove any extra spaces from the start or end of string

    course_name = name[1].split(' ')              # getting course name so course_name[last string] = number of video
    file_num = course_name[len(course_name) -1 ]  # getting file number
    file_num = file_num.strip()[1:].zfill(2)       # formatting the num to be 2 digits and remove any extra spaces
    new_name = '{} {}{}'.format(file_num, name[0], file_ext)  # new file name that we wanted in the first place

    os.rename(f, new_name)


