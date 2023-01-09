import os
import cv2
import glob
import numpy as np
import random
import argparse
from aug import util
from aug import script

parser = argparse.ArgumentParser(description='Contents of Augmentation')

parser.add_argument('-ip','--input_path', required=False, default='../data/te/', help='In-put data(image) path', )
parser.add_argument('-op','--output_path', required=False, default='../data/te2/', help='Out-put data(image) path')

opt = parser.parse_args() 

if __name__ == '__main__':

	script.input_path_defalt = opt.input_path
	script.output_path_defalt = opt.output_path

	sppace = ''

	temp=script.levelChoice()
	script.inputPtah()
	script.outputPath()

	img_files = glob.glob(opt.input_path+'\\*.png')
	cnt = len(img_files)
	idx=0

	itma = True
	count_img = 0
	count_total = 0

	while itma:
		image = cv2.imread(img_files[idx])
		img = image.copy()
		cv2.imshow('images',img)
		cv2.waitKey(0)

		count_aug = 0
		util.all_clear()
		if int(temp) == 1:
			sppace = util.level_1(img)
		if int(temp) == 2:
			sppace = util.level_2(img)
		if int(temp) == 3:
			sppace = util.level_3(img)
		if int(temp) == 4:
			sppace = util.level_4(img )
		for a in sppace:
			cv2.imwrite(opt.output_path+"/img_%d____aug_%d.jpg" % (count_img,count_aug), a)
			print("처리중_%06d" %count_total)
			count_total+=1
			count_aug +=1

		idx += 1
		if idx >= cnt:
			itma = False
		count_img +=1