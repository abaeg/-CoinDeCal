# -CoinDeCal
An android app to detect Pakistani Rupee Coins and Calculate total amount.

### Introduction
Given an image with multiple coins, detect coins using Hough Transform. Moreover, classify coins to find out its value using a Machine learning algorithm (depending on the accuracy) and calculate total amount.

### Tools and Tech
Python, SkLearn, OpenCv, Flask, Android Studio, Java
### Dataset
One hundred and twenty RGB  images were collected using Google images and manual image capturing. Its breakdown is shown below:<br />
&emsp;●	1 Rupee Coin: 30 images<br />
&emsp;●	2 Rupee Coin: 30 images<br />
&emsp;●	2 Rupee Coin: 30 images<br />
&emsp;●	2 Rupee Coin: 30 images<br />
Images were read from the google drive, resized into 64x64x3 and stored into X. Moreover, its corresponding label was manually stored in Y.

### Data Augmentation

Since 120 images were not enough to get maximum accuracy, we used augmentation to create more data using existing data.Several rotating and blurring techniques were used to increase the dataset size. Moreover, after data augmentation a total of 8640 images were produced. Its breakdown is shown below:<br />
&emsp;●	1 Rupee Coin: 2160 images<br />
&emsp;●	2 Rupee Coin: 2160 images<br />
&emsp;●	2 Rupee Coin: 2160 images<br />
&emsp;●	2 Rupee Coin: 2160 images<br />

### Train and Test Data
A split of 10% was done and as a result number of training images equals 7776 and number of testing images equals 864.
Feature Vector Extraction
As sklearn.svm.SVC takes input in the form of 2D-array hence all the images were converted to 1D-array using the flatten function of Numpy library. 
Model
The model, sklearn.svm.SVC used belongs to the Sklearn library.

### Model Accuracy
Sklearn’s accuracy_score and confusion matrix is used to see the accuracy of the test data on the previously trained model. The accuracy achieved is 99%.

![image](https://user-images.githubusercontent.com/34359431/152700890-fe5a3549-e3fb-47b7-9df9-01a6ce24f2de.png)

### Coin Detection
Given an image where multiple coins exist, using a circle detection algorithm namely Hough Transform, coins are detected and cropped to produce multiple images (one image for each coin).
![image](https://user-images.githubusercontent.com/34359431/152700902-822fb235-ed26-4191-9687-b48d6cf7e37a.png)


### Sharpening Image
As real-time images are mostly blurred and out of focus so to resolve this problem, images are sharpened using the following code snippet.

### Predicting Labels
Multiple images gathered from coin detection are then sent to the classifier for prediction and the results are added together to get the total amount.

### User Interface
Front-end is kept simple and easy to use because focus was more on functionality than design for this particular project.It designed and developed on Android Studio.While using CoinDeCal, user can either take an image from camera or upload an existing image from gallery.  The image content then goes to the model for prediction and the results are sent back to the android application. The screen then shows the total amount calculated.

![image](https://user-images.githubusercontent.com/34359431/152700914-4e9a4a46-b4cd-4137-8f62-5aa6c9280313.png)

### How to Run the project?
To train and save the machine learning model , you can simply use the Model_Training.ipynb file.
If you want to use full application, then you need to create an android studio project and then add java and xml resources from "Andoid Application" folder.This app will communicate with a server to get predicted results , so you need to install flask on a local machine.Then place the file named "app" from  "Andoid Application\Serevr Side" in your flask project directory.

