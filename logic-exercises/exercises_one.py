def print_numbers():
    for i in range(0,101):
        
        if i and  i % 2 == 0:
            print(i, 'Buzz')
        elif i % 5 == 0:
            print(i, 'Buzz')
        else:
            print(i)


if __name__ == '__main__':
    print_numbers()
