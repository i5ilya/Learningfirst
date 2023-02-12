a, *_, c = 'abcd'

def myprint(*args, **kwargs):
    print(f'Got some key el {kwargs}')
    for arg in args:
        print(arg)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if __name__ == '__main__':
    # print(f'{a=}')
    # print(f'{b=}')
    # print(f'{c=}')
    #print(*[1, 2, 3])
    #exemple(1,2, c=3, d=4)
    myprint(sobak = 'barabak')
    #print(*thisdict)