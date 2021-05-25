---
jupytext:
  formats: notebooks//ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3 tags = ['hide-cell']
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
```

# Work and energy

The Newton-Euler equations relate forces to acceleration. Forces and
accelrations are vector quantities. Work and energy are _scalar_
quantities that result from 

- $\mathbf{F} \cdot d \mathbf{r} = dW$
- $m \mathbf{a} \cdot d \mathbf{r} = dT$

where $d \mathbf{r}$ is the change position of an object and $dW$ is the
work done to the object and $dT$ is the change in kinetic energy of
object. 

## Conservation of energy

The first law of thermodynamics 

$$T_1 + V_1 + W^{1\rightarrow 2} = T_2 + V_2$$

where 

- $T_1,~T_2$: kinetic energy
- $V_1,~V_2$: potential energy
- $W^{1\rightarrow 2}: work done to the system (not included in the
  potential energy changes)
