import string
def is_pangram(s):
    sentence = s
    # Convert the sentence to lowercase for case insensitivity
    sentence = sentence.lower()
    
    # Create a set of letters found in the sentence
    letters_found = set(filter(lambda x: x.isalpha(), sentence))
    
    # Check if the set of letters found is equal to the set of all lowercase letters
    return set(string.ascii_lowercase) == letters_found

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
print(is_pangram("This isn't a pangram!"))
