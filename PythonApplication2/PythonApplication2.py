import numpy as np
for k in range(401,501):
  
    path0="C:/Users/Ryo Koishihara/Documents/GitKraken/FacialLandmarkDetection/FacialLandmarkDetection/gain_"
    t=k
    t_zero = str(t).zfill(8)
    path_name=str(t_zero)
    path_txt=".txt"
    
    f0=open(path0+path_name+path_txt)
    zahyou=[s.strip() for s in f0.readlines()]
    path1="C:/Users/Ryo Koishihara/Downloads/005/annot/"

    real_seido=0
    path_pts=".pts"
    path3="C:/Users/Ryo Koishihara/Documents/GitKraken/FacialLandmarkDetection/FacialLandmarkDetection/speed.txt"
    
    for i in range (1,501):

        s=i
        s_zero = str(s).zfill(6)
        real_path=path1+str(s_zero)+path_pts
        f=open(real_path)
        zahyou2=[s.strip() for s in f.readlines()]
        seido=0
        eye_x=0
        eye_y=0
        for j in range(1,69):
            za=zahyou[68*(i-1)+j-1].split(",")
            za2=zahyou2[2+j].split()
            seido+=np.linalg.norm(np.array([float(za[0])-round(float(za2[0])),float(za[1])-round(float(za2[1])) ]))

            if(j>=37 and j<=42):
                eye_x+=round(float(za2[0]))
                eye_y+=round(float(za2[1]))
            if(j>=43 and j<=48):
                eye_x-=round(float(za2[0]))
                eye_y-=round(float(za2[1]))

   
        seido/= (np.linalg.norm(np.array([eye_x/6,eye_y,6]))*68)

        real_seido+=seido
    

        f.close()

    real_seido/=(500)

    print(real_seido)
    f0.close()