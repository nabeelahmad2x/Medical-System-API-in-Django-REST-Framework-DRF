import bcrypt


def set_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password

def check_password(self, password):
    return bcrypt.checkpw(password.encode(), self.password)