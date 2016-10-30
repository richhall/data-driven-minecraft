#Run peterborough_cathedral_west_front_removed.py first!

from plyfile import PlyData, PlyElement
import sys
from pymclevel import mclevel
#from pymclevel import pocket
#from leveldbpocket import PocketLeveldbWorld

LEVEL_PATH = "outputs/peterborough-cathedral"

X_OFFSET = 57
Z_OFFSET = 38
Y_OFFSET = 69

level = mclevel.fromFile(LEVEL_PATH);

plydata = PlyData.read('data/peterborough-cathedral/west_front_dense_point_cloud.ply')

d = {}
print(len(d))

for e in plydata['vertex']:
    x=int(round(e['x']))
    y=int(round(e['y']))
    z=int(round(e['z']))
    key = "x"+str(x)+"y"+str(y)+"z"+str(z)
    d[key] = (x,y,z)
    
print(len(d))

for key, (x,y,z) in d.items():
    level.setBlockAt(X_OFFSET+x,Y_OFFSET+y,Z_OFFSET+z,level.materials.Sandstone.ID)
    #level.generateLights();

level.generateLights();
level.saveInPlace();


