#initiate a class
class employee:
    # special method/magic mentod/dunder metnod - constructor
    def __init__(self):
        self.salary=50000
        self.id = 123
        self.designation ="Data Scientist"
    def travel(self,destination):
        print(f"Employee is travelling to {destination}")
# create an object/instance of the class
sam = employee()
print(sam.salary)
sam.travel("Kerala")
print(type(sam))