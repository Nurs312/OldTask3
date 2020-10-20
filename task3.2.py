students_number = int(input('Число студентов: '))
apples = int(input('Число яблок: '))
x = apples % students_number
y = apples // students_number
print(f' Каждому студенту доствнеться по {y} яблок.')
print(f' В корзине останеться {x} яюлок.')
