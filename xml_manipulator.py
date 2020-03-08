import xml.etree.ElementTree as ET\


PATH = "d:\\Games\\steamapps\\common\\Besiege\\Besiege_Data\\SavedMachines\\"


#* READING
# Global position
# print('Global position:')
# root[0][0].attrib['x'] = '3'
# print(root[0][0].attrib['x'])

# tree.write('/Users/startz/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/train_0_2.bsg')
# # add this line "<?xml version="1.0" encoding="utf-8"?>"

# with open('/Users/startz/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/train_0_2.bsg', 'r+') as f:
#     content = f.read()
#     f.seek(0, 0)
#     f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n' + content)

# Global rotation
# print('\n Global rotation:')j
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

def print_save(save_obj):
    print(f"print_save({save_obj})")
    for child in save_obj.getroot().iter():
        print(child.tag, child.attrib)


def save_as_xml(save_obj):
    print(f"save_as_xml({save_obj})")
    filename = save_obj.getroot().attrib['name']
    full_filename = PATH + f"{filename}.bsg"
    save_obj.write(full_filename)

    #add header
    with open(full_filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n\n' + content)


def manipulate_save_object(save_obj):
    print(f"manipulate_save_object({save_obj})")
    # print(save_obj.getroot().attrib['name'])
    root = save_obj.getroot()
    root.attrib['name'] = "xml_generated"
    
    # Change position of block with ID 15
    for block in root.iter('Block'):
        
        if block.attrib['id'] == '15':
            pos = next(block.iter('Position'))
            print(pos.tag, pos.attrib)
            pos.attrib['y'] = '0.5'
            pos.attrib['z'] = '0'
    
    
    # root.attrib['Blocks'] = 


def get_save_object(save_name):
    print(f"get_save_object({save_name})")
    tree = ET.parse(PATH + f"{save_name}.bsg")
    root = tree.getroot()
    # print(root.attrib['name'])
    # print_save(root)
    return tree

def main():
    save_obj = get_save_object('xml_original')
    manipulate_save_object(save_obj)
    save_as_xml(save_obj)


if __name__ == "__main__":
    main()
