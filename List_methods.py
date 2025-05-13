def main():
    my_list = []
    print("Initial list:", my_list)

    # Append: adds a single element at the end
    my_list.append(10)
    print("After append(10):", my_list)

    # Add (Insert): insert an element at a specific index
    my_list.insert(0, 5)
    print("After insert(0, 5):", my_list)

    # Extend: adds multiple elements from another iterable
    my_list.extend([20, 30, 40])
    print("After extend([20, 30, 40]):", my_list)

    # Delete using remove(): removes the first occurrence of a value
    my_list.remove(10)
    print("After remove(10):", my_list)

    # Delete using pop(): removes element at specified index or last element
    popped = my_list.pop()
    print("After pop():", my_list, "| Popped value:", popped)

    # Delete using del: removes element at index or entire list
    del my_list[0]
    print("After del my_list[0]:", my_list)

    # Clear the list
    my_list.clear()
    print("After clear():", my_list)


if __name__ == "__main__":
    main()
