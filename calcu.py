def tempchange(Fahrenheit):
    Celsius = (Fahrenheit - 32) * (5 / 9)
    return Celsius


fahtocel = tempchange(32)
print("The new temperature is", fahtocel)
fahtocel = tempchange(80)
print("The new temperature is", fahtocel)
fahtocel = tempchange(73)
print("The new temperature is", fahtocel)
fahtocel = tempchange(42)
print("The new temperature is", fahtocel)
