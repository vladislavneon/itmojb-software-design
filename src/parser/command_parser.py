import shlex
import re
from src.parser.environment import Environment
from src.parser.token_type import Token
from src.command.external import ExternalCommand


class CommandParser:
    def __init__(self):
        self.env = Environment()
        self.commands = {}
        self.external_command = ExternalCommand

    def add_command(self, command_name, command_class):
        """
        Adds `command_class` to parser instance and bind it with `command_name`
        :param command_name: str, name which be used to call the command in the interpreter
        :param command_class: ShellCommand, class-object containing command implementation
        """
        self.commands[command_name] = command_class

    def build_command(self, command_name, command_args):
        if command_name in self.commands:
            return self.commands[command_name](*command_args)
        else:
            return self.external_command(command_name, *command_args)

    def tokenize(self, command_text):
        tokens = shlex.shlex(command_text)
        tokens.wordchars += '$_-./'
        token_items = []
        for token in tokens:
            if token[0] == '\'':
                token_items.append(Token(token[1:-1], 'quoted'))
            elif token[0] == '"':
                token_items.append(Token(token[1:-1], 'd_quoted'))
            else:
                token_items.append(Token(token, 'plain'))
        return token_items

    def substitute(self, token):
        while True:
            var = re.search(r'\$\w+', token)
            if not var:
                break
            var = var.group(0)[1:]
            var_value = self.env.get_var(var)
            token = token.replace('$' + var, var_value, 1)
        return token

    def check_assignment(self, command_text, tokens):
        if len(tokens) != 3:
            return False
        if tokens[1].content != '=':
            return False
        if not re.fullmatch(r'\w+', tokens[0].content):
            return False
        if not re.match(r'\w+=\S', command_text):
            return False
        var_name = tokens[0].content
        var_value = tokens[2].content
        self.env.set_var(var_name, var_value)
        return True

    def parse(self, command_text):
        """
        Parses string `command_text` returning a sequence of commands
        :param command_text: str, line entered by a user
        :return: list[ShellCommand], list of commands to execute via pipeline
        """
        tokens = self.tokenize(command_text)
        for token in tokens:
            if token.needs_substy():
                token.content = self.substitute(token.content)
        if self.check_assignment(command_text, tokens):
            return []
        commands = []
        command_name_flag = True
        cur_command_name = ''
        cur_command_args = []
        for token in tokens:
            if token.content == '|':
                commands.append(self.build_command(cur_command_name, cur_command_args))
                command_name_flag = True
                cur_command_name = ''
                cur_command_args = []
            else:
                if command_name_flag:
                    cur_command_name = token.content
                    command_name_flag = False
                else:
                    cur_command_args.append(token.content)
        commands.append(self.build_command(cur_command_name, cur_command_args))

        return commands
