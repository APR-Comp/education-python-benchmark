from reference import sort_age
from copy import copy

from fuzzingbook.Grammars import is_valid_grammar
from fuzzingbook.Grammars import convert_ebnf_grammar
from fuzzingbook.Grammars import Grammar

input_grammar: Grammar = convert_ebnf_grammar({
    "<start>": ["[<entry>(,<entry>)*]"],
    "<entry>": ["(<gender>,<age>)"],
    "<age>": ["<nzdigit><digit>?"],
    "<gender>": ["\"F\"", "\"M\""],
    "<nzdigit>":[str(x) for x in range(1,10)], 
    "<digit>": [str(x) for x in range(10)]
})

assert is_valid_grammar(input_grammar)

def entrypoint(s: str):
    if s is None:
        return -1

    l = eval(s)
    l = list(set(map(lambda x: (x[0],int(x[1]) % 40) , l)))

    return (copy(l), sort_age(l))


