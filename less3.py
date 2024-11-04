def is_even(number):
    last_num = str(number)[-1]
    if last_num in "02468":
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")