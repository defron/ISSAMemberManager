__author__ = 'Defron'

from ISSA.MemberMailer.Objects import Member


class HelloWorld():
    def print_msg(self):
        if(True):
            print('hello world')
        else:
            # Impossible
            raise Exception('This is impossible!!!!')

if (__name__ == '__main__'):
    print_hello = HelloWorld()
    print_hello.print_msg()
    billy = Member()
    billy.first_name = "Billy"
    billy.last_name = "Bob Thorton"
    billy.email = "billy@bobthorton.com"
    billy.phone = "8947546789"
    billy.grad_year = "2015"
    print(billy)