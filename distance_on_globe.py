import math

# Taking input from user in degrees
print("Enter lat/long of starting point (in degrees): ")
lat_1 = float(input('Lat: '))
long_1 = float(input('Long: '))
print("")
print("Enter lat/long of ending point (in degrees): ")
lat_2 = float(input('Lat: '))
long_2 = float(input('Long: '))

# Convert degrees into radians
lat_1 = lat_1 * math.pi / 180
lat_2 = lat_2 * math.pi / 180
long_1 = long_1 * math.pi / 180
long_2 = long_2 * math.pi / 180

# define variables
R = 3958.8  # radius of earth in miles
a_1 = (lat_2 - lat_1) / 2
a_2 = (long_2 - long_1) / 2

# Formula and final calculations
A = ((math.sin(a_1)) ** 2) + math.cos(lat_1) * math.cos(lat_2) * ((math.sin(a_2)) ** 2)
d = 2 * R * math.atan2(math.sqrt(A), math.sqrt(1 - A))

# Show the results
print(f"Distance is {d} mi.")
