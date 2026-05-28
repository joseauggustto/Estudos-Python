#Vamos lá...
 
from sys import is_stack_trampoline_active
distance_mi = 10 
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == 0:
    print("False")

elif distance_mi <= 1:

    if is_raining == True:
        print("False")
    elif is_raining == False:
        print("True")

# Média distância

if distance_mi > 1 and distance_mi <= 6: 
    if is_raining == True and has_bike == False:
        print("False")
    elif is_raining == False and has_bike == False:
        print("False")
    elif has_bike == True and is_raining == False:
        print("True")
    
if distance_mi > 6:
    if has_ride_share_app == True:
        print("True")
    elif has_car == True:
        print("True")
    else:
        print("False")