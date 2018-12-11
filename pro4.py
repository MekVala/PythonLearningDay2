# Variable Length Argument


def demo_func(name, *var):
    print("Name From Argument: ", name)
    print("Variable Length Argument:")
    for x in range(len(var)):
        print(var[x])


demo_func("Mihir", "hello", "world", "!")
