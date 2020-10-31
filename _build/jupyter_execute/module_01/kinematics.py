#!/usr/bin/env python
# coding: utf-8

# # Geometry of motion - kinematics
# 
# # Position
# 
# Classical physics describes the position of an object using three
# independent coordinates e.g. 
# 
# $$
# \mathbf{r}_{P/O} = x\hat{i} + y\hat{j} + z\hat{k}
# $$ (position)
# 
# where $\mathbf{r}_{P/O}$ is the position of point $P$ _with respect to the point
# of origin_ $O$, $x,~y,~z$ are magnitudes of distance along a
# Cartesian coordinate system and $\hat{i},~\hat{j}$ and $\hat{k}$ are
# unit vectors that describe three

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# # Velocity
# 
# The velocity of an object is the change in position, equation
# {eq}`position`, per length of time.
# 
# $$
# \mathbf{v}_{P/O} = \frac{d\mathbf{r}_{P/O}}{dt} = \dot{x}\hat{i} + \dot{y}\hat{j} +
# \dot{z}\hat{k}
# $$ (velocity)
# 
# ```{note}
# The notation $\dot{x}$ and $\ddot{x}$ is short-hand for writing out
# $\frac{dx}{dt}$ and $\frac{d^2x}{dt^2}$, respectively.
# ```
# 
# The definition of velocity in equation {eq}`velocity` depends upon the change in position of all
# three independent coordinates, where
# $\frac{d}{dt}(x\hat{i})=\dot{x}\hat{i}$. 
# 
# 
# ```{note}
# Remember the chain rule: $\frac{d}{dt}(x\hat{i})=\dot{x}\hat{i} +
# x\dot{\hat{i}}$, but $\dot{\hat{i}}=0$ because this unit vector is not
# changing direction. You'll see other unit vectors later that _do
# change_.
# ```
# 
# {numref}`postion-velocity`
# ## Example - GPS vs speedometer
# You can find velocity based upon postion, but you can only find changes
# in position with velocity. Consider tracking the motion of a car driving
# down a road using GPS. You determine its motion and create the position,
# $\mathbf{r} = x\hat{i} +y\hat{j}$, where
# 
# 
# $x(t) = 4t +3$ and $y(t) = 3t - 1$
# 
# To get the velocity, calculate $\mathbf{v} = \dot{\mathbf{r}}$
# 
# $\mathbf{v} = 4\hat{i} +3 \hat{j}$

# In[2]:


t = np.arange(0,5)
x = 4*t + 3
y = 3*t -1
plt.plot(x,y,'o')
plt.quiver(x,y,4,3)
plt.title('Position of car on road every 1 second'+
    '\nvelocity shown as arrow')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)');


# ## Speed
# 
# The speed of an object is the
# [magnitude](https://www.mathsisfun.com/algebra/vectors.html) of the
# velocity, 
# 
# $|\mathbf{v}_{P/O}| = \sqrt{\mathbf{v}\cdot\mathbf{v}} =
# \sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2}$
# 
# # Acceleration
# 
# The acceleration of an object is the change in velocity per length of
# time. 
# 
# $\mathbf{a}_{P/O} = \frac{d \mathbf{v}_{P/O} }{dt} = \ddot{x}\hat{i} +
# \ddot{y}\hat{j} + \ddot{z}\hat{k}$
# 
# where $\ddot{x}=\frac{d^2 x}{dt^2}$ and $\mathbf{a}_{P/O}$ is the
# acceleration of point $P$ _with respect to the point of origin_ $O$. 
# 
# # Rotation and Orientation
# 
# The definitions of position, velocity, and acceleration all describe a
# single point, but dynamic engineering systems are composed of rigid
# bodies is needed to describe the position of an object.

# In[3]:


from IPython.core.display import SVG

SVG(filename='./images/position_angle.svg')


# _In the figure above, the center of the block is located at
# $r_{P/O}=x\hat{i}+y\hat{j}$ in both the left and right images, but the
# two locations are not the same. The orientation of the block is
# important for determining the position of all the material points._
# 
# In general, a rigid body has a _pitch_, _yaw_, and _roll_ that describes
# its rotational orientation, as seen in the animation below. We will
# revisit 3D motion in Module_05

# In[4]:


from IPython.display import YouTubeVideo
vid = YouTubeVideo("li7t--8UZms?loop=1")
display(vid)


# # Rotation in planar motion
# 
# Our initial focus is planar rotations e.g. yaw and roll are fixed. For a
# body constrained to planar motion, you need 3 independent measurements
# to describe its position e.g. $x$, $y$, and $\theta$
