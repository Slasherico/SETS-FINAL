def panagram(input_string):
    alphset = set('abcdefghijklmnopqrstuvxyz')
    inpt_string = set(input_string.lower())
    return alphset <= inpt_string

input_string = 'The quick brown fox jumps over the lazy dog'
if panagram(input_string):
    print('Its a panagram')
else:
    print('Not a pangram')