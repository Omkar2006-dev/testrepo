print("Python list easy & medium level questions test")
print("1.Create a list of numbers [2, 4, 6, 8, 10] and print the first and last element.")
nums = [2, 4, 6, 8, 10]
print(nums)
print("first element:",nums[0])
print("last element:",nums[4])
# Add "orange" to the list ["apple", "banana", "mango"].
fruits = ["apple","banana","mango"]
print(fruits)
fruits.append("orange")
print(fruits)
# Replace the third element in the list [10, 20, 30, 40] with 99.
nums = [10, 20, 30, 40]
print(nums)
nums[2] = 99
print(nums)
# Count how many times 7 appears in [1, 7, 3, 7, 5, 7].
nums = [1, 7, 3, 7, 5, 7]
print(nums)
print(nums.count(7))
# Check if 15 exists in the list [5, 10, 15, 20].
nums  = [5, 10, 15, 20]
print(nums)
if 15 in nums :
    print("found")
# Reverse the list [1, 2, 3, 4, 5] without using slicing
nums = [1, 2, 3, 4, 5]
print(nums)
nums.reverse()
print(nums)
# Find the maximum and minimum from [12, 7, 25, 3, 18].
nums = [12, 7, 25, 3, 18 ]
print(max(nums))
print(min(nums))
# Remove duplicates from [1, 2, 2, 3, 4, 4, 5].
nums = [1, 2, 2, 3, 4, 4, 5 ]
print(nums)
unique = list(set(nums))
print(unique)
# Rotate the list [10, 20, 30, 40, 50] so that the last element comes first.
nums = [10, 20, 30, 40, 50]
print(nums)
new_nums = [nums[-1]] + nums[:-1]
print(new_nums)            
# Find the common elements between [1, 2, 3, 4] and [3, 4, 5, 6].
list01 =  [1, 2, 3, 4]
list02 =  [3, 4, 5, 6]
print(list01)
print(list02)
common = list(set(list01) & set(list02))
print(common)
