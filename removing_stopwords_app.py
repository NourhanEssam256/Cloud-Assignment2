# importing the needed libraries
import re
from collections import Counter
from nltk.corpus import stopwords


# Read the contents of the "random_paragraphs.txt" file
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Remove stop words from the text
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = re.findall(r"\b\w+\b", text.lower())
    return [word for word in words if word not in stop_words]


# Count the frequency of each word
def count_word_frequency(words):
    return Counter(words)


# Display word frequency count to the console
def display_word_frequency(word_frequency):
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")


# Main function
def main():
    file_path = "random_paragraphs.txt"
    text = read_file(file_path)
    words = remove_stopwords(text)
    word_frequency = count_word_frequency(words)
    print("The frequency of words after removing stopwords : ")
    display_word_frequency(word_frequency)


if __name__ == "__main__":
    main()
