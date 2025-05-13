def sort_sentence(sentence):
    for char in "-.,\n":
        sentence = sentence.replace(char, " ")
    
    words = sentence.split()
    words.sort()

    sorted_sentence = ' '.join(words)
    return sorted_sentence

def main():
    sentence = input("Enter a sentence: ")
    sorted_result = sort_sentence(sentence)
    print("\nSorted Sentence:")
    print(sorted_result)

if __name__ == "__main__":
    main()
