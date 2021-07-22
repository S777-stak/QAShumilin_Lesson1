new_gen = (item * 2 for item in range(100) if item % 2 == 0)
for item in new_gen:
    print(item)

# Well done
# Same could be implemented with generator function
