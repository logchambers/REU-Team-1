# REU-Team-1<br>
<br>
Team 1 UMBC REU Summer 2022 <br>
<b>Title:</b> Big Data and Machine Learning Techniques for Atmospheric Gravity Wave Detection<br>
<b>Team Members:</b> Hannah Nguyen, Jorge Gonzalez, Kathryn Chen, Theodore Chapman, Logan Chambers<br>
<b>Mentors:</b> Dr. Jianwu Wang<br>
<b>Colaborators:</b> Dr. Jia Yue, Dr. Chenxi Wang, Dr. Sanjay Purushotham<br>
<b>Abstract:</b> Atmospheric gravity waves are produced when gravity attempts to restore disturbances through stable layers in the atmosphere. They have a visible effect on many atmospheric phenomena such as global circulation and air turbulence. Despite their importance, however, little research has been conducted on how to detect gravity waves using machine learning algorithms. We faced two major challenges in our research: our labeled dataset was extremely small, and our raw data had a lot of noise. In this study, we explored various methods of preprocessing and transfer learning in order to address those challenges. We pre-trained an autoencoder on unlabeled data before training it to classify labeled data. We also created a custom CNN by combining certain pre-trained layers from the InceptionV3 Model trained on ImageNet with custom layers and a custom learning rate scheduler. Our best model outperformed state-of-the-art architectures with a test accuracy 6.36% higher than the best performing baseline architecture.<br>
<br>
<b>Navigating the Repository</b><br>
The names of each directory in this repository correspond to their purpose.<br>
<b>Analysis</b> contains test_dataloaders<br>
<b>Data Loaders</b> sample minibatches from a dataset, giving us the flexibility to choose from different sampling strategies.<br>
<b>Models</b> contains all models of our CNN and ConvLSTMs as well as sample outputs from each model and a copy of the land mask that is used to filter out land values.<br>
<b>Preprocessing</b> is where the train and test data sets for each model can be found as well as the code from which they were derived.<br>
<b>Utils</b><br>
<br>
<b>Cite Our Work</b><br>
<b>Paper information:</b> Hannah Nguyen, Jorge Gonzalez, Kathryn Chen, Theodore Chapman, Logan Chambers, Seraj Mostafa, Jianwu Wang. Big Data and Machine Learning Techniques for Atmospheric Gravity Wave Detection. Not yet accepted by the 2022 IEEE International Conference on Big Data which is in December 2022.
<br>
<b>Publication</b>:
Not yet accepted by the 2022 IEEE International Conference on Big Data which is in December 2022.
