# Contruindo um score de personagem RPG. Vamos lá...

full_dot = '●'
empty_dot = '○'

def create_character(name, power, intelligence, charisma):

    if not isinstance(name, str):
        return "The character name should be a string"
    
    elif name.strip() == "":
        return "The character should have a name"
    
    elif len(name) > 10:
        return "The character name is too long"
    
    elif " " in name:
        return "The character name should not contain spaces"
    
    elif not (isinstance(power, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"
    
    elif power < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    elif power > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    elif (power + intelligence + charisma) != 7:
        return "The character should start with 7 points"
    # -----------
      
    p_bolinhas = '●' * power + '○' * (10 - power)
    i_bolinhas = '●' * intelligence + '○' * (10 - intelligence)
    c_bolinhas = '●' * charisma + '○' * (10 - charisma)

    return (f"{name}\n" 
            f"STR {p_bolinhas}\n" 
            f"INT {i_bolinhas}\n" 
            f"CHA {c_bolinhas}\n")
    

personagem = create_character("ren", 4, 2 ,1)
print(personagem)