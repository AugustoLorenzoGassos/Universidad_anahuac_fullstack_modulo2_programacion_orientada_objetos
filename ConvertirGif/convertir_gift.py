import imageio.v3 as iio

filenames = ['ConvertirGif\Kibo1.jpeg','ConvertirGif\Kibo2.jpeg','ConvertirGif\Kibo3.jpeg','ConvertirGif\Kibo4.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))
print("antes de escribir")
iio.imwrite('kibo.gif', images, duration = 500, loop = 0)
print("después de escribir")
