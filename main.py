
def words(file_content):
    return file_content.split()

def dico(file_content):
    histo = {}
    for word in words(file_content):
        for c in word:
            if 'a' <= c <= 'z':
                if histo.get(c):
                    histo[c] += 1
                else:
                    histo[c] = 1
    return histo

def report(name, content):
    print(f"--- Begin report of {name} ---")
    print(f"{len(words(content))} words found in the document")
    histograme = dict(sorted(dico(content).items(), key=lambda x: x[0]))
    for c,time in histograme.items():
        print(f"The '{c}' character was found {time} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        report("books/frankenstein.txt", file_contents)

if '__name__ == __main__':
    main()
