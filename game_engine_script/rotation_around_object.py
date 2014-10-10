#===================================
#
#  ¶�۪������ ver 1.0
#  �@��:sand9985
#  ����ЫO�d������
#====================================

import bge
import mathutils
import GameLogic
import math

def rotation_around_object(point,obj_name,axis,degree):
    cont=bge.logic.getCurrentController()  #���o�ثe������
    obj=cont.owner #�Ҳ�
    obj2=GameLogic.getCurrentScene().objects[obj_name] #���o�����I����    
    vec=point-obj2.position #�⪫��y�Ъ��V�q   
 
    tra=mathutils.Matrix.Translation(-1*vec)
    tra*=mathutils.Matrix.Rotation(math.radians(degree), 4, axis) #����x�}
    tra*=mathutils.Matrix.Translation(vec)   
    obj.localTransform*=tra
    
p= mathutils.Vector((-4.58969, 0.6509, 1.6419))   #����_�l�I
rotation_around_object(p,"Cube",[0,0,1],3)
    
