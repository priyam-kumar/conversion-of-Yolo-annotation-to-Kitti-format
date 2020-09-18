from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np

class data2kitti():
    def __init__(self, images_dir, labels_dir, kitti_base_dir, kitti_resize_dims):
        self.images_dir = images_dir
        self.labels_dir = labels_dir
        # self.count_mask = category_limit[0]
        # self.count_no_mask = category_limit[1]
        self.kitti_base_dir = kitti_base_dir
        self.kitti_resize_dims = kitti_resize_dims
        
        try:
            os.makedirs(self.kitti_base_dir+'\\train\\images',mode=0o777)
        except:
            print("Directory Already Exists")
            print(kitti_base_dir)
            self.kitti_images = self.kitti_base_dir+str('\\train\\images')
            print(self.kitti_images)
        try:
            os.makedirs(self.kitti_base_dir+ '\\train\\labels',mode=0o777)
        except:
            print("Directory Already Exists")
            self.kitti_labels = self.kitti_base_dir+str('\\train\\labels')
            print(self.kitti_labels)
        
    def get_image_metafile(self, image_file):
        image_name = os.path.splitext(image_file)[0]
        return os.path.join(self.labels_dir, str(image_name+'.txt'))

    def get_total_classes(self, labels_dir):
        self.labels_dir = labels_dir
        category_name = []        
        with open(labels_dir+"/classes.txt", 'r') as classes_file:
            for classes in classes_file:
                category_name.append(classes.replace("\n",""))
        return category_name

    def make_labels(self, image_name, category_names, bboxes):
        # Process image
        file_image = os.path.splitext(image_name)[0]
        img = Image.open(os.path.join(self.images_dir, image_name)).convert("RGB")
        resize_img = img.resize(self.kitti_resize_dims)
        # print(f"images dir {os.path.join(self.kitti_images, file_image + '.jpg')}")
        resize_img.save(os.path.join(self.kitti_images, file_image + '.jpg'), 'JPEG')
        
        # Process labels
        with open(os.path.join(self.kitti_labels, file_image + '.txt'), 'w') as label_file:
            for i in range(0, len(bboxes)):
                resized_bbox = self.resize_bbox(img=img, bbox=bboxes[i], dims=self.kitti_resize_dims)
                out_str = [category_names[i].replace(" ", "")
                           + ' ' + ' '.join(['0'] * 1)
                           + ' ' + ' '.join(['0'] * 2)
                           + ' ' + ' '.join([b for b in resized_bbox])
                           + ' ' + ' '.join(['0'] * 7)
                           + '\n']
                label_file.write(out_str[0])

    def resize_bbox(self, img, bbox, dims):
        img_w, img_h = img.size
        x_min, y_min, x_max, y_max = bbox
        ratio_w, ratio_h = dims[0] / img_w, dims[1] / img_h
        new_bbox = [str(int(np.round(x_min * ratio_w))), str(int(np.round(y_min * ratio_h))), str(int(np.round(x_max * ratio_w))),
                    str(int(np.round(y_max * ratio_h)))]
        return new_bbox


    def get_data_attributes(self,labels_dir):       
        image_extensions = ['.jpeg', '.jpg', '.png']
        _count_mask = 0
        _count_no_mask = 0       
        category_name = self.get_total_classes(labels_dir = labels_dir)
        print(category_name)        
        for image_name in os.listdir(self.images_dir):
            if image_name.endswith('.jpeg') or image_name.endswith('.jpg') or image_name.endswith('.png'):
                labels_txt = self.get_image_metafile(image_file=image_name)
                if os.path.isfile(labels_txt):                    
                    bboxes = []
                    categories= []
                    with open(os.path.join(self.labels_dir, labels_txt), 'r') as label_file:
                        for line in label_file:
                            bbox =list(map(float,line[1:].split()))
                            if(line[0] == "0"):
                                categories.append(category_name[int(line[0])])
                                _count_no_mask += 1
                            elif line[0] == '1':
                                categories.append(category_name[int(line[0])])
                                _count_mask += 1
                            bboxes.append(bbox)
                    if bboxes:
                        self.make_labels(image_name=image_name, category_names=categories, bboxes=bboxes)
        print("Kaggle Dataset: Total Mask faces: {} and No-Mask faces:{}".format(_count_mask, _count_no_mask))
        return _count_mask, _count_no_mask


def main():
    images_dir = 'D:\\demo_mask\\images'
    labels_dir = 'D:\\demo_mask\\labels'
    kitti_base_dir = 'D:\\demo_mask\\kitti_labels'
    kitti_resize_dims = (480,272)
    category_limit = [2,2]
    medical_mask2kitti = data2kitti(images_dir=images_dir, labels_dir=labels_dir,
                                      kitti_base_dir=kitti_base_dir, kitti_resize_dims=kitti_resize_dims)
    medical_mask2kitti.get_data_attributes(labels_dir = labels_dir)

if __name__ == '__main__':
    main()