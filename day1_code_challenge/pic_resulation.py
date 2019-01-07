from PIL import Image

pic = "509934.jpg"
Pic1=Image.open(pic)
size=Pic1.size
print 'the resolution of Image file ( width x height ) is ' +str(size[0])+'x'+str(size[1])
