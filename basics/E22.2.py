# Reversing the script from E22.py to perform only Decoding!

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line: # This LOC is asking did readline() actually read something?
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    raw_bytes = line.strip()
    raw_bytes = raw_bytes[:-2] # removing the last 2 bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # bytes ---> decode() ---> Unicode string

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", "rb") # "rb" tells Python to read binary

main(languages, input_encoding, error)    