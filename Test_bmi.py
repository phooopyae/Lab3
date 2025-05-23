import Lab2.bmi as bmi
def test_bmi_normal_weight() : 
    test_value = 0 
    result = bmi.calculate_bmi(1.5,45)
    assert (result == test_value)

def test_bmi_over_weight(): 
    test_value = 1 
    result = bmi.calculate_bmi(1.5,60)
    assert (result == test_value)

def test_bmi_under_weight():  
    test_value = -1
    result = bmi.calculate_bmi(1.5,40)
    assert (result == test_value)

