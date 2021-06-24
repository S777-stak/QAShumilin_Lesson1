global_logic = ["John Dow", "John Row", "John Flow"]
toshiba = ["Nick Dow", "John Row", "Nick Flow"]
toshiba_new = list(set([i for i in toshiba if i not in global_logic]))
print(toshiba_new)