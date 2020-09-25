def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    # take the shark distance and the pontoon distance
    # and divide them both by the speed of each object
    # if the dolphin is True, shark speed / 2
    my_time = pontoon_distance/you_speed
    shark_time = shark_distance/shark_speed
    if dolphin:
        shark_time *= 2
    if my_time < shark_time:
        return "Alive!"
    else:
        return "Shark Bait!"
    # Don't get eaten!
print((shark(12, 50, 4, 8, True)))
# should return "Alive!"
print((shark(7, 55, 4, 16, True)))
# should return "Alive!"
print((shark(24, 0, 4, 8, True)))
# should return "Shark Bait!"