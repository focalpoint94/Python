

nums = list(map(int, input()))

result = 0

if nums[0] != 0 and nums[1] != 0 and nums[0] != 1 and nums[1] != 1:
    result += nums[0] * nums[1]
else:
    result += nums[0] + nums[1]

for num in nums[2:]:
    if num == 0 or num == 1:
        result += num
    else:
        result *= num

print(result)
