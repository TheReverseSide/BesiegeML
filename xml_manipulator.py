import xml.etree.ElementTree as ET

tree = ET.parse('/Users/startz/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/train_0.bsg')
root = tree.getroot()


#* READING
# Global position
# print('Global position:')
# root[0][0].attrib['x'] = '3'
# print(root[0][0].attrib['x'])

tree.write('/Users/startz/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/train_0_2.bsg')
# add this line "<?xml version="1.0" encoding="utf-8"?>"

with open('/Users/startz/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/train_0_2.bsg', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n' + content)

# Global rotation
# print('\n Global rotation:')
# print(root[0][1].attrib)

# #* all item attributes
# print('\nBlocks:') # Need to start from 3 to get all blocks
# for elem in root[2:]:
#     for subelem in elem:
#         print(subelem.attrib)

#* one specific item's data
# print('\nItem #2 data:')
# print(root[0][1].text)

#* all items data
# print('\nAll item data:')
# for elem in root:
#     for subelem in elem:
#         print(subelem.text)

'''
Before starting execution, find range of things that we can manipulate (e.g machine name block element, coordinates)
Randomize those parameters, save them to a file and run them
Save score to something
Run for 10 min
Save best to a specific file
'''