#===================================
#
#  �Ĥ@�H�ٵ��� ver 1.0
#  �@��:sand9985
#  ����ЫO�d������
#====================================

import bge
import mathutils
import GameLogic
import math

#�����V�q
vec = mathutils.Vector((0.0, -8.0, 0.0))

def first_person(name):
    cont=bge.logic.getCurrentController() #���o�ثe������camera 
    obj=cont.owner #�Ҳ�
    player=GameLogic.getCurrentScene().objects[name]
    rotation = player.worldOrientation.to_euler()
    degree=math.radians(90) #�¦V����
    obj.worldOrientation = [degree, 0, rotation.z] 
    obj.position=player.position
    vec.rotate(rotation)
    obj.position+=vec
    
    
first_person("Cube")

