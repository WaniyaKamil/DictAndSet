lion_list = ["scary", "big", "cat"]
elephant_list =["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals = {
    "lion": lion_list,
    "elephant": elephant_list ,
    "teddy": teddy_list ,
}

things = animals.copy()
print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])