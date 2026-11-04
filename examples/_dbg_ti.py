from floris import FlorisModel
import numpy as np

fmodel = FlorisModel("examples/inputs/gch.yaml")
fmodel.set(layout_x=[0, 500.0], layout_y=[0.0, 0.0])
fmodel.set(wind_directions=[270,270,270,270], wind_speeds=[8,8,10,10], turbulence_intensities=[0.06,0.06,0.06,0.06])
fmodel.run()
ff = fmodel.core.flow_field
ti = ff.turbulence_intensity_field_sorted
print("ti shape", ti.shape)
ti_avg = np.mean(ti, axis=(2,3))
print("ti_avg per (findex, turbine):")
print(ti_avg)
# Also check the raw TI field at turbine 1 grid points, findex 0
print("ti raw at turbine 1 (findex 0) min/max/mean:")
print(np.min(ti[0,1]), np.max(ti[0,1]), np.mean(ti[0,1]))
# Print powers
print("powers:")
print(fmodel.get_turbine_powers())
