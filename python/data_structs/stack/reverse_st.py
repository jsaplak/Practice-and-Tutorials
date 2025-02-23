from stack import Stack

stack = Stack()
for c in "hello":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
