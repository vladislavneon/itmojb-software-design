from enum import Enum


class TokenType(Enum):
    QUOTED = 1
    DOUBLE_QUOTED = 2
    PLAIN = 3

class Token:
    def __init__(self, content, token_type):
        self.content = content
        self.token_type = token_type

    def needs_substy(self):
        if self.token_type == TokenType.QUOTED:
            return False
        return True