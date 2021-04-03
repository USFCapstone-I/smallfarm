# get fastai library ---------------------------------------------------------
!pip install -Uqq fastbook
import fastbook
from fastbook import *
from fastai import *
from fastai.vision.widgets import *
import time

# load the models -------------------------------------------------------------
cattle_model = load_learner('HERE') # put the path of the .pkl file 
fly_model = load_learner('HERE')    # put the path of the .pkl file
vocab1 = cattle_model.dls.vocab     # vocab1 == ['multiple', 'none', 'single']
vocab2 = fly_model.dls.vocab        # vocab2 == ['fly', 'no_fly']

# take pictures --------------------------------------------------------------- <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TO-DO
'use webcam/IP camera to take a picture and save the url'
dest = 'HERE' # 'HERE' == '/folder_path/file_name.jpg'
urls = 'HERE' # 'HERE' == url of the image to download
download_url(urls,dest)
im = Image.open(dest)
im.to_thumb(128,128) # display image

# analyze image ---------------------------------------------------------------
result1 = cattle_model.predict('HERE') # 'HERE' == dest or put path of the image if not downloaded
                                       # result1 == ('none', tensor(1), tensor([5.1471e-18, 1.0000e+00, 1.3131e-10]))

# converting accuracy from string to a float
buf = str(result1[2])
idx = buf.find('[')
accur = buf[idx+1:-2]
accur = accur.split(',')
for i in range(2):
  accur[i] = float(accur[i])

# check if accuracy is greater than 80% in order to run image in the fly_model ----

if vocab1[2]==result1[0]:
    print('single')
    
    if 10*(1-accur[2])>2:
        print("disregard")
        #send info to NuvIoT
        #send image to NuvIoT for trainning purposes
    
    elif 10*(1-accur[2])<2:
        print("run image into fly_model")
        result2 = fly_model.predict('HERE') # 'dest' or put path of the image if not downloaded
        
        if result2[0]=='fly':
            # converting accuracy into a float
            buf2 = str(result2[2])
            idx2 = buf2.find('[')
            accur2 = buf2[idx2+1:-2]
            accur2 = accur2.split(',')
            for i in range(2):
                accur2[i] = float(accur2[i])
            #-------------------------------
            print("fly detected")
            print("accuracy: " + str(accur2[0]))

            # WILL THE PREVIOUS CODE WORK? for ----------------------------------- <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TO-DO
            #send info to NuvIoT
            #send image to NuvIoT
            #send command to spray cattle

elif vocab1[0]==result1[0]:
    print('multiple')
    
    if 10*(1-accur[0])>2:
        print("disregard")
        #send info to NuvIoT
        #send image to NuvIoT for trainning purposes

    elif 10*(1-accur[0])<2:
        print("run image into fly_model")
        result2 = fly_model.predict('HERE') # put path of the image
    
        if result2[0]=='fly':
            # converting accuracy into float
            buf2 = str(result2[2])
            idx2 = buf2.find('[')
            accur2 = buf2[idx2+1:-2]
            accur2 = accur2.split(',')
            for i in range(2):
                accur2[i] = float(accur2[i])
            #-------------------------------
            print("fly detected")
            print("accuracy: " + str(accur2[0]))
            
            # WILL THE PREVIOUS CODE WORK? for --------------------------- <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TO-DO
                #send info to NuvIoT 
                #send image to NuvIoT
                #send command to spray cattle
                # ALSO line 41 & 69
    
elif vocab1[1]==result1[0]:
    print('none')
    
    if 10*(1-accur[1])>2:
        print("disregard")
        #send info to NuvIoT ?
        #send image to NuvIoT for trainning purposes ?

    elif 10*(1-accur[1])<2:
        print("run image into fly_model")
        result2 = fly_model.predict('HERE') # put path of the image
    
        if result2[0]=='fly':
            # converting accuracy into float
            buf2 = str(result2[2])
            idx2 = buf2.find('[')
            accur2 = buf2[idx2+1:-2]
            accur2 = accur2.split(',')
            for i in range(2):
                accur2[i] = float(accur2[i])
            #-------------------------------
            print("fly detected")
            print("accuracy: " + str(accur2[0]))
            
            # WILL THE PREVIOUS CODE WORK? for --------------------------- <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TO-DO
                #send info to NuvIoT 
                #send image to NuvIoT
                #send command to spray cattle
                # ALSO line 41 & 69 

time.sleep(15) // 15 seconds