def hello(name=None):
    if name:
        return f"Hello, {name.capitalize()}!"
    else:
        return "Hello, World!"
