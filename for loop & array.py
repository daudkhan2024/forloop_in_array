## For loop
#loop over different arrays and
#collections or letters in strings

friends = ["jim","khan"]
for friend in friends:
    print(friend)

classmates = {"name:khan","namee:shayan"}
for name in classmates:# you can write insted of name anything
    print(name)

#to use range
for index in range(0,4):
     print(index)

friends = ["ahmad","khan","shayan"]
for index in range (len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("its not first iteration")
# difference of index and i
for i in range (5):
    if i == 0:
        print("its fration")
    else:
        print("its not first iteration")


# Exponent Function
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result  * base_num
    return result
print(raise_to_power(3,4))


#2D listed and Nested list

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[1][1])

for row in number_grid:
    print(row)


# to access each element
for row in number_grid:
    for col in row:
        print(col)

