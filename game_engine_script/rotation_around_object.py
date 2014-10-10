#===================================
#
#  繞著物體旋轉 ver 1.0
#  作者:sand9985
#  轉載請保留此標籤
#====================================

import bge
import mathutils
import GameLogic
import math

def rotation_around_object(point,obj_name,axis,degree):
    cont=bge.logic.getCurrentController()  #取得目前的控制
    obj=cont.owner #模組
    obj2=GameLogic.getCurrentScene().objects[obj_name] #取得中心點物件    
    vec=point-obj2.position #兩物件座標的向量   
 
    tra=mathutils.Matrix.Translation(-1*vec)
    tra*=mathutils.Matrix.Rotation(math.radians(degree), 4, axis) #旋轉矩陣
    tra*=mathutils.Matrix.Translation(vec)   
    obj.localTransform*=tra
    
p= mathutils.Vector((-4.58969, 0.6509, 1.6419))   #旋轉起始點
rotation_around_object(p,"Cube",[0,0,1],3)
    
