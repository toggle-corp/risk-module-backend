import os
import subprocess
#import imageio


def create_raster_tile(file, source_id):
    """
    Work flow convert the geotiff file that is in 16-bit to 8-bit for mapbox
    """
    print(file)
    username = 'togglecorp'
    """file = imageio.imread(file)
    file = file / 256
    # now this file will be 8-bit tiff
    file = file.astype('uint8')"""
    # upload this file
    upload_command = f'mapbox upload {username}.data {file}'
    upload = subprocess.Popen(upload_command, stdout=subprocess.PIPE, shell=True)
    output, err = upload.communicate()
    upload_id = output
    print(upload_id, "test")
    create_tileset = f'mapbox datasets create-tileset ckw4px83t06yi21pndbxpnpg5 {username}'
    tileset = os.system(create_tileset)
