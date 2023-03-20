import sys
import pytsk3

# Get the name of the disk image from command line argument
image_filename = sys.argv[1]

# Create an Img_Info object to represent the image file
disk_image = pytsk3.Img_Info(image_filename)

# Create a Volume_Info object to access the partitions
volume_info = pytsk3.Volume_Info(disk_image)

# Loop through each partition and print its attributes
for partition in volume_info:
    print("Partition:", partition.addr)
    print("Description:", partition.desc)
    print("Start sector:", partition.start)
    print("Length:", partition.len)
    print()


