# here go again 

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, smart, charisma):

    # Nome personagem

    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    
    # Estatísticas Personagem

    if not isinstance(strength, int) or not isinstance(smart, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    elif strength <= 0 or smart <= 0 or charisma <= 0:
        return "All stats should be no less than 1"
    
    elif strength > 4 or smart > 4 or charisma > 4:
        return "All stats should be no more than 4"

    elif strength + smart + charisma != 7:
        return "The character should start with 7 points"
    
    STR = full_dot * strength + empty_dot * (10 - strength)
    SMART = full_dot * smart + empty_dot * (10 - smart)
    CHA = full_dot * charisma + empty_dot * (10 - charisma)
    
    return f"{name}\nSTR {STR}\nINT {SMART}\nCHA {CHA}"

print(create_character('ren', 4, 2, 1))



    

