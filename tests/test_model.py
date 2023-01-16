from deepface import DeepFace
import numpy as np
import os
import time
from matplotlib import pyplot as plt

image_path='E:\\Codes\\Python_projects\\CV\\Final_project\\test_image'
data_path='E:\\Codes\\Python_projects\\CV\\Final_project\\test_small'
model_names=['VGG-Face','Facenet']
hit_score=[5,3,2,1]
test_type=0
test_epochs=10
test_images=[]
image_names=[]

def normalize(value_list):
    maxn=0
    for value in value_list:
        if value>maxn:
            maxn=value
    result=[]
    for value in value_list:
        result.append(100.0*value/maxn)
    return result
            
for r, d, f in os.walk(image_path): # r=root, d=directories, f = files
    for file in f:
        if ('.jpg' in file.lower()) or ('.png' in file.lower()):
            exact_path = r + "/" + file
            test_images.append(exact_path)
            image_names.append(file.split('.')[0])
            
if test_type==0:
    fname='test_accuracy_result.txt'
    pname0='test_accuracy_distance.png'
    pname1='test_accuracy_precision.png'
    pname2='test_accuracy_socre.png'
    out_file=open(fname,'w')
    p=np.arange(5)
    w=0.45
    move=w/len(model_names)
    for model_choice in range(len(model_names)):
        out_file.write('Testing {}:'.format(model_names[model_choice])) 
        result=DeepFace.find(test_images,data_path,model_name=model_names[model_choice],distance_metric='euclidean',enforce_detection=False,prog_bar=True,silent=True)
        #print(result)
        score_sum=0
        hit_list=[]
        dis_list=[]
        score_list=[]
        cnt=0
        for df in result:
            out_file.write('results for {}:\n'.format(image_names[cnt]))
            l=len(df['identity'])
            hit=0
            hit_cnt=0
            score=0
            for i in range(l):
                if i>4:
                    break
                path=df['identity'][i]
                f=path.split('\\')
                if f[-1].split('/')[0]==image_names[cnt]:
                    if i<4:
                        score+=(hit_score[i])
                    hit+=1
                hit_cnt+=1
                out_file.write('{:2d}:{} {:f}\n'.format(i,f[-1],df['{}_euclidean'.format(model_names[model_choice])][i]))
            score_sum+=score
            score_list.append(score)
            if hit_cnt==0:
                hit_cnt=1
            hit_list.append(hit/hit_cnt)
            dis_list.append(df['{}_euclidean'.format(model_names[model_choice])][0])
            cnt+=1
        print('{} Score: {:d}'.format(model_names[model_choice],score_sum))
        out_file.write('Score: {:d}\n\n'.format(score_sum))
        posx=p-w+move*(model_choice*2+1)
        n_dis_list=normalize(dis_list)
        plt.figure(0)
        plt.bar(posx,n_dis_list,width=w,label=model_names[model_choice])
        for i in range(5):
            plt.text(posx[i],n_dis_list[i],'{:.3f}'.format(dis_list[i]),fontsize=8,ha='center',va='bottom')
        plt.figure(1)
        plt.bar(posx,hit_list,width=w,label=model_names[model_choice])
        for i in range(5):
            plt.text(posx[i],hit_list[i],'{:.0f}%'.format(hit_list[i]*100),fontsize=8,ha='center',va='bottom')
        plt.figure(2)
        plt.bar(posx,score_list,width=w,label=model_names[model_choice])
        for i in range(5):
            plt.text(posx[i],score_list[i],'{:d}'.format(score_list[i]),fontsize=8,ha='center',va='bottom')
        
    out_file.close()
    plt.figure(0)
    plt.ylabel('Minimum Distance')
    plt.xlabel('Test cases')
    plt.legend()
    plt.savefig(pname0)
    plt.figure(1)
    plt.ylabel('Precision')
    plt.xlabel('Test cases')
    plt.legend()
    plt.savefig(pname1)
    plt.figure(2)
    plt.ylabel('Score')
    plt.xlabel('Test cases')
    plt.legend()
    plt.savefig(pname2)
    
    
elif test_type==1:
    fname='test_time_result.txt'
    pname='test_time.png'
    out_file=open(fname,'w')
    plt.figure(0)
    for model_choice in range(len(model_names)): 
        out_file.write('Testing {}:\n'.format(model_names[model_choice])) 
        t0=time.time()
        t1=t0
        times=[]
        for k in range(test_epochs):
            result=DeepFace.find(test_images,data_path,model_name=model_names[model_choice],distance_metric='euclidean',enforce_detection=False,prog_bar=True,silent=True)
            t2=time.time()
            out_file.write('Round {:2d}: {:8f}s\n'.format(k,t2-t1))
            times.append(t2-t1)
            t1=t2
        tt=time.time()-t0
        out_file.write('Total time: {:5f}s\n\n'.format(tt))
        print('{} Total time: {:5f}s'.format(model_names[model_choice],tt))
        plt.plot(range(test_epochs),times,label=model_names[model_choice])
        for i in range(test_epochs):
            plt.text(i,times[i]+0.05,'{:.3f}'.format(times[i]),fontsize=8,ha='center',va='bottom')
    out_file.close()
    plt.figure(0)
    plt.ylabel('Time Used in One Round')
    plt.xlabel('Test cases')
    plt.legend()
    plt.savefig(pname)
    