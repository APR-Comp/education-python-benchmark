from fuzzingbook.Grammars import Grammar
from fuzzingbook.Grammars import convert_ebnf_grammar
from fuzzingbook.Grammars import is_valid_grammar
from reference import contains_unique_day
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
max_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


input_grammar: Grammar = convert_ebnf_grammar({
    "<start>": ["(\"<month>\",[ <date> (,<date>)+ ])"],
    "<date>": ["(\"<month>\",<integer>)"],
    "<integer>": ["<nzdigit><digit>*"],
    "<nzdigit>": [str(x) for x in range(1, 10)],
    "<digit>": [str(x) for x in range(10)],
    "<month>": months
})

assert is_valid_grammar(input_grammar)


def entrypoint(s: str):
    if s is None:
        return []

    x, l = eval(s)
    l = list(map(lambda x: (x[0], x[1] % max_days[x[0]]), l))

    return ('"'+x+'"', l, contains_unique_day(x, l))
