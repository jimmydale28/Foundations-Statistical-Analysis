import numpy as np
from scipy import stats

def pooled_sd(sd1, sd2, n1, n2):
	return (((sd1 ** 2) * (n1 -1)) + ((sd2 ** 2) * (n2 - 1))) / (n1 + n2 - 2)

mean_treatment, sd_treatment, n_treatment = 4.9, 1.8, 22
mean_control, sd_control, n_control = 6.1, 1.8, 22

sd = pooled_sd(sd_treatment, sd_control, n_treatment, n_control)

point_estimate = (mean_treatment - mean_control)
df = (22 + 22 - 2) 

se = (np.sqrt(((sd ** 2)/n_treatment) + 
	((sd ** 2)/n_control)))
#Based on 95% 
confidence_interval = (2.0181 * se)
#CDF
p_value = stats.t.sf(np.abs(confidence_interval), df)
print(p_value)
