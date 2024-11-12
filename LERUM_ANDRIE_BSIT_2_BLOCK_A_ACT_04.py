students = {}
names = []

while True:
    name = input("Enter student's name (or type 'stop' to finish): ")
    if name.lower() == 'stop':
        break
    first_letter = name[0].upper()
    if first_letter not in students:
        students[first_letter] = [name]
    else:
        students [first_letter].append(name)

for letter, names in students.items():
    print (f"{letter}: {', '.join(names)}")

