import re
from json import loads


TOKEN_TYPES = {
    'WRITE': r'write',
    'READ': r'read',
    'IF': r'if',
    'IF_SO': r'if so',
    'SELECTOR': r'selector',
    'LOOP': r'loop',
    'UNTIL': r'until',
    'INT': r'int',
    'FLOAT': r'float',
    'CHAR': r'char',
    'STRING': r'"[^"]*"',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'NUMBER': r'\d+(\.\d+)?',
    'SEMICOLON': r';',
    'LEFT_PAREN': r'\(',
    'RIGHT_PAREN': r'\)',
    'LEFT_BRACE': r'{',
    'RIGHT_BRACE': r'}',
    'COMMA': r',',
    'OPERATOR': r'==|!=|<=|>=|<|>|[+\-*/%]',
    'ASSIGN': '='
}

def tokenize(code):
    tokens = []
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_TYPES.items())
    for match in re.finditer(token_regex, code):
        for name, value in match.groupdict().items():
            if value is not None:
                if name in ["STRING", "NUMBER"]:
                    value = name.lower()
                if name == "IDENTIFIER":
                    value = 'variable'
                tokens.append((name, value))
    return tokens

def load_first_follow():
    with open("first_follow.json", "r") as file:
        return loads(file.read())


def read_input_file(address):
    with open(address, 'r') as file:
        return file.read()


def find_row_index(first_follow, notTerminal_input):
    for index, notTerminal in enumerate(first_follow['Nonterminal']):
        if notTerminal == notTerminal_input:
            return index


def isTerminal(variable, first_follow):
    if variable in first_follow['Nonterminal']:
        return False
    return True


def match(variable, look_head):
    if variable == "string":
        return True

    if variable != look_head:
        print(variable, look_head)
        raise f"not matched look head and variable -> {variable}, {look_head}"


def find_transition(variable, terminal, first_follow, stack):
    index = find_row_index(first_follow, variable)

    rule = first_follow[terminal][index]
    print(rule, terminal, variable)

    if rule == '':
        raise "can't parse method"
    else:
        rule = rule.split(" ")

        for r in rule[::-1]:
            if '->' in r:
                return stack
            if r != "":
                if r != "''":
                    stack.append(r.replace("->", ""))



def parser(tokens, first_follow):
    stack = ['$', 'S']
    head = 0

    while stack:
        variable = stack.pop()
        if variable == "$":
            print("Parse successfully!")
            break

        terminal = tokens[head][1].lower()

        if isTerminal(variable, first_follow):
            if variable not in ['main', 'so', 'variable', 'OUTPUT', 'number']:
                match(variable, terminal)
            head += 1
        else:
            if tokens[head][0] == "STRING":
                terminal = 'string'
            if tokens[head][0] == "IDENTIFIER":
                terminal = 'number'
                if variable in ["STATEMENT", "MATH"]:
                    terminal = "variable"
            find_transition(variable, terminal, first_follow, stack)



def main():
    input_code = read_input_file("source")
    first_follow = load_first_follow()
    tokens = tokenize(input_code)
    print(tokens)
    parser(tokens, first_follow)


if __name__ == "__main__":
    main()
