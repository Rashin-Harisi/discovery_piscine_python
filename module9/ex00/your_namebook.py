#!/usr/bin/env python3

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

def array_of_names(persons):
    arr = []

    for first, last in persons.items():
        fullname = first.capitalize() + " " + last.capitalize()
        arr.append(fullname)

    return arr

print(array_of_names(persons))

