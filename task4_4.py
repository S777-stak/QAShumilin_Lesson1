
import re

name = ["FirstItem", "FriendsList", "MyTuple"]
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)

# Seems like regular expression is correct. I have see similar solution on stack overflow.
# But I am getting error when trying to run script:
# Traceback (most recent call last):
#   File "/home/local/DO/mykyta.lymarchuk/PycharmProjects/homeworks/SergeyShumilin/QAShumilin_Lesson1/task4_4.py", line 5, in <module>
#     name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
#   File "/usr/lib/python3.9/re.py", line 210, in sub
#     return _compile(pattern, flags).sub(repl, string, count)
# TypeError: expected string or bytes-like object