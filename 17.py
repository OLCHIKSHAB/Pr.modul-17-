array = [int(x) for x in input("Введите числа в любом порядке через пробел от 1 до 500: ").split()]

def merge_sort(array):  # "разделяем"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выход из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # затем правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))


def binary_search(array, element, left, right):
    if left > right:  # если левая часть превышает правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # середина
    if array[middle] == element:  # если элемент в середине,
        return middle  # то возвращаем
    elif element < array[middle]:  # если элемент меньше чем в середине
        # рекурсивно ищем в левой часте
        return binary_search(array, element, left, middle - 1)
    else:  # то в правой
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 500: "))
        if element < 0 or element > 500:
            raise Exception
        break
    except ValueError:
        print("Ввести число!")
    except Exception:
        print("Неправильный диапазон!")

print(binary_search(array, element, 0,  len(array)))


