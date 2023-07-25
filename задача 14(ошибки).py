def image_info(**image):
    if 'image_title' not in image:
        raise TypeError("The key 'image_title' isn't here")
    if 'image_id' not in image:
        raise TypeError("The key 'image_id' ish't here")
    print(image)
    print(type(image))
    info = (
        f"Image '{image['image_title']}'"
        f" has id {image['image_id']}"
    )
    return (info)


try:
    info = image_info(image_title='my cat', image_id=5136)
except TypeError as e:
    print(e)

print(info)
