def main():
    x = 1
    x_add_two = x + 2

    # This condition is obviously true
    if x_add_two == 3:
        print("math wins")  # run

    # A negated condition can also be true
    if not x_add_two == 1:
        print("math wins here too")  # run

    # There are else statements as well, which get run
    # if the initial condition fails. Notice that one
    # line gets skipped, and that this conditional
    # does not help you make a conclusive assessment
    # on the variable's true value
    if x_add_two == 1:
        print("math lost here...")  # skip
    else:
        print("math wins otherwise")  # run

    # Else statements also get run once every other
    # if and elif condition fails. Notice that multiple
    # lines get skipped, and that all of the conditions
    # could have been compressed to 'x_add_two != 3'
    # for simplicity. In this case, less is more
    if x_add_two == 1:
        print("nope not this one...")  # skip
    elif x_add_two == 2:
        print("nope not this one either...")  # skip
    elif x_add_two < 3 or x_add_two > 3:
        print("nope not quite...")  # skip
    else:
        print("math wins finally")  # run


if __name__ == "__main__":
    main()
