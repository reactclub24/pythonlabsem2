# Write a function that accepts a string as an argument and
# returns the no. of vowels that the string contains.
# Another function to return number of consonants.
def main():
    str_in = input('Enter a string ')
    str_lower = str_in.lower()
    vow = 'aeiou'
    num = vowels(str_lower, vow)
    print('Number of vowels in a given string is', num)
    num = consonants(str_lower, vow)
    print('Number of consonants in a given string is', num)


# defining a function to find number of vowels in a string
def vowels(string, vow):
    count = 0
    for x in string:
        if x in vow:
            count = count + 1
    return count


# defining a function to find number of consonants in a string
def consonants(string, vow):
    count = 0
    for x in string:
        if x not in vow and x != ' ':
            count = count + 1
    return count


# calling main method
main()
