

cookie = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
pairs = cookie.split('&')
for pair in pairs:
   new_dict = dict([pair.split('=', maxsplit=1)])

