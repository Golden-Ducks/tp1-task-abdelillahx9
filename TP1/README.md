line 24

Use string.punctuation bcz it's better than hardcoding a specific string manually

line 26

avoid using .replace() inside a loop.. it creates a new string every time
for better performance, use a single loop for characters or re.sub()

line 37

btw, you can use .get() here to handle the dict lookup and the "else" case in one line

line 47

instead of calling the function 4 times manually, use a list and a for loop
