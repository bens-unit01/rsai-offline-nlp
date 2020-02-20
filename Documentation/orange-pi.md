


#### Links Orange PI  
#### Armbian 
- **armbian website:** https://www.armbian.com/orange-pi-zero/ 
- **getting started:** https://docs.armbian.com/User-Guide_Getting-Started/ 
- **h3disp:**  https://forum.armbian.com/index.php/topic/752-tutorial-h3disp-change-display-settings-on-h3-devices/?hl=h3disp
- **armbian beta images:** http://image.armbian.com/betaimages/ 

- **github website:** https://github.com/orangepi-xunlong?tab=repositories 
- **Orange PI forum:** http://www.orangepi.org/orangepibbsen/forum.php 
- **static ip wlan0:** http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/ 
- **sun-xi guide:** http://linux-sunxi.org/Fex_Guide 
- **specs, pinouts:** http://linux-sunxi.org/Xunlong_Orange_Pi_Zero 
               https://i1.wp.com/oshlab.com/wp-content/uploads/2016/11/Orange-Pi-Zero-Pinout-banner2.jpg?fit=1200%2C628&ssl=1      


- **Doc, wifi:**  http://linux-sunxi.org/Wifi 
- **sunxi-tools:** http://linux-sunxi.org/Sunxi-tools 

- **uart srial debug pinout:** http://linux-sunxi.org/File:OPi_Zero_UART.jpg     
                               http://linux-sunxi.org/UART     

- **download images:** https://mega.nz/#F!wh8l2BjK!OBep3nMldBletvNNwkH2Jg    
- **download and build:** http://www.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=342 
- **download images links:** http://orangepi.su/content.php?p=99&c=OS%20dlya%20Orange%20Pi 
- **download images mega-upload:** https://mega.nz/#F!m40jgBYQ!-uNiWmKhGoQUAqnWQvlr-w!2pcTUZYD 
- **flash android:** http://orangepi.su/content.php?p=69&c=Ustanovka%20Android%20na%20Orange%20Pi 
- **article mali drivers Odroid:** http://forum.odroid.com/viewtopic.php?f=83&t=6933 
- **dev mali web site:** http://malideveloper.arm.com/documentation-hub/ 

## Build
- **cocos2d:** http://malideveloper.arm.com/documentation/partner-tutorials/the-modern-cocos2d-x-platform/ 
- **Display, AV driver, fex file:** http://www.orangepi.org/Docs/Docscn/Kerneldriversporting.html#Porting_AV_driver 
- **Building u-boot, script.bin and linux-kernel:** http://www.orangepi.org/Docs/Building.html 
- **xradio driver source:** https://github.com/fifteenhex/xradio/tree/original 

#### Lubuntu 
- **Lubuntu installation:** http://www.orangepi.cn/Docs/Docscn/SDcardinstallation.html 
- **FAQ:** http://www.orangepi.org/Docs/FAQ.html 
- **Doc, login:** http://www.orangepi.org/Docs/LogintotheOrangePi.html 
- **installation debian:** http://www.cnx-software.com/2015/09/01/getting-started-with-orange-pi-pc-pi-2-and-pi-plus-development-boards/ 
- **installation, resize file-system:** https://www.s-config.com/orange-pi-needs-to-go-back-into-the-oven/ 
#### Misc notes 
```
DRI : Direct Rendering Infrastructure  
login ssh armbian image :  raouf/bbking456
login ssh armbian image 1er login :  root/1234
login ssh lubuntu image : orangepi/orangepi  
eth0 static ip (eth0) : 10.10.250.83   (branche a wow-extreme)  HWaddr 16:a2:0e:09:da:79 
wlan0 :  Link encap:Ethernet  HWaddr 14:89:79:6e:d0:bf
          inet addr:10.10.250.84  Bcast:10.10.250.255  Mask:255.255.255.0
wlan0 orange-pi-zero :   HWaddr 3c:e3:56:5e:86:64 
wlan0 PI 3 : 
 40:a5:ef:0e:d8:97
 b8:27:eb:4f:93:bf

/etc/network/interfaces    //conf reseau 
/etc/wpa_supplicant/     // param wifi 
/etc/init.d/             //scripts initialisation  
/etc/init.d/bootmisc.sh   //initialisation lors du bootup  

/boot/config-3.4.113-sun8i   // fichier de configuration 
/boot/bin                  // fichiers .bin 
 --> ligne 2794  
/etc/modules-load.d/modules.conf
/lib/modules/3.4.113-sun8i$   // scripts pour charger les pilotes
/var/cache/man/5532:          // on peut l-utiliser pour liberer de l-espace  

iw list              // details sur wlan0 
uname -a             // version de l-OS
          pour la version debian server on :  Linux orangepizero 3.4.113-sun8i #50 SMP PREEMPT Mon Nov 14 08:41:55 CET 2016 armv7l GNU/Linux     
lsb_release -a        : 


sudo nmtui           // utilitaire configuration reseau  
sudo nmtui-connect   // pour se connecter au wifi 
iwconfig wlan0       // parametres reseau 
lsmod                // affiche les modules charge 
arp -a                 // ip-to-physical address translation table  
specs : H2+ SoC 
apt-cache xfce          // cherche le package xfce 

dpkg-reconfigure  
dpkg-reconfigure locales  // setup langue, time zone 
dpkg -l | grep alsa       // verifier si alsa est installe 
sudo apt-get --purge remove gimp         // supprimer un package

// android 
https://github.com/igorpecovnik/lib/blob/master/patch/kernel/sun8i-default/z-0003-add-additional-video-modes.patch  
http://www.cnx-software.com/2016/11/10/allwinner-h2-linux-android-sdk-and-allwinner-xr819-wifi-driver-released/ 



console=tty1 console=ttyS0,115200  

----
// contenu de /etc/armian.txt 
Title:                  Armbian 5.24 Orangepizero Ubuntu xenial default
Kernel:                 Linux 3.4.113
Build date:             14.11.2016
Authors:                http://www.armbian.com/authors
Sources:                http://github.com/igorpecovnik/lib
Support:                http://forum.armbian.com/
Changelog:              http://www.armbian.com/logbook/
Documentation:          http://docs.armbian.com/



```


#### Issues 
- **Wifi:** https://forum.armbian.com/index.php/topic/2907-opi-zero-incoming-ssh-cant-connect/     
            https://github.com/igorpecovnik/lib/commit/76444a386f652a9800f968c98cc56c87aecd7456     
- **TV-OUT issue:** http://www.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=705 
                 http://orange314.com/Getting_video_from_AV-OUT    
                 https://forum.armbian.com/index.php/topic/1352-orangepi-pc-tv-out/     
    http://www.orangepi.org/orangepibbsen/forum.php?mod=viewthread&tid=1349&page=3#pid12309   
    https://forum.armbian.com/index.php/topic/1352-orangepi-pc-tv-out/     
    http://linux-sunxi.org/Display    
#### Desktop manager 

 installer xserver : https://forum.armbian.com/index.php/topic/822-installing-x-server-files/      
commande : apt-get -y install xorg lightdm xfce4 tango-icon-theme gnome-icon-theme
 tft-lcd 5-inchs : http://www.ebay.com/itm/5-Inch-TFT-LCD-Car-Rear-View-Rearview-Monitor-With-Stand-Reverse-Backup-Camera-/121763367503?hash=item1c59a98a4f:g:dvwAAOSwEetV-9sr 


http://linux-sunxi.org/Mali_binary_driver 

https://forum.armbian.com/index.php/topic/1940-lime2-jessie-default-desktop-no-fbturbo/ 

https://forum.armbian.com/index.php/topic/299-udoo-problems-with-build/
// commande fex 
"Usage: ./sunxi-fexc [-vq] [-I <infmt>] [-O <outfmt>] [<input> [<output>]]" 

infmt:  fex, bin  (default:fex)
outfmt: fex, bin, uboot  (default:bin)

//build natively 
make all CROSS_COMPILE=  

```
    ntsc(screen1_output_mode = 14)
    resultat de lsmod : 

raouf@orangepizero:~$ lsmod
Module                  Size  Used by
bmp085                  3487  0
pcf8591                 3363  0
xradio_wlan           210530  0
mac80211              358445  1 xradio_wlan



parms  
```
  
- **fex** https://github.com/igorpecovnik/lib/commit/ed4dd944fc04f9a83461729182762cb1b409fb6a#diff-951c387741874ac5d0623910f597ec0c     
          http://pastebin.com/480BYtj3     
          https://forum.armbian.com/index.php/topic/2808-orange-pi-zero-went-to-the-market/page-2#entry19336     
          http://linux-sunxi.org/Fex_Guide#disp_init_configuration    
          http://www.imajeenyus.com/computer/20130301_android_tablet/android/fex2bin_etc.html 

 

- **audio** 
           https://www.howtoforge.com/tutorial/arch-linux-installation-with-xfce-desktop/2/ 
```
Pour utiliser un usb-mic on fait : 
    voir index de la carte      'cat /proc/asound/cards'
    on peut aussi faire         'arecord -l' 
     changer carte par defaut dans   /usr/share/alsa/alsa.conf     
         2 lignes a changer : 

defaults.ctl.card 2 
defaults.pcm.card 2 
voir --> http://raspberrypi.stackexchange.com/questions/37177/best-way-to-setup-usb-mic-as-system-default-on-raspbian-jessie     

on change aussi ~/.asoundrc commme suit : 
pcm.!default {
  type asym
   playback.pcm {
     type plug
     slave.pcm "hw:0,0"
   }
   capture.pcm {
     type plug
     slave.pcm "hw:2,0"                 ***** ligne a changer 
   }
}

la commande pour enregistrer va etre comme suit: 
                 'arecord -D plughw:2 --duration=10 -f cd -vv test01.wav' 

autres modules peut etre necessaire : 
libatlas-base-dev
sudo apt-get install -y vlc vlc-nox vlc-data


```  
