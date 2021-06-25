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

