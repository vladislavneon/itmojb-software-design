class NoSuchVariableError(ValueError):
    def __init__(self, message):
        super().__init__(f'Environment error: {message}')

class Environment:
    def __init__(self):
        self.variables = {}

    def get_var(self, var_name):
        """
        Returns value of variable `var_name` in the environment
        :param var_name: str, variable name
        :return: str, variable value
        :raises: NoSuchVariableError
        """
        if var_name not in self.variables:
            raise NoSuchVariableError(f'no variable {var_name}')
        return self.variables[var_name]

    def set_var(self, var_name, value):
        """
        Assigns value `value` to variable `var_name` in the environment
        :param var_name: str, variable name
        :param value: str, variable value
        """
        self.variables[var_name] = value
