import os, datetime, time

from PIL import Image



################## make direc #########################################
def makedirec():
    global naljja, naldirec
    
    naljja = datetime.datetime.now()
    naldirec = naljja.strftime('%Y%m%d_%H%M%S')
    os.makedirs(naldirec)
#######################################################################



################## rotate_txt      ####################################
def rotate_txt():
        original_image = Image.open(filename)

        original_image = original_image.rotate(360 - x_degree, expand = True, fillcolor = 'white')

        file_front_name, file_back_name = os.path.splitext(filename)

        original_image.save(os.path.join(naldirec, file_front_name + '.png'))

        original_image.close()   
#######################################################################



################## exist file #########################################
def exist_file():
    if (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp') or filename.lower().endswith('.pcx')):
        return True
    

#######################################################################



################## how degree #########################################
def how_degree():
    global x_degree


    degree_in_file = open('degree.txt')
    x_degree = float(degree_in_file.read())

#######################################################################
    


################## main       #########################################

naljja = 0
naldirec = 0
makedirec()

x_degree = 0
how_degree()

for filename in os.listdir('.'):
    if exist_file():    
        rotate_txt()

#######################################################################
