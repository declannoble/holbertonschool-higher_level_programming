#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    result = dir(hidden_4)
    for name in result:
        if name[0:2] == '__':
            continue
        print(name)
