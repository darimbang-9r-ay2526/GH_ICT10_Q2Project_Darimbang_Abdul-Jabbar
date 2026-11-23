# Project
from pyscript import display, document

def search(e):
    document.getElementById('display').innerHTML = " "
    nickname = document.getElementById('country').value

    display(nickname, target="display")



elements = {"H":  ("Hydrogen",    1,  1.008),
            "He": ("Helium",      2,  4.0026),
            "C":  ("Carbon",      6,  12.011),
            "N":  ("Nitrogen",    7,  14.007),
            "O":  ("Oxygen",      8,  15.999),
            "F":  ("Fluorine",    9,  18.998),
            "Ne": ("Neon",       10,  20.180),
            "P":  ("Phosphorus", 15,  30.974),
            "S":  ("Sulfur",     16,  32.06),
            "Cl": ("Chlorine",   17,  35.45),
            "Ar": ("Argon",      18,  39.948),
            "Se": ("Selenium",   34,  78.971),
            "Br": ("Bromine",    35,  79.904),
            "Kr": ("Krypton",    36,  83.798),
            "I":  ("Iodine",     53,  126.90),
            "Xe": ("Xenon",      54,  131.29),
            "Rn": ("Radon",      86,  222)
                                            }
def element_finder(e):
    document.getElementById('result').innerHTML = " "

    elementresults = document.getElementById('Non-Metal Element').value.strip().title()


    result = elements.get(elementresults,("The Element Is not in the system.","-", "-"))

    document.getElementById('result').innerHTML = f"""
    Symbol:{elementresults}<br>
    Element: {result[0]}<br>
    Atomic Number: {result[1]}<br>
    Atomic Mass:{result[2]}
    """

def members(e):

    document.getElementById('output').innerHTML = ''
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    full_name= first_name + last_name


    Grade7 = {'Austin Maneja', 'Anton Dela Rosa', 'Abdul Ibrahim', 'Ranbhir Sekhon'}
    Grade8 = {'Hans Ukwatte', 'Iohann Villanueva', 'Mani Tubo', 'Sinko Kaba'}
    Grade9 = {'Zhaimer Mamacotao', 'Zeeshan Dalidig', 'Arkin Estacio', 'Ben Bocarie'}
    Grade10 = {'Khail Resurreccion', 'Sebastian Uclaray', 'Raver Estacio', 'Zangief Briones'}
    members = (Grade7| Grade8 | Grade9 | Grade10)
    members.add(full_name)

    display(f'List of members {members} amount of members {len(members)}', target='output')

