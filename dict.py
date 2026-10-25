#Dic = {"key" : "value"}


student = {
    "name" : "Alice",
    "Age" : 20,
    "city" : "Bangkok",
    "Pet" : ["Dog", "Cat"]
}


print(student)
print(student["name"])
print(student["Age"])
print(student["Pet"][0])


print("\n*****************\n")


#method
student.update({"Country" : "Thailand"})
print(student)
print(student.keys())
print(student.values())
print(student.get("Pet"))
