def route_info(dict):
    if (dict.get('distance')
            and isinstance(dict['distance'], int)):
        return f"Distance to your destination is {dict.get('distance')}"
    if (not dict.get('distance')
            and dict.get('speed')
            and dict.get('time')
            and type(dict.get('speed') is int)
            and type(dict.get('time') is int)):
        return f"Distance to your destination is {dict.get('speed') * dict.get('time')}"
    return "No distance info is available"


print(route_info({'distance': 100}))
print(route_info({'speed': 30, 'time': 2}))
print(route_info({'acceleration': 10}))
