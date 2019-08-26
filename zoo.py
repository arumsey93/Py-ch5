zoo = ("Fox", "Zebra", "Tyler")
#print(zoo)

print(zoo.index("Tyler"))

animal_to_find = "Tyler"
if animal_to_find in zoo:
    print("This Animal is here:", animal_to_find)
else:
    print("Animal Coming Soon!")

animals = ("Cow", "Monkey", "Lion")
(first_animal, second_animal, third_animal) = animals
print(first_animal)
print(second_animal)
print(third_animal)

zoo_list = list(zoo)
zoo_list.extend(["Horse"])
zoo_list.extend(["Turtle"])
zoo_list.extend(["Pig"])
print(zoo_list)

zoo = tuple(zoo_list)
print(zoo)
