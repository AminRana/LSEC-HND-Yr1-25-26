nums = [3, 7, 19, 2, 8, 3, 9, 1, 6]
print(nums)

nums.append(4)
print(nums)

index_of_2 = nums.index(2)
nums.insert(index_of_2 + 1, 23)
print(nums)

print(nums[4:7])

nums.extend([3, 6, 9, 12])
print(nums)

nums.reverse()
print(nums)
nums.reverse()
print(nums)

del nums[3]
print(nums)

nums.sort(reverse=True)
print(nums)

odds = [n for n in nums if n % 2 !=0]
print(odds)

print(sum(nums))
