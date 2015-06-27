from ISSA.MemberMailer.Objects.member import Member


class Officer(Member):

    officer_position = ""
    board_year = ""
    org_email = ""
    current = None

    def is_current_officer(self):
        pass

    def __str__(self):
        return self.first_name + " " + self.last_name

    def create_officer(self):
        if self == Member:
            return self.officer_position
