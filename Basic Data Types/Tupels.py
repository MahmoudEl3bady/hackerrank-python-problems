
# import __builtins__
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    _hash = hash(t)
    print(_hash)