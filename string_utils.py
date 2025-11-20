def split_before_uppercases(formula):
    """
    פיצול לפני כל אות גדולה, כשהאות הגדולה נשארת בתחילת המקטע.
    דוגמאות:
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6B" -> ["C6", "H12", "O6", "B"]
      "water"    -> ["water"]
      ""         -> []
    """
    if formula == "":
        return []

    parts = []
    current = ""

    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch

    if current:
        parts.append(current)
    return parts

def split_at_digit(formula):
    """
    פיצול במפגש הספרה הראשונה:
    מחזיר (prefix, count) כאשר:
      - prefix: החלק לפני הספרה הראשונה (יכול להיות גם "" אם מתחיל בספרה)
      - count: כל רצף הספרות מהספרה הראשונה ועד הסוף כ-int
    אם אין ספרות כלל — מחזיר (formula, 1)
    דוגמאות:
      "H22"   -> ("H", 22)
      "NaCl"  -> ("NaCl", 1)
      "123"   -> ("", 123)
    """
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1



def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    counts = {}
   
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        counts[atom_name] = counts.get(atom_name, 0) + atom_count
    # Step 3: Return the completed dictionary
    return counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
