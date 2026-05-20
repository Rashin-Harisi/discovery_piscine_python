#!/usr/bin/env python3

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}


def find_the_readheads(data):
    return (list(filter(lambda key  : data[key] == 'red', data)))

print(find_the_readheads(dupont_family))