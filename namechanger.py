import os 
   
def namechanger(folder='01_xyz', pref_from_front=True, len_pref=2, len_suf=7):
	"""change the name of files in a folder according to the folder's name.
        Args:
		folder: 	 relative path of the folder (str)
		pref_from_front: Choose whether you want to take the prefix of your filename
			 	 from the front or rear of your foldername (bool_ex)
		len_pref: 	 number of characters you want from your foldername for the prefix of
	                  	 your filename in (int)
		len_suf: 	 number of characters for the suffix (int)
	"""
	os.chdir(folder)
	print(os.getcwd())

	for i,f in enumerate(os.listdir()):	 
		f_name, f_ext = os.path.splitext(f)
		# Define prefix:
		if pref_from_front:
			f_name_pref = folder[:len_pref]
		else:
			f_name_pref = folder[-len_pref:]
		# Define suffix:
		f_name_suf = '{num:0{len_suf}d}'.format(num=i+1, len_suf=len_suf-1)
		# Add prefix and suffix separated by '_':
		f_name = f_name_pref + '_' + f_name_suf
		new_name = '{}{}'.format(f_name, f_ext)
		os.rename(f, new_name)

namechanger(folder='01_xyz_input', pref_from_front=True, len_pref=2, len_suf=5)
