from PIL import Image,ImageColor,ImageTransform
image=Image.open("pillow/img.jpg")

print("======================================")
print("         IMAGE STUDIO                 ")
print("======================================")
oprxn=input("1. Change extension\n2. Rotate\n3. Crop\n4. Flip\n5. Resize\n  ")

if oprxn=="1":
    new_ext=input("\nPNG(png)\nJPG(jpg)\n\n")
    if new_ext=="png":
        new_ext_img=image.save("pillow/newimg.png")      
    if new_ext=="jpg":
        new_ext_img=image.save("pillow/newimage.jpg")
if oprxn=="2":
    rotn_angle=float(input("\n\nEnter Rotation Angle "))
    colr=input("Enter BG color ")
    rot_img=image.rotate(rotn_angle,expand=True,fillcolor=ImageColor.getcolor(colr,"RGBA"))
    rot_img.save("pillow/newimage.jpg")
if oprxn=="3":
    left_x,top_y,right_x,bottom_y=input("Enter the cordinates of new image(left,top,right,bottom) ").split()
    crop_img=image.crop((int(left_x),int(top_y),int(right_x),int(bottom_y)))
    crop_img.save("pillow/newimage.jpg")
if oprxn=="4":
    flip_type=input("Horizontal(h) or Vertical(v) ")
    if flip_type=="h":
        flip_img=image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        flip_img.save("pillow/newimage.jpg")
    if flip_type=="v":
        flip_img=image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        flip_img.save("pillow/newimage.jpg")
if oprxn=="5":
    xsize=int(input("Enter magnification scale "))
    size_img=(image.size[0]*xsize,image.size[1]*xsize)
    better_img=image.resize(size_img)
    better_img.save("pillow/newimage.jpg")
