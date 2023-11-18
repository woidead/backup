# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_name(self):
#         print(self.name)
        
# my_object = MyClass('aziz', 18)
# # my_object.show_name()
# # print(my_object.name)
# # print(my_object.age)
# print(my_object.__dict__)
# print(my_object.__dir__())

class Parser:
    def __init__(self,data:dict):
        self.data = data
    
    def get_keys_tuple(self):
        return tuple(self.data.keys())
    
    def get_values_tuple(self):
        return tuple(self.data.values())
    
    def get_keys_list(self):
        return list(self.data.keys())
    
    def get_values_list(self):
        return list(self.data.values())
    
    def get_keys_set(self):
        return set(self.data.keys())
    
    def get_values_set(self):
        return set(self.data.values())

classroom_data_1 = {
    "Student": "John Doe",
    "Age": 20,
    "Grade": "A",
    "Course": "Computer Science"
}
my_class = Parser(classroom_data_1)

keys_tuple = my_class.get_keys_tuple()
values_tuple = my_class.get_values_tuple()
keys_list = my_class.get_keys_list()
values_list = my_class.get_values_list()
keys_set = my_class.get_keys_set()
values_set = my_class.get_values_set()

print(keys_tuple)
print(values_tuple)
print(keys_list)
print(values_list)
print(keys_set)
print(values_set)