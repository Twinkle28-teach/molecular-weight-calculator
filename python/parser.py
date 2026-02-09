from elements import atomic_weights

def parse_formula(formula):
    stack = [0]  # base level
    i = 0
    
    while i < len(formula):

        # Opening bracket
        if formula[i] in '([':
            stack.append(0)
            i += 1

        # Closing bracket
        elif formula[i] in ')]':
            i += 1
            number = ""

            while i < len(formula) and formula[i].isdigit():
                number += formula[i]
                i += 1

            multiplier = int(number) if number else 1
            group_weight = stack.pop()
            stack[-1] += group_weight * multiplier

        # Element parsing
        else:
            if i + 1 < len(formula) and formula[i:i+2] in atomic_weights:
                element = formula[i:i+2]
                i += 2
            else:
                element = formula[i]
                i +=1

            number = ""

            while i < len(formula) and formula[i].isdigit():
                number += formula[i]
                i += 1
            
            count = int(number) if number else 1
            if element not in atomic_weights:
                raise ValueError(f"Unknown element symbol: {element}")
            stack[-1] += atomic_weights[element]* count

    return stack[0]



def calculate_molecular_weight(formula):
    # Handle hydrate(.)
    if "." in formula:
        parts = formula.split(".")
        total = 0

        for part in parts:
            i = 0
            num = ""
            while i < len(part) and part[i].isdigit():
                num += part[i]
                i += 1
            multiplier = int(num) if num else 1

            compound = part[i:]
            total += multiplier*parse_formula(compound)
        return total
    else:
        return parse_formula(formula)
    
    