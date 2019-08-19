"""
Handling Errors
As we get more familiar with the Python programming language, 
we run into errors and exceptions. These are complaints that 
Python makes when it doesn’t understand what you want it to do. 
Everyone runs into these issues, so it is a good habit to read and understand them. 
Here are some common errors that we might run into when printing strings:

Example:
        print("Mismatched quotes will cause a SyntaxError')
        print(Without quotes will cause a NameError)

If the quotes are mismatched Python will notice this and inform you that your code has an error 
in its syntax because the line ended (called an EOL) before the double-quote that was supposed to 
close the string appeared. The program will abruptly stop running with the following message:

    SyntaxError: EOL while scanning a string literal
    This means that a string wasn’t closed, or wasn’t closed with the same quote-character that started it.

Another issue you might run into is attempting to create a string without quotes at all.
Python treats words not in quotes as commands, like the print statement. 
If it fails to recognize these words as defined (in Python or by your program elsewhere) Python will complain 
the code has a NameError. This means that Python found what it thinks is a command, but doesn’t know 
what it means because it’s not defined anywhere.

"""
#Fix the two print statements to successfully debug the program!

print("How do you make a hot dog stand?')
print(I live in Sydney Australia)