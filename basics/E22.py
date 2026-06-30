# Character Encoding!!!!
import sys # Imports Python's built-in sys module
script, input_encoding, error = sys.argv # sys.argv stores command-line arguments
# The first element of sys.argv is always the script name
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line: # This LOC is asking did readline() actually read something?
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() #strip() removes whitespace from both ends.
    raw_bytes = next_lang.encode(encoding, errors=errors) # encode() ---> bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # bytes ---> decode() ---> Unicode string

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8") # encoding="utf-8" tells Python how to interpret the bytes inside the file

main(languages, input_encoding, error) # Starts everything


# When you give an encoding that doesn't exist, you will get an error that the encoding doesn't exist