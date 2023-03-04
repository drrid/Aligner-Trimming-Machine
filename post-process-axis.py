f = open('points.gcode','r')
filedata = f.read()
f.close()

newdata = filedata.replace("Y-","H").replace("Z","Y").replace("H","Z").replace('Y','Y-').replace('Y--','Y')
# newdata = newdata.replace("Z-","Y")
# newdata = newdata.replace("H","Z")

f = open('points2.gcode','w')
f.write(newdata)
f.close()
