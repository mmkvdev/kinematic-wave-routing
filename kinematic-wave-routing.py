option = ''
section = input('Select an option: (a) Rectangular Section (b) Trapezoidal Section ')

if section == 'a':
	rectangular_bottom_width = int(input('Enter the bottom width (in m) '))
else:
	trapezoidal_bottom_width = int(input('Enter the bottom width (in m) '))
	trapezoidal_side_slope = int(input('Enter the slide slope ((in degrees with vertical)) '))
	print(trapezoidal_bottom_width,trapezoidal_side_slope)

longitudinal_channel_slope = input('Enter the longitudinal slope of the channel ')
simulation_channel_length = int(input('Enter the length (L) of the channel (in m) '))

dx = 0
dt = 0
dx = int(input('Enter the value of dx: '))
dt = int(input('Enter the value of dt: '))
