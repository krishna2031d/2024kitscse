class Emp:
    def __init__(self,name,salary): # initialize the function the arguments 'name' and 'salary'
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'[name={self.name},salary={self.salary}]'
    def __repr__(self):
        return self.__str__()
    
employees = [
    Emp('Dravid',20000),
    Emp('Ganguly',30000),
    Emp('Sachin',25000)
]
tot = 0.0
for e in employees: # element iterator
    tot += e.salary
    print(e)  # print each emp

print(f'total sal is {tot}')