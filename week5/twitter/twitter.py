def main():
    twitter_test()

def twitter_test(sentes):
    sentence =[]
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    print("Output:", end='')
    for char in sentes:
        if char in vowels:
            pass
        else:
            sentence.append(char)
    return (str("".join(sentence)))



if __name__ == '__main__':
    twitter_test()