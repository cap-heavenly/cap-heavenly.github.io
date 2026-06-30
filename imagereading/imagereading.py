import imageio as iio
import time
def lighttoascii(pixel, discswitch):
    # Convert the pixel to grayscale (assuming pixel is a tuple of RGB values)
    if discswitch:
        r, g, b, x = pixel
    else:
        r, g, b = pixel
    greypx = int((r + g + b) / 3)
    # Map the grayscale value to an ASCII character
    if greypx < 10:
        return "'"
    elif greypx < 20:
        return "."
    elif greypx < 40:
        return ":"
    elif greypx < 60:
        return "*"
    elif greypx < 80:
        return "/"
    elif greypx < 100:
        return "}"
    elif greypx <= 255:
        return "#"
# Load the image

cline = []
pswitch = True
rswitch = True
# Print the image shape or type to confirm it's loaded
def toascii(image, pswitch, rswitch, compswitch, cline, discswitch):
    if compswitch:
        for row in image:
            if rswitch:
                for pixel in row:
                    if pswitch:
                        cline.append(lighttoascii(pixel, discswitch))
                    pswitch = not pswitch
                print(''.join(cline))
                cline = []
            rswitch= not rswitch
    else:
        for row in image:
            for pixel in row:
                cline.append(lighttoascii(pixel, discswitch))
            print(''.join(cline))

    time.sleep(20)
    print("done")
print("Welcome to the ASCII art generator!")
print("This program will convert an image to ASCII art.")
while True:
    print("""Please select an option:
[1] milesteller.png [dont choose doesn't work]
[2] rock.webp
[3] flood.jpg
[4] test.png
[5] Custom""")
    imgchoice = input()
    if imgchoice == "1":
        image = iio.v3.imread("milesteller.png")
        discswitch = False
    elif imgchoice == "2":
        image = iio.v3.imread("rock.webp")
        discswitch = True
    elif imgchoice == "3":
        image = iio.v3.imread("flood.jpg")
        discswitch = False
    elif imgchoice == "4":
        image = iio.v3.imread("test.png")
        discswitch = False
    elif imgchoice == "5":
        print("Please enter the name of your image and ensure it is in the image reader folder:")
        imgpath = input()
        image = iio.v3.imread(imgpath)
    else:
        print("Invalid choice. Please try again.")
    print("Was your image sourced from discord? (y/n)")
    discchoice = input().lower()
    if discchoice == "y":
        discswitch = True
    else:
        discswitch = False
    print("Would you like to add compression? (y/n)")
    compchoice = input().lower()
    if compchoice == "y":
        compswitch = True
    else:
        compswitch = False
    print("Processing image...")
    time.sleep(3)
    toascii(image, pswitch, rswitch, compswitch, cline, discswitch)
    x = input()
    