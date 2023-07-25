def update_car_info(**dict):
    dict['is_aviable'] = True
    return dict


car = update_car_info(brand='Gucci', price=345)

print(car)
