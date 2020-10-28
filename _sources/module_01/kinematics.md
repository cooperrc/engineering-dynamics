---
jupytext:
  formats: md:myst
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  name: python3
---

# Geometry of motion - kinematics

# Position

Classical physics describes the position of an object using three
independent coordinates e.g. 

$\mathbf{r}_{P/O} = x\hat{i} + y\hat{j} + z\hat{k}$

where $\mathbf{r}_{P/O}$ is the position of point $P$ _with respect to the point
of origin_ $O$, $x,~y,~z$ are magnitudes of distance along a
Cartesian coordinate system and $\hat{i},~\hat{j}$ and $\hat{k}$ are
unit vectors that describe three 

```{code-cell} ipython3
---
tags: [hide-input]
---
import numpy as np
r = np.array([1,2,3])
print(r)
```

# Velocity

The velocity of an object is the change in position per length of time.

$\mathbf{v}_{P/O} = \frac{d\mathbf{r}_{P/O}}{dt} = \dot{x}\hat{i} + \dot{y}\hat{j} +
\dot{z}\hat{k}$

This definition of velocity depends upon the change in position of all
three independent coordinates, where
$\frac{d}{dt}(x\hat{i})=\dot{x}\hat{i}$. 

## Speed

The speed of an object is the
[magnitude](https://www.mathsisfun.com/algebra/vectors.html) of the
velocity, 

$|\mathbf{v}_{P/O}| = \sqrt{\mathbf{v}\cdot\mathbf{v}} =
\sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2}$

# Acceleration

The acceleration of an object is the change in velocity per length of
time. 

$\mathbf{a}_{P/O} = \frac{d \mathbf{v}_{P/O} }{dt} = \ddot{x}\hat{i} +
\ddot{y}\hat{j} + \ddot{z}\hat{k}$

where $\ddot{x}=\frac{d^2 x}{dt^2}$ and $\mathbf{a}_{P/O}$ is the
acceleration of point $P$ _with respect to the point of origin_ $O$. 

# Rotation _in planar motion_

The definitions of position, velocity, and acceleration all describe a
single point, but dynamic engineering systems are composed of rigid
bodies is needed to describe the position of an object. 

```python
from IPython.core.display import SVG
SVG(filename='../dyn-logo.svg')
```
