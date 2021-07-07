

cookie = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
pairs = cookie.split('&')
for pair in pairs:
   new_dict = dict([pair.split('=', maxsplit=1)])

# I have add this one: "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             " - correct
# But was used this one: "name=Amanda=sssss&age=32&&salary=1500&currency=quro" - incorrect
# Script failed after run with error:

# Traceback (most recent call last):
#   File "/home/local/DO/mykyta.lymarchuk/PycharmProjects/homeworks/SergeyShumilin/QAShumilin_Lesson1/task4_3.py", line 6, in <module>
#     new_dict = dict([pair.split('=', maxsplit=1)])
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

# 2 empty lines in the top of module
# too much lines in the end of module
