class Container:
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"

container = Container('plastic')

print(repr(container))
print(container.category)