# Check if it is cloudy or sunny. If sunny and hot, then go out with jacket. If only sunny the go out as you wish.If it is cloudy, then check if it is raining. IF it is only cloudy then go out as you wish. IF rainy go out with umbrella.

sunny = input("Enter 'yes' if it is sunny:")
cloudy = input("Enter 'yes' if it is cloudy:")

if ( sunny == 'yes' and cloudy == 'yes'):
    print('Go out with a Jacket.')
elif ( sunny == 'yes'):
    print('Go out as you wish.')
elif ( cloudy == 'yes'):
    rain = input("Enter 'yes' if it is raining:")
    print('Go out with an Umbrella.')
if(cloudy == 'yes'):
    print('Go out as you wish')