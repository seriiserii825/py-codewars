def findTheParityOutlier(integers):
    odd = [i for i in integers if i % 2 != 0]
    even = [i for i in integers if i % 2 == 0]
    return odd[0] if len(odd) == 1 else even[0]
# print(findTheParityOutlier([6,2,4,5]))
print(findTheParityOutlier([1,3,4,5]))
