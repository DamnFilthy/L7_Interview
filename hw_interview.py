"""
Стек - абстрактный тип данных, представляющий собой список элементов,
организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю.
Или с магазином в огнестрельном оружии(стрельба начнётся с патрона, заряженного последним).

Необходимо реализовать класс Stack со следующими методами:
isEmpty - проверка стека на пустоту. Метод возвращает True или False.
push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
size - возвращает количество элементов в стеке.
"""

"""

Пример сбалансированных последовательностей скобок:

(((([{}]))))
[([])((([[[]]])))]{()}
{{[()]}}

Несбалансированные последовательности:

}{}
{{[(])]}}
[[{())}]

"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def check_balance(line):
    s = Stack()
    balanced = True
    index = 0
    while index < len(line) and balanced:
        symbol = line[index]
        if symbol == "(" or symbol == '[' or symbol == '{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            elif s.peek() == chr(40) and symbol == chr(41) or s.peek() == chr(91) and symbol == chr(
                    93) or s.peek() == chr(123) and symbol == chr(125):
                s.pop()
            else:
                balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


# Check balanced
print(check_balance('(((([{}]))))'))
print(check_balance('[([])((([[[]]])))]{()}'))
print(check_balance('{{[()]}}'))

# Check unbalanced
print(check_balance('}{}'))
print(check_balance('{{[(])]}}'))
print(check_balance('[[{())}]'))
