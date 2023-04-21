
# Crime Detection using Machine-Learning
Crime Detection using Machine Learning and web3 is a project that aims to detect criminal activities in video footage using machine learning techniques and store the information in a database using django and web3 as auth.



## Installation


 Download or clone the repository
```bash
  git clone https://github.com/AkhilAndroid/Crime-Detection-using-Machine-Learning.git
  cd Crime-Detection-using-Machine-Learning-and-web3
```
Now install the dependencies 
```bash
  pip install -r requirement.txt
```
Download the pre-trained models and video from Google Drive.  
```bash
https://bit.ly/40m9Ka4
```
Extract the files and place them in the root directory of the project.


## Demo
Run the following command 

Start the server:
```
python manage.py runserver
```
Make sure you install Metamask in Chrome

Open http://127.0.0.1:8000/api in Chrome browser to access the web interface.

Replace video4.mp4 with your video in main.py
```
# Load the video
vid = imageio.get_reader('video4.mp4',  'ffmpeg')
cap = cv2.VideoCapture('video4.mp4')
```

Now run:
```
python main.py
```

Check the result in the website
