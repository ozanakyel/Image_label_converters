# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import glob

lut={}
lut["tip1"] =0
lut["tip2"] =1
lut["tip3"] =2
lut["tip4"] =3
lut["tip5"] =4
lut["tip6"] =5
lut["tip7"] =6
lut["tip8"] =7
lut["tip9"] =8
lut["tip10"] =9
lut["tip11"] =10
lut["tip12"] =11
lut["tip12"] =12
lut["tip14"] =13
lut["tip15"] =14
lut["tip16"] =15
lut["tip17"] =16
lut["tip18"] =17
lut["tip19"] =18
lut["tip20"] =19
lut["tip21"] =20
lut["tip22"] =21
lut["tip23"] =22
lut["tip24"] =23
lut["tip25"] =24
lut["tip26"] =25
lut["tip27"] =26
lut["tip28"] =27


def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_xml2yolo( lut ):

    for fname in glob.glob("*.xml"):
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)



def main():
    convert_xml2yolo(lut)


if __name__ == '__main__':
    main()