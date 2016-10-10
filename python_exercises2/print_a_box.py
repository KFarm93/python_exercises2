w = int(raw_input("Width? "))
l = int(raw_input("Length? "))
width = w * "*"
length = l * "*"
length_space = (l - 4) * " "

print "*" * w
for number in range(l-4):
    print "*", length_space, "*"
print "*" * w
