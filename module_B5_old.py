def input_xo(message):
    k = input(message).lower()
    if len(k) != 2:
        print('input key and value')
        input_xo(message)
    if k[0] in ['a','b','c'] and k[1] in ['1','2','3']:
        if test[k] == '-':
            return k
        else:
            print('cell is not empty')
            input_xo(message)
    else:
        print('no such cell')
        input_xo(message)


test = {'a1':'-','b1':'-','c1':'-','a2':'-','b2':'-','c2':'-','a3':'-','b3':'-','c3':'-'}


print('  a b c \n1',*list(test.values())[0:3],'1\n2',*list(test.values())[3:6],'2\n3',*list(test.values())[6:9],'3\n  a b c\n')


def play_xo():
    global player
    try:
        if player == 'o':
            player = 'x'
        else:
            player = 'o'
    except NameError:
        player = 'x'

    k = input_xo(f'{player}: ')
    test[k] = player
    print('  a b c \n1', *list(test.values())[0:3], '1\n2', *list(test.values())[3:6], '2\n3',*list(test.values())[6:9], '3\n  a b c\n')
    if '-' not in test.values():
        print('Finish')
    else:
        play_xo()

play_xo()
