def digitSum(n):
    dsum = 0
    for i in str(n):
        dsum += int(i)
    return dsum

List = [367, 111, 452, 562, 6726, 873]

#using the function on odd elements of the list 
newList = [digitSum(j) for j in List if j & 1]

print(newList)