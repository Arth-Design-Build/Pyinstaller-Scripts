import shutil
import os
import sys
import os.path

# Location to where you want to copy the files
path = R"C:\Users\$USERNAME\AppData\Roaming\Autodesk\Revit\Addins\2019"
exp_var = os.path.expandvars(path)
dest_folder = exp_var

# List of files you want to copy
file_list = ['MyRevitCommands.dll', 'MyRevitCommands.pdb', 'MyRevitCommands.addin', 'EPPlus.dll', 'EPPlus.xml', 'EPPlus.System.Drawing.dll', 'EPPlus.Interfaces.dll', 'Microsoft.IO.RecyclableMemoryStream.dll', 'Microsoft.IO.RecyclableMemoryStream.xml']

for file_name in file_list:
    source_path = sys._MEIPASS + '\\' + file_name
    dest_path = os.path.join(dest_folder, file_name)
    shutil.copy(source_path, dest_path)

#pyinstaller --onefile --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\MyRevitCommands.dll;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\MyRevitCommands.pdb;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\MyRevitCommands.addin;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\EPPlus.dll;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\EPPlus.xml;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\EPPlus.System.Drawing.dll;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\EPPlus.Interfaces.dll;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\Microsoft.IO.RecyclableMemoryStream.dll;." --add-data "C:\Users\ASUS\AppData\Roaming\Autodesk\Revit\Addins\2019\Microsoft.IO.RecyclableMemoryStream.xml;." adb_scripts_2019.py