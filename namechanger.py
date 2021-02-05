import os 
   
def namechanger(folder='01_xyz', pref_from_front=True, len_pref=2, len_suf=7):
	"""change the name of files in a folder according to the folders name.
        Args:
		folder: string relative path of the folder
		pref_from_front: Choose whether you want to take the prefix of your filename
					     from the front or rear of your foldername
		len_pref: number of characters you want from your foldername for the prefix of
				  your filename in
		len_suf: number of characters for the suffix
	"""
	os.chdir(folder)
	print(os.getcwd())

	for i,f in enumerate(os.listdir()):	
		f_name, f_ext = os.path.splitext(f)

		if pref_from_front:
			f_name_pref = folder[:len_pref]
		else:
			f_name_pre = folder[len_pref:]
		f_name_suf = '{num:0{len_suf}d}'.format(num=i+1, len_suf=len_suf-1)
		f_name = f_name_pref + '_' + f_name_suf

		new_name = '{}{}'.format(f_name, f_ext)
		os.rename(f, new_name)

namechanger(folder='01_xyz', len_suf=5)

 

