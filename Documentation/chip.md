
## Notes for CHIP board 



#### Links 

-http://docs.getchip.com/chip.html#install-and-update-software     
-https://getchip.com/pages/chip    
-https://bbs.nextthing.co/    
-**projet python acec CHIP:** http://sammachin.com/the-10-echo/      
-**qq utilitaires python:** https://github.com/xtacocorex?tab=repositories    
-**github du next-thing-co:** https://github.com/NextThingCo  
-**hardware documentation:** https://github.com/NextThingCo/CHIP-Hardware 
-**docs:** http://www.chip-community.org/index.php/HOW-TO_compile_Chip%27s_Linux_kernel_and_modules_on_Chip_itself  
-**docs:** http://www.chip-community.org/index.php/Chip9$_U-Boot:_how_to_test_a_new_kernel_(in_a_safe_way)  
-**docs: pinout** http://www.chip-community.org/index.php/Hardware_Information#Pin_overview 
-**article lie au U-boot** : https://blog.night-shade.org.uk/2014/01/fw_printenv-config-for-allwinner-devices/      

#### Install Java
http://www.oracle.com/technetwork/java/javase/downloads/index.html     
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html    
http://www.rpiblog.com/2014/03/installing-oracle-jdk-8-on-raspberry-pi.html    
https://wiki.debian.org/JavaPackage    
-**installation java8, meilleur technique:** http://www.webupd8.org/2013/12/oracle-java-ppa-updated-with-arm-support.html      



#### Keywords & commands  
```

florence package : virtual keyboard  
conky  package   : utilitaire pour afficher les performance du system 

sudo blkid            // donne list des modules de stockage 

stty                   // change terminal line settings 
stty -F /dev/ttyS0     // affiche info sur UART0
stty -F /dev/ttyS0 -echo ispeed 9600 line 0          // desactive echo 
/etc/systemd/system/               // services system 
sudo systemctl poweroff            // shutting off CHIP
sudo cat /proc/tty/driver/serial             // autres infos sur l-UART
aplay -l dump           // liste les cartes audio

sudo systemctl list-units  | grep loaded   // list les modules chargés 
 
sudo systemctl list-unit-files        // liste tout les services 
```


#### Startup script 
```

https://forum.xfce.org/viewtopic.php?id=5550
some keywords: 
upstart 
systemd
cron
/etc/rc.local
/etc/init.d
cat /proc/uptime
uptime
/etc/systemd/system

example de service : https://gist.github.com/naholyr/4275302  

Pour lancer une application au moment du boot on a 2 options, en utilisant ('systemd') ou bien methode
1- classique ( /etc/init.d et la commande 'update-rc.d' ). 
commandes : 

'install -Dm744 initd_alexa.sh /etc/init.d/AlexaPi'
'update-rc.d AlexaPi defaults'

2- via systemd : 
log lorsqu-on fait 'sudo systemctl enable AlexaPi.service'  
Created symlink from /etc/systemd/system/default.target.wants/AlexaPi.service to /usr/lib/systemd/system/AlexaPi.service.   
sudo systemctl status AlexaPi.service 

systemctl daemon-reload
systemctl enable AlexaPi.service


sudo journalctl -xb

sudo systemctl start  AlexaPi
sudo systemctl status -l AlexaPi
sudo systemctl stop  AlexaPi
 
https://www.freedesktop.org/software/systemd/man/systemd.exec.html   // doc sur systemd 

```

#### Notes, commandes 
```

sudo systemctl set-default multi-user.target    //mode headless
sudo systemctl set-default graphical.target     // mode graphique 

```


#### Misc 
```

Gui pour terminal (charva + lanterna) https://github.com/viktor-podzigun/charva-lanterna 

i2c driver : http://stackoverflow.com/questions/16728587/i2c-driver-in-linux 
next-thing-CHIP wlan0 mac address : chip-2      38:a2:8c:5e:7a:97 
                      mac address  chip-1        a0:2c:36:25:00:2c


// resultat lsusb avec mic d-amazon 
Bus 002 Device 002: ID 0d8c:013c C-Media Electronics, Inc. CM108 Audio Controller
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

// resultat lsusb avec mic de ST 
Bus 002 Device 003: ID 0483:5730 STMicroelectronics
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

// resultat dmesg 
[  112.465000] usb 2-1: new full-speed USB device number 2 using ohci-platform
[  112.680000] input: C-Media Electronics Inc.       USB PnP Sound Device as /devices/platform/soc@01c00000/1c14400.usb/usb2/2-1/2-1:1.2/0003:0D8C:013C.0001/input/input1
[  112.735000] hid-generic 0003:0D8C:013C.0001: input,hidraw0: USB HID v1.00 Device [C-Media Electronics Inc.       USB PnP Sound Device] on usb-1c14400.usb-1/input2
[  113.070000] usbcore: registered new interface driver snd-usb-audio
[  221.890000] usb 2-1: USB disconnect, device number 2
[  229.100000] usb 2-1: new full-speed USB device number 3 using ohci-platform



login pour le chip board : 
username : chip     
pwd : chip     
https://github.com/fordsfords/wlan_pwr/blob/gh-pages/wlan_pwr   // desactive power saving pour le wifi 
resultat de 'uname -a' :  Linux chip 4.4.13-ntc-mlc #1 SMP Tue Dec 6 21:38:00 UTC 2016 armv7l GNU/Linux
java version "1.8.0_111" 
fsck              // check l-integrite de systeme de fichier 
sudo amixer cset numid=3 1               // set the audio out, 0=auto, 1=3.5mm socket or 2=HDMI output
sudo amixer cget numid=3                // avoir la valeur
             numid=2 1        // mute 1, unmute 0
sudo amixer cset numid=1 -- -400       // set volume  
```




#### UART
```

Enable UART

#!/bin/bash

sudo systemctl stop serial-getty@ttyS0.service

sudo systemctl disable serial-getty@ttyS0.service

sudo chgrp dialout /dev/ttyS0

sudo chmod g+rw /dev/ttyS0



http://eclipsesource.com/blogs/2012/10/17/serial-communication-in-java-with-raspberry-pi-and-rxtx/

https://yoursunny.com/t/2016/CHIP-wireless-UART/

https://bbs.nextthing.co/t/second-serial-port/4163/22           // activation 2eme UART, methode qu-on utilise  


// resultat de "sudo cat /proc/tty/driver/serial" avant modif 
serinfo:1.0 driver revision:
0: uart:U6_16550A mmio:0x01C28400 irq:28 tx:7842 rx:0 RTS|CTS|DTR|DSR|CD|RI
1: uart:U6_16550A mmio:0x01C28C00 irq:29 tx:27639 rx:3502 RTS|CTS|DTR
2: uart:unknown port:00000000 irq:0
3: uart:unknown port:00000000 irq:0

// apres modif

0: uart:U6_16550A mmio:0x01C28400 irq:27 tx:7892 rx:0 RTS|CTS|DTR|DSR|CD|RI
1: uart:U6_16550A mmio:0x01C28C00 irq:29 tx:27543 rx:3502 RTS|CTS|DTR
2: uart:U6_16550A mmio:0x01C28800 irq:28 tx:0 rx:0 CTS
3: uart:unknown port:00000000 irq:0


```

#### Methode utilise pour activer uart2 
voir https://bbs.nextthing.co/t/second-serial-port/4163/22 
```

For people who doesn-t want to recompile anything    
    
1 - Get my compiled device tree file and install in /boot    
    
sudo bash (password chip)    
cd /boot    
rm sun5i-r8-chip.dtb    
wget https://dl.dropboxusercontent.com/u/48891705/chip/serial/sun5i-r8-chip.dtb    
exit    
    
2 - Copy the c code to enable the uart2.    
cd /home/chip    
wget https://dl.dropboxusercontent.com/u/48891705/chip/serial/setGPIOuart2    
chmod +x setGPIOuart2    
    
3 - now reboot and when it is done execute setGPIOuart2    
sudo ./setGPIOuart2    

4- ajouter les lignes suivantes dans '/etc/rc.local' :     
    cd /home/chip/bin/
    sudo ./setGPIOuart2
    

```



----
#### Issues       

- Memory corruption:** http://ideaheap.com/2013/07/stopping-sd-card-corruption-on-a-raspberry-pi/ 

- probleme memoire flash :       
      
[  838.920000] UBIFS error (ubi0:0 pid 567): ubifs_readdir: cannot find next direntry, error -22      
probleme similaire : https://bbs.nextthing.co/t/chip-switches-to-readonly-refuses-to-let-me-write-until-i-reboot/12418/8           
solution 1 : reflasher      
solution 2 : minimiser les ecriture dans la memoir NAND --> http://www.chip-community.org/index.php/Flash       
      
- probleme txrxComm librairie -> http://stackoverflow.com/questions/15199768/maven-surefire-plugin-dlls-and-java-library-path      
- probleme audio ne marche pas lorsqu-on le lance via a boot script 
   https://github.com/alexa-pi/AlexaPi/blob/master/src/scripts/initd_alexa.sh    
   https://github.com/alexa-pi/AlexaPi/wiki/Running-as-root    
   tuto sur les usergroups : https://www.cyberciti.biz/faq/linux-show-groups-for-user/     
   solution : 1- ajouter root au group audio ' sudo usermod -a -G audio root'  
                  autre alternative ' sudo adduser root audio' 
                  on verifie qu-il appartient a ce groupe par : 'groups root'
                  liste des utilisateurs connecte : 'users' 

               2- ajouter le fichier .asoundrc dans /root    (voir dans le dossier 'scripts' dans le projet 'alexa-testing') 


- probleme script de demarrage ( via systemd) : erreur = 'Failed at step EXEC spawning” even with proper group permissions'
  solution :
              1- mettre l-option 'ProtectHome' a false ( ProtectHome=false ) dans l-unite de service. 
              2- Lors du demarrage automatique de l-app, le playback ne marche pas a cause de la variable
                VLC_PLUGIN_PATH. La solution est de lancer l-app via maven (mvn exec:exec)  
  
- probleme boot time : 
https://bbs.nextthing.co/t/chip-os-boot-time/318/6
https://github.com/NextThingCo/CHIP-SDK    

----      



#### Board setup       
```      
- activer wifi           
    nmcli device wifi list              
    sudo nmcli device wifi connect '(your wifi network name/SSID)' password '(your wifi password)' ifname wlan0              
- installation de git           
       sudo apt-get update              
       sudo apt-get install git-core           
- install vim    'apt-get install vim' 
- installer java8 -- voir lien plus haut        
- installer tmux          
- activer le serial port sur uart2 -- voir lien plus haut         
- installer librairies pour java 'sudo apt-get install librxtx-java' 
- desactiver le xserver --> sudo systemctl set-default multi-user.target 
- cloner le projet alexa-testing         
- lancer script dans le projet alexa ( installation de mvn etc ...) 
- supprimer le dossier alexa-testing et le recloner 
- copier le script de lancement (alexa-startup.sh) dans home (~) 
- appliquer modifs dans /etc/rc.local ( voir dans <proj-alexa>/scripts/rc.local )
#- changer ajout 'root' au groupe 'audio'
#- copier '.asoundrc' dans '/root'
- copier fichier AlexaPi.service dans '/etc/systemd/system'
- faire 'sudo systemctl enable AlexaPi' 
- faire 'sudo systemctl satrt AlexaPi' 
- faire 'sudo systemctl status AlexaPi' pour verifier que tout est correct  
- rebouter le systeme et croiser les doigts !!  

- (optionel) : pour regler le probleme relatif au NAND -> suivre indications dans http://www.chip-community.org/index.php/Flash   
               ne pas appliquer la derniere commande 'fw_setenv bootargs root=ubi0:rootfs rootfstype=ubifs ro fastboot noswap earlyprintk ubi.mtd=4'   

``` 


#### Logs 
- 1 probleme hostname service 
         Starting Hostname Service...
[FAILED] Failed to start Hostname Service.



chip@chip:~$ systemctl status systemd-hostnamed.service
? systemd-hostnamed.service - Hostname Service
   Loaded: loaded (/lib/systemd/system/systemd-hostnamed.service; static)
   Active: failed (Result: exit-code) since Thu 2017-01-12 17:50:42 UTC; 59s ago
     Docs: man:systemd-hostnamed.service(8)
           man:hostname(5)
           man:machine-info(5)
           http://www.freedesktop.org/wiki/Software/systemd/hostnamed
  Process: 327 ExecStart=/lib/systemd/systemd-hostnamed (code=exited, status=226/NAMESPACE)
 Main PID: 327 (code=exited, status=226/NAMESPACE)



- 2 probleme snowboy kitt_ai 

INFO:main: Starting Wake Word Agent
INFO:WakeWordAgent: State set to IDLE(2)
terminate called after throwing an instance of 'std::ios_base::failure'
  what():  basic_filebuf::underflow error reading the file
Aborted


- 3 probleme NAND 
- compilation du wakeWord agent :    
    1- cmake .    
    2- make    

logs lie au probleme de NAND  : 
```
[  283.485000] UBIFS error (ubi0:0 pid 501): ubifs_read_node: bad node at LEB 28:307424, LEB mapping status 1      
[  283.495000] Not a node, first 24 bytes:      
[  283.495000] 00000000: 47 e8 4d 05 dc 8e 72 f7 30 7b 1d 45 2e 10 42 a3 bf 47 44 4e 7d 8f 98 a0                          G.M...r.0{.E..B..GDN}...      
[  283.510000] UBIFS error (ubi0:0 pid 501): do_readpage: cannot read page 0 of inode 86519, error -22      
[  283.540000] UBIFS error (ubi0:0 pid 501): ubifs_read_node: bad node type (125 but expected 1)      
[  283.550000] UBIFS error (ubi0:0 pid 501): ubifs_read_node: bad node at LEB 28:307424, LEB mapping status 1      
[  283.560000] Not a node, first 24 bytes:      
[  283.565000] 00000000: 47 e8 4d 05 dc 8e 72 f7 30 7b 1d 45 2e 10 42 a3 bf 47 44 4e 7d 8f 98 a0                          G.M...r.0{.E..B..GDN}...      
[  283.580000] UBIFS error (ubi0:0 pid 501): do_readpage: cannot read page 0 of inode 86519, error -22      
[  425.860000] UBIFS error (ubi0:0 pid 510): ubifs_read_node: bad node type (125 but expected 1)      
[  425.870000] UBIFS error (ubi0:0 pid 510): ubifs_read_node: bad node at LEB 28:307424, LEB mapping status 1      
[  425.880000] Not a node, first 24 bytes:      
```

- 4 probleme exception pour le format audio 
```
21:27:46.805 [RequestThread] INFO  com.amazon.alexa.avs.http.AVSClient - This response successfully had no content.
21:27:50.148 [Thread-2] INFO  com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Received wake word detected
21:27:50.149 [Thread-2] INFO  com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Wake Word Detected ......
21:27:50.157 [Thread-41] INFO  com.amazon.alexa.avs.AVSApp - Wake Word was detected
21:27:50.169 [Thread-42] DEBUG com.amazon.alexa.avs.wakeword.WakeWordIPCSocket - Sending command IPC_PAUSE_WAKE_WORD_ENGINE to all connected clients
21:27:50.177 [Thread-42] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
21:27:51.200 [Thread-42] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
21:27:52.208 [Thread-42] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
21:27:53.215 [Thread-42] WARN  com.amazon.alexa.avs.AVSController - Could not open the microphone line.
21:27:54.234 [Thread-42] ERROR com.amazon.alexa.avs.AVSApp - An error occured creating speech request
javax.sound.sampled.LineUnavailableException: line with format PCM_SIGNED 16000.0 Hz, 16 bit, mono, 2 bytes/frame, little-endian not supported.
        at com.sun.media.sound.DirectAudioDevice$DirectDL.implOpen(DirectAudioDevice.java:513) ~[?:1.8.0_111]
        at com.sun.media.sound.AbstractDataLine.open(AbstractDataLine.java:121) ~[?:1.8.0_111]
        at com.sun.media.sound.AbstractDataLine.open(AbstractDataLine.java:153) ~[?:1.8.0_111]
        at com.amazon.alexa.avs.AudioCapture.startCapture(AudioCapture.java:79) ~[classes/:?]
        at com.amazon.alexa.avs.AudioCapture.getAudioInputStream(AudioCapture.java:61) ~[classes/:?]
        at com.amazon.alexa.avs.AVSController.getMicrophoneInputStream(AVSController.java:296) ~[classes/:?]
        at com.amazon.alexa.avs.AVSController.startRecording(AVSController.java:274) [classes/:?]
        at com.amazon.alexa.avs.AVSApp$1.actionPerformed(AVSApp.java:172) [classes/:?]
        at com.amazon.alexa.avs.PushButton$1.run(PushButton.java:23) [classes/:?]
        at java.lang.Thread.run(Thread.java:745) [?:1.8.0_111]

```




#### Pocketspinx 
```
cloner :https://github.com/cmusphinx/sphinxbase 
 'git clone https://github.com/cmusphinx/sphinxbase.git'

installer libtool, autoconf, bison:
     'sudo apt-get install libtool'
     'sudo apt-get install autoconf'
     'sudo apt-get install bison'
     'sudo apt-get install libasound2-dev'
     'sudo apt-get install libpulse-dev'
// en compact  sudo apt-get -y install libtool autoconf bison libasound2-dev libpulse-dev  
installer les affaire de python : 
      'sudo apt-get install -y python python-dev python-pip build-essential swig '
installer sphinxbase : 
      //'./autogen.sh --enable-fixed'    
      './autogen.sh     ' 
      './configure'
      'make' 
      'sudo make install' 
 
clone pocketsphinx : https://github.com/cmusphinx/pocketsphinx.git 
       $ ./autogen.sh
       $ ./configure
       $ make clean all
       $ make check
       $ sudo make install

On ajoute les variables d-environement dans .bashrc : 
   'export LD_LIBRARY_PATH=/usr/local/lib' 
   'export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig'



pour python : 

1- installer PortAudio : http://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error 
2- sudo pip install pyaudio
3- install pocketsphinx-python 'sudo pip install pocketsphinx'


 
```




```
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib/python2.7/dist-packages/sphinxbase

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.



----------------------------------------------------------------------

```

#### autres
```
pipe avec pocket sphinx : 

    plughw:1,0 -r 16000 -f S16_LE | ssh -C user@192.168.86.101 sox - test.wav 
and then use it using, 
    pocketsphinx_continuous -dict ~/4568.dic -lm ~/4568.lm -infile ~/test.wav 


Resultat de arecord | => arecord -l
**** List of CAPTURE Hardware Devices ****
card 0: sun4icodec [sun4i-codec], device 0: CDC PCM Codec-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0


```

