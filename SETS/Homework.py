def panagram(input_string):
    alphset = set('1234567890')
    inpt_string = set(input_string.lower())
    return alphset <= inpt_string

input_string = (input("Enter a series of numbers: "))
if panagram(input_string):
    print('Its a panagram')
else:
    print('Not a pangram')