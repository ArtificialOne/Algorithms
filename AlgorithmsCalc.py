def electric_calc():
    print("1. Calculate Voltage, Joules (Current * Resistance)")
    print("2. Calculate Resistance, Ohms (Voltage / Current)")
    print("3. Calculate Current, Amps (Voltage / Resistance)")
    print("4. Calculate Wattage (Voltage * Current)")
    print("5. Calculate Milliamps (Amps * 1000)")
    print("6. Exit Program")
    number = (input("> "))

    if (number == "1"):
        print("\n- Identifying Voltage -\n")
        i = float(input("Current or Amps: "))
        res = float(input("Resistence: "))
        volt = i * res
        print(f"Voltage =  {volt:.2f}\n")

    elif(number == "2"):
        print("\n- Identifying Resistance - \n")
        volt = float(input("Voltage: "))
        i = float(input("Current or Amps: "))
        res = volt / i
        print(f"Resistance = {res:.2f}\n")

    elif(number == "3"):
        print("\n- Identifying Current -\n")
        volt = float(input("Voltage: "))
        res = float(input("Resistence: "))
        i = volt / res
        print(f"Current = {i:.2f}\n")

    elif(number == "4"):
        print("\n- Identifying Wattage -\n")
        volt = float(input("Voltage: "))
        i = float(input("Current or Amps: "))
        watt = volt * i
        print(f"Wattage = {watt:.2f}\n")

    elif(number == "5"):
        print("\n- Identifying Milliamps -\n")
        amps = float(input("Current or Amps: "))
        miliamp = amps * 1000
        print(f"Milliamps: {miliamp:.2f}\n")


def mass_calc():
    print("Which values are known?")
    print("1. Density & Volume")
    print("2. Force & Acceleration")
    print("3. Weight & Gravitational Acceleration")
    number = (input("> "))
    if (number == "1"):
        density = float(input("Enter Density: "))
        volume = float(input("Enter Volume: "))
        mass = density * volume
        print(f"Mass = {mass:.2f}\n")

def temperature():
    print("What do you want to convert?")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    number = (input("> "))
    if (number == "1"):
        f_temp = float(input("F. Temperature: "))
        c_temp = (f_temp * (9/5) + 32)
        print(f"Celsius = {c_temp:.2f}\n")
    elif (number=="2"):
        c_temp = float(input("C. Temperature: "))
        f_temp = ((c_temp - 32) * 5/9)
        print(f"Fahrenheit = {f_temp:.2f}\n")

def distance():
    print("What distance do you want to calculate?")
    print("1. Feet to meters")
    print("2. Meters to feet")
    print("3. Inches to centimeters")
    print("4. Centimeters to inches")
    number = (input("> "))
    if (number == "1"):
        feet=float(input("Enter footage: "))
        meters=feet*0.3048
        print(f"Total meters: {meters:.2f}\n")
    if (number == "2"):
        meters=float(input("Enter meters: "))
        feet=meters*3.280839895
        print(f"Total footage: {feet:.2f}\n")
    if (number == "3"):
        inches=float(input("Enter inches: "))
        centimeters=inches*2.54
        print(f"Total Centimeters: {centimeters:.3f}\n")
    if (number == "4"):
        centimeters=float(input("Enter centimeters: "))
        inches=centimeters*0.3937007874
        print(f"Total inches: {inches:.3f}\n")


def physics():
    import math
    print("What physics do you want to calculate?")
    print("1. Free Fall Algorithm")
    print("2. Feet or Meters")
    #print("2. Some other algorithm")
    #print ("3. Some other algorithm")
    number = (input("> "))
    if (number == "1"):
        print("What variables are known?")
        print("1. Time")
        print("2. Height")
        number = (input("> "))
        if (number == "1"):
            time=float(input("Time in seconds: "))
            height=(1/2 * 9.8 * (time**2))
            velocity=(9.8*time)
            print(f"The height is = {height:.2f} meters, and the velocity is = {velocity:.2f} meters per second.\n")
        if (number == "2"):
            height=float(input("Height in meters: "))
            time=math.sqrt((height / .5 / 9.8))
            velocity=(9.8*time)
            print(f"The amount of time until touchdown is = {time:.2f} in seconds, and the velocity is {velocity:.2f} meters per second.\n")


while True:
    print("1. Calculate Electricity")
    print("2. Calculate Mass")
    print("3. Calculate Temperature")
    print("4. Calculate Distance")
    print("5. Calculate Algorithms")
    number = (input("> "))
    if (number == "1"):
        electric_calc()
    elif (number == "2"):
        mass_calc()
    elif (number == "3"):
        temperature()
    elif (number == "4"):
        distance()
    elif(number == "5"):
        physics()
    else:
        print("\nPlease enter a valid selection\n")

#Current = Amperage (Net Flow)
#Voltage = Joules per Coulomb (Pressure)
#Resistance = Ohms
#1 Horsepower = 726 Watts


## Δx = Displacement ------------> ((v+v0) / 2) * t
## Δx = Displacement ------------> v0*t + ((1/2) * a * (t^))

## t = Time Interval ------------> v**2 = v0*^2 + (2*a*Δx)

## v0 = Initial Velocity

## v = Final Velocity ------------> v=(v0)+(at)

## a = Constant Acceleration


## Free Fall Formula ------------> g = -9.8 m/(s*^2) AKA Gravitational Acceleration = -9.8 meters per second squared 
## Velocity ------------> Gravitational Acceleration * Time
## Height ------------> 1/2 * Gravitational Acceleration * ((Time^2)), m
## Velocity ------------> Gravitational Acceleration * Time, m/s



#Drop ball from cliff, takes 10 seconds to hit, how high are you?
#-------------> .5 * (9.8 m/s^2) * ((10s^2)) =  *********** 490m ***********
#What is the Velocity of the ball?
#-------------> 9.8 m/s^2 * 10s =               *********** 98m/s ***********


#Drop ball from cliff, takes 20 seconds to hit, how high are you?
#-------------> .5 * (9.8 m/s^2) * ((20s^2)) =  *********** 1960m ***********
#What is the Velocity of the ball?
#-------------> 9.8 m/s^2 * 20s =               *********** 196m/s ***********
