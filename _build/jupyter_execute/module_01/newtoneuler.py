import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# The Newton-Euler equations

Engineering mechanics uses 6 equations of motion to describe the
relationship between applied forces and moments to the motion of rigid
bodies. These 6 equations are the _Newton-Euler_ kinetic equations, you
can write the equations succinctly as vector-relationships between
forces and acceleration as 

- $\mathbf{F} = m\mathbf{a}$ equations 1-3
- $\mathbf{M}_{G} = \frac{d}{dt}\mathbf{h}_G$ equations 4-6

where $\mathbf{F}$ is the resultant sum of forces on a rigid body,
$\mathbf{M}_{G}$ is the resultant sum of moments about a rigid body's
center of mass, and $\mathbf{h}_G is the _angular momentum_ of a rigid
body. Angular momentum is a description of the inertia in a rigid body
due to spinning. To start, we are limiting our study to 3-DOF planar
rigid body motion. This simplifies the Newton-Euler equation to 3
coupled differential equations as such, 

1. $\mathbf{F}\cdot\hat{e}_1 = m\mathbf{a}\cdot\hat{e}_1$ 
2. $\mathbf{F}\cdot\hat{e}_2 = m\mathbf{a}\cdot\hat{e}_2$ 
3. $\mathbf{M}_{G}\cdot\hat{e}_3 = I_{zz}\alpha$

where $\hat{e}_{1},~\hat{e}_{2},$ and $\hat{e}_{3}$ are three orthogonal
unit vectors, $I_{zz}$ is the moment of inertia for the rigid body, and
$\alpha$ is the angular acceleration of the rigid body. Every rigid body
in an engineering system can be described by the Newton-Euler equations. 

> __Note:__ The mass of an object describes how difficult it is to move
> it in a straight line. The moment of inertia describes how difficult
> it is to rotate an object. The units for moment of inertia are
> $kg-m^2$ (in SI). A quick explanation of moment of inertia is that it
> is the variance in the center of mass. 

## Example

Consider a baseball that is thrown. It has an initial velocity of 6 m/s
at an angle of 60$^o$ from the ground and its rotating 10 times/sec.
Determine the acceleration of the baseball and its maximum height. 

In this example, consider the three planar Newton-Euler equations by
first drawing a Free Body Diagram as seen below. 

![baseball FBD](./images/baseball_FBD.svg)

The force of gravity acts over the entire object equally and no other
forces are present. Now, write out the 3 Newton-Euler equations

> __Note:__ You will include force of drag, but for now just consider
> the motion without drag. 

1. $0 = m\ddot{x}$
2. $-mg = m\ddot{y}$
3. $0 = I_{zz}\ddot{\theta}$

Integrating the three equations, you get three equations to describe the
position and angle of the baseball. 

1. $x(t) = x(0)+6\cos\frac{\pi}{3}t$ 
2. $y(t) = y(0)+6\sin\frac{\pi}{3}t-\frac{gt^2}{2}$ 
3. $\theta(t) = \theta(0)+10\frac{rot}{s}\frac{2\pi~rad}{rot}t$ 



t = np.linspace(0,1.1,10)
x = 6*np.cos(np.pi/3)*t
y = 6*np.sin(np.pi/3)*t-9.81*t**2/2
theta = 10*2*np.pi*t
plt.plot(x,y,'o')
plt.xlabel('distance (m)')
plt.ylabel('height (m)');

A freefalling object does not have an applied moment, so the angular 
acceleration is 0 rad/s/s. The ball will continue spinning until an
external moment is applied. 

## Galileo's rolling experiment

Galileo is credited with creating the field of kinematics. One of his
earliest experiments was to measure the position and speed of a ball
rolling on an incline plane. He determined that the position was
proportional to the square of time. This means that the motion is
described by constant acceleration. 

Here, consider a lacrosse ball rolling on a slope. Before you create
the equations of motion for the ball, consider the kinematics of a
rolling ball. The point-of-contact between the ground and ball has the
same velocity both on the ball and the ground. The ground isn't moving,
so the point-of-contact isn't moving. 

The ball rolls down an incline of 5$^o$ and its speed is increasing at 

As before, start
with the free body diagram and

![ball rolling FBD](./images/ball-rolling_FBD.svg)

1. $mg\sin\alpha - F_f = m\ddot{x}$
2. $N-mg\cos\alpha = m\ddot{y}$
3. $-r\cdotF_f = I_{zz}\ddot{\theta}$


