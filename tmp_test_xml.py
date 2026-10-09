import xml.etree.ElementTree as ET
try:
    ET.parse('src/robot_scene.xml')
    print('XML parse OK')
except Exception as e:
    print(f'XML parse error: {e}')
