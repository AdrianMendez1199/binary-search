import random

def binary_search(numbers,number_to_find, low, high):
 
    if low > high:
        return False
    
    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True 
    elif numbers[mid] > number_to_find:
       return binary_search(numbers, number_to_find, low,  mid - 1)
    else:
       return binary_search(numbers, number_to_find, mid + 1, high)


def generate_random_number():
    random_number = []

    for i in range(0, 10):
        idx = random.randint(0,50000)
        random_number.append(idx)

    return random_number

def run():
    numbers = generate_random_number()
    ordened_numbers = sorted(numbers)
    number_to_find = int(input('enter a number to check if it is on the list \n'))
    result = binary_search(ordened_numbers, number_to_find, 0, len(numbers) -1)
    
    print(result)


if __name__ == "__main__":
    run()