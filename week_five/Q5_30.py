import numpy as np

mean_99carat, sd_99carat, n_99carat = 44.51, 13.32, 23
mean_1carat, sd_1carat, n_1carat = 56.81, 16.13, 23

point_estimate = (mean_99carat - mean_1carat)
df = (23 - 1) 

se = (np.sqrt(((sd_99carat ** 2)/n_99carat) + ((sd_1carat ** 2)/n_1carat)))

confidence_interval = (1.717144 * se)

upper = (se + confidence_interval)
lower = (se - confidence_interval)
print(upper, lower)
