__author__ = 'Defron'


class HelloWorld():
    def print_msg(self):
        if(True):
            print('hello world')
        else:
            # Impossible
            raise Exception('This is impossible!!!!')


if (__name__ == '__main__'):
    printhello = HelloWorld()
    printhello.print_msg()

