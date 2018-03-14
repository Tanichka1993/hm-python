# MESSAGE = 'I am %s %s, I am studying at the %s with %s, my average mark is %f'
MESSAGE = 'I am {} {}, I am studying at the {} with {}, my average mark is {}'

name = input("Enter your name: ").capitalize()
surname = input("Enter your surname: ").capitalize()
group_name = input("Enter your name of group: ")
university = input("Enter your name of university: ").upper()
average_mark = float(input("Enter your average mark : "))

# print(MESSAGE % (name, surname, university, group_name, average_mark))
print(MESSAGE.format(name, surname, university, group_name, average_mark))
