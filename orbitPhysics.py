import numpy as PI

"""OrbitPhysics class"""
"""This class implements the necessary methods to calculate orbits """
class OrbitPhysics:
    G = 4 * PI.pi**2

    def euler_method(self, x0, y0, vx0, vy0, relativeHoleMass, relativeStarMass, xPositions, yPositions):
        orbitEnergy = PI.array([])
        dt = .001
        # Initialize velocities
        vx = vx0
        vy = vy0

        # Initialize positions
        x = x0
        y = y0

        for i in PI.linspace(0,1,3001): # Itera 100 vegades
            r = PI.sqrt(x**2+y**2)
            ax = - self.G * relativeHoleMass*x/r**3
            ay = - self.G * relativeHoleMass*y/r**3
            #calc next position and next vel
            x = x + vx*dt
            y = y + vy*dt
            vx = vx + ax*dt
            vy = vy + ay*dt
            xPositions.append(x)
            yPositions.append(y)
            orbitEnergy = PI.append(orbitEnergy,.5*relativeStarMass*(vx**2+vy**2)-self.G*relativeStarMass*relativeHoleMass/r)
        return orbitEnergy
