import imageio.v3 as iio
filenames=["first-img.jpg","second-img.jpg"]
images=[]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('team.gif',images,duration=500,loop=0)
    