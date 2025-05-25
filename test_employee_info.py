import employee_info as em

def test_get_employee_by_age_range():  
    test = em.get_employees_by_age_range('25','35')
    result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert (test == result)

def test_calculate_average_salary(): 
    test = em.calculate_average_salary()
    result = 60166.666666666664
    assert (test == result)

def test_get_employees_by_dept() : 
    test = em.get_employees_by_dept('Marketing')
    result = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    assert (test == result)