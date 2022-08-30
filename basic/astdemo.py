import ast
syntaxTree = ast.parse("""
temp = 20
for x in range(temp):
    print(x)
    
""")

print(ast.dump(syntaxTree))