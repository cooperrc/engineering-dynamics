---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python tags=["hide-cell"]
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
```

# Mechanical advantage

In the diagram below, there is a 50-N force, $F$, applied downwards on a
constrained linkage system. There is a restoring force, $R$, that
maintains a slow change in the angle of the mechanism, $\theta$, as it
changes from $89^o$ to $-89^o$. Your
goal is to determine the necessary restoring force $R$ as a
function of angle $\theta$. 


```python tags=["hide-input"]
from IPython.core.display import SVG
SVG(filename='./images/position_angle.svg')
```

## Kinematics

This system has two rigid bodies connected at point $A$ by a pin and the
whole system is pinned to the ground at $O$. Point $B$ slides
along a horizontal surface. The total degrees of freedom are

3 (link 1) + 3 (link 2) - 2 constraints ($O$) - 2 constraints ($A$) - 1
constraint ($B$) - 1 constraint ($\theta$-fixed) = __0 DOF__

For a given angle $\theta$, there can only be one configuration in the
system. Create the constraint equations using the relative position of
point $A$ as such

$\mathbf{r}_A = \mathbf{r}_B + \mathbf{r}_{A/B}$

where 

$\mathbf{r}_A = L(\cos\theta \hat{i}+ \sin\theta \hat{j})$

$\mathbf{r}_B = d\hat{i}$

$\mathbf{r}_{A/B} = L(-\cos\theta \hat{i} + \sin\theta \hat{j})$

solving for the $\hat{i}-$ and $\hat{j}-$components creates two
equations that describe the state of the system

$\theta = \theta$ which states because we have an isosceles triangle,
two angles have to be equal

$d = 2 L \cos\theta$ so $\mathbf{r}_{B} = 2L \cos\theta \hat{i}$

```python tags=["hide-input"]
theta = np.linspace(89,-89)*np.pi/180
d = 2*1*np.cos(theta)
plt.plot(theta*180/np.pi, d)
plt.xlabel(r'$\theta$ (deg)')
plt.ylabel('d (m)');
```

