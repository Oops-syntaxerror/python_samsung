# Read 2 string input from user, whether it is raining and lightning, then do not go out. If it is only raining then either go out with umbrella or play in water

rain = input("Enter 'yes' if it is raining:")

light = input("Enter 'yes' if it lighting:")

if ( rain == 'yes' and light == 'yes' ):
    print('Do not go out')
if ( rain == 'yes' ):
    print('Go out with an Umberella or play in Water.')