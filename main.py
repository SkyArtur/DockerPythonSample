from controller import ControllerPerson

if __name__ == '__main__':
    program = ControllerPerson()
    while program.execute:
        program.opening()
        program.menu()
