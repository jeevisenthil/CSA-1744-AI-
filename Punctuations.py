import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def main():
    input_str = input("Enter a string: ")
    result = remove_punctuation(input_str)
    print("String without punctuation:", result)

if __name__ == "__main__":
    main()
