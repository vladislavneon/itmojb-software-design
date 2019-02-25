class Environment:
    def __init__(self):
        self.variables = {}

    def get_var(self, var_name):
        if var_name not in self.variables:
            raise ValueError(f'no variable {var_name}')
        return self.variables[var_name]

    def set_var(self, var_name, value):
        self.variables[var_name] = value
