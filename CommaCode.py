def commacode(list):
    rval = ''
    for i in list[0:len(list)-1]:
        rval += i + ', '

    rval += 'and ' + list[-1]
    return rval;

spam = ['Dan', 'Greg','Evan']
print(commacode(spam))