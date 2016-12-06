class Calc_List:
    def __init__(self):
        self.items = []

    def push(self,item):
        if not item.isdigit() and item != '.':
            self.items.append(Operation(item))
        elif item.isdigit() or item == '.':
            if self.isEmpty():
                self.items.append(Value(item))
            elif type(self.items[-1]) == Value:
                self.items[-1].add_digit(item)
            else:
                self.items.append(Value(item))

    def remove_last(self):
        if self.isEmpty():
            pass
        elif type(self.items[-1]) == Value:
            if len(self.items[-1].val) > 1:
                self.items[-1].val = self.items[-1].val[:-1]
            else:
                self.items.remove(self.items[-1])
        else:
            self.items.remove(self.items[-1])

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def calc_to_str(self):
        calc = ''
        for item in self.items:
            if type(item) == Value:
                calc += item.val
            elif type(item) == Operation:
                calc += item.operator
        return calc

    def print_calc(self):
        print(self.calc_to_str())

    def evaluate(self):
        if self.isEmpty():
            return
        else:
            try:
                result = eval(self.calc_to_str())
            except Exception as e:
                return "Error"
            return result

class Operation:
    def __init__(self,op):
        self.operator = op

class Value:
    def __init__(self,newval):
        self.val = newval

    def add_digit(self,newval):
        self.val += newval
