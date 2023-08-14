# triangulation-flip

Perform flips on triangulated polygons!
You will need to install python, pip, and tkinter.
---------------------------------------------------

# Configuration

There is a config file, which must be called flip_config.txt, and must be placed in the same folder as the main python file.

The config file has two options:

- sides: the number of sides of the polygon
- size: the radius (presumably) in pixels of the polygon

The name of the options must stay as is given above, and the formatting must also stay as in the config file given in the repository. 
Namely, the format must have the name and the number directly connected by the equal sign, no spaces!

# App Features

In a triangulated polygon, a diagonal is an edge shared by two triangles. These two triangles create a quadrilateral, and quadrilaterals have two diagonals. A flip move replaces one diagonal for the other. Finite sequences of flips produce all possible triangulations.

To flip a diagonal, simply left click on it.

# To-do:
- Create config file for users to input the number of sides and size of the polygon.
- Add instructions for installation.
- Recreate program for the web.
- Clean-up the code
