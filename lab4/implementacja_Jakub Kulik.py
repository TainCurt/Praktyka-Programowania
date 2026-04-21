class Regulamin: #singleton
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Regulamin, cls).__new__(cls)
            print("Utworzono regulamin")
        return cls._instance

    def show(self):
        print("To jest jedyny regulamin w systemie")


r1 = Regulamin()
r2 = Regulamin()

r1.show()

print(r1 is r2) 