def main():
    print("Hello from src!")
    with open(r"C:\Users\Paul\Documents\Python Projects\mathe_freunde\wordlist.txt") as f:
        print(f"the official wordlist countains {len([x for x in f])} - 5 letter words!")


if __name__ == "__main__":
    main()
