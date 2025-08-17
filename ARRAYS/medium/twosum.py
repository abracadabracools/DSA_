#  Two Sum Problem
# Problem Statement:
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
#
# You may assume that each input has exactly one solution, and you may not use the same element twice
from torchgen.api.cpp import return_type

# solution based on difference principle


arr = [1,5,7,8,3]

tar = 8

diff = [tar-i for i in arr]

# print(f'diff -- {diff}')

for i in diff:
    if i in arr:
        sec = arr.index(i)
        fir = diff.index(i)
        break
print(f'indices,numbers  -  {arr[fir]} , {arr[sec]} ')

