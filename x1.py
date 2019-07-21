import xml.etree.ElementTree as ET
import xml.dom
import xml.sax
import xml.parsers

tree = ET.parse('ccountry.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    
for neighbor in root.iter('neighbor'):
     print(neighbor.attrib)

for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)
     
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output.xml')

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output.xml')

# Top-level elements
al=root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
cl=root.findall("./country/neighbor")
for ne in cl:
    print(ne.attrib)
    

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
for yr in root.findall("./*[@name='Singapore']/year"):
    print(yr.tag,yr.text)


# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

xml_str="""<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
"""

#root = ET.parse('actors.xml')
root=ET.fromstring(xml_str)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)
        
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print (name.text)
    for char in actor.findall('role:character', ns):
        print (' |-->', char.text)
