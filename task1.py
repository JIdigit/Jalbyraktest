def is_even(num):
    check=num/2
    check1=int(check)
    check=check-check1
    while check:
        return False
        break
    else:
        return True
        

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
    print("YOUR CODE IS CORRECT!")
test_is_even()