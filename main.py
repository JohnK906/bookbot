def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)

    char_dict = letter_count(file_contents)  

    sorted_chars = get_char_list(char_dict)  
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for char_data in sorted_chars:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")

def letter_count(contents):
    dict = {}
    lowered_contents = contents.lower()
    for char in lowered_contents:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def get_char_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            char_list.append(new_dict)
          
    char_list.sort(key=sort_on, reverse=True)
    return char_list

if __name__ == "__main__":
    main()