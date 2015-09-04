class Employee:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return "Name: "+self.name+", Age: "+str(self.age)
        
    def __lt__(self,other):
        return self.age < other.age
        

if __name__ == '__main__':
    employee1 = Employee("John",25)
    print employee1
    
    employee2 = Employee("Jane",24)
    print employee2
    
    employees = [employee1,employee2]
    print "Before sorting:"
    print employees
    employees.sort()
    print "After sorting:"
    print employees