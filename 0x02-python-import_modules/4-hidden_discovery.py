#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    [print(i) for i in dir(hidden_4) if not i.startswith('__')]
