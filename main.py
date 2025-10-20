from stats import count_words, get_book_text, count_characters, create_dict_of_chars, sort_on
import sys

if len(sys.argv)<2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)



    
def main():
    print(get_book_text(sys.argv[1]))

#placeholder for main()

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}") #made f-string for changeability
print("----------- Word Count ----------")


count_words("books/frankenstein.txt")

print("Found "+str(count_words(sys.argv[1]))+" total words")

character_dictionary = count_characters(sys.argv[1])

print("-------- Character Count --------")  #printed characted dict here before


character_count_sorted = create_dict_of_chars(character_dictionary) 

for pair in character_count_sorted:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")



print("============= END ===============")
 
