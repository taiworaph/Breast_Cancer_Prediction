from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def main():
    
    ### Get the location to store the csv file after download from the USF webpage
    print("Please file save-2-location has to be in the format--\"~/Desktop/Mammogram_Labels.csv\"")
    Location = input("Please can you put the location for file download: ")
    if len(list(Location) == 0:
        print("Please a save-2-location is needed - Goodbye!")
        break
    
    
    CancerTypes = ["normals/", "benigns/", "cancers/"]
    NormalFiles = ["normal_01/","normal_02/","normal_03/","normal_04/","normal_05/","normal_06/","normal_07/","normal_08/","normal_09/","normal_10/","normal_11/","normal_12/"]
    CancerFiles = ["cancer_01/","cancer_02/","cancer_03/","cancer_04/","cancer_05/","cancer_06/","cancer_07/","cancer_08/","cancer_09/","cancer_10/","cancer_11/","cancer_12/","cancer_13/","cancer_14/","cancer_15/"]
    BenignFiles = ["benign_01/","benign_02/","benign_03/","benign_04/","benign_05/","benign_06/","benign_07/","benign_08/","benign_09/","benign_10/","benign_11/","benign_12/","benign_13/","benign_14/"]
    url1 = "http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/"
    url2 = "overview.html"



    filename = []
    date_of_study = []
    patient_age = []
    film = []
    film_type = []
    Density = []
    date_digitized = []
    digitizer = []

    File_Name1 = []
    Total_Abnormality =[]
    Lesion_type = []
    #Assesment = []
    Subtlety = []
    Pathology = []


    File_Name2 = []
    Total_Abnormality2 = []
    Lesion_Type2 = []
    #Assesment2 = []
    Subtlety2 =[]
    Pathology2 = []


    File_Name3 = []
    Total_Abnormality3 = []
    Lesion_Type3 = []
    #Assesment3 = []
    Subtlety3 =[]
    Pathology3 = []


    File_Name4 = []
    Total_Abnormality4 = []
    Lesion_Type4 = []
    #Assesment4 = []
    Subtlety4 =[]
    Pathology4 = []

    for ii in CancerTypes:
        if ii == "normals/":
            for iii in NormalFiles:
                html4 = urlopen(url1+ii+iii+url2)
                bsObj1 = BeautifulSoup(html4)
                Links3 = []
                for link in bsObj1.findAll("a", {}): 
                    if 'href' in link.attrs: 
                        Links3.append(link.attrs['href'])

                for iv in Links3[1:]:
                    htmlReal = urlopen(url1+ii+iii+iv)
                    bsObjR = BeautifulSoup(htmlReal)
                    dataFrame = bsObjR.findAll("pre",{})

                    YY = str(dataFrame).split('\n')[2:11]

                    filename.append((YY[0].split(' '))[1])
                    date_of_study.append((YY[1].split(' ', 1))[1])
                    patient_age.append((YY[2].split(' '))[1])
                    film_type.append((YY[4].split(' '))[1])
                    Density.append((YY[5].split(' '))[1])
                    date_digitized.append((YY[6].split(' ', 1))[1])
                    digitizer.append((YY[7].split(' '))[1])

                    #Appending N/A to other values so that there is continuity#
                    File_Name1.append("NA")
                    Total_Abnormality.append("NA")
                    Lesion_type.append("NA")
                    #Assesment.append("N/A")
                    Subtlety.append("NA")
                    Pathology.append("NA")


                    File_Name2.append("NA")
                    Total_Abnormality2.append("NA")
                    Lesion_Type2.append("NA")
                    #Assesment2.append("N/A")
                    Subtlety2.append("NA")
                    Pathology2.append("NA")


                    File_Name3.append("NA")
                    Total_Abnormality3.append("NA")
                    Lesion_Type3.append("NA")
                    #Assesment3.append("N/A")
                    Subtlety3.append("NA")
                    Pathology3.append("NA")


                    File_Name4.append("NA")
                    Total_Abnormality4.append("NA")
                    Lesion_Type4.append("NA")
                    #Assesment4.append("N/A")
                    Subtlety4.append("NA")
                    Pathology4.append("NA")


        elif ii == "benigns/":
            ix = CancerTypes[1]
            for iii in BenignFiles:
                URL = str(url1)+ ix + str(iii)
                print(URL)
                html4 = urlopen(URL+url2)
                bsObj1 = BeautifulSoup(html4)
                Links3 = []
                for link in bsObj1.findAll("a", {}): 
                    if 'href' in link.attrs: 
                        Links3.append(link.attrs['href'])

                for iv in Links3[2:]:
                    htmlReal = urlopen(URL+iv)
                    bsObjR = BeautifulSoup(htmlReal)
                    dataFrame = bsObjR.findAll("pre",{})

                    YY = str(dataFrame).split('\n')[2:11]
                    YYY = []
                    for ii in dataFrame:
                        iii = ii.get_text()
                        YYY.append(str(iii).split('\n'))

                    if len(YYY) == 3:
                        print(URL+iv)
                        YYX= YYY[0][2:11]
                        filename.append((YYX[0].split(' '))[1])
                        date_of_study.append((YYX[1].split(' ', 1))[1])
                        patient_age.append((YYX[2].split(' '))[1])
                        film_type.append((YYX[4].split(' '))[1])
                        Density.append((YYX[5].split(' '))[1])
                        date_digitized.append((YYX[6].split(' ', 1))[1])
                        digitizer.append((YYX[7].split(' '))[1])

                        YYZ= YYY[1][1:10]
                        File_Name1.append((YYZ[0].split(' '))[1])
                        Total_Abnormality.append((YYZ[2].split(' '))[1])
                        Lesion_type.append((YYZ[4].split(' ', 1))[1])
                        #Assesment.append((YYZ[5].split(' '))[1])
                        Subtlety.append((YYZ[6].split(' '))[1])
                        Pathology.append((YYZ[7].split(' '))[1])

                        YYA = YYY[2][1:10]
                        File_Name2.append((YYA[0].split(' '))[1])
                        Total_Abnormality2.append((YYA[2].split(' '))[1])
                        Lesion_Type2.append((YYA[4].split(' ', 1))[1])
                        #Assesment2.append((YYA[5].split(' '))[1])
                        Subtlety2.append((YYA[6].split(' '))[1])
                        Pathology2.append((YYA[7].split(' '))[1])
                        #Appending N/A to other values so that there is continuity#


                        File_Name3.append("NA")
                        Total_Abnormality3.append("NA")
                        Lesion_Type3.append("NA")
                        #Assesment3.append("N/A")
                        Subtlety3.append("NA")
                        Pathology3.append("NA")


                        File_Name4.append("NA")
                        Total_Abnormality4.append("NA")
                        Lesion_Type4.append("NA")
                        #Assesment4.append("N/A")
                        Subtlety4.append("NA")
                        Pathology4.append("NA")    

                    elif len(YYY) == 5:
                        print(URL+iv)
                        YYX= YYY[0][2:11]
                        filename.append((YYX[0].split(' '))[1])
                        date_of_study.append((YYX[1].split(' ', 1))[1])
                        patient_age.append((YYX[2].split(' '))[1])
                        film_type.append((YYX[4].split(' '))[1])
                        Density.append((YYX[5].split(' '))[1])
                        date_digitized.append((YYX[6].split(' ', 1))[1])
                        digitizer.append((YYX[7].split(' '))[1])

                        YYZ= YYY[1][1:10]
                        File_Name1.append((YYZ[0].split(' '))[1])
                        Total_Abnormality.append((YYZ[2].split(' '))[1])
                        Lesion_type.append((YYZ[4].split(' ', 1))[1])
                        #Assesment.append((YYZ[5].split(' '))[1])
                        Subtlety.append((YYZ[6].split(' '))[1])
                        Pathology.append((YYZ[7].split(' '))[1])

                        YYA = YYY[2][1:10]
                        File_Name2.append((YYA[0].split(' '))[1])
                        Total_Abnormality2.append((YYA[2].split(' '))[1])
                        Lesion_Type2.append((YYA[4].split(' ', 1))[1])
                        #Assesment2.append((YYA[5].split(' '))[1])
                        Subtlety2.append((YYA[6].split(' '))[1])
                        Pathology2.append((YYA[7].split(' '))[1])

                        YYB = YYY[3][1:10]
                        File_Name3.append((YYB[0].split(' '))[1])
                        Total_Abnormality3.append((YYB[2].split(' '))[1])
                        Lesion_Type3.append((YYB[4].split(' ', 1))[1])
                        #Assesment3.append((YYB[5].split(' '))[1])
                        Subtlety3.append((YYB[6].split(' '))[1])
                        Pathology3.append((YYB[7].split(' '))[1])

                        YYC = YYY[4][1:10]
                        File_Name4.append((YYC[0].split(' '))[1])
                        Total_Abnormality4.append((YYC[2].split(' '))[1])
                        Lesion_Type4.append((YYC[4].split(' ', 1))[1])
                        #Assesment4.append((YYC[5].split(' '))[1])
                        Subtlety4.append((YYC[6].split(' '))[1])
                        Pathology4.append((YYC[7].split(' '))[1])


        elif ii == "cancers/":
            ixx = CancerTypes[2]
            for iii in CancerFiles:
                URL1 = str(url1)+ ixx + str(iii)
                print(URL1)
                html4 = urlopen(URL1+url2)
                bsObj1 = BeautifulSoup(html4)
                Links3 = []
                for link in bsObj1.findAll("a", {}): 
                    if 'href' in link.attrs: 
                        Links3.append(link.attrs['href'])

                for iv in Links3[2:]:
                    htmlReal = urlopen(URL1+iv)
                    bsObjR = BeautifulSoup(htmlReal)
                    dataFrame = bsObjR.findAll("pre",{})

                    YY = str(dataFrame).split('\n')[2:11]
                    YYY = []
                    for ii in dataFrame:
                        iii = ii.get_text()
                        YYY.append(str(iii).split('\n'))

                    if len(YYY) == 3:
                        print(URL1+iv)
                        YYX= YYY[0][2:11]
                        filename.append((YYX[0].split(' '))[1])
                        date_of_study.append((YYX[1].split(' ', 1))[1])
                        patient_age.append((YYX[2].split(' '))[1])
                        film_type.append((YYX[4].split(' '))[1])
                        Density.append((YYX[5].split(' '))[1])
                        date_digitized.append((YYX[6].split(' ', 1))[1])
                        digitizer.append((YYX[7].split(' '))[1])

                        YYZ= YYY[1][1:10]
                        File_Name1.append((YYZ[0].split(' '))[1])
                        Total_Abnormality.append((YYZ[2].split(' '))[1])
                        Lesion_type.append((YYZ[4].split(' ', 1))[1])
                        #Assesment.append((YYZ[5].split(' '))[1])
                        Subtlety.append((YYZ[6].split(' '))[1])
                        Pathology.append((YYZ[7].split(' '))[1])

                        YYA = YYY[2][1:10]
                        File_Name2.append((YYA[0].split(' '))[1])
                        Total_Abnormality2.append((YYA[2].split(' '))[1])
                        Lesion_Type2.append((YYA[4].split(' ', 1))[1])
                        #Assesment2.append((YYA[5].split(' '))[1])
                        Subtlety2.append((YYA[6].split(' '))[1])
                        Pathology2.append((YYA[7].split(' '))[1])
                        #Appending N/A to other values so that there is continuity#


                        File_Name3.append("NA")
                        Total_Abnormality3.append("NA")
                        Lesion_Type3.append("NA")
                        #Assesment3.append("N/A")
                        Subtlety3.append("NA")
                        Pathology3.append("NA")


                        File_Name4.append("NA")
                        Total_Abnormality4.append("NA")
                        Lesion_Type4.append("NA")
                        #Assesment4.append("N/A")
                        Subtlety4.append("NA")
                        Pathology4.append("NA")    

                    elif len(YYY) == 5:
                        print(URL1+iv)
                        YYX= YYY[0][2:11]
                        filename.append((YYX[0].split(' '))[1])
                        date_of_study.append((YYX[1].split(' ', 1))[1])
                        patient_age.append((YYX[2].split(' '))[1])
                        film_type.append((YYX[4].split(' '))[1])
                        Density.append((YYX[5].split(' '))[1])
                        date_digitized.append((YYX[6].split(' ', 1))[1])
                        digitizer.append((YYX[7].split(' '))[1])

                        YYZ= YYY[1][1:10]
                        File_Name1.append((YYZ[0].split(' '))[1])
                        Total_Abnormality.append((YYZ[2].split(' '))[1])
                        Lesion_type.append((YYZ[4].split(' ', 1))[1])
                        #Assesment.append((YYZ[5].split(' '))[1])
                        Subtlety.append((YYZ[6].split(' '))[1])
                        Pathology.append((YYZ[7].split(' '))[1])

                        YYA = YYY[2][1:10]
                        File_Name2.append((YYA[0].split(' '))[1])
                        Total_Abnormality2.append((YYA[2].split(' '))[1])
                        Lesion_Type2.append((YYA[4].split(' ', 1))[1])
                        #Assesment2.append((YYA[5].split(' '))[1])
                        Subtlety2.append((YYA[6].split(' '))[1])
                        Pathology2.append((YYA[7].split(' '))[1])

                        YYB = YYY[3][1:10]
                        File_Name3.append((YYB[0].split(' '))[1])
                        Total_Abnormality3.append((YYB[2].split(' '))[1])
                        Lesion_Type3.append((YYB[4].split(' ', 1))[1])
                        #Assesment3.append((YYB[5].split(' '))[1])
                        Subtlety3.append((YYB[6].split(' '))[1])
                        Pathology3.append((YYB[7].split(' '))[1])

                        YYC = YYY[4][1:10]
                        File_Name4.append((YYC[0].split(' '))[1])
                        Total_Abnormality4.append((YYC[2].split(' '))[1])
                        Lesion_Type4.append((YYC[4].split(' ', 1))[1])
                        #Assesment4.append((YYC[5].split(' '))[1])
                        Subtlety4.append((YYC[6].split(' '))[1])
                        Pathology4.append((YYC[7].split(' '))[1])
                        
                        


    True3= np.vstack((filename, date_of_study, patient_age, film_type, Density, date_digitized, digitizer, File_Name1, Total_Abnormality, Lesion_type,Subtlety, Pathology, File_Name2, Total_Abnormality2, Lesion_Type2, Subtlety2, Pathology2, File_Name3, Total_Abnormality3, Lesion_Type3,Subtlety3, Pathology3, File_Name4, Total_Abnormality4, Lesion_Type4, Subtlety4, Pathology4))
    True3= True3.transpose()
    Column_Names1= ['File_Name', 'Date', 'Age', 'Film-Type', 'Breast-Density', 'Date-Digitized', 'Digitizer-Platform','File_Name1', 'Abnormality-Count1', 'Lesion-Type1', 'Subtlety1', 'Pathology1', 'File_Name2', 'Abnormality-Count2', 'Lesion-Type2','Subtlety2', 'Pathology2', 'File_Name3', 'Abnormality-Count3', 'Lesion-Type3', 'Subtlety3', 'Pathology3','File_Name4', 'Abnormality-Count4', 'Lesion-Type4', 'Subtlety4', 'Pathology4']
    True4 = pd.DataFrame(True3,columns= Column_Names1)
    ## This patch of file generates the Mammogram Labels and Saves them to the specified location parsed as an argument
    True4.to_csv(Location, sep = ',')

if "__name__" == __main__:
    main()
    