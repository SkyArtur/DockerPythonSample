from controller import ControllerPerson

if __name__ == '__main__':
    program = ControllerPerson()
    program.opening()
    while program.execute:
        program.menu()
