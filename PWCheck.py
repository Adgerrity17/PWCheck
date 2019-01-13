import re
print('This code will check your PW for strength')
print('Your PW must have 1 upper case letter, 1 lower case letter, and 1 number, and be more than 8 characters long')

capReg = re.compile(r'.*[A-Z]{1,9}.*')
lowerReg = re.compile(r'.*[a-z]{1,9}.*')
digitReg = re.compile(r'.*\d{1,9}.*')



def checkPassword(text):
    if capReg.search(text) and lowerReg.search(text) and digitReg.search(text) and len(text) > 7:
        print('Good work')
    else:
        print('Your PW did not meet the requirements')
        NewPw = input('Please enter a new PW: ')
        print(checkPassword(NewPw))

pw = input('Please enter your PW: ')
print(checkPassword(pw))