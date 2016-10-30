import sys
import logging
import os
import shutil
from PIL import Image
from pymclevel import mclevel
from pymclevel.mclevelbase import PlayerNotFound
#from pymclevel import pocket
#from leveldbpocket import PocketLeveldbWorld

LEVEL_PATH = "levels/pc/flat_world_640_64_62"
OUTPUT_LEVEL_PATH = "outputs/peterborough-cathedral"
DSM_PATH = "data/peterborough-cathedral/dsm_trimmed.png"
DTM_PATH = "data/peterborough-cathedral/dtm_trimmed.png"
BUILDINGS_PATH = "data/peterborough-cathedral/"
ROADS_PATH = "data/peterborough-cathedral/"
CATHEDRAL_PATH = "data/peterborough-cathedral/cathedral.png"

X_OFFSET = 0
Z_OFFSET = 128
Y_OFFSET = 64

# uncomment to start from a blank level
#if os.path.exists(OUTPUT_LEVEL_PATH):
#    shutil.rmtree(OUTPUT_LEVEL_PATH)
#shutil.copytree(LEVEL_PATH,OUTPUT_LEVEL_PATH)

level = mclevel.fromFile(OUTPUT_LEVEL_PATH);

R_OLD, G_OLD, B_OLD, A_OLD = (0, 0, 0, 255)
R_NEW, G_NEW, B_NEW, A_NEW = (0, 174, 239, 255)

dsm_image = Image.open(DSM_PATH)
dtm_image = Image.open(DTM_PATH)
cathedral_mask = Image.open(CATHEDRAL_PATH)
#buildings_mask = Image.open(BUILDINGS_PATH)

rgba_dsm_image = dsm_image.convert('RGBA')
rgba_dtm_image = dtm_image.convert('RGBA')
rgba_cathedral_mask = cathedral_mask.convert('RGBA')
#rgba_buildings_mask = buildings_mask.convert('RGBA')

dsm_pixels = rgba_dsm_image.load()
dtm_pixels = rgba_dtm_image.load()
cathedral_pixels = rgba_cathedral_mask.load()
#buildings_pixels = rgba_buildings_mask.load()

replaced_blocks = 0

x_extent, z_extent = cathedral_mask.size
print(x_extent, z_extent)
for x in range(x_extent-1):
    for z in range(z_extent-1):
        cr, cg, cb, ca = cathedral_pixels[x, z]
        #print(cr)
        if (cr) == 255 and ca == 255 and x>0 and z>0:
            terrain_height, tg, tb, ta = dtm_pixels[x, z]
            surface_height, sg, sb, sa = dsm_pixels[x, z]
            surface_height_1_block_west, sg, sb, sa = dsm_pixels[x-1, z]
            surface_height_1_block_east, sg, sb, sa = dsm_pixels[x+1, z]
            surface_height_1_block_south, sg, sb, sa = dsm_pixels[x, z-1]
            surface_height_1_block_north, sg, sb, sa = dsm_pixels[x, z+1]
            for block_height in range(0, surface_height+1):
                translated_x = X_OFFSET + x
                translated_z = Z_OFFSET - z_extent + z
                translated_y = Y_OFFSET + (block_height/2)
                if  (block_height >= terrain_height):
                    if  (block_height < surface_height_1_block_west-2) and (block_height < surface_height_1_block_east-2) and (block_height < surface_height_1_block_south-2) and (block_height < surface_height_1_block_north-2):
                        if (block_height % 2 == 0):  
                            level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Air.ID)
                             #print(translated_x,translated_y,translated_z)
                            replaced_blocks += 1
                    else:
                        if (block_height % 2 == 0):
                            if ((x > 55) and (x < 65)):
                                level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Air.ID)
                            else:
                                level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Sandstone.ID)
                        #else:
                        #    level.setBlockAt(translated_x,(block_height-1)/2,translated_z,level.materials.SandstoneSlab.ID)
                else:
                    if (block_height % 2 == 0):  
                        level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Grass.ID)
                if (block_height == surface_height):
                    if (((x >= 65) or(x <= 55)) or translated_y > 94):
                        if (block_height % 2 == 0):
                            level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Sandstone.ID)
                   #     else:
                   #         level.setBlockAt(translated_x,(Y_OFFSET + ((block_height-1)/2)),translated_z,level.materials.Sandstone.ID)
            #level.setBlockAt(x,(height-y),20,level.materials.BlockofGold.ID)
            #pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)
            #print(x, y)
        else:
            terrain_height, tg, tb, ta = dtm_pixels[x, z]
            for block_height in range(0, terrain_height+1):
                translated_x = X_OFFSET + x
                translated_z = Z_OFFSET - z_extent + z
                translated_y = Y_OFFSET + (block_height/2)
                if (block_height % 2 == 0):
                    level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Grass.ID)
                if (cg) == 216 and block_height == terrain_height:
                    level.setBlockAt(translated_x,translated_y,translated_z,level.materials.BlockofGold.ID)

try:
    level.setPlayerPosition((float(0),float(100),float(0)))
except PlayerNotFound:
    print("Player not found")

#rgb_im.save(NEW_PATH)
#level.setBlockAt(translated_x,translated_y,translated_z,level.materials.Air.ID)
level.generateLights();
level.saveInPlace();
print(replaced_blocks)
