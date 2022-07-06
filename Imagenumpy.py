(venv) $ python -m pip install numpy

# Using NumPy to subtract images

>>> import numpy as np
>>> from PIL import Image

>>> with Image.open("house_left.jpg") as left:
...     left.load()
...
>>> with Image.open("house_right.jpg") as right:
...     right.load()
...

>>> left_array = np.asarray(left)
>>> right_array = np.asarray(right)

>>> type(left_array)
<class 'numpy.ndarray'>
>>> type(right_array)
<class 'numpy.ndarray'>

>>> difference_array =  right_array - left_array
>>> type(difference_array)
<class 'numpy.ndarray'>
>>> difference = Image.fromarray(difference_array)
>>> difference.show()

# Using Numpy to create images

>>> import numpy as np
>>> from PIL import Image

>>> square = np.zeros((600, 600))
>>> square[200:400, 200:400] = 255

>>> square_img = Image.fromarray(square)
>>> square_img
<PIL.Image.Image image mode=F size=600x600 at 0x7FC7D8541F70>
>>> square_img.show()
>>> square_img = square_img.convert("L")


>>> red = np.zeros((600, 600))
>>> green = np.zeros((600, 600))
>>> blue = np.zeros((600, 600))
>>> red[150:350, 150:350] = 255
>>> green[200:400, 200:400] = 255
>>> blue[250:450, 250:450] = 255

>>> red_img = Image.fromarray(red).convert("L")
>>> green_img = Image.fromarray(green).convert("L")
>>> blue_img = Image.fromarray((blue)).convert("L")
>>> square_img = Image.merge("RGB", (red_img, green_img, blue_img))
>>> square_img
<PIL.Image.Image image mode=RGB size=600x600 at 0x7FC7C817B9D0>

>>> square_img.show()
