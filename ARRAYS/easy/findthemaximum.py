

test_array = [1,2,3,4,5]
temp=None

for i in range(len(test_array)):
    if i==0:
        temp = test_array[i]
    if test_array[i] > temp:
        temp = test_array[i]


print(f' largest value = {temp}')