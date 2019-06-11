import numpy as np

def drive(dist, abPedal, stAngle, speed, isOnRoad):
    """
    dist: list of distances from obstacle [nearest wall / end of road]
    abPedal: acc/break pedal value
    stAngle: steering angle
    isOnRoad: if car is on road or not
    
    returns `abPedal` and `stAngle`
    algo: all else is useless, use left and right dist and try to equate them
            if they are nearly eqaul, increase the speed else reduce it
    """

    if not isOnRoad:
        # go right, slowly
        return 0.75, 2

    # the first and last values respectively
    left_dist, right_dist = dist[0], dist[-1]
    diff = right_dist - left_dist

    if diff > 0:
        if stAngle > -5:
            stAngle -= 1
    else:
        if stAngle < 5:
            stAngle += 1

    # if diff is not THAT much, accelerate!
    if speed < 10:
        if diff < 0.5 * min(left_dist, right_dist):
            abPedal += 0.5
        else:
            abPedal -= 0.5

    return abPedal, stAngle
