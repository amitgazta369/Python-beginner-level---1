# list = []
#
# for i in range (100):
#     if i%2==0:
#         list.append(i)
#
# print(list)
# comprehension format
# list = [i for i in range(100) if i%3==0]
# print(type(list))
# dictionary comprehension
# dict1 = {i : f"item{i}" for i in range(1, 500) if i%100==0}
# print(dict1)
# dict1 = {i : f"item{i}" for i in range(10)}
# dict2 = {value:key for key , value in dict1.items()}
# print(dict1)

# set comprehension-- value is taken only once
# dresses = {dress for dress in ["dress1", "dress2","dress1", "dress2","dress3", "dress4","dress5"]}
# print(dresses)
# generator comprehension-- isse hum yield krte hai value generate krwa skte hai we use paranthesis()
# they are special type iterators
evens = (i for i in range (100) if i%3==0)
for item in evens:
    print(item)