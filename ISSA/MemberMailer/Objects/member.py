__author__ = 'Defron'

class Member():
    first_name = ""
    last_name = ""
    email = ""
    phone = ""
    grad_year = ""

    def is_current_member(self):
        pass

    def __str__(self):
        return self.first_name + " " + self.last_name