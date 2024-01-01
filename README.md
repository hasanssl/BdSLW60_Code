Before You Jump In

*****Assuming you downloaded the code from Github

Dataset and Annotation

step 0-0: download the BdSLW60 dataset from Kaggle. link: BdSLW60. 
          COPY/DOWNLOAD ALL THE CONTENTS IN BdSL60 FOLDER. You will first get the folder empty before copying.
       
step 0-1: (Optional) If you want to run the DTW_SVM 'pipeline pipeline_SVM_DTW.ipynb':
	  download the DTW_BdSLW60 dataset from Kaggle. link: DTW_BdSLW60 
	  Overwrite the DTW folder already there.
	  
step 0-2: (Optional) If you have changed the dataset annotation and want to generate JSON files again. 
          Think before you do this. If you have a video editing tool and can see the video frame by frame, then do it.
          (Raw annotation text files are available in the dataset BdSLW60 wordwise subfolders)
          
          Run the python script  'RUN_THIS_JSON.py' available in 'OPTIONAL_JSON_CREATION' Folder 
          this will overwrite the default annotation json file provided with the dataset.

Preprocesing

step 1-0: (Optional) Something about DTW experiment. If you have performed step 0-1
	  Edit the last cell of 'PREPROCESSING/RUN_THIS_CREATE_NUMPY.ipynb' and set the flag DTW_weights_available  to True
	  
step 1-1: run the 'PREPROCESSING/RUN_THIS_CREATE_NUMPY.ipynb'
          This will generate all the mediapipe landmarks and numpy files, and will generate normalized data.
          The first time run may take several hours (10 hours or more) because it will extract landmarks from videos.
          (Subsequent runs will take much less time as the landmark extractions will not be repeated)
          
step 1-2: (Optional and discouraged) Run the script 'DTW Distance Calculation.ipynb' available OUTSIDE PREPROCESSING folder.
          You may do this if you changed data annotations and perfomed step 0-2. 
          
          CAUTION: This is very computation intensive and takes more than 5 days with 60 computers calculating the distances for each class.
          
step 1-3: (Optional) If you want to check the number of missing hand landmarks in the dataset. We wrote the code to justify the poorly classified
          classes/words. The script also finds out number of right handed and left handed samples from each signer.
          RUN: 
	  
             	PREPROCESSING/missing_handpoint_count.ipynb
              
              
Machine Learning:

step 2-0: Run the 4(four) scripts for LSTM WITH ATTTENTION pipeline in any sequence.
          The experiements are with all data but with different configurations.
            
             All 1629 features (Pose, Face and Hand Landmarks)
        	Left Hand data Flipped:  Hand Landmarks horizontally flipped centering around the middle of two shoulders
                       pipeline_LSTM_1629_FLIPPED_ST5_B64.ipynb
                NO FLIP: 
                       pipeline_LSTM_1629_ST5_B64.ipynb
                       
             225 features (Pose, and Hand Landmarks, NO FACE)
        	Left Hand data Flipped:  Hand Landmarks horizontally flipped centering around the middle of two shoulders
                       pipeline_LSTM_225_FLIPPED_ST5_B64.ipynb
		       pipeline_LSTM_225_FLIPPED_no_stop_B64.ipynb
        	NO FLIP:  
          	       pipeline_LSTM_225_ST5_B64.ipynb
		       pipeline_LSTM_225_no_stop_B64.ipynb

step 2-1: SVM pipeline with short gesture plonged to 164 frames by uniformly duplicating frames. All 164 frame features are fed as input to SVM.
          feture dimension 164x1629.   
	  RUN: 
	  
              		pipeline_SVM.ipynb
	      		pipeline_SVM_POSE_HAND.ipynb
	 		pipeline_SVM_POSE_HAND_NO_FLIP.ipynb
	      
step 2-2: SVM with DTW distances. No need to plong the gestures. Highly computationally intensive to calculate the distances.
          Run if you have performed step 0-1 and checked step 1-2.
          feature dimension still 60x1629.
	  RUN:
	  
              pipeline_SVM_DTW.ipynb
	      pipeline_SVM_DTW_POSE_HAND.ipynb
              
              
MOST PROBABLY YOU ARE READING THIS LINE
Thank You!
