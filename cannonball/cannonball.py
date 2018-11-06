from math import sin, cos, radians


def getInputs():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1

    # calculate the maximum height achieved by the cannonball
    def maxheight(self):
        self.maxheight = self.ypos
        if self.yvel > 0:
            time = self.yvel / 9.8
            self.maxheight += time * (self.yvel/2.0)
        return self.maxheight


def main():
    angle, vel, h0, time = getInputs()
    ball = Projectile(angle, vel, h0)
    maxheight = ball.maxheight()
    while ball.getY() > 0:
        ball.update(time)
    print("\nDistance: {0: 0.1f} meters.".format(ball.getX()))
    print("\nMaximum height : {0: 0.1f} meters.".format(maxheight))


if __name__ == '__main__':
    main()

