#============================
#
#  ���󲾰ʸ}�� ver 1.0
#  �@��:sand9985
#  ����ЫO�d������
#====================================
import bge
import mathutils
import math



def Player():
    cont=bge.logic.getCurrentController()  #���o�ثe������
    obj=cont.owner #��e���Ҳ�
    
    key = bge.logic.keyboard.events  #���oblender ��L�ƥ� 
    kbleft = key[bge.events.LEFTARROWKEY] #����
    kbright = key[bge.events.RIGHTARROWKEY]   #���k
    kbup    = key[bge.events.UPARROWKEY]  #���W
    
    m=mathutils.Matrix.Identity(4)
    if kbup>0:
        m*= mathutils.Matrix.Translation((0, 0.1, 0.0))
    if kbleft>0:
        m*= mathutils.Matrix.Rotation(math.radians(1.0), 4, 'Z')     
    if kbright>0:
        m*=mathutils.Matrix.Rotation(math.radians(-1.0), 4, 'Z')     
    obj.localTransform*=m
    
 
   
    

Player() #���a�D�n�޿�