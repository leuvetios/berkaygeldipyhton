class Stack:
    def wiew(self):
        for x in range(len(Stack)) :
            print(Stack[x])
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



postfix = []
temp = []
operator = -10
operand = -20
leftparentheses = -30
rightparentheses = -40
empty = -50


def infix2postfix(s):
    if s is '(':
        return 0
    elif s is '+' or '-':
        return 1
    elif s is '*' or '/' or '%':
        return 2
    else:
        return 99


def typeof(s):
    if s is '(':
        return leftparentheses
    elif s is ')':
        return rightparentheses
    elif s is '+' or s is '-' or s is '*' or s is '%' or s is '/':
        return operator
    elif s is ' ':
        return empty
    else:
        return operand


infix = input("İnfix  : ")

def sonuc(postfix2):

    for i in infix:
        type = typeof(i)
        if type is leftparentheses:
            temp.append(i)
        elif type is rightparentheses:
            next = temp.pop()
            while next is not '(':
                postfix.append(next)
                next = temp.pop()
        elif type is operand:
                postfix.append(i)
        elif type is operator:
            p = infix2postfix(i)
            while len(temp) is not 0 and p <= infix2postfix(temp[-1]):
                postfix.append(temp.pop())
            temp.append(i)
        elif type is empty:
            continue

while len(temp) > 0:
    postfix.append(temp.pop())

print ( "Postfix : ", ''.join(postfix))

s = Stack()
s.push(postfix)
s.push('true')
print(s.pop())
