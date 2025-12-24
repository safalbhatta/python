# Uncomment the line below to use interactive input
# array = list(map(int, input("Enter the array elements separated by spaces: ").split()))

# Use a hardcoded array for testing purposes
array = [1, 2, 4, 6, 3, 7, 8]
print(array)
sorted_array=sorted(array)
print(sorted_array)
sum1=0
max_num = max(sorted_array)
print(max_num)
sum1 = max_num * (max_num + 1) // 2
print(sum1)
missing_number = sum1 - sum(sorted_array)
print(missing_number)
 