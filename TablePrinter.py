tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def max(table):
    max = 0
    for i in table:
        if len(i) > max:
            max = len(i)
    return max


def printTable(table):
    tableSizes = []
    for i in range(len(table) - 1):  # Creates a second table, tableSizes, out of the lengths of each element in the table
        for j in range(len(table[i]) - 1):
            tableSizes[i][j] = len(str(table[i][j]))

    for i in range(len(tableSizes)):
        maxLen = max(tableSizes[i])
        for j in range(len(tableSizes[i])):
            table[i][j].rjust(maxLen)

    for i in table:
        for j in i:
            print(j + ' ', end='')
        print('')


printTable(tableData)
