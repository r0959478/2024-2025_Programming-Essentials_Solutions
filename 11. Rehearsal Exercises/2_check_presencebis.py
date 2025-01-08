# FUNCTIONS ---------------------------------------

def lookup_classes():
    set_c = set()
    with open("classlist.csv") as file:
        line = file.readline()
        while line:
            fields = line.rstrip().split(';')
            set_c.add(fields[3])
            line = file.readline()
    return set_c

def control(mclass):
    att_list = []

    with open("classlist.csv") as file:
        line = file.readline()
        while line:
            fields = line.rstrip().split(';')
            if fields[3] == mclass:
                presence = input(fields[2]+' '+fields[1]+': ')

                student = fields[1]+';'+fields[2]+";"
                if presence == '':
                    student += 'OK\n'
                elif presence in 'nN':
                    student += 'NOT\n'
                else:
                    student += '?\n'
                att_list.append(student)
            line = file.readline()
    return att_list


# main
classes = list(lookup_classes())
classes.sort()
for c in classes:
    print(c)

myclass = input('In which class do you want to do the check: ')
attendance_list = control(myclass)

if len(attendance_list) == 0:
    print("This class doesn't exit")
else:
    with open(myclass+".csv", "w") as output:
        output.write('Attendance list ' + myclass + '\n' )
        output.writelines(attendance_list)