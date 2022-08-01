Usage:
on taki use bash meta_train.sh
args are model_name dataset-dataset_args labelset num_epochs
e.g. bash meta_slurm.sh basic_autoencoder fft_data_256 2018 200

elsewhere use meta_train.py
python3 meta_train.py model_name dataset_name-dataset_args labels_to_use num_epochs
e.g. python3 meta_train.py basic_autoencoder fft_data_256-rgb 2018 200

Dataset args are used in data_loaders/load_data.py
dataset names are declared in utils/paths.py

This is a work in progress atm because I was rewriting it to make it easier to work on my project when I gave up on my project. I'll clean it up ... on the 26th probably, but the structure will remain the same.
The hdf5toPNG and fft processing are in preprocessing/hdf5_to_images.py


*************************************************************************************************************************************************************************


Team 1 UMBC REU Summer 2022
**Title:** Big Data and Machine Learning Techniques for Atmospheric Gravity Wave Detection <br>
**Team Members:** Hannah Nguyen, Jorge Gonzalez, Kathryn Chen, Theodore Chapman, Logan Chambers <br>
**Mentors:** Dr. Jianwu Wang <br>
**Colaborators:** Dr. Jia Yue, Dr. Chenxi Wang, Dr. Sanjay Purushotham <br>
**Abstract:** Atmospheric gravity waves are produced when gravity attempts to restore disturbances through stable layers in the atmosphere. They have a visible effect on many atmospheric phenomena such as global circulation and air turbulence. Despite their importance, however, little research has been conducted on how to detect gravity waves using machine learning algorithms. We faced two major challenges in our research: our labeled dataset was extremely small, and our raw data had a lot of noise. In this study, we explored various methods of preprocessing and transfer learning in order to address those challenges. We pre-trained an autoencoder on unlabeled data before training it to classify labeled data. We also created a custom CNN by combining certain pre-trained layers from the InceptionV3 Model trained on ImageNet with custom layers and a custom learning rate scheduler. Our best model outperformed state-of-the-art architectures with a test accuracy 6.36% higher than the best performing baseline architecture.<br>
<br>
### Navigating the Repository<br>
The names of each directory in this repository correspond to their purpose. <br>
<b>*Analysis*</b> contains test_dataloaders<br>
<b>*Data Loaders*</b> sample minibatches from a dataset, giving us the flexibility to choose from different sampling strategies. <br>
<b>*Models*</b> contains all models of our CNN and ConvLSTMs as well as sample outputs from each model and a copy of the land mask that is used to filter out land values.<br>
<b>*Preprocessing*</b> is where the train and test data sets for each model can be found as well as the code from which they were derived. <br>
<b>*Utils*
<br>
### Cite Our Work<br>
Paper information: Hannah Nguyen, Jorge Gonzalez, Kathryn Chen, Theodore Chapman, Logan Chambers, Seraj Mostafa, Jianwu Wang. Big Data and Machine Learning Techniques for Atmospheric Gravity Wave Detection. Not yet accepted by the 2022 IEEE International Conference on Big Data which is in December 2022.<br>
### Publication<br>
Not yet accepted by the 2022 IEEE International Conference on Big Data which is in December 2022.
