import os
import sys
import shutil
from os import getcwd, makedirs
from os.path import join,exists
from wand.image import Image, Color


def convert_pdf(filename, output_path, resolution=300):
    """ Convert a PDF into images.

        All the pages will give a single png file with format:
        {pdf_filename}-{page_number}.png

        The function removes the alpha channel from the image and
        replace it with a white background.
    """
    all_pages = Image(filename=filename, resolution=resolution)
    for i, page in enumerate(all_pages.sequence):
        with Image(page) as img:
            img.format = 'tiff'
            img.background_color = Color('white')
            img.alpha_channel = 'remove'
            image_filename = os.path.splitext(os.path.basename(filename))[0]
            image_filename = '{}-{}.tiff'.format(image_filename, i)
            image_filename = join(output_path, image_filename)

            img.save(filename=image_filename)
if __name__=="__main__":
	#filename=raw_input().strip()
	filename = "n-400"
	img_path_300 = join(getcwd(),"300TIFF")
	img_path_200 = join(getcwd(),"200TIFF")
	if not exists(img_path_300):
		makedirs(img_path_300)
	if not exists(img_path_200):
		makedirs(img_path_200)
	convert_pdf(filename+".pdf",img_path_300,300)

	convert_pdf(filename+".pdf",img_path_200,200)
	print "Done"