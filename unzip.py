import glob
import sys
import os
import shutil



input_zip_file = sys.argv[1]
tmp_directory = sys.argv[2]
output_directory = sys.argv[3]

if not os.path.exists(tmp_directory):
	os.makedirs(tmp_directory)

if not os.path.exists(output_directory):
	os.makedirs(output_directory)

# Extract zip file to tmp_directory
return_val = os.system(f"""unzip {input_zip_file} -d {tmp_directory}""")
if return_val != 0:
	print("Fail to unzip images")
	sys.exit(-1)

img_extenstions = ["*.jpeg", "*.png", "*.jpg", "*.JPG", "*.JPEG"]
images = []

for img_extenstion in img_extenstions:
	glob_pattern = f"{tmp_directory}/**/{img_extenstion}"
	# print("glob pattern: ", glob_pattern)
	images.extend(glob.glob(glob_pattern, recursive=True))
	# print(images)

for image in images:
	filename = os.path.basename(image)
	shutil.copy(image, f"{output_directory}/{filename}")

print(os.system(f"ls -l {output_directory}"))