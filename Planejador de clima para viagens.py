#Vamos lá...

distance_mi = 1
is_raining = True
has_bike = True 
has_car = False 
has_ride_share_app = True 

if distance_mi <= 3 and is_raining == False:
    print('Vai de Bike')

elif distance_mi <= 3 and is_raining == True:
    print('Use um app de carro')

else:
    print('Não vai')

# -------------------------


if distance_mi > 1 and distance_mi <= 6 and is_raining == True and has_bike == False: #18
    print(False)

if distance_mi > 1 and distance_mi <= 6 and is_raining == False and has_bike == False: #19
    print(False)

if distance_mi >1 and distance_mi <=6 and has_bike == True and is_raining == False: #20
    print(True)

if distance_mi > 6 and has_ride_share_app == True: #21
    print(True)

if distance_mi > 6 and has_car == True: #22
    print(True)

if distance_mi > 6 and has_car == False and has_ride_share_app == False: #23
    print(False)