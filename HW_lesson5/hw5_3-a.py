# 3. a Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк).Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open("f_5_3_a.txt") as employees:
    salaries = []
    print(f'Сотрудники имеющие з/п менее 20 тыс.руб.:')

    for employee in employees:
        last_name, salary = employee.split()
        salary = int(salary)
        if salary < 20_000:
            print(last_name, salary)
            salaries.append(salary)
            sr_salary = sum(salaries)/len(salaries)

    print(f'Средняя з/пл сотрудников с з/п менее 20 тыс.руб.: {sr_salary}')


