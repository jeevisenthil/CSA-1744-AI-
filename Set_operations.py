def input_set(prompt):
    raw_input = input(prompt)
    return set(map(int, raw_input.strip().split()))

def main():
    print("Enter elements of Set A (separated by space):")
    setA = input_set("Set A: ")
    
    print("Enter elements of Set B (separated by space):")
    setB = input_set("Set B: ")

    print("\nSet A:", setA)
    print("Set B:", setB)

    # Union
    print("Union (A | B):", setA | setB)

    # Intersection
    print("Intersection (A & B):", setA & setB)

    # Difference
    print("Difference (A - B):", setA - setB)
    print("Difference (B - A):", setB - setA)

    # Symmetric Difference
    print("Symmetric Difference (A ^ B):", setA ^ setB)

    # Subset and Superset
    print("Is A subset of B?:", setA.issubset(setB))
    print("Is A superset of B?:", setA.issuperset(setB))

    # Adding and Removing Elements
    try:
        value_to_add = int(input("Enter a value to add to Set A: "))
        setA.add(value_to_add)
        print("Set A after adding:", setA)

        value_to_remove = int(input("Enter a value to remove from Set A: "))
        setA.remove(value_to_remove)
        print("Set A after removing:", setA)
    except ValueError:
        print("Please enter valid integers.")
    except KeyError:
        print("Element not found in Set A.")

if __name__ == "__main__":
    main()
