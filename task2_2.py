global_logic = ["John Dow", "John Row", "John Flow"]
toshiba = ["Nick Dow", "John Row", "Nick Flow"]
toshiba_new = list(set([i for i in toshiba if i not in global_logic]))
print(toshiba_new)
# Good buat make names of variable more readable 'i' not clear what is it.
# if John Dow employee exist in both companies it means that it is not same person.
# so converting to set was not needed
# Take a look on some alternative solutions of this task
# It could be resolved with next operations:
# 1.
# global_logic.clear()
# or
# 2.
# while global_logic:
#     toshiba.append(global_logic.pop())
# print(toshiba)
# print(global_logic)
