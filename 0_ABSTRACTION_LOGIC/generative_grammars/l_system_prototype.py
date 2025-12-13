"""
TÍTULO: Protótipo de Sistema-L (Lindenmayer System)
DESCRIÇÃO: 
Motor lógico agnóstico para expansão de gramáticas gerativas.
Usa reescrita de strings para simular crescimento biológico ou arquitetura fractal.
"""

def expand_grammar(axiom, rules, iterations):
    current_string = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current_string:
            next_string += rules.get(char, char)
        current_string = next_string
    return current_string

# Exemplo: Algae Growth (A -> AB, B -> A)
axiom = "A"
rules = {"A": "AB", "B": "A"}
print(f"Gen 5: {expand_grammar(axiom, rules, 5)}")
