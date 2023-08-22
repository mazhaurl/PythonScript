#SHUFFLE SPLIT VERSION 1.0.2
#DATE: 2023.01.29
#MD MAZHAURL ISLAM SHUVO (WWW.SHUVOFX.COM)


import nuke

def my_shuffleSplit():

    #SELECTED NODE AND CREATE NDOER VARIABLE FOR RED 
    my_selectedNode = nuke.selectedNode()

    my_shuffleNode = nuke.createNode('Shuffle')

    #Set ALL RED
    my_shuffleNode['red'].setValue('red')
    my_shuffleNode['green'].setValue('red')
    my_shuffleNode['blue'].setValue('red')
    my_shuffleNode['alpha'].setValue('red')

   
   #NODE POSITION

    my_selectedNode_xpos = my_selectedNode['xpos'].value()

    my_selectedNode_ypos = my_selectedNode['ypos'].value()


    my_shuffleNode.setInput(0, my_selectedNode )

    my_shuffleNode['xpos'].setValue(my_selectedNode_xpos  -150)
    my_shuffleNode['ypos'].setValue(my_selectedNode_ypos+150)


    
    #COLOR AND LABLE

    my_shuffleNode['tile_color'].setValue( int('%02x%02x%02x%02x' % (int(1*255),int(0*255),int(0*255),255),16))

    my_shuffleNode['label'].setValue('RED')

#=========================================================================================================

    #SELECTED NODE AND CREATE NDOER VARIABLE FOR GREEN 
    my_shuffleNode = nuke.createNode('Shuffle')


    #Set All GREEN
    my_shuffleNode['red'].setValue('green')
    my_shuffleNode['green'].setValue('green')
    my_shuffleNode['blue'].setValue('green')
    my_shuffleNode['alpha'].setValue('green')
        
     #NODE POSITION
    my_selectedNode_xpos = my_selectedNode['xpos'].value()

    my_selectedNode_ypos = my_selectedNode['ypos'].value()


    my_shuffleNode.setInput(0, my_selectedNode )

    my_shuffleNode['xpos'].setValue(my_selectedNode_xpos  +0)
    my_shuffleNode['ypos'].setValue(my_selectedNode_ypos+150)

     #Color and Lable Change

    my_shuffleNode['tile_color'].setValue( int('%02x%02x%02x%02x' % (int(0*255),int(1*255),int(0*255),255),16))

    my_shuffleNode['label'].setValue('GREEN')

#===============================================================================================


    #SELECTED NODE AND CREATE NDOER VARIABLE FOR BLUE 
    my_shuffleNode = nuke.createNode('Shuffle')


   #Set All BLUE

    my_shuffleNode['red'].setValue('blue')
    my_shuffleNode['green'].setValue('blue')
    my_shuffleNode['blue'].setValue('blue')
    my_shuffleNode['alpha'].setValue('blue')
    
     #NODE POSITION
    my_selectedNode_xpos = my_selectedNode['xpos'].value()

    my_selectedNode_ypos = my_selectedNode['ypos'].value()


    my_shuffleNode.setInput(0, my_selectedNode )

    my_shuffleNode['xpos'].setValue(my_selectedNode_xpos  +150)
    my_shuffleNode['ypos'].setValue(my_selectedNode_ypos+150)


    #Color and Lable Change
    my_shuffleNode['tile_color'].setValue( int('%02x%02x%02x%02x' % (int(0*255),int(0*255),int(1*255),255),16))


    my_shuffleNode['label'].setValue('BLUE')
