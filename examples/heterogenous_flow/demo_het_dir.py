# Copyright 2020 NREL
 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
 
# See https://floris.readthedocs.io for documentation
 

# Make in the inflow direction heterogenous

import matplotlib.pyplot as plt
import floris.tools as wfct
import pandas as pd
import numpy as np

fi = wfct.floris_interface.FlorisInterface("../example_input.json")

# Set layout to 4 turbines
fi.reinitialize_flow_field(layout_array=[[0,0,500,500],[100,400,100,400]])
fi.calculate_wake()

# Get hor plane
hor_plane = fi.get_hor_plane()

# Introduce variation in wind direct
fi.reinitialize_flow_field(wind_direction=[270,280],wind_layout=[[0,0],[0,500]])
fi.calculate_wake()
hor_plane_het_dir = fi.get_hor_plane()

# Plot
fig, axarr = plt.subplots(2,1,figsize=(6,10))

ax = axarr[0]
im = wfct.visualization.visualize_cut_plane(
    hor_plane,
    ax,
    minSpeed=4,
    maxSpeed=9
)
cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.04)
cbar.set_label("Wind Speed (m/s)", labelpad=+10)
ax.set_title("Homogenous")

ax = axarr[1]
im = wfct.visualization.visualize_cut_plane(
    hor_plane_het_dir,
    ax,
    minSpeed=4,
    maxSpeed=9
)
cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.04)
cbar.set_label("Wind Speed (m/s)", labelpad=+10)
ax.set_title("Heterogenous")

# Note that applying turbines requires first learning the 
# wind direction the turbines are aligned to
wind_direction_at_turbine = fi.floris.farm.wind_map.turbine_wind_direction
wfct.visualization.plot_turbines(
    ax=ax,
    layout_x=fi.layout_x,
    layout_y=fi.layout_y,
    yaw_angles=[-1 * d for i,d in enumerate(wind_direction_at_turbine)],
    D = 126
)

plt.show()
