import lark
text = open("18.in").read()

@lark.v_args(inline=True)
class Calc(lark.Transformer):
	from operator import add, mul
	number = int
	start = staticmethod(lambda *a: sum(a))

# Part 1
print(lark.Lark(r"""
start: (expr "\n")* expr "\n"?
?atom: /\d+/ -> number
     | "(" expr ")"
?expr: atom
     | expr " + " atom -> add
     | expr " * " atom -> mul
""", parser="lalr", transformer=Calc()).parse(text))

# Part 2
print(lark.Lark(r"""
start: (expr "\n")* expr "\n"?
?atom: /\d+/ -> number
     | "(" expr ")"
?exp1: atom
     | exp1 " + " atom -> add
?expr: exp1
     | expr " * " exp1 -> mul
""", parser="lalr", transformer=Calc()).parse(text))
