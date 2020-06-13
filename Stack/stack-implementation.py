class stack:
    def __init__(self):
        self.items=[]
    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def push(self, ele):
        self.items.append(ele)
        return "Pushed successfully"

    def isEmpty(self):
        if len(self.items)==0:
            return True
        return False


stac=stack()
print(stac.push(1))
print(stac.push(2))
print("Popped element is", stac.pop())
print("Top element is", stac.top())
print(stac.isEmpty())
