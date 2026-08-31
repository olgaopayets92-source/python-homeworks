my_heigh = 161
print(my_heigh)

my_name = "Ольга"               # сначала только имя
my_name = "Ольга Опаец"         # теперь имя и фамилия
print(my_name)

pet_name = input("Как зовут вашего питомца? ")  #пользовательский ввод
print("Ваш любимчик — " + pet_name)

# 4) Создание функции
def print_python():
    print("Учу Python!")

print_python()

# 5) Вывод слова "Студент" по буквам
def print_letter(let):
    print(let, end='')

print_letter('С')
print_letter('т')
print_letter('у')
print_letter('д')
print_letter('е')
print_letter('н')
print_letter('т')