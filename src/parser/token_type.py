class Token:
    def __init__(self, content, token_type):
        self.content = content
        self.token_type = token_type

    def needs_substy(self):
        if self.token_type == 'quoted':
            return False
        return True