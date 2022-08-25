def search(array, element):
    mid = 0
    start = 0
    end = len(array)
    error1 = array[0]
    error2 = array[-1]
    step = 0

    while start <= end:
        step = step + 1
        mid = (start + end) // 2
        try:
            if element == array[mid]:
                return mid
        except IndexError:
            return False
        if element == error2:
            return False
        if element < error1:
            return False
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if len(array) // 2:
        return array[end]
    else:
        return array[start]


class Error(Exception):
    pass


class letters_(Error):
    pass


while True:
    try:
        numbers = input("Введите числа через пробел: ")
        for i in numbers:
            if i.isalpha():
                raise letters_
        break
    except letters_:
        print("Необходимо вводить только числа!")
while True:
    try:
        number = int(input("Введите любое число: "))
        break
    except ValueError:
        print("Введено не корректное значение")

numbers = numbers.split()
numbers = list(map(int, numbers))
numbers.sort()
answer = (search(numbers, number))
if answer == False:
    print("Искомое число выходит за диапазон")
    print(numbers)
else:
    print(numbers)
    print("номер позиции элемента, который меньше введенного пользователем числа - " + str(numbers.index(answer)))
    print("номер позиции элемента, который больше введенного пользователем числа или равен ему - " + str(
        numbers.index(answer) + 1))
