# Initial list
nums = [3, 7, 19, 2, 8, 3, 9, 1, 6]

# a) Place the number 4 at the end of the list
nums.append(4)
print("a)", nums)

# b) Place 23 between the 2 and the 8
index_8 = nums.index(8)  # Find index of 8
nums.insert(index_8, 23)
print("b)", nums)

# c) Print the 5th to 7th numbers (index 4 to 6)
print("c)", nums[4:7])

# d) Add the list [3, 6, 9, 12] to nums
nums.extend([3, 6, 9, 12])
print("d)", nums)

# e) Reverse the list
nums.reverse()
print("e)", nums)

# f) Delete the 4th number (index 3)
del nums[3]
print("f)", nums)

# g) Sort the list in descending order
nums.sort(reverse=True)
print("g)", nums)

# h) Print out all odd numbers
odd_nums = [n for n in nums if n % 2 == 1]
print("h)", odd_nums)

# i) Add all numbers of the list
total = sum(nums)
print("i)", total)
