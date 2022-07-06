PS> python -m venv venv
PS> .\venv\Scripts\activate
(venv) PS> python -m pip install Pillow

#Image reading and storing a temporary file

>>> from PIL import Image
>>> filename = "buildings.jpg"
>>> with Image.open(filename) as img:
...     img.load()
...

>>> type(img)
<class 'PIL.JpegImagePlugin.JpegImageFile'>

>>> isinstance(img, Image.Image)
True
>>> img.show()

>>> img.format
'JPEG'

>>> img.size
(1920, 1273)

>>> img.mode
'RGB'
>>> cropped_img = img.crop((300, 150, 700, 1000))
>>> cropped_img.size
(400, 850)

>>> cropped_img.show()

>>> low_res_img = cropped_img.resize(
...     (cropped_img.width // 4, cropped_img.height // 4)
... )
>>> low_res_img.show()

>>> low_res_img = cropped_img.reduce(4)

>>> cropped_img.save("cropped_image.jpg")
>>> low_res_img.save("low_resolution_cropped_image.png")
