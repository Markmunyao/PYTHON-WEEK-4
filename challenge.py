class Employee:  # Class names usually start with a capital letter in Python.
    def __init__(self, name, age, department, id):
        self.name = name
        self.age = age
        self.department = department
        self.id = id

    def start(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class EmployeeDetails(Employee):  # Note the capitalization here for consistency.
    def start(self):
        return f"my name is {self.name}, I am {self.age} years old, I work in {self.department}, and my ID is {self.id}"

# Create an instance of EmployeeDetails, not Employee
employee_details_instance = EmployeeDetails("MARK KUSU", 24, "FINANCE", 234)
worker_details_instance=EmployeeDetails("kuchi",24,"distribution",235)

# Now, call the start method on your instance to print the details.
print(employee_details_instance.start())
print(worker_details_instance.start())
