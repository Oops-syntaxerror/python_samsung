'''Check if it is cloudy or sunny. If sunny and hot, then go out with jacket. If only sunny the go out as you wish.
If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy then check if it is lightning.
If it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water. If it is only cloudy and lightning then do not go out.'''

cloudy = input("Enter 'yes' if it is cloudy:")
sunny = input("Enter 'yes' if it is sunny:")

if ( sunny == 'yes' and cloudy == 'yes'):
    print('Go out with a jacket.')
elif ( sunny == 'yes' ):
    print('Go as you wish!!')

if ( cloudy == 'yes'):
    rain = input("Enter 'yes' if it is raining:")
    
    if( rain == 'yes'):
        light = input("Enter 'yes' if its is lighting:")
        if ( light == 'yes'):
            print('Do not go out.')
        else:
            print('Go out with an Umbrella or play in water')
    else:
        light = input("Enter 'yes' if its is lighting:")
        print('Do not go out.')