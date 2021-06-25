bigno_blacklist = ["John Dow", "John Row", "John Flow"]
poker_blacklist = ["Nick Dow", "John Row", "Nick Flow"]
majong_blacklist = ["Jina Dow", "John Row", "Jina Flow"]
blacklist = []

for i in bigno_blacklist:
        for j in poker_blacklist:
            for k in majong_blacklist:
                if i == j == k:
                    blacklist.append(i)
                    break
print(blacklist)

# Not bad but this solution has complexity O(n^3).
# Also you choose lists but this task was oriented on sets instead so it could
# be easily solved with intersection operation.
# Since you know that everyone in each list is unique.
# Also it is hard to understand what is i, j and k variables try to name them
# with some clear naming like bingo_person, poker_person, majong_person
