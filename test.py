def main():
    try:
        int('a')
    except ValueError:
        return(-1)
x = main()
print(x)