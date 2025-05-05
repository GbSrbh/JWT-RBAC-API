import bcrypt

class PasswordHandler:
    def __init__(self, salt_rounds: int = 12):
        self.salt_rounds = salt_rounds

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt(rounds=self.salt_rounds)
        return bcrypt.hashpw(password.encode(), salt).decode()

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
