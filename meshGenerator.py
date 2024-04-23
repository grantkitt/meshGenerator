"""
*** INFO ***

This script generates a mesh for a simulation similar to the circular cylinder lab, but for a polygon. 

Firstly triangles are made from the polygon to create planes normal to the x and y directions,
then trapezoids are formed from the triangle slants extending outwards to create the full rectangular shape.

The script then generates boundary conditions from the block face normals and generates the output file, `blockMeshDict`.

A plot is also generated to ensure the mesh is correct.

*** NOTE ***

- When copying a circular cylinder lab folder, the following items need to be changed:
    1. Delete `cylinder` dictionary in 0/p and 0/U files.
    2. Append 
        `polygon 
        {
            type            zeroGradient;
        }

        outside 
        {
            type            slip;
        }`  
        to the 0/p file.
    3. Append
        `polygon 
        {
            type            fixedValue;
            value           uniform (0 0 0);
        }

        outside 
        {
            type            zeroGradient;
        }`
        to the 0/U file.
    4. Replace all occurences of `cylinder` with `polygon` in the forceCoeffs and forces files.
    5. Replace the blockMeshDict file with the one generated by this script.

*** INFO ***

- As the number of sides increases, the resolution of the wake and foreground increases due to there being a
    larger amount of internal connector blocks. Keep this in mind when determining mesh resolution.

*** PARAMETERS ***

    >>> sides | Number of sides of the polygon.
        ... Minimum: 4
        ... Must be a power of 2 (e.g. 4, 8, 32, 64, etc.)
    >>> diameter | Diameter of the polygon. [m]
    >>> foreground | Length of the foreground. [m]
    >>> wake | Length of the wake. [m]
    >>> width | Width of the polygon. [m]
    >>> height | Height of the polygon. [m]
        ... The mesh generates bottom points of -height/2 and top points of height/2.
    >>> resolution | The number of cells per block in the x and y directions.
        ... The number of z cells is always 1. 
        ... simpleGrading shouldn't need to be changed.

*** USAGE ***

    1. Install required packages:
        - matplotlib
        - numpy
    2. Change parameters to required values.
    3. Run `python meshGenerator.py` in the terminal.

"""

import matplotlib.pyplot as plt

from etc.generator import MeshGeneration

sides = 8
diameter = 3
foreground = 2
wake = 10
width = 4
height = 0.1
resolution = 10

MeshGeneration(sides, diameter, foreground, wake, width, height, resolution)

### Uncomment the next line to show the mesh plot.
# plt.show()