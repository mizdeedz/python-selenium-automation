"""
HW5
4** Amazon interview question
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
"""


def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    for l in string:  # 0(n)
        if string.count(l) == 1:  # 0(n)
            return l
    return ""
    # 0(n) * 0(n) = 0(n^2)

print(unique_letter('llajhgjvv'))


def unique_letter_optimal(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    d = {}
    # google
    for l in string:  # 0(n)
        if l not in d:
            d[l] = 1  # d = {'g' : 1, 'o' : 1}, first iter
        else:
            d[l] += 1 # d = {'g' : 1, 'o' : 2}, 2nd iter, etc.

    for k, v in d.items():  # 0(n)
        if v == 1:
            return k

    return ""

print(unique_letter('llajhgjvv'))