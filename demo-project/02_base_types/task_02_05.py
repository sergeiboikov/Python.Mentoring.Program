"""
Модуль формирования отчета о средней ЗП по сотрудникам за 2020 год.
"""

employees = [
    (1, 'Шершуков', 'Виктор', 'Кузьмич',),
    (2, 'Битова', 'Анастасия', 'Юрьевна',),
    (3, 'Кириллов', 'Валентин', 'Владиславович',),
    (4, 'Игнатьев', 'Игорь', 'Дмитриевич',),
]

emails = [
    (1, 1, 'shershuko@mail.ru',),
    (2, 1, 'shershuko-v@mail.ru',),
    (3, 2, 'bitova@mail.ru',),
    (4, 2, 'bitova@mail.ru',),
    (5, 3, 'kirillov@mail.ru',),
    (6, 3, 'kirillov@mail.ru',),
]

salary = [
    (1, '2019-12-01', 'salary', 50000),
    (1, '2020-01-01', 'salary', 50000),
    (1, '2020-02-01', 'salary', 50000),
    (1, '2020-03-01', 'salary', 50000),
    (1, '2020-04-01', 'salary', 50000),
    (1, '2020-05-01', 'salary', 50000),
    (1, '2020-06-01', 'salary', 53000),
    (1, '2020-07-01', 'salary', 53000),
    (1, '2020-08-01', 'salary', 53000),
    (1, '2020-09-01', 'salary', 53000),
    (1, '2020-10-01', 'salary', 53000),
    (1, '2020-11-01', 'salary', 53000),
    (1, '2020-12-01', 'salary', 53000),
    (1, '2021-01-01', 'salary', 53000),
    (1, '2019-12-01', 'bonus', 10000),
    (1, '2020-01-01', 'bonus', 10000),
    (1, '2020-02-01', 'bonus', 9000),
    (1, '2020-03-01', 'bonus', 11000),
    (1, '2020-04-01', 'bonus', 10000),
    (1, '2020-05-01', 'bonus', 5000),
    (1, '2020-06-01', 'bonus', 10000),
    (1, '2020-07-01', 'bonus', 10000),
    (1, '2020-08-01', 'bonus', 10000),
    (1, '2020-09-01', 'bonus', 10000),
    (1, '2020-10-01', 'bonus', 10000),
    (1, '2020-11-01', 'bonus', 10000),
    (1, '2020-12-01', 'bonus', 10000),
    (1, '2021-01-01', 'bonus', 10000),
    (2, '2019-12-01', 'salary', 60000),
    (2, '2020-01-01', 'salary', 60000),
    (2, '2020-02-01', 'salary', 60000),
    (2, '2020-03-01', 'salary', 62000),
    (2, '2020-04-01', 'salary', 62000),
    (2, '2020-05-01', 'salary', 62000),
    (2, '2020-06-01', 'salary', 62000),
    (2, '2020-07-01', 'salary', 62000),
    (2, '2020-08-01', 'salary', 62000),
    (2, '2020-09-01', 'salary', 62000),
    (2, '2020-10-01', 'salary', 65000),
    (2, '2020-11-01', 'salary', 65000),
    (2, '2020-12-01', 'salary', 65000),
    (2, '2021-01-01', 'salary', 65000),
    (2, '2019-12-01', 'bonus', 10000),
    (2, '2020-01-01', 'bonus', 10000),
    (2, '2020-02-01', 'bonus', 9000),
    (2, '2020-03-01', 'bonus', 11000),
    (2, '2020-04-01', 'bonus', 10000),
    (2, '2020-05-01', 'bonus', 5000),
    (2, '2020-06-01', 'bonus', 10000),
    (2, '2020-07-01', 'bonus', 7000),
    (2, '2020-08-01', 'bonus', 7000),
    (2, '2020-09-01', 'bonus', 7000),
    (2, '2020-10-01', 'bonus', 7000),
    (2, '2020-11-01', 'bonus', 7000),
    (2, '2020-12-01', 'bonus', 7000),
    (2, '2021-01-01', 'bonus', 7000),
    (3, '2019-12-01', 'salary', 60000),
    (3, '2020-01-01', 'salary', 60000),
    (3, '2020-02-01', 'salary', 60000),
    (3, '2020-03-01', 'salary', 60000),
    (3, '2020-04-01', 'salary', 60000),
    (3, '2020-05-01', 'salary', 60000),
    (3, '2020-06-01', 'salary', 60000),
    (3, '2020-07-01', 'salary', 60000),
    (3, '2020-08-01', 'salary', 60000),
    (3, '2020-09-01', 'salary', 60000),
    (3, '2020-10-01', 'salary', 60000),
    (3, '2020-11-01', 'salary', 64000),
    (3, '2020-12-01', 'salary', 64000),
    (3, '2021-01-01', 'salary', 64000),
    (4, '2019-12-01', 'salary', 61000),
    (4, '2020-01-01', 'salary', 61000),
    (4, '2020-02-01', 'salary', 61000),
    (4, '2020-03-01', 'salary', 61000),
    (4, '2020-04-01', 'salary', 61000),
    (4, '2020-05-01', 'salary', 63000),
    (4, '2020-06-01', 'salary', 63000),
    (4, '2020-07-01', 'salary', 63000),
    (4, '2020-08-01', 'salary', 63000),
    (4, '2020-09-01', 'salary', 63000),
    (4, '2020-10-01', 'salary', 63000),
    (4, '2020-11-01', 'salary', 63000),
    (4, '2020-12-01', 'salary', 63000),
    (4, '2021-01-01', 'salary', 63000),
    (4, '2019-12-01', 'bonus', 7000),
    (4, '2020-01-01', 'bonus', 7000),
    (4, '2020-02-01', 'bonus', 7000),
    (4, '2020-03-01', 'bonus', 7000),
    (4, '2020-04-01', 'bonus', 7000),
    (4, '2020-05-01', 'bonus', 7000),
    (4, '2020-06-01', 'bonus', 7000),
    (4, '2020-07-01', 'bonus', 7000),
    (4, '2020-08-01', 'bonus', 7000),
    (4, '2020-09-01', 'bonus', 7000),
    (4, '2020-10-01', 'bonus', 7000),
    (4, '2020-11-01', 'bonus', 7000),
    (4, '2020-12-01', 'bonus', 7000),
    (4, '2021-01-01', 'bonus', 7000),
]

# Main list for result set
emp_list = []
# Set for unique employees ids
emp_unique_ids = set()
# List for average salary and bonuses
salary_2020_list = []

for emp in employees:
    # Define dictionary for employees info and fill it with initial data and default values
    emp_info_dict = {'Empl_ID': emp[0], 'FIO': f'{emp[1]} {emp[2]} {emp[3]}', 'Salary': None, 'Bonus': None,
                     'Email': [None]}
    emp_list.append(emp_info_dict)
    # Fill emp_unique_ids with unique employees ids
    emp_unique_ids.add(emp[0])

for emp_id in emp_unique_ids:
    # Define variables for calculating average salary and bonuses
    salary_sum = 0
    salary_cnt = 0
    bonus_sum = 0
    bonus_cnt = 0
    for salary_item in salary:
        # Filtering data for 2020 year and particular employee
        if salary_item[0] == emp_id and salary_item[1][0:4] == '2020':
            if salary_item[2] == 'salary':
                # Calc total salary for employee
                salary_sum += salary_item[3]
                salary_cnt += 1
            if salary_item[2] == 'bonus':
                # Calc total bonuses for employee
                bonus_sum += salary_item[3]
                bonus_cnt += 1
    # Define dictionary with average salary and bonuses per employee
    emp_salary_info_dict = {'Empl_ID': emp_id,
                            'Salary_avg': (salary_sum / salary_cnt) if salary_cnt > 0 else None,
                            'Bonus_avg': (bonus_sum / bonus_cnt) if bonus_cnt > 0 else None}
    # Add info about employees' average salary to salaries' list
    salary_2020_list.append(emp_salary_info_dict)

# Fill emp_list with info about emails, average salary and average bonus
for emp_info_dict in emp_list:
    for email in emails:
        if email[1] == emp_info_dict.get('Empl_ID'):
            if email[2] not in emp_info_dict.get('Email'):
                # To ensure uniqueness of emails in list, if default value in the list is None, assign value
                if emp_info_dict.get('Email')[0] is None:
                    emp_info_dict.get('Email')[0] = email[2]
                # Else add value to existed items in the list
                else:
                    emp_info_dict.get('Email').append(email[2])
    # Add to employees' dictionary data about average salary and bonuses
    for salary_info_dict in salary_2020_list:
        if salary_info_dict['Empl_ID'] == emp_info_dict['Empl_ID']:
            emp_info_dict['Salary'] = salary_info_dict['Salary_avg']
            emp_info_dict['Bonus'] = salary_info_dict['Bonus_avg']
    # Output result set
    for email in emp_info_dict['Email']:
        print(f'{emp_info_dict["Empl_ID"]}, {emp_info_dict["FIO"]}, {emp_info_dict["Salary"]},'
              f'{emp_info_dict["Bonus"]}, {email}')
