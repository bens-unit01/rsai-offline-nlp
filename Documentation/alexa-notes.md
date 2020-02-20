


#### Keywords;
```
  AVS : Alexa Voice Service 
  ARN : Amazon Ressource Name
  AWS Lambda :  Version light d-un service web, voir -> https://aws.amazon.com/lambda/ 
  AWS IAM : Identity and Access Management
  Access Key Id, Secret Access Key: chaque utilisateur on a une paire  
  Intent : an action that fulfills a user-s spoken request  
  Slots : arguments of an Intent, this is optional 
  Alexa CoHo : connected home 
  Amazon S3:  Amazon Simple Storage Service 
  Amazon EC2: Amazon Elastic Compute Cloud 
  Amazon AMI : Amazon Machine Image 
  AWS Elastic Beanstalk: web service deployed on an EC2
  M2M : machine to machie communication 
  RTP, RSTP : protocols for video streaming 
  CoAP: Constrained Application Protocol
  AWS Signature Version 4 authentication  : port 443,  utilise clientID and clientSecret, 
                                         utilise dans MQTT via websockets 
  TLS 1.2 (Transport Layer Security) with X.509 certificate-based mutual authentication : utilise RSA key ( private et public)  
  ALPN : Application-Layer Protocol Negotiation  
```

#### Misc notes
```
ip aws server : 52.8.126.217  
mosquitto_sub -h 10.10.10.31 -t kitchen   //souscrire a un MQTT broker 
 
aws iam get-user 
aws configure 

ARN - arn:aws:lambda:us-east-1:846724577827:function:Chemistry  
IoT shadow    https://a2xii7mud1uyci.iot.us-east-1.amazonaws.com/things/test-robot-01/shadow   
The required native libraries are named "libvlc.dll" and "libvlccore.dll". 	

Client ID:amzn1.application-oa2-client.71a603166b4b4c30aa35e6809a59a232

Client Secret:469170eaaa983f2518d2443d424e87fff54ee0bb9cef27362cf0a032cb10bd1f

-- aws user : raouf
Access Key ID: AKIAJHXV4QGIAVFJFXCA
Secret Access Key: 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


services.msc        //check running services on windows 
netstat -an          //list of tcp ports 

gksu pcmanfm        // lancer file manager comme root 


No X11 DISPLAY variable was set, but this program performed an operation which requires it.
        at java.awt.GraphicsEnvironment.checkHeadless(GraphicsEnvironment.java:204)
        at java.awt.Window.<init>(Window.java:536)
        at java.awt.Frame.<init>(Frame.java:420)
        at java.awt.Frame.<init>(Frame.java:385)
        at javax.swing.JFrame.<init>(JFrame.java:189)
        at com.amazon.alexa.avs.AVSApp.<init>(AVSApp.java:115)
        at com.amazon.alexa.avs.AVSApp.<init>(AVSApp.java:108)
        at com.amazon.alexa.avs.AVSApp.main(AVSApp.java:103)
 




--



"which" in powershell -> gcm 

supported platformes : web, android/kindle, iOS n


Manage your contents and devices : https://www.amazon.com/mn/dcw/myx.html#/home/content/booksAll/dateDsc/

Rem : Alexa music skills are not supported on applications 

public void startRecording(RecordingRMSListener rmsListener, RequestListener requestListener)
--> AVSController.java 


275: public void sendEvent(RequestBody body, InputStream inputStream, RequestListener listener, AudioInputFormat audiotype)    --> AVSClient.java 

src/main/java/com/amazon/alexa/avs/message/response/AlexaExceptionResponse.java

set OPENSSL_CONF={OpenSSL installation location}\bin\openssl.cfg
rem: sur windows on a fait ca sur dans les param avance du systeme 


com.amazon.alexa.avs.http.AVSClient - HttpClient stopping



```

#### Voice rec
```
- Sensory : [http://www.sensory.com/](http://www.sensory.com/)
- SnowBoy : [https://snowboy.kitt.ai/](https://snowboy.kitt.ai/) 
            [https://github.com/Kitt-AI/snowboy](https://github.com/Kitt-AI/snowboy)

```

#### Hardware possible 
**Dev board de chez ST**  http://www.st.com/content/st_com/en/products/embedded-software/mcus-embedded-software/stm32-embedded-software/stm32cube-expansion-software/x-cube-wifi1.html
**Particle ** https://docs.particle.io/guide/getting-started/build/photon/ 


#### Stuff pour le Raspberry PI 
```
username/password : pi/raspberry 
sudo apt-get install matchbox-keyboard      // clavier virtuel 
sudo apt-get install fswebcam 		    // support pour la webcam 
dpkg --get-selections                       // liste les package installe 
groups pi                                    // voir si on a le droit d-acceder a l-audio
printenv                                      // affiche certain parametres du system -- meme chose que env 
arecord -D plughw:1 --duration=10 -f cd -vv ~/rectest.wav   // enregistrer audio 
aplay rectest-01.wav                        // lecture d-un fichier audio 
sudo raspi-config                          // config tool 
/etc/apt/sources.lit                        //site utilise par apt-get 
apt-cache search                            // chercher un package 
ResponseBody  - Directive 
Message
export DISPLAY=:0      // pour lancer une application sur le PI 
https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=150438          // installer firefox 
set OPENSSL_CONF={OpenSSL installation location}\bin\openssl.cfg


 set OPENSSL_CONF=/c/Users/raouf/bin/OpenSSL-Win32/bin/openssl.cfg
 set OPENSSL_CONF=C:\Users\raouf\bin\OpenSSL-Win32\bin\openssl.cfg


/c/Users/raouf/bin/OpenSSL-Win32/bin/openssl
c:\Users\raouf\bin\OpenSSL-Win32\bin\


C:\Program Files\VideoLAN\VLC\


VLC_PATH

wlan0     Link encap:Ethernet  HWaddr b8:27:eb:4f:93:bf
wlan1     Link encap:Ethernet  HWaddr 40:a5:ef:0e:d8:97

pour utiliser hdma-vga adapter on doit activer les 2 commande suivante dans /boot/config.txt
"hdmi_safe=1"
"hdmi_force_hotplug=1" 

```



#### Maven 
```

-Xbootclasspath/p:ref-lib/alpn-boot-8.1.9.v20160720.jar  // a ajouter dans "run conf"/arguments/VM arguments 
 eclipse debug mvn : https://blog.jooq.org/2015/06/23/how-to-debug-your-maven-build-with-eclipse/ 
 debug + breakpoints : http://stackoverflow.com/questions/22229088/intellij-idea-13-debugger-dont-stop-on-breakpoint-in-java-for-maven-project 


mvn exec:exec -Dexec.executable=java "-Dexec.args=-classpath %classpath -Dgreeting=\"Hello\" com.mycompany.app.App"
mvn exec:exec -Dexec.executable=java "-Dgreeting=\"Hello\" com.amazon.alexa.avs.AVSApp"
com.amazon.alexa.avs.AVSApp


-Xdebug -Xnoagent -Djava.compile=NONE -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=5005

-Xdebug -Xrunjdwp:transport=dt_socket,address=5005,server=n,suspend=y

mvn exec:exec -Dexec.executable=java "-Dexec.args=-classpath %classpath -agentlib:jdwp=transport=dt_socket,server=y,address=127.0.0.1:5005,suspend=y com.amazon.alexa.avs.AVSApp"

mvn exec:exec -Dexec.executable=java  -Djna.library.path=/c/Program\ Files/VideoLAN/VLC/ "-Dexec.args=-classpath %classpath -agentlib:jdwp=transport=dt_socket,server=y,address=5005,suspend=n com.amazon.alexa.avs.AVSApp"

mvn exec:exec -Dexec.executable=java  "-Dexec.args=-classpath %classpath -agentlib:jdwp=transport=dt_socket,server=y,address=5005,suspend=y com.amazon.alexa.avs.AVSApp"

setup pour -Xbootclasspath/p --> http://stackoverflow.com/questions/4444410/overriding-java-system-library-with-newer-class-on-mac  

mvn install         // lancer une compilation 
mvn exec:exec       // lancer l-execution de l-app

// creation d-une app java console 
mvn archetype:generate -DgroupId=com.wowwee  -DartifactId=pi-gpio   -DarchetypeArtifactId=maven-archetype-quickstart   -DinteractiveMode=false

// mvn add a jar file 
http://stackoverflow.com/questions/4955635/how-to-add-local-jar-files-in-maven-project 

```
#### aws cli
```
 aws iot delete-thing --thing-name test-robot-01               // remove an IoT thing 
 aws iot set-logging-options --logging-options-payload roleArn="arn:aws:iam::846724577827:role/IoTLoggingRole",logLevel="INFO"  
 aws iot describe-endpoint 

```
#### Issues
- Send custom directives : https://forums.developer.amazon.com/questions/30904/alexa-skill-set-to-send-custom-directives-to-my-al.html 
```
bytes: {"directive":
		{"header":
			{"namespace":"SpeechSynthesizer",
                         "name":"Speak",
                         "messageId":"d88e0ad7-2455-47a1-99ea-ffd0f6837162",
                         "dialogRequestId":"8daa1053-40d1-4ae2-a7fb-caaa8393427e"},
                         "payload":{"url":"cid:ValidatedSpeakDirective_amzn1.ask.skill.f2990059-f8ca-49ac-ba93-2790f719c8e4_a74a2f38-1c61-4191-9739-cd5c7f735363_1070750403",
                         "format":"AUDIO_MPEG",
                         "token":"amzn1.as-ct.v1.ThirdPartySdkSpeechlet#ACRI#ValidatedSpeakDirective_amzn1.ask.skill.f2990059-f8ca-49ac-ba93-2790f719c8e4_a74a2f38-1c61-4191-97                                  39-cd5c7f735363"
                          }
                 }
         }

```
- alpn issue : 1. http://www.eclipse.org/jetty/documentation/9.4.x/alpn-chapter.html  
               2. http://www.javaworld.com/article/2916548/java-web-development/http-2-for-java-developers.html?page=2   
               3. http://mvnrepository.com/artifact/org.mortbay.jetty.alpn/alpn-boot
- setup eclipse pour alpn-boot :
  http://www.eclipse.org/jetty/documentation/current/alpn-chapter.html#alpn-versions


- ssl certificate issue : http://stackoverflow.com/questions/19540289/how-to-fix-the-java-security-cert-certificateexception-no-subject-alternative     
                          https://bowerstudios.com/node/1007     
			  https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/docs/authorizing-your-alexa-enabled-product-from-a-website      
                          /etc/ssl       // emplacement certificats 

                         http://stackoverflow.com/questions/24720013/apache-http-client-ssl-certificate-error 
			   **tuto ssl:** https://samhobbs.co.uk/2014/04/ssl-certificate-signing-cacert-raspberry-pi-ubuntu-debian 

			    **solution du probleme:** http://stackoverflow.com/questions/10258101/sslhandshakeexception-no-subject-alternative-names-present 
			   classe concerne -> 
			./main/java/com/amazon/alexa/avs/auth/companionservice/CompanionServiceClient.java



- node js server on aws ec2 issue : 
          http://stackoverflow.com/questions/5309910/https-setup-in-amazon-ec2 
          voir "generate self signed certificate" :  https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/docs/reference-implementation-guide#Generating%20Self-Signed%20Certificates
           - avoir liste ports : "sudo netstat -tulpn" 
	   - tester le port : "telnet 52.8.126.217 3000" 
	   **solution**: 
	   src/main/java/com/amazon/alexa/avs/auth/companionservice/CompanionServiceClient.java


- startup : 

https://blog.htbaa.com/news/tmux-scripting      
http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS     
http://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up      
http://www.howtogeek.com/howto/ubuntu/a-live-view-of-a-logfile-on-linux/    //get logs with tail 


- pwm : 

http://letsmakerobots.com/node/38460    
https://www.pololu.com/product/713    
https://javatutorial.net/raspberry-pi-dim-led-pwm-java
http://wiringpi.com/reference/software-pwm-library/

http://raspberrypi.stackexchange.com/questions/49600/how-to-output-audio-signals-through-gpio 




- modif voix alexa :  http://puredata.info/docs/raspberry-pi 

OpenAL (using JOAL or LWJGL).
java and IME
JavaSound

Java Sound Audio Engine
OpenMAX
http://stackoverflow.com/questions/18687310/how-to-modify-pitch-of-sound-file-java
http://stackoverflow.com/questions/12220980/vlc-j-audio-pitch-control





//  bug - l-app s-arrete 
// log
17:01:12.548 [RequestThread] INFO  com.amazon.alexa.avs.http.AVSClient - This response successfully had no content.
17:01:55.641 [Thread-2] INFO  com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Received wake word detected
17:01:55.642 [Thread-2] INFO  com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Wake Word Detected ......
17:01:55.645 [Thread-116] INFO  com.amazon.alexa.avs.AVSApp - Wake Word was detected
17:01:55.654 [Thread-117] DEBUG com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Sending command IPC_PAUSE_WAKE_WORD_ENGINE to all connected clients
17:01:55.662 [Thread-117] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
17:01:56.681 [Thread-117] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
17:01:57.689 [Thread-117] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
17:01:58.700 [Thread-117] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
17:01:59.714 [Thread-117] ERROR com.amazon.alexa.avs.AVSApp - An error occured creating speech request
javax.sound.sampled.LineUnavailableException: line with format PCM_SIGNED 16000.0 Hz, 16 bit, mono, 2 bytes/frame, little-endian not supported.
        at com.sun.media.sound.DirectAudioDevice$DirectDL.implOpen(DirectAudioDevice.java:513) ~[?:1.8.0_111]
        at com.sun.media.sound.AbstractDataLine.open(AbstractDataLine.java:121) ~[?:1.8.0_111]
        at com.sun.media.sound.AbstractDataLine.open(AbstractDataLine.java:153) ~[?:1.8.0_111]
        at com.amazon.alexa.avs.AudioCapture.startCapture(AudioCapture.java:79) ~[classes/:?]
        at com.amazon.alexa.avs.AudioCapture.getAudioInputStream(AudioCapture.java:61) ~[classes/:?]
        at com.amazon.alexa.avs.AVSController.getMicrophoneInputStream(AVSController.java:296) ~[classes/:?]
        at com.amazon.alexa.avs.AVSController.startRecording(AVSController.java:274) [classes/:?]
        at com.amazon.alexa.avs.AVSApp$1.actionPerformed(AVSApp.java:174) [classes/:?]
        at com.amazon.alexa.avs.PushButton$1.run(PushButton.java:23) [classes/:?]
        at java.lang.Thread.run(Thread.java:745) [?:1.8.0_111]




