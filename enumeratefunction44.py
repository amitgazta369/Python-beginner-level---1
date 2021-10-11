# used to sort item in a list by even or odd otherwise choicewise

# for even number items

l1 = ["bhindi", "gobhi", "kelaa", "apple", "amrud"]

for index, item in enumerate(l1):
    if index%2==0:
        print(f"my dear please buy{item}")
# for odd number items
l1 = ["bhindi", "gobhi", "kelaa", "apple", "amrud"]

for index, item in enumerate(l1):
    if index % 2 == 1:
        print(f"my dear please buy {item}")