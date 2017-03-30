#import modules to help us achieve our program aims
import time 
import webbrowser

""" Purpose of program is to open up a web browser every 2 hours to remind the
    user to take a break."""

# we've decided to take 3 breaks total
numberBreaks = 3

# we're starting with 0 breaks taken
breakCount = 0

# let user know what time the program started
print('The program started on ' + time.ctime()) 

# while the number of breaks taken is less than the total number of breaks
# to be taken:

while breakCount < numberBreaks:
    # keep track of time for a total of 2*60*60 seconds (using 10 for testing)
    time.sleep(10) 
    webbrowser.open("https://www.youtube.com/watch?v=DDWKuo3gXMQ&feature=youtu.be&t=45s")
    breakCount += 1
