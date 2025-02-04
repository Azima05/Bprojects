myfamily = ("mother", "father", "sister", "brother", "sister")

print("Type of myfamily:", type(myfamily))  
print("First sister in family:", myfamily[2])  
print("Second sister in family:", myfamily[4])
myfamily = myfamily + ("me",)
print("After adding 'me':", myfamily)

myfamily = tuple(item for item in myfamily if item != "brother")
print("After removing 'brother':", myfamily)
