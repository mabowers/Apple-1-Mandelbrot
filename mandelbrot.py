x_julia = -0.95
y_julia = -0.25

def mandelbrot_point(x, y, max_iterations):
    xC = x # x_julia #
    yC = y #y_julia #
    iterations = 1
    done = False

    xx = x*x
    yy = y*y

    while(iterations < max_iterations):
       
        # check if escaped
        xx = x*x
        yy = y*y
        if(xx + yy > 4):
            break

        # calculate new x and y
        xtemp = xx - yy + xC
        y = 2*x*y + yC
        x = xtemp

        # increment iteration counter
        iterations = iterations + 1
       
    return iterations


# Apple-I screen is 40 chars wide by 24 chars high
pixels_x = 40
pixels_y = 23

# Plotting characters (0 to 15)
characters = [' ','.',':',',',';','!','-','^','+','=','/','&','*','%','#','@']
print(len(characters))

print('****************************************')

print('MANDELBROT SET GENERATOR')
print('')
print('ENTER PARAMETERS:')
print('(E.G. X=-0.5, Y=0, WIDTH=2, ITER=10)')
print('')

#x_center       = float(input("X CENTER = "))
#y_center       = float(input("Y CENTER = "))
#width          = float(input("WIDTH = "))
#max_iterations = int(input("MAX ITERATIONS = "))

# DEFAULTS
x_center       = float(0)
y_center       = float(0)
width          = float(4)
max_iterations = int(16)

#x_center       = float(-1.1512401656925)
#y_center       = float(-0.2315547206635)
#width          = float(0.5)
#max_iterations = int(65535)

pixel_pitch = width / 40

x_start = x_center - ((pixels_x)/2)*pixel_pitch
y_start = y_center - ((pixels_y-1)/2)*pixel_pitch

print('pixel pitch = ' + str(pixel_pitch))
print('x start = ' + str(x_start))
print('y start = ' + str(y_start))

x_coord = x_start
y_coord = y_start

print("")

for y in range(0,pixels_y):
    for x in range(0,pixels_x):
        # for x pixel
        result = mandelbrot_point(x_coord,y_coord,max_iterations)
        
        #print('RESULT IS ' + str(result))
        print(characters[(result%16)-1], end='')

        x_coord = x_coord + pixel_pitch # go to next x pixel

    # for each line
    x_coord = x_start
    y_coord = y_coord + pixel_pitch
    print("") # print a new line character

print("")