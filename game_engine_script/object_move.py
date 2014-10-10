#============================
#
#  物件移動腳本 ver 1.0
#  作者:sand9985
#  轉載請保留此標籤
#====================================
import bge
import mathutils
import math



def Player():
    cont=bge.logic.getCurrentController()  #取得目前的控制
    obj=cont.owner #當前的模組
    
    key = bge.logic.keyboard.events  #取得blender 鍵盤事件 
    kbleft = key[bge.events.LEFTARROWKEY] #按左
    kbright = key[bge.events.RIGHTARROWKEY]   #按右
    kbup    = key[bge.events.UPARROWKEY]  #按上
    
    m=mathutils.Matrix.Identity(4)
    if kbup>0:
        m*= mathutils.Matrix.Translation((0, 0.1, 0.0))
    if kbleft>0:
        m*= mathutils.Matrix.Rotation(math.radians(1.0), 4, 'Z')     
    if kbright>0:
        m*=mathutils.Matrix.Rotation(math.radians(-1.0), 4, 'Z')     
    obj.localTransform*=m
    
 
   
    

Player() #玩家主要邏輯