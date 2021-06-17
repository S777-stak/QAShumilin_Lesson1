john_friends = ["James", "Mark", "Petr"]
marta_friends = ["Santa", "Flora", "Ilona"]
lat, long = (50.10, 36.13)
john = {"full_name": 'JohnSmith', "age": 33, "salary": 3000, "gender": True, "friends":[john_friends], "coordinates": (lat, long)}
print(john)
marta = {"full_name": "MartaSmith", "age": 30, "salary": 5000, "gender": False, "friends": [marta_friends], "coordinates": (lat, long)}
print(marta)

# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
#  Look on how dict is described. It is more preferable view on real projects.
# print(john)
#
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")