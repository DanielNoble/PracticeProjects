tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    #  Iterate through every value in table, finding the max length of a column
    for i in range(len(table)):
        max = 0
        for j in table[i]:
            if len(j) > max:
                max = len(j)

        #  Apply the max length of a column through rjust() to each value in the column
        for j in range(len(table[i])):
            table[i][j] = table[i][j].rjust(max + 1)

    #  Print out the table, [0,0] [1,0] [2,0] enter (iterate through row first, then column)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i], end='')
        print('')


printTable(tableData)
