def print_params(a = 1, b = 'строка', c = True):
    print(a, b,c)

print_params()
print_params(b = 25)  #работает
print_params(c = [1,2,3])  #работает!

values_list = (18, "Олег", True)
values_dict = {"a": False, "b": 12, "c": "Логунов"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ("Urban", 2024)
print_params(*values_list_2, 42)  #работает!!
