# I think i need to write this conspect, because i don't understand how to work with
# regular expressions. I want to start from the basics and get to advanced examples eventually.

# Let' start

import re

# Metacharester \b suggest blank
# Example:
text = 'scattered plot with the cat'
result = re.findall(r'cat', text)
print(result) # expected output: ['cat', 'cat']
result = re.findall(r'\bcat', text)
print(result) # expected output: ['cat'], because \b suggest 'blank'

# Metacharester '[' and ']' suggest set of characters, that i wish to match
# Example:
text = 'foo bar baz'
result = re.findall(r'[fb]', text)
print(result) # expected output: ['f', 'b', 'b'], because f and b is in the set
result = re.findall(r'[b-z]', text)
print(result) # expected output: ['f', 'o', 'o', 'b', 'r', 'b', 'z'], because a is not in the set

# Metacharesters is not active inside [] construction (except \)
# Example:
text = 'foo bar baz$'
result = re.findall(r'[$]', text)
print(result) # expected output: ['$'], because $ in [], even though it's a special symbol

# Metacharester '^' inside [] match any charester, except chareset after caret
# Example:
text = 'foo bar baz$'
result = re.findall(r'[^fob ]', text)
print(result) # expected output: ['a', 'r', 'a', 'z', '$']

# [a-zA-Z0-9_] will match all charester, which marked as letter in the Unicode database
# allias for this expression: \w
text = 'foo bar baz$'
result = re.findall(r'[a-zA-Z0-9_]', text)
print(result == re.findall(r'\w', text)) # expected output: True

# \d Matches any decimal digit; this is equivalent to the class [0-9]
# \D Matches any non-digit charester; this is equivalent to the class [^0-9]
# \s Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v]
# \S Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
# \w Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
# \W Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

# '.' match any charester, except newline charester
# Example:
text = 'foo_123 Zs$∑'
result = re.findall(r'.', text)
print(result)  # expected output: ['f', 'o', 'o', '_', '1', '2', '3', ' ', 'Z', 's', '$', '∑']

# Operator for repeating regexp things 0 or more time -- '*'
# '*' are greedy, so it will match as much as possible
# For example, ca*t will match 'ct' (0 'a' characters), 'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth.
# Example:
text = 'foob foooooooooooooooooooooooooob fb'
result = re.findall(r'f\w*b', text)
print(result) # expected outputp: ['foob', 'foooooooooooooooooooooooooob', 'fb']

# Operator for repeating regexp things 1 or more time -- '+'
# Unlike '*', the '+' operator wants at least one character, making it non-optional.
# Example:
text = 'foob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo+b', text)
print(result) # expected output: ['foob', 'foooooooooooooooooooooooooob'], because 'fb' don't have 'o'

# Operator for repeating regexp things zero or one time -- '?'
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo?b', text)
print(result) # expected output: ['fob', 'fb']

# For customizing repeats using {min, max}
# You can omit either `min` or `max`; in that case, a reasonable value is assumed for the missing value. 
# Omitting `min` is interpreted as a lower limit of 0, while omitting `max` results in an upper bound of infinity.
# The simplest case {count} matches the preceding item exactly `count` times.
# Example:

# Min and max
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo{0,1}b', text)
print(result) # expected output: ['fob', 'fb']

# Min and missing max
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo{1,}b', text)
print(result) # expected output: ['fob', 'foooooooooooooooooooooooooob']

# Missing min and max
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo{,3}b', text)
print(result) # expected output: ['fob', 'fb']

# Missin min and missing max
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo{,}b', text)
print(result) # expected output: ['fob', 'foooooooooooooooooooooooooob', 'fb']

# Count
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo{1}b', text)
print(result) # expected output: ['fob']


# Other metacharesters
# Alternation, or the “or” operator is '|'. It matches the expression to its left, or the expression to its right.
# Example:
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fob|fb', text)
print(result) # expected output: ['fob', 'fb']

# For search a pattern at the beggining of lines used '^'.
# Example:
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'^fo*b', text)
print(result) # expected output: ['fob']

# For search a pattern at the end of a line used '$'.
# Example:
text = 'fob foooooooooooooooooooooooooob fb'
result = re.findall(r'fo*b$', text)
print(result) # expected output: ['fb']


