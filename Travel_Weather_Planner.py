distance_mi = 5
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi == False:
    print("False")
elif distance_mi <= 1:
    if(is_raining == False):
        print("True")
    else:
        print("False")
elif distance_mi >= 1 and distance_mi <= 6:
    if(has_bike and (is_raining == False)):
        print("True")
    else:
        print("False")
elif has_ride_share_app:
    print("True")
elif has_car:
    print("True")
else:
    print("False")