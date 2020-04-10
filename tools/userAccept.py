import login


def userAccept(input):
    while True:
        try:
            validation = input('? is this correct: %s [y/n]' % input)
        except ValueError:
            print('selection rejected, return to profile selection')
            login.verifySelection()
        else:
            print('%s confirmed...' % profile)
            break
