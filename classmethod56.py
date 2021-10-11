class Employee:
    no_of_leaves = 15  #(class variable)
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"name is {self.name} and salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


harry = Employee("harry", 266, "instructor")
rohan = Employee("rohan",16161, "student")

harry.change_leaves(78)


print(harry.no_of_leaves)
# we can use class mmethod as alternative constructor