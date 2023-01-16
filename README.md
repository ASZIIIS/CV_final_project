# CV_final_project

## Introduction

This is the final project for CS308 Computer Vision in Sustech.

It implements a face recognition system providing 3 modes to users via a GUI interface:

|            | Mode1                                                        | Mode2                                                        | Mode3                                                        |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Name**   | Face Recognition                                             | Face Comparison                                              | Face Analysis                                                |
| **Input**  | an image or video                                            | two images or videos                                         | an image or video                                            |
| **Output** | corresponding personal information from VGG2 images dataset  | similarity between the two faces                             | estimated information including age, gender, race, and emotion |
| **GUI**    | ![](D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116183806888.png) | ![](D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116183832661.png) | ![](D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116183857228.png) |


The following are the setups and usages of this project.



## Set up

The setting up is provided in *environment.yml*, while you can also use the command below to download the packages.

```
pip install {module name}
```

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {module name}
```

 



## Usage

After the environment setting, you can directly run main.py and enter the welcoming page.

Any of the three modes can be selected upon your preference.

<img src="D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116181505531.png" style="zoom: 67%;" /> 

The interfaces have slight differences, but GUI functionalities are generally the same, as illustrated bellow.

<img src="D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116184409187.png" style="zoom:67%;" /> 

When first clicking the **Start** button, it calls the downloading procedure of CNN weights.h5 files.

<img src="D:\Grade3\CS308 ComputerVision\proj\CV_final_project\images\image-20230116175755777.png" style="zoom: 50%;" /> 

**Note:** The weight files are too big to be added to our repository, so you may have to download it yourself and may try a proxy in case of network congestion.



**Contributors:**

ASZIIIS    [ASZIIIS (github.com)](https://github.com/ASZIIIS)

starquakee   [starquakee (starquakee) (github.com)](https://github.com/starquakee)

afovo   [afovo (github.com)](https://github.com/afovo)

