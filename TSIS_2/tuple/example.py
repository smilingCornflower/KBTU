# All examples are available for tuples, except of these

tpl = ("Silent Hill 2", "GTA V", "Red Dead Redemption 2", "Minecraft")

try:
    tpl[0] = "Spider Man"
except TypeError as err:
    print(err)

try:
    tpl.append("Spider Man")
except AttributeError as err:
    print(err)

# Append
tpl = tpl + ("Spider Man",)

# Change item of some index
tpl = tpl[:-1] + ("Spider Man 2",)
print(tpl)

# ("Hello") -> "Hello"
# ("Hello",) -> ("Hello")
# If you try to create a tuple with one item, variable assigns to item directly
