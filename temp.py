def yoloToPascalVoc(x_center, y_center, w, h,  image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w)/2
    y1 = ((2 * y_center * image_h) - h)/2
    x2 = x1 + w
    y2 = y1 + h
    return [x1, y1, x2, y2]

# car=toBWImage(cv2.imread("car-14.png"))
# cv2.imwrite("outputs/BWcar.png",car)
# # display("outputs/BWcar.png")
# # now lets do some cropping and stuff 
# i=Image.open("outputs/BWcar.png")
# l="3 0.714796 0.558474 0.447959 0.221011"
# # l="3 0.286735 0.536174 0.457143 0.19227"
# m=l.split(" ")
# m=m[1:]
# i.crop(yoloToPascalVoc(float(m[0]),float(m[1]),float(m[2]),float(m[3]),i.width,i.height))