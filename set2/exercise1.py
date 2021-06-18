"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will print each word in the list line by line 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] 

for word in some_words:
    print(word) # It printed each word in the list line by line 

# I don't think this will print any results because x is not a defined variable 
for x in some_words:
    print(x) # No results were printed 

print(some_words)

# I think this will print 'some_words contains more than 3 words' because it contains 6 words (>3)
if len(some_words) > 3: 
    print('some_words contains more than 3 words') # It printed 'some_words contains more than 3 words 


def usefulFunction(): 
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) 

usefulFunction() 
