def read_books():
    list = []
    with open("books.txt") as file:
        line = file.readline().strip()
        while line:
            list.append(line)
            line = file.readline().strip()
    return list


def menu():
    choice = '?'
    while choice not in 'abcsABCS':
        print('\ta - Overview')
        print('\tb - Longest title')
        print('\tc - 5 letters on a row')
        print('\ts - Stop ')
        choice = input('\tMake your choice: ').lower()
    return choice


def print_list(bo):
    print('\nList of books:\n')
    for i in range(len(bo)):
        print(i+1, bo[i])
    print()


# hoofdprogramma
books = read_books()
choice = menu()


while choice != 's':
    if choice == 'a':
        print_list(books)
    elif choice == 'b':
        print_list(books)
        max_length = len(books[0])

        for i in range(len(books)):
            if len(books[i]) > max_length:
                max_length = len(books[i])
        print('The longest title has', max_length, 'characters\n')

    elif choice == 'c':
        booknumber = int(input("Enter booknumber max " + str(len(books)) +": "))
        book = books[booknumber-1]

        for i in range(len(book)):
            if i % 5 == 0:
                print()
            print(book[i], end=' ')
        print()
    choice = menu()

