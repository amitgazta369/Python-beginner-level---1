# how to use class method as alternative constructor*
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


    @classmethod
    def from_str_(cls, string):
        params = string.split("-")
        print(params)
        return cls(params[0], params[1], params[2])
        #   return cls(*string.split("-"))


harry = Employee("harry", 266, "instructor")
rohan = Employee("rohan",16161, "student")
karan = Employee.from_str_("karan78-262637-teacher")

print(karan.name,karan.role,karan.salary,)

harry.change_leaves(78)


print(harry.no_of_leaves)