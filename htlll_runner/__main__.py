import sys
from ply.lex import lex

tokens = (
    'COMMENT',
    'KERNEL_START',
    'KERNEL_END',
    'IMPORT_START',
    'IMPORT_END',
    'MODULE',
    'ENV_VARS_START',
    'ENV_VARS_END',
    'VAR',
    'INPUT_START',
    'INPUT_END',
    'PROMPT',
    'PY_START',
    'PY_END',
    'FUNCTION',
    'VALUE',
    'SCRIPT_START',
    'SCRIPT_END',
    'BASE_TAG',
    'OPTION',
    'ARGS',
    'LITERAL'
)

# Tokens
t_COMMENT = r'\#.*'
t_KERNEL_START = r'<kernel>'
t_KERNEL_END = r'</kernel>'
t_IMPORT_START = r'<import>'
t_IMPORT_END = r'</import>'
t_MODULE = r'<module>'
t_ENV_VARS_START = r'<envVars>'
t_ENV_VARS_END = r'</envVars>'
t_VAR = r'<var\s+name=".*?">'
t_INPUT_START = r'<input>'
t_INPUT_END = r'</input>'
t_PROMPT = r'<prompt>'
t_PY_START = r'<py>'
t_PY_END = r'</py>'
t_FUNCTION = r'<function>'
t_VALUE = r'<value\s+name=".*?"/>'
t_SCRIPT_START = r'<script>'
t_SCRIPT_END = r'</script>'
t_BASE_TAG = r'<(\w+)>'
t_OPTION = r'<option>'
t_ARGS = r'<args>'
t_LITERAL = r'<literal>'
lexer = lex()

def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else None
    if file_name is None:
        raise ValueError('No file name provided')
    with open(file_name, 'r') as f:
        script = f.read()
    # I need to learn to tokenize, parse the tokens to get commands, and then run the commands


if __name__ == '__main__':
    main(sys.argv[1])