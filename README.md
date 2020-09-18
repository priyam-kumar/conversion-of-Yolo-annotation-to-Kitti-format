# conversion-of-Yolo-annotation-to-Kitti-format
Below is the README for this repo for windows.

collect the dataset from your favourite website. 
This repo provide the dataset for demo purpose which contain images of both mask, no_mask and labels in the txt format for YOLO annotation:

download the dataset provided in this repo 

Their are two file 
 -> main.py
 ->data2kitti.py
 
open the cmd and run the below command
 > cd <downloaded folder>\Yolo_to_kitti_converter
 
 Now run the 
 > python main.py --help
 
 output:
 usage: main.py [-h] [--dataset-path DATASETS_PATH] [--kitti-base-path KITTI_BASE_PATH]
               [--input-dims_width INPUT_DIMS_WIDTH] [--input-dims_height INPUT_DIMS_HEIGHT]

optional arguments:
  -h, --help            show this help message and exit
  --dataset-path DATASETS_PATH
                        path to dataset
  --kitti-base-path KITTI_BASE_PATH  [default will be dataset path]
                        path to save converted data set
  --input-dims_width INPUT_DIMS_WIDTH  [default= 960]
                        input dimensions by width
  --input-dims_height INPUT_DIMS_HEIGHT [default = 544]
                        input dimensions by height

You have to provide the path of the dataset folder by writing the following command 
> python main.py --dataset-path <path to dataset> --kitti-base-path <path to save converted dataset> --input-dims_width <width> --input-dims_width<height>
  
After running above cmd you get your kitti dataset

