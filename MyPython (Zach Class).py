#!/usr/bin/python3

def main():
## create an empty list
    mylist = []

## open a SLOT at the END of the list to ADD the value
    mylist.append("monday morning")

    mylist.append("tuesday")

    mylist.append("wednesday")

    mylist.append("thursday")

    print(mylist)

## print monday on the screen
    print(mylist[0])

    studiomovies = {}

    ## we want to create the KEY pixar and map to a value
    studiomovies["pixar"] = "toystory"

    studiomovies["universal"] = "jaws"

    studiomovies["paramount"] = "raiders of lost ark"

    # map studiomoviespixar to a LIST that has TWO items in it
    studiomovies["pixar"] = ["toy story", "up"]

    print(studiomovies["pixar"][1])

if __name__ == "__main__":
    main()


