from data2kitti import data2kitti
import os
import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument('--dataset-path', dest='datasets_path',
                                 help='path to dataset', type=str)
parser.add_argument('--kitti-base-path', dest='kitti_base_path',
                                 help='path to save converted data set', type=str)
parser.add_argument('--input-dims_width', dest='input_dims_width', default=960,
                                 help = 'input dimensions by width', type = int)
parser.add_argument('--input-dims_height', dest='input_dims_height', default=544,
                                 help='input dimensions by height', type=int)

args = parser.parse_args()
dataset_base_dir = args.datasets_path
kitti_base_dir = args.kitti_base_path
if(kitti_base_dir == None):
	kitti_base_dir = os.path.join(dataset_base_dir,"kitti_data")
kitti_resize_dims = (args.input_dims_width, args.input_dims_height)

total_masks, total_no_masks = 0, 0
count_masks, count_no_masks = 0, 0

images_dir = os.path.join(dataset_base_dir,'images')
labels_dir = os.path.join(dataset_base_dir,'labels')
kitti_dataset = data2kitti(images_dir=images_dir, labels_dir=labels_dir, kitti_base_dir=kitti_base_dir, kitti_resize_dims=kitti_resize_dims)
count_masks, count_no_masks = kitti_dataset.get_data_attributes(labels_dir = labels_dir)