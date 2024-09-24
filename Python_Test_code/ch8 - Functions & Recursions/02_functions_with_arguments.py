def computer(name):
    print("its a computer, " + name)

computer("shiv")
computer("sahil")


# ---------------------------------------------------------------

# Example - 2
def computer(name, lastname):
    print("its a computer, " + name + " " + lastname)

computer("shiv", "singh")
computer("sahil", "singh")
computer("Aman", "singh")
computer("Vishal", "singh")
# ---------------------------------------------------------------

# Example - 3
def computer(name, lastname):
    print("its a computer, " + name + " " + lastname)
    return "Done"

a = computer("shiv", "singh")
print(a)
