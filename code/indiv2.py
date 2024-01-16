if __name__ == '__main__':
    line = input("введите предложение: ")

    for ind in range(len(line)-1):
        if line[ind] == line[ind+1]:
            print(ind+1, ind+2)
            break
    else:
        print('Таких символов нет')