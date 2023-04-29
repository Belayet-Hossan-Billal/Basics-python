# Regular expressions(findall method)
"""import re
string = "Hello my Name is Belayet "
print(re.findall(r"Belayet", string))"""
# identifier '\d'
"""import re
info = "Hello i live in dandarban 9 which is near street 23"
print(re.findall(r"\d",info))"""

# using '+' modifier
"""import re
data = "Hello I Live on lane 8 which is near streer 42"
print(re.findall(r"\d+", data))"""

# finding(search) a word
"""import re
if re.search("awesome","Isn'this an awesome view!"):
    print("You are Awesome")"""
# re.split method
import re
result = re.split(r"s","Awesome")
print(result)

