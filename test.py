def main():

    try: return(int('a'))
    except ValueError: return(-1)

x = main()

if x == ValueError: print(1)
print(x)