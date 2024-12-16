from collections import defaultdict
def main():
    with open("./books/frankenstein.txt") as f:
        content = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count = count_chr(content)
        for k,v in count.items():
            print("the character {} appeared {} times".format(k,v))

        print("--- End report ---")
        #print(content)
def count_words(content):
    words = content.split()
    return str(len(words))
def count_chr(content):
    count = defaultdict(int)
    for c in content:
        count[c.lower()] = count[c.lower()] + 1
    return count

if __name__ == "__main__":
    print("this is main function")
    main()
