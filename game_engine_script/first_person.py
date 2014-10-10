#===================================
#
#  第一人稱視角 ver 1.0
#  作者:sand9985
#  轉載請保留此標籤
#====================================

import bge
import mathutils
import GameLogic
import math

#偏移向量
vec = mathutils.Vector((0.0, -8.0, 0.0))

def first_person(name):
    cont=bge.logic.getCurrentController() #取得目前的控制camera 
    obj=cont.owner #模組
    player=GameLogic.getCurrentScene().objects[name]
    rotation = player.worldOrientation.to_euler()
    degree=math.radians(90) #朝向物件
    obj.worldOrientation = [degree, 0, rotation.z] 
    obj.position=player.position
    vec.rotate(rotation)
    obj.position+=vec
    
    
first_person("Cube")

