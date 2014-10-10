#============================
#
#  畫格狀點 ver 1.0
#  作者:sand9985
#  轉載請保留此標籤
#====================================

import bge

def draw_grid(x1,x2,y1,y2):
    color=[1,1,1]
    for j in range(y1,y2-1,-1):
        v=[x1,j,0]
        v2=[x2,j,0]
        bge.render.drawLine(v, v2, color) 
    for i in range(x1,x2+1):
        v=[i,y1,0]
        v2=[i,y2,0]
        bge.render.drawLine(v, v2, color)

    
        
            
draw_grid(-10,10,10,-10)
