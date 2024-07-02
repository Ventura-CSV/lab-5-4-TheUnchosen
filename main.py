import random


def minmax(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(len(numbers)):
        if i == 0:
            minval = numbers[i]
        elif minval > numbers[i]:
            minval = numbers[i]
        if maxval < numbers[i]:
            maxval = numbers[i]
        
        

    ########################################
    # Do not delete the return statement
    ########################################
    return minval, maxval


def main():

    numbers = [1, 2, 3, 4, 5]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value:{minval}')

    numbers = [random.randint(0, 100) for i in range(10)]
    minval, maxval = minmax(numbers)
    print('List values', *numbers)
    print(f'Max value: {maxval} \t Min value: {minval}')


if __name__ == '__main__':
    main()
