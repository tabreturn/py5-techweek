size(420*2, 297*2)
#size(420*2, 297*2, SVG, 'plot_me.svg')  # uncomment for svg

columns = 10
rows = 5
tile_width = width/columns
tile_height = height/rows

for row in range(rows):
    for column in range(columns):
        translate(column*tile_width, row*tile_height)
        # your code goes here
        rect(0, 0, tile_width, tile_height)
        line(0, 0, tile_width, tile_height)
        circle(30, 20, 10)
        reset_matrix()

#exit_sketch()  # uncomment for svg


# vpype is a veritable swiss army knife for plotter-ready vector graphics
# install "vpype" via the thonny package manager (tools > manage packages)
'''
import vpype_cli
vpype_cli.execute('read plot_me.svg write vpyped.svg')
vpype_cli.execute('read vpyped.svg write --pen-up vpyped.svg')
vpype_cli.execute('read vpyped.svg linesort write --pen-up vpyped.svg')
vpype_cli.execute('read plot_me.svg linemerge write vpyped.svg')
'''
