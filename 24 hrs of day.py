for h in range(0, 24):
    if h == 0:
        print("12 Midnight")
    elif h == 12:
        print("12 Noon")
    elif h < 12:
        print(h, "AM")
    else:
        print(h-12, "PM")
