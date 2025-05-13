def main():
    # 1. Creating a List and a Nested List
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, [4, 5, 6]]

    print("Fruits List:", fruits)
    print("Numbers List (with Nested List):", numbers)

    # 2. Length of Lists
    print("\nLength of Fruits List:", len(fruits))
    print("Length of Numbers List:", len(numbers))

    # 3. Concatenation
    combined_list = fruits + ["orange", "grape"]
    print("\nConcatenated List:", combined_list)

    # 4. Membership Test
    print("\nIs 'banana' in fruits?", 'banana' in fruits)
    print("Is 4 in numbers?", 4 in numbers)

    # 5. Iteration through List
    print("\nIterating through Fruits List:")
    for fruit in fruits:
        print(fruit)

    # 6. Indexing
    print("\nFirst Fruit:", fruits[0])
    print("Element from Nested List (5):", numbers[3][1])

    # 7. Slicing
    print("\nSliced Fruits (first two):", fruits[0:2])
    print("Sliced Numbers (nested part):", numbers[3][0:2])

if __name__ == "__main__":
    main()
