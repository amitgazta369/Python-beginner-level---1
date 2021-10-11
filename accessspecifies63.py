# public -everyone can access variable se koi mtlb ni isse kahi bhi use kar sakte hai
# protected - specific can see denoted by _protec is claas me use kar sakte hai ye fir ise bnai jne wali class me(only sub classes can access)
# private - only u can see denoted by  __protec

class Employee:
    no_of_leaves = 15  #(class variable)
    var = 9
    _protec = 77
    __private = 90


    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


emp = Employee("hrry",  226, "programerr")
print(emp._protec)
# print(emp.__private)
# if we wnt to access private var wee use

print(emp._Employee__private)
# we can use __pr for private