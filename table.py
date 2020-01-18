# prints a line in the table give:
# 1. symbol - which character to print in/as a line
# column width - the number of character in each column
# number of columns


def printLine(symbol, column_width_in_chars, number_of_columns):
    print('-' * column_width_in_chars * number_of_columns)


# prints the table given:
# 1. 2D List to print
# 2. headingPresent - boolean representing whether the first element of
# the 2D list is of headings [False by default]

# 3. number_of_tabs - number of tabs in each column
# 4. number of spaces in each tab [4 by default]

# Assumptions
# 1. width of each column is same
# 2. lengths of nested lists are uniform


def printTable(list_to_print, number_of_tabs,
               number_spaces_in_a_tab=4, headingPresent=False):

    # the number of tabs in each colmun [provided by the user]
    number_of_tabs_per_column = int(number_of_tabs)

    # the number of spaces per tab [provided by user]
    number_spaces_in_a_tab = 4

    # column width calculated using previous two variables [calculated]
    # NOTE: assumes the width of each column is same
    column_width_in_chars = int(number_of_tabs * number_spaces_in_a_tab)

    # number of columns in total [calculated]
    # NOTE: assumes that the length of nested lists are uniform
    # hence picks up first nested list and gets it's length
    number_of_columns = len(list_to_print[0])

    # giving the table a padding above of 1 blank line
    print()

    for index, miniList in enumerate(list_to_print):
        # e.g. of miniList -> ['text1', 'text2', 'text3']

        for li in miniList:

            # e.g. of li -> 'text1'
            numSpaces = column_width_in_chars - len(li)

            # calculating number of spaces required to print
            # to complete the column
            spaces = ' ' * numSpaces

            # printing listItem and ending with required number of spaces
            print(li, end=spaces)

        # after having printed minilist, go to next line
        print()

        # if we just printed the heading, and if there is a heading
        # print a line of chars to demarcate it.
        if (index == 0 and headingPresent):
            printLine('-', column_width_in_chars, number_of_columns)

    # giving the table a padding below of 1 blank line
    print()
