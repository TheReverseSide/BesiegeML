import random
import xml.etree.ElementTree as ET\


PATH = "d:\\Games\\steamapps\\common\\Besiege\\Besiege_Data\\SavedMachines\\"

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
    with open(full_filename, 'r+') as stream:
        content = stream.read()
        stream.seek(0, 0)
        stream.write('<?xml version="1.0" encoding="utf-8"?>' + '\n\n' + content)


def manipulate_save_object(save_obj):
    print(f"manipulate_save_object({save_obj})")
    # print(save_obj.getroot().attrib['name'])
    root = save_obj.getroot()
    root.attrib['name'] = "xml_generated"

    # Change position of block with ID 15
    for block in root.iter('Block'):
        if block.attrib['id'] == '31':
            pos = next(block.iter('Position'))
            print(pos.tag, pos.attrib)
            pos.attrib['x'] = f'{random.uniform(-8.0, 8.0):.2}'
            pos.attrib['z'] = f'{random.uniform(-8.0, 8.0):.2}'


def get_save_object(save_name):
    print(f"get_save_object({save_name})")
    tree = ET.parse(PATH + f"{save_name}.bsg")
    return tree


def main():
    save_obj = get_save_object('xml_original')
    manipulate_save_object(save_obj)
    save_as_xml(save_obj)


if __name__ == "__main__":
    main()
