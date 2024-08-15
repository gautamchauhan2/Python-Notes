#WAP to enter marks of 3 subjects from the user and store them in a dictionary . Start with an empty dictionary & add one by one . Use subjects name as key &marks as value.

marks={}
x=input("Enter the chem:")
marks.update({"chem":x})
x=input("Enter the phy:")
marks.update({"phy":x})
x=input("Enter the math:")
marks.update({"math":x})

print(marks)