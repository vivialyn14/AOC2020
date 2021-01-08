from helpers.utils import get_puzzle_input

test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class GamesConsole:
    def __init__(self):
        self.hello = "Hello"
    def accumulator(self):