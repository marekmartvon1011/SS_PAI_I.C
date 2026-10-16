x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x >= y:
    max = x
else:
    max = y
if max < z:
    max = z
print(max)

name = input("zadaj svoje meno: ")
vek = input("zadaj vek: ?")
print("volám sa " + name + " a mám " + vek + "rokov")
print("ahoj", name, "ako sa maš?")