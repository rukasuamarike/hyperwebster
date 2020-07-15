import sys


def base(): # makes first digit list
    alpha = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for k in alpha:
        res.append(k)
    return res


def it(past): # adds next digit to past list
    alpha = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for i in past: # for chars in past
        for k in alpha: # for letters in alpha
            r = i + k
            res.append(r)
    return res


def web(chars):
    final = []
    for i in range(chars):
        if i == 0:
            current = base()
        else:
            current = it(final)
        final += current # combine lists
    return final


def save_file(file, content): # saves the array to a txt file
    with open(file, 'a') as f:
        for i in range(len(content)):
            f.write(content[i]+", ")
            if i%25 == 0:
                f.write("{}\n".format(content[i]))
        f.close()


def main():
    length = input("maximum word length:")
    k = web(length)
    k.sort()
    k = list(dict.fromkeys(k))
    savefile = input("[save file] filename:")
    save_file(savefile, k)
    print(k)


if __name__ == '__main__':
    main()
