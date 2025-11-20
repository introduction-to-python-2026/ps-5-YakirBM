def split_before_uppercases(formula: str):
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


def split_at_digit(formula: str):
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


def count_atoms_in_molecule(molecular_formula: str):
    """מקבל נוסחה מולקולרית (string) ומחזיר מילון של ספירת אטומים.
    לדוגמה: 'H2O' → {'H': 2, 'O': 1}
    """
    counts = {}

    # פיצול לרכיבי אטום/מספר לפי אותיות גדולות
    for atom_chunk in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom_chunk)
        counts[atom_name] = counts.get(atom_name, 0) + atom_count

    return counts


def parse_chemical_reaction(reaction_equation: str):
    """מקבל משוואת תגובה (string) ומחזיר מגיבים ותוצרים כ־lists.
    דוגמה: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])
    """
    reaction_equation = reaction_equation.replace(" ", "")  # מסיר רווחים לפישוט
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """מקבל רשימת נוסחאות מולקולריות ומחזיר רשימת מילונים של ספירת אטומים.
    דוגמה: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]
    """
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
