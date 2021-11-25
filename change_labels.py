"""
##      crop.py
##      version 1
##      python --version : 3.6.13
##      cv2.__version__ : 4.5.4-dev
##      pandas.__version__ : 0.25.3
##      tqdm.__version__ : 4.62.3
##      numpy.__version__ : 1.17.3
##      emailremoved@ ( ozan.akyel54@gmail.com )
##      @author : Ozan AKYEL, Mehmet OKUYAR, A. Mucahit TARAKCI

"""
import pandas as pd
import glob
from tqdm import tqdm
import numpy as np
import os

#===== .txt yolu girilecek ==================
txt_path = "C:/Users/MEHMET/Desktop/veri" 

datas = glob.glob(txt_path+"/*.txt")
try:
    new_path = os.path.join(txt_path, "changed labels")
    os.mkdir(new_path)
except:
    pass

for i in tqdm(range(len(datas))):
    
    name = datas[i].split('\\')[-1]
    save_path = new_path+'/'+name
    
    try:
        data = pd.read_csv(datas[i], sep=" ", header=None)
    
   
        for i in range(1,len(data.loc[0:,:0])+1):
            row = data.iloc[i-1:i,:1].values
            row = int(row)

            if row == 15: # değişecek etiket bilgisi
                data.iloc[i-1:i,:1] = 0 # hedef etiket bilgisi


        with open(save_path,"w") as f:
            np.savetxt(f, data, fmt=["%d","%f","%f","%f","%f"])
        
    except:
        pass