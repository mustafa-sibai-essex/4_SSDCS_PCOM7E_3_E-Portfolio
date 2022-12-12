
class Variable:
    def __init__(self, realValue, fakeValue):
        self.realValue = realValue
        self.fakeValue = fakeValue

    def GetValue(self, isAuthorized):
        if isAuthorized:
            return self.realValue
        else:
            return self.fakeValue

userIsAuthorized = False

balance = Variable(150, 999)

username = input('Please enter your username\n')
password = input('Please enter your password\n')

if username == 'David' and password == 'David@123':
    userIsAuthorized = True

print('You account balance is {0}'.format(balance.GetValue(userIsAuthorized)))