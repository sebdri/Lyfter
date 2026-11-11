def my_bubble_sort(list_to_order):
    if not isinstance(list_to_order, list):
        raise ValueError("my_bubble_sort solo acepta listas")

    length = len(list_to_order)
    for out_index in range(length - 1):
        for index in range(length - 1, out_index, -1):
            current = list_to_order[index]
            new_current = list_to_order[index - 1]

            if current < new_current:
                list_to_order[index] = new_current
                list_to_order[index - 1] = current

    return list_to_order


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 7, 6, 8]
    print(my_bubble_sort(lista))