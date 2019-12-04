#!/usr/bin/python3

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    gotresp = requests.get(AOIF_BOOKS)

    got_dj = gotresp.json()

    pprint.pprint (got_dj)

if __name__ == "__main__":
    main()

#Part(2)
def main():
    gotresp = requests.get(AOIF_BOOKS)

    got_dj = gotresp.json()

    for singlebook in got_dj:
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"|tAPI URL -> {singlebook['url']}\n")
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f".tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

if __name__ == "__main__":
    main()

#Part(3)
import requests
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"
def main():
    got_charToLookup = input("What is the name of the character we should lookup? " )

    gotresp = requests.get(AOIF_CHAR + "?name =" + got_charToLookup)

    got_dj = gotresp.json()

    print(f"The character {got_charToLookup} has the URL: {got_dj[0]['url']}")

if __name__ == "__main__":
    main()

    

