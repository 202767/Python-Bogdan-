class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution


first_image = Image('1920x1080', 'image1', 'jpg')
second_image = Image('1280x720', 'image2', 'png')

print(first_image.__init__)
print(first_image.resolution)
first_image.resize("720x360")
print(first_image.resolution)
print(second_image.resolution)
second_image.resize("1080x1920")
print(second_image.resolution)
