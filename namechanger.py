import os 
import json
from PIL import Image
   
def namechanger(folderpath, pref_from_front=True, len_pref=3, len_suf=7):
	"""change the name of files in a folder according to the folders name.
        Args:
		folderpath: path of the folder (raw string)
		pref_from_front: Choose whether you want to take the prefix of your filename
					     from the front or rear of your foldername (bool)
		len_pref: number of characters you want from your foldername for the prefix of
				  your filename in (int)
		len_suf: number of characters for the suffix (int)
	"""
	os.chdir(folderpath)
	print(os.getcwd())
	foldername = os.path.split(folderpath)[-1]
	# In this dict we store the old filename as a key and the new filename as the value
	old_to_new_dict={}

	for i,f in enumerate(os.listdir()):	 
		f_name_old, f_ext = os.path.splitext(f)
		# Define prefix:
		if pref_from_front:
			f_name_pref = foldername[:len_pref]
		else:
		    f_name_pref = foldername[-len_pref:]
		# Define suffix:
		f_name_suf = '{num:0{len_suf}d}'.format(num=i+1, len_suf=len_suf-1)
		# Add prefix and suffix separated by '_':
		f_name_new = f_name_pref + '_' + f_name_suf
		f_name_new = '{}{}'.format(f_name_new, f_ext)
		old_to_new_dict[f_name_old] = f_name_new
		os.rename(f, f_name_new)

	# create json dict
	dict_name = 'old_to_new_dict_' + foldername + '.json'
	with open(dict_name, 'w') as json_file:
		json.dump(old_to_new_dict, json_file)


def remove_exif(folderpath):
	"""remove the exifs from images in folder.
        Args:
		folderpath: path of the folder (raw string)
	"""
	os.chdir(folderpath)
	print(os.getcwd())
	for imagepath in os.listdir():
		image = Image.open(imagepath)
		image.save(imagepath)

folderpath=r'01_xyz_input'
remove_exif(folderpath=folderpath)
# uncomment to call function namechanger:
#namechanger(folderpath=folderpath, pref_from_front=True, len_pref=3, len_suf=7)




