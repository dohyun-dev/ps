import re

s = "".join(re.findall("\w|\d", input()))
print(s == s[::-1])