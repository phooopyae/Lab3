import price_info as price
def test_total_cost_shopping(): 
    expected = 46.75
    test = price.total_cost_shopping()
    assert (expected == test)
    
def test_cost_of_fruit(): 
    expected = 12
    test = price.cost_of_fruits('apple',10)
    assert (expected == test)