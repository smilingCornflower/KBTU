def kids(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kids(name="Alice", age=7, hobby="Drawing")

