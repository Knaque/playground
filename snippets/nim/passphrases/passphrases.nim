import strutils, unicode

const alphabet = "abcdefghijklmnopqrstuvwxyz"
const numbers = "0123456789"

proc playPass*(s: string, n: int): string =
    for c in s:
        if c.toLowerAscii() in alphabet:
            var new_letter = alphabet.find(c.toLowerAscii()) + n
            if new_letter >= alphabet.len: new_letter -= alphabet.len
            result = result & alphabet[new_letter]
        elif $c in numbers: result = result & $(9 - parseInt($c))
        else: result = result & c
    for i, c in result:
        if c in alphabet:
            if i mod 2 == 0: result[i] = result[i].toUpperAscii
            else: result[i] = result[i].toLowerAscii
    result = result.reversed()

echo playPass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)