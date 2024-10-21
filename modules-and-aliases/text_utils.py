# Defining a function to reverse the string input
def reverse_string(string):
    words = string.split(' ')
    words.reverse()
    reversed_string = " ".join(words)
    return reversed_string

# Defining a function to capitalize the string input
def capitalize_string(string):
    capitalized_string = string.capitalize()
    return capitalized_string