class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
    
    def contact_info(self):
        print(f"{self.name}'s email is {self.email} and phone number is {self.phone}.")

sonny = Person("Sonny", 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

sonny.contact_info()
jordan.contact_info()

#print(f"{sonny.name}'s email {sonny.email} and {sonny.name}'s number is {sonny.phone}.")

#print(f"{jordan.name}'s email is {jordan.email} and {jordan.name}'s phone number is {jordan.phone}'")
