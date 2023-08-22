# PythonScript


#md_backdrop_v22.08.2023.0.1

import nuke
import nukescripts

def md_backdrop():
    def hex_color_to_rgb(red, green, blue):
        return int('%02x%02x%02x%02x' % (int(red*255),int(green*255),int(blue*255),255),16)
    
    p = nuke.Panel('MD Backdrop')
    
    p.addEnumerationPulldown('my choices', 'User Plate DN CC Key Transfrom 3D')
    
    p.addSingleLineInput('Custom', '')
    
    p.show()
    #for Plate
    if p.value('my choices') == 'User':
       bd_node = nukescripts.autoBackdrop()
       bd_node['label'].setValue(p.value('Custom'))
       bd_node['note_font'].setValue('bold')
       bd_node['note_font_size'].setValue(50)
       
    
    
    #for Plate
    elif p.value('my choices') == 'Plate':
       bd_node = nukescripts.autoBackdrop()
       bd_node['label'].setValue('Plate')
       bd_node['note_font'].setValue('bold')
       bd_node['note_font_size'].setValue(50)
       bd_node['tile_color'].setValue(hex_color_to_rgb(.24,.24,.24))
    #for DN
    elif p.value('my choices') == 'DN':
         bd_node = nukescripts.autoBackdrop()
         bd_node['label'].setValue('DN')
         bd_node['note_font'].setValue('bold')
         bd_node['note_font_size'].setValue(50)
         bd_node['tile_color'].setValue(hex_color_to_rgb(.50,.50,.50))
    
    #For CC
    elif p.value('my choices') == 'CC':
         bd_node = nukescripts.autoBackdrop()
         bd_node['label'].setValue('CC')
         bd_node['note_font'].setValue('bold')
         bd_node['note_font_size'].setValue(50)
         bd_node['tile_color'].setValue(hex_color_to_rgb(.15,.20,.25))
    
    # For Key
    elif p.value('my choices') == 'Key':
         bd_node = nukescripts.autoBackdrop()
         bd_node['label'].setValue('Key')
         bd_node['note_font'].setValue('bold')
         bd_node['note_font_size'].setValue(50)
         bd_node['tile_color'].setValue(hex_color_to_rgb(.15,.25,.15))
    
    
    
    # For Transfrom
    elif p.value('my choices') == 'Transfrom':
         bd_node = nukescripts.autoBackdrop()
         bd_node['label'].setValue('Transfrom')
         bd_node['note_font'].setValue('bold')
         bd_node['note_font_size'].setValue(50)
         bd_node['tile_color'].setValue(hex_color_to_rgb(.3,0,.3))
    
    # For 3D
    elif p.value('my choices') == '3D':
         bd_node = nukescripts.autoBackdrop()
         bd_node['label'].setValue('3D')
         bd_node['note_font'].setValue('bold')
         bd_node['note_font_size'].setValue(50)
         bd_node['tile_color'].setValue(hex_color_to_rgb(.05,0.01,.03))
    
    else:
        pass
