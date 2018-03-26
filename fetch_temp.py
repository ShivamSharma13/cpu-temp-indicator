import os

def reach_thermal_file():
	try:
		os.chdir('/sys/')
	except FileNotFoundError:
		print('Could not find a desired file structure. Tested for Ubuntu 16.04 Only.')
		return 0
	sys_path = os.path.abspath(os.curdir)
	#Might want to look for other possible branches possessing thermal section in ubuntu.
	class_path = os.path.join(sys_path , 'class')
	try: 
		os.chdir(class_path)
	except FileNotFoundError:
		print('Could not find a desired file structure. Tested for Ubuntu 16.04 Only.')
		return 0
	sub_directories = os.listdir()
	possible_thermal_directory = list()
	for sub_directory in sub_directories:
		if 'thermal' in sub_directory:
			possible_thermal_directory.append(os.path.join(os.curdir , sub_directory))
	if len(possible_thermal_directory) == 1:
		os.chdir(possible_thermal_directory[0])
	else:
		return 0
	thermal_sub_directories = os.listdir()
	possible_zones = list()
	'''
	Expected Directory Structure
	
	--sys
		|
	----class
			|
	--------thermal
				|
	------------thermal_zone0
	------------thermal_zone1	
	------------thermal_zone2
	------------thermal_zone3
	'''
	for root, dirs, files in os.walk(os.path.abspath(os.curdir)):
		for directory in dirs:
			if 'thermal' in directory:
				directory_path = os.path.join(os.path.abspath(os.curdir), directory)
				for sub_root, sub_dirs, sub_files in os.walk(directory_path):
					if 'type' in sub_files:
						with open (os.path.join(directory_path, 'type')) as file:
							text = file.read()
							if 'x86_pkg_temp' not in text:
								continue
					if 'temp' in sub_files:
						#print(os.path.join(directory_path, 'temp'))
						return (os.path.join(directory_path, 'temp'))

if __name__ == '__main__':
	reach_thermal_file()