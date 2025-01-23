
def interp(a: float, b: float, between_percent: float) -> float:
    return a + between_percent*(b-a)

def interp2d(pt_1: list, pt_2: list, between_percent: float) -> list:
    return [ interp(pt_1[0], pt_2[0], between_percent), interp(pt_1[1], pt_2[1], between_percent) ]