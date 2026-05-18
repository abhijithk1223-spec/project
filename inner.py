class outer:
    def __init__(self):
        self.name = "outer class"

    class inner:
        def __init__(self):
            self.name = "inner class"

        def display(self):
            print("This is the Inner Class")


outer = outer()
print(outer.name)

inner = outer.inner()
print(inner.name)