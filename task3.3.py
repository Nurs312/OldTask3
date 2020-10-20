a_class = int(input('Число студентов класса "А": '))
b_class = int(input('Число студентов класса "Б": '))
c_class = int(input('Число студентов класса "В": '))
desks_number_a = a_class // 2
desks_number_b = b_class // 2
desks_number_c = c_class // 2
print(f''' "A" классу нужно {desks_number_a} парт, 
"Б" классу нужно {desks_number_b} парт, 
"В" классу нужно {desks_number_c} парт.''')