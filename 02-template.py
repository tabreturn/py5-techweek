size(420*4, 297*4, SVG, 'out.svg')

columns = 10
rows = 4

tile_width = width/columns
tile_height = height/rows

for column in range(columns):

    for row in range(rows):

        translate(column*tile_width, row*tile_height)
        #rect(0, 0, tile_width, tile_height)
        line(0, 0, tile_width, tile_height)
        reset_matrix()

exit_sketch()

# SECTION ?: VPYPE ============================================================

# vpype is a veritable swiss army knife for plotter-ready vector graphics
# https://vpype.readthedocs.io/en/stable/index.html

# 1. install "vpype" via the thonny package manager (tools > manage packages)
# 2. note how the layer-1 markeup draws in this (hardly efficient) order: 
#    rect -> line -> rect

import vpype_cli
vpype_cli.execute('read out.svg write --pen-up vpyped.svg')
#vpype_cli.execute('read out.svg linesort write --pen-up vpyped.svg')
vpype_cli.execute('read out.svg linemerge write --pen-up vpyped.svg')











