
#this program is running on PyCharm latest version easily
def dayOfTheWeek(S, K): # define a method to return day of the week for specific number
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    b = days[(days.index(S) + K) % 7]    # formula showing the easy function
    return b

S, K = 'Sat', 23
print(dayOfTheWeek(S, K))