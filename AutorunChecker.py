import os, shutil

os.chdir('C:\\')

# for file in os.listdir():
# 	for filename in os.listdir():
# 		if filename.endswith('.autorun') or filename.endswith('.txt'):
# 			print(filename)
dir = ['C:\\', 'D:\\']
for i in range(0, 2):
	# print(i)
	if i == 0:
		print('C:\\')
	else:
		print('D:\\')
	for folders, subfolders, files in os.walk(dir[i]):
		for file in files:
			if file.endswith('.autorun'):
				print(file)
