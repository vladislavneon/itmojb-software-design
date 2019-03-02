class NoSuchVariableError(ValueError):
    def __init__(self, message):
        super().__init__(f'Environment error: {message}')

class Environment:
    def __init__(self):
        self.variables = {}

    def get_var(self, var_name):
        if var_name not in self.variables:
            raise NoSuchVariableError(f'no variable {var_name}')
        return self.variables[var_name]

    def set_var(self, var_name, value):
        self.variables[var_name] = value
