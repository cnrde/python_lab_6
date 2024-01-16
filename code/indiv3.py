if __name__ == '__main__':
    print("введите предложение: ")
    print(''.join(char for i, char in enumerate(
        input()) if not (char == 'о' and i % 2 == 0)))