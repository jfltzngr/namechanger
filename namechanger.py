import os 
import json
from PIL import Image
   
def namechanger(folderpath, remove_exif=None, pref_from_front=True, len_pref=3, len_suf=7):
	"""change the name of files in a folder according to the folders name.
        Args:
		folder: string relative path of the folder
		remove_exif: remove the exifs from the images 
		pref_from_front: Choose whether you want to take the prefix of your filename
					     from the front or rear of your foldername
		len_pref: number of characters you want from your foldername for the prefix of
				  your filename in
		len_suf: number of characters for the suffix
	"""
	os.chdir(folderpath)
	print(os.getcwd()) 
	foldername = os.path.split(folderpath)[-1]
	# In this dict we store the old filename as a key and the new filename as the value:
	old_to_new_dict={}

	for i,f in enumerate(os.listdir()):	 
		# remove the exifs first:
		if remove_exif:	
			try:
				image = Image.open(f)
				image.save(f)
			except:
				print('File {} could not be opened'.format(f))
				pass
		f_name_old, f_ext = os.path.splitext(f)
		# Define prefix:
		if pref_from_front:
			f_name_pref = foldername[:len_pref]
		else:
		    f_name_pref = foldername[-len_pref:]
		# Define suffix:
		f_name_suf = '{num:0{len_suf}d}'.format(num=i, len_suf=len_suf)
		# Add prefix and suffix separated by '_':
		f_name_new = f_name_pref + '_' + f_name_suf
		f_name_new = '{}{}'.format(f_name_new, f_ext)
		old_to_new_dict[f_name_old] = f_name_new
		os.rename(f, f_name_new)

	# create json dict
	dict_name = 'old_to_new_dict_' + foldername  + '.json'
	with open(dict_name, 'w') as json_file:
		json.dump(old_to_new_dict, json_file)



#Standard application:
folderpath=r'01_xyz_input'
# uncomment to call function namechanger:
namechanger(folderpath=folderpath, remove_exif=True, pref_from_front=True, len_pref=2, len_suf=6)

# # Loop through all subfolders in a directory:
# folderpath=r'01_xyz_input'
# os.chdir(folderpath)
# for subfolderpath in os.listdir():	
# 	try:
# 		namechanger(os.path.join(folderpath,subfolderpath), remove_exif=True, pref_from_front=True, len_pref=2, len_suf=6)
# 	except NotADirectoryError:
# 		print('The path "{}" is too hot to handle!'.format(os.path.join(folderpath,subfolderpath)))
# 		pass 