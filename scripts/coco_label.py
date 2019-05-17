import os
import json
from os import listdir, getcwd
from os.path import join

FILEDIR=os.path.dirname(os.path.abspath(__file__))

classes = ["person","bicycle","car","motorcycle","airplane","bus","train",
           "truck","boat","traffic light","fire hydrant","stop sign","parking meter",
           "bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra",
           "giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis",
           "snowboard","sports ball","kite","baseball bat","baseball glove","skateboard",
           "surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon",
           "bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza",
           "donut","cake","chair","couch","potted plant","bed","dining table","toilet","tv",
           "laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink",
           "refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]

#box form[x,y,w,h]
def convert(size,box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = box[0]*dw
    y = box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    return (x,y,w,h)

def convert_annotation():
    with open('../coco/annotations/instances_train2017.json','r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open('/home/shawnliu/workPlace/expG-darknet/coco/coco_label/%s.txt'%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = list(filter(lambda item3: item3['id'] == category_id,data['categories']))
            print(type(value1))
            #print(type(value1[0]))
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()

if __name__ == '__main__':
    #convert_annotation()
    file_dir="/home/shawnliu/workPlace/expG-darknet/coco/images/train2017/"
    list_file = open('/home/shawnliu/workPlace/expG-darknet/coco/train2017.txt', 'w')
    for root, dirs, files in os.walk(file_dir): 
        for file in files: 
            list_file.write(str(file_dir)+str(file)+'\n')
