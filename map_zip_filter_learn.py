# zip part
s = 'a', 'b', 'c'
t = (10, 20, 30)
z = 1, 2, 3
new_dic = (zip(s, t, z))
# zip part end

# filter() part

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_even(number):
    if number % 2 == 0:
        return True
    return False


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


check_lambda = lambda x: x % 2 == 0

x2 = lambda x: x * 2


def x2(x):
    return x * 2


if __name__ == '__main__':
    numbers_even = list(filter(check_even, numbers))
    letters_vowel = list(filter(filter_vowels, letters))
    print(numbers_even)
    print(letters_vowel)
    number_even_lambda = list(filter(check_lambda, numbers))
    print(number_even_lambda)
    print(list(map(x2, numbers)))
