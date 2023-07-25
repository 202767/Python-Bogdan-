button_default = {
    'text': 'Buy now',
    'color': 'green',
    'height': 200,
    'width': 300
}

button_sizes = {
    'height': 300,
    'width': 400
}

button_style = {'color': 'purple'}

new_button = button_default | button_sizes | button_style

print(new_button)
