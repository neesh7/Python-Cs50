# Concept of escape sequences
print("hello\nworld")  # \n is used for new line
print("hello\tworld")  # \t is used for tab space
print("hello\\world")  # \\ is used to print single backslash
print('hello "world"')  # using single quote to print double quote
print("hello 'world'")  # using double quote to print single quote
print("hello \"world\"")  # using escape sequence to print double quote inside double quote
print('hello \'world\'')  # using escape sequence to print single quote inside single quote
print(r"hello\nworld")  # r is used to print raw string means escape sequences will not be processed
print("hello\bworld")  # \b is used for backspace
print("hello\rworld")  # \r is used for carriage return
print("hello\fworld")  # \f is used for form feed
print("hello\vworld")  # \v is used for vertical tab
print("hello\aworld")  # \a is used for alert (bell)
print("hello\0world")  # \0 is used for null character
print("hello\100world")  # \100 is used for octal value
print("hello\x40world")  # \x40 is used for hexadecimal value
print("hello\u0040world")  # \u0040 is used for unicode value
print("hello\U00000040world")  # \U00000040 is used for unicode value with 8 digits
print("hello\b\bworld")  # multiple backspace
print("hello\t\tworld")  # multiple tab space
print("hello\n\nworld")  # multiple new line