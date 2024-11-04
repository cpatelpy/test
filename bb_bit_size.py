#/bin/python
#Name: bb_bit_size.py
#Creation Date: 09 June 2024
#Author: Rahul Suthar
#Purpose: Find minimum blind/burried drill size
#Special Requirements: None
#Revision History:
#Rev 1.0.0 

#script created to chek min drill bit size on blind buried drills

import os
from Environment import EDITS_STEP_NAME
from GenesisMatrix import GenesisMatrix
from GenesisLayer import GenesisLayer
from Interface import Interface

# Define the job, form, and PCB_WRK
JOB = os.environ.get('JOB')
FORM = os.environ.get('FORM')

# Create an Interface object
interface = Interface()

# Create a GenesisMatrix object
matrix = GenesisMatrix(JOB)

# Get the drill layer list
drill_layer_list = matrix.drillLayersNames()

# Filter the drill layer list
new_drill_layer_list = [layer for layer in drill_layer_list if layer not in ["drill", "drill_v"]]

# Loop through the new drill layer list
for layer in new_drill_layer_list:
    # Create a GenesisLayer object
    genesis_layer = GenesisLayer(JOB, EDITS_STEP_NAME, layer)

    # Get the minimum hole size
    min_hole_size = genesis_layer.getMinHoleSize()

    # Check if min_hole_size is not empty
    if min_hole_size:
        # Output results
        print("Drill Layer: {}".format(layer))
        print("Minimum hole size: {}".format(min_hole_size))
        interface.PAUSE('Layer: {} --> Found Minimum Hole Size {} mil. Please Verify with Dielectric Thickness!'.format(layer, min_hole_size))
    else:
        interface.PAUSE('Layer: {} --> Found Blank, Please Verify!'.format(layer))

# If new_drill_layer_list is empty
if not new_drill_layer_list:
    interface.PAUSE('No blind & Buried vias!')

# Change form button color to green
# interface.COM('edit_form,job={},form={},elem=bb_bit_size,color=99000'.format(JOB, FORM))

print("Script completed successfully.")

exit() 