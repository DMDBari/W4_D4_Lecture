# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


def solution(lst):
    counter = 0
    output = 0
    for num in lst:
        if num == 1:
            counter += 1
            if counter > output:
                output = counter
        else:
            if counter > output:
                output = counter
            counter = 0
    return output