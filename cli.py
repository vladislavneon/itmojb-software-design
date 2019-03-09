from src.interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter()
    while True:
        command_text = input().strip()
        stream = interpreter.execute(command_text)
        if interpreter.state.should_exit:
            print('bye')
            break
        print(stream, end='')
