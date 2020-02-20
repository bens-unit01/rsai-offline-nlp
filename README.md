# README #

In this repository we have the source code of the RSAI-offline app. RSAI-offline provide  some basic offline chat capabilities.  

### Modules
 The application contains 3 main modules :     
        1. Offline speech recognition using pocketsphinx and Gstreamer     
        2. Natural Language Processing using AIML     
        3. TTS, text-to-speech module     


#### Setup of the "Offline speech recognition" module
Following is the procedure to setup this speech module on an Orange_PI_zero 
running the armbian [debian jessie image](https://www.armbian.com/donate/?f=https://dl.armbian.com/orangepizero/Debian_jessie_default.7z).  
```
  1- Clone the repository : 'https://bitbucket-username@bitbucket.org/wowweehk/rsai-offline.git'     
    ( preferably in the home directory ~ )     
  2- Edit your Orange_PI_zero username in the system.conf file.     
     using vim or nano editor, open ~/rsai-offline/system.conf. Go to line      
     74 and change 'raouf' with your username.     
  3- Copy the file download the file cmusphinx.tag.gz from      
 https://drive.google.com/file/d/0BzCQYi90icxaZFktcnEwc3Q2NXc/view?usp=sharing      
   in a flash disk and copy it to ~/rsai-offline folder.         
  4- Run the installation script:  ./setup.sh    
     This will take about 30 minutes to install pocketsphinx, gstreamer and   
    all dependencies. At the end of the installation, the system will    
    reboot.    

  5- The app is ready now, make sure to have a usb microphone plugged in,    
      run the app : . ~/rsai-offline/run       





```


#### Setup of the "Offline Natural Langugae Processing" module
```
 To setup the NLP module you'll need :
 1- Install aiml package : 'sudo pip install aiml' 
 
 You can test the is by running : 'python aiml-test.py'.
 To test the demo with both speech recognition and language processing you'll need 
 first to install first the speech recognition module. 


```




