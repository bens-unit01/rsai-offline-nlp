


## SPEECH RECOGNITION 

#### Links   

**CMU sphinx:** http://cmusphinx.sourceforge.net/2016/06/should-you-select-raspberry-pi-3-or-raspberry-pi-b-for-cmusphinx/  
**Differentes versions:** http://cmusphinx.sourceforge.net/wiki/versions     

**Comparaison +ieurs engine:** http://suendermann.com/su/pdf/oasis2014.pdf     
**Download links for Sphinx:** http://cmusphinx.sourceforge.net/wiki/download    

**Talking chatbot:**    https://www.youtube.com/watch?v=BxWAUbXWZYI&index=3&list=PLsAtoG7tyRONWPHNUkVYRv7mgNFvp0OMt       

**chatbot, aiml + python:** http://www.devdungeon.com/content/ai-chat-bot-python-aiml#existing-aiml-files    
**chatbot, aiml + python, un autre site: http://riotsw.com/blog/?p=92    
**tuto, pocketsphinx:** http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/     
**projet ROS, pocketsphinx + gstreamer:** http://wiki.ros.org/pocketsphinx    
**installation sur raspberry pi:** http://cmusphinx.sourceforge.net/wiki/raspberrypi  
**installation sur linux:** http://jrmeyer.github.io/installation/2016/01/09/Installing-CMU-Sphinx-on-Ubuntu.html      
**tuto sur raspberry pi:** https://wolfpaulus.com/embedded/raspberrypi2-sr/       
**tuto 2 sur raspberry pi:** https://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/    
**convertir audio au format de pocketsphinx:** http://stackoverflow.com/questions/13693006/convert-audio-files-for-cmu-sphinx-4-input  
**autre tuto sur raspberry pi:** https://coderwall.com/p/_a_scg/how-to-setup-speech-recognition-using-a-raspberrypi-pocketsphinx-ps3eye     



**tunning 1:** https://sourceforge.net/p/cmusphinx/discussion/help/thread/b3f85f5d/      
**tunning 2:** https://sourceforge.net/p/cmusphinx/discussion/help/thread/2f0b15cb/?limit=25      
**tunning 3:** https://sourceforge.net/p/cmusphinx/discussion/help/thread/4341476f/?limit=25       
**tuning 4:** http://cmusphinx.sourceforge.net/wiki/decodertuning     
**tunning 5 + performance test:** https://www.element14.com/community/roadTestReviews/2166/l/roadtest-review-a-raspberry-pi-3-model-b-review    
**quelques parametres:** http://cmusphinx.sourceforge.net/wiki/pocketsphinxhandhelds     
**pocketsphinx models:** https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/US%20English/    
**demo, rapide sur android:** https://github.com/andrenatal/PsContinuous     
**une autre demo sur android:** https://www.youtube.com/watch?v=fSD0wkxdWco    



**pocketsphinx FAQ:** http://cmusphinx.sourceforge.net/wiki/faq      
**finite state grammar example:** https://sourceforge.net/p/cmusphinx/discussion/help/thread/38ed41de/?limit=25     
** ILA, pocketsphinx + java:** https://sites.google.com/site/ilavoiceassistant/how-tos/installing-pocketsphinx     
**Adaptation tuto:** https://www.youtube.com/watch?v=IAHH6-t9jK0
**Training procedure:** https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=en&ie=UTF8&prev=_t&rurl=translate.google.com&sl=auto&sp=nmt4&tl=en&u=https://github.com/mondhs/lt-pocketsphinx-tutorial/tree/master/training&usg=ALkJrhh01rRFFO1C1pizko_pLSaViimMjA


**discusion pocketsphinx + turtlebot:** https://sourceforge.net/p/cmusphinx/discussion/help/thread/d7cc9fc9/?limit=25    
**discussion adapt vs training:** https://news.ycombinator.com/item?id=11173872    
**plusieur projet en C pour raspberry, utilise google speech rec:** https://github.com/StevenHickson/PiAUISuite    



**building a language model:** http://cmusphinx.sourceforge.net/wiki/tutoriallm       


**Demo rapide avec python + gstreamer:** https://www.youtube.com/watch?v=o_op-FsLuFM   
                                         git https://bitbucket.org/matthew3/speakpython/wiki/Home 
                                         source code gstpocketspinx        // https://github.com/skerit/cmusphinx/blob/master/pocketsphinx/src/gst-plugin/gstpocketsphinx.h    
                              voir aussi : https://github.com/gnu-user?tab=repositories       
                                      et : https://devpost.com/software/speakpython      


**Pocketsphinx + gstreamer:** http://cmusphinx.sourceforge.net/wiki/gstreamer      
**Training tuto:** https://sites.google.com/site/ilavoiceassistant/how-tos/installing-pocketsphinx    

**Natural Language Processing:** https://github.com/6thsolution/ApexNLP     


**models pour pocketsphinx:** http://www.repository.voxforge1.org/downloads/Main/Trunk/AcousticModels/Sphinx/      


#### Keywords 
CMU sphinxtrain (v1.0.8) toolkit
vocabulary model

fsg     finite state grammar  


keyword lists
grammars and statistical language models
phonetic statistical language models


#### Autres  
CMU Sphinx
Pocketsphinx
Jasper            https://jasperproject.github.io/   https://github.com/jasperproject/jasper-client     
Jarvis
Kaldi            https://sourceforge.net/projects/kaldi/                 
                 https://github.com/kaldi-asr/kaldi          
kaldi sur android : http://jcsilva.github.io/2017/03/18/compile-kaldi-android/     
Kaldi + Gstreamer https://github.com/alumae/kaldi-gstreamer-server   
Inprotk          https://sourceforge.net/projects/inprotk/ 
Julius 
Pocketsphinx 
Dragon 
ISIP speech recognizer
HTK
Sphrachcore
NICO
Intel AVSR dictaiton machines


#### Demo python 
PyAudio, Pyaiml, Pocketsphinx, Espeak




#### Divers 
```

apt-cache search libasound         // checker voir package incluant ce mot cle 
commande 1 : pocketsphinx_continuous -hmm /usr/local/share/pocketsphinx/model/en-us/en-us -lm 6610.lm -dict 6610.dic -samprate 16000/8000/48000 -inmic yes  -fwdflat yes -bestpath no -fwdtree no
 


pocketsphinx_continuous -hmm /usr/local/share/pocketsphinx/model/en-us/en-us -lm ../../models/6610.lm -dict ../../models/6610.dic -samprate 16000/8000/48000 -inmic yes  -fwdflat yes -bestpath no -fwdtree no 

commande 2 : pocketsphinx_continuous -lm /home/pi/scarlettPi/config/speech/lm/scarlett.lm -dict /home/pi/scarlettPi/config/speech/dict/scarlett.dic -hmm /home/pi/scarlettPi/config/speech/model/hmm/en_US/hub4wsj_sc_8k -silprob  0.1 -wip 1e-4 -bestpath 0 


-fwdflat no -bestpath no
-fwdflat yes -bestpath no -fwdtree no

pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -lm 6610.lm -dict 6610.dic -samprate 16000/8000/48000 -inmic yes  -fwdflat no -bestpath no 
pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -kws phrases.list -kws_threshold 1e-20 -dict 6610.dic -samprate 16000/8000/48000 -inmic yes  -fwdflat no -bestpath no 


pocketsphinx_continuous  -hmm ~/tmp/model-test-01 -jsgf gramjsgf.jsgf  -dict dic.dic -samprate 8000 -maxhmmpf 3000 -maxwpf 10 -pl_window 2 -backtrace no -bestpath no -fwdflat no -fwdtree yes -inmic yes 



//---------------------------------
pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -jsgf gramj.gram -dict pizza.dict  -samprate 16000/8000/48000  -inmic yes -fwdtree no -fwdflat no -bestpath no -maxhmmpf 3000 -maxwpf 10 -pl_window 2 -backtrace no 

pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -jsgf gramj.gram -dict pizza.dict  -samprate 16000/8000/48000  -inmic yes -fwdtree no -fwdflat no -bestpath no -maxhmmpf 3000 -maxwpf 10 -pl_window 2 -backtrace no -ds 2 


pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -jsgf gramj.gram -dict pizza.dict -samprate 16000/8000/48000 -inmic yes -fwdtree no -fwdflat no -bestpath no 




pocketsphinx_continuous  -hmm ~/tmp/model-en-us-semi -jsgf gramj.gram -dict pizza.dict  -samprate 16000/8000/48000  -inmic yes -fwdtree no -fwdflat no -bestpath no -maxhmmpf 2000 -maxwpf 10 -pl_window 2 -backtrace yes 



pathgram   gramj.txt
pathdic    dic.dic
-jsgf

KWS
FSG  : finite state grammar 




    this.c.setString("-hmm",gram.pathhmm);
201
202                 // LEXICAL MODEL
203                 this.c.setString("-dict",gram.pathdic);
204
205                 // LM
206                 this.c.setString("-jsgf",gram.pathgram);
207
208                 // LOG FILES
209                 //c.setString("-rawlogdir", "/sdcard/Android/data/pocketsphinx");
210                 pocketsphinx.setLogfile("/sdcard/Android/data/pocketsphinx/pocketsphinx.log");
211
212                 this.c.setFloat("-samprate", 8000);
213                 this.c.setInt("-maxhmmpf", 3000);
214                 this.c.setInt("-maxwpf", 10);
215                 this.c.setInt("-pl_window", 2);
216                 this.c.setBoolean("-backtrace", true);
217                 this.c.setBoolean("-bestpath", true);
218                 this.c.setBoolean("-fwdflat", true);
219                 this.c.setBoolean("-fwdtree", true);
220



183                 this.c.setFloat("-samprate", 8000);
184                 this.c.setInt("-maxhmmpf", 2000);
185                 this.c.setInt("-maxwpf", 10);
186                 this.c.setInt("-pl_window", 2);
187                 this.c.setBoolean("-backtrace", true);
188                 this.c.setBoolean("-bestpath", false);


183                 this.c.setFloat("-samprate", 8000);
184                 this.c.setInt("-maxhmmpf", 2000);
185                 this.c.setInt("-maxwpf", 10);
186                 this.c.setInt("-pl_window", 2);
187                 this.c.setBoolean("-backtrace", true);
188                 this.c.setBoolean("-bestpath", false);





```


#### Training 
```
// dictionnaire
A               1
ANCHOVIES       2
I               3
LARGE           4
MEDIUM          5
MUSHROOMS       6
ORDER           7
PEPPERONI       8
PIZZA           9
SMALL           10
TO              11 
WANT            12
WITH            13


doc training : http://cmusphinx.sourceforge.net/wiki/tutorialadapt     
doc language model : http://cmusphinx.sourceforge.net/wiki/tutoriallm    
sphinxtrain  : https://github.com/cmusphinx/sphinxtrain    


conversion format wav : http://audio.online-convert.com/convert-to-wav     


ffmpeg -i 4.wav -ar 16000 -ac 1 4-2.wav  //commande ffmpeg 
ffmpeg -i input.mp3 -acodec pcm_s16le -ac 1 -ar 16000 output.wav

``` 

#### Issues
```
1- log: 
  Could not link test program to Python. Maybe the main Python library has been
  installed in some non-standard library path. If so, pass it to configure,
  via the LDFLAGS environment variable.
  Example: ./configure LDFLAGS="-L/usr/non-standard-path/python/lib"
  ============================================================================
   ERROR!
   You probably have to install the development version of the Python package
   for your distribution.  The exact name of this package varies among them.
  ============================================================================

See `config.log' for more details'
solution -> installer les modules de python-dev : 
      'sudo apt-get install -y python python-dev python-pip build-essential swig '



2- logs : build pocketsphinx-python : 
Fatal error: can't create build/temp.linux-armv7l-2.7/../sphinxbase/src/libsphinxbase/lm/ngram_model_trie.o: No such file or directory
error: command 'arm-linux-gnueabihf-gcc' failed with exit status 1


running install
running bdist_egg
running egg_info
writing pocketsphinx.egg-info/PKG-INFO
writing top-level names to pocketsphinx.egg-info/top_level.txt
writing dependency_links to pocketsphinx.egg-info/dependency_links.txt
reading manifest file 'pocketsphinx.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
no previously-included directories found matching 'build'
no previously-included directories found matching 'dist'
warning: no files found matching '*.h' under directory 'sphinxbase/include'
warning: no files found matching '*.c' under directory 'sphinxbase/src'
warning: no files found matching '*.h' under directory 'sphinxbase/src'
warning: no files found matching '*.i' under directory 'sphinxbase/swig'
no previously-included directories found matching 'sphinxbase/include/wince'
no previously-included directories found matching 'sphinxbase/include/android'
no previously-included directories found matching 'sphinxbase/src/sphinx_adtools'
no previously-included directories found matching 'sphinxbase/src/sphinx_cepview'
no previously-included directories found matching 'sphinxbase/src/sphinx_fe'
no previously-included directories found matching 'sphinxbase/src/sphinx_jsgf2fsg'
no previously-included directories found matching 'sphinxbase/src/sphinx_lmtools'
warning: no files found matching '*.h' under directory 'pocketsphinx/include'
warning: no files found matching '*.c' under directory 'pocketsphinx/src'
warning: no files found matching '*.h' under directory 'pocketsphinx/src'
warning: no files found matching '*.i' under directory 'pocketsphinx/swig'
no previously-included directories found matching 'pocketsphinx/src/gst-plugin'
no previously-included directories found matching 'pocketsphinx/src/programs'
writing manifest file 'pocketsphinx.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-armv7l/egg
running install_lib
running build_py
copying ../sphinxbase/swig/python/sphinxbase.py -> build/lib.linux-armv7l-2.7/sphinxbase
running build_ext
building 'sphinxbase._sphinxbase' extension
swigging ../sphinxbase/swig/sphinxbase.i to ../sphinxbase/swig/sphinxbase_wrap.c
swig -python -modern -threads -I../sphinxbase/include -I../sphinxbase/include/sphinxbase -Iinclude -outdir ../sphinxbase/swig/python -o ../sphinxbase/swig/sphinxbase_wrap.c ../sphinxbase/swig/sphinxbase.i
arm-linux-gnueabihf-gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -D_FORTIFY_SOURCE=2 -g -fstack-protector-strong -Wformat -Werror=format-security -fPIC -DSPHINXBASE_EXPORTS -DPOCKETSPHINX_EXPORTS -DHAVE_CONFIG_H -D_CRT_SECURE_NO_DEPRECATE -D_USRDLL -DSPHINXDLL -I../sphinxbase/include -I../sphinxbase/include/sphinxbase -Iinclude -I/usr/include/python2.7 -c ../sphinxbase/swig/sphinxbase_wrap.c -o build/temp.linux-armv7l-2.7/../sphinxbase/swig/sphinxbase_wrap.o -Wno-unused-label -Wno-strict-prototypes -Wno-parentheses -Wno-unused-but-set-variable -Wno-unused-variable -Wno-unused-result
Assembler messages:
Fatal error: can't create build/temp.linux-armv7l-2.7/../sphinxbase/swig/sphinxbase_wrap.o: No such file or directory
error: command 'arm-linux-gnueabihf-gcc' failed with exit status 1





issue - Delai de 5 seconds : 


INFO: continuous.c(261): Listening...
INFO: cmn_live.c(120): Update from < 31.72  9.10 -7.55 11.74  4.57  1.42 -6.82 -6.90  3.71 -3.25  6.10  2.56 -1.70 >
INFO: cmn_live.c(138): Update to   < 33.09  9.90 -7.06 10.44  3.03  1.95 -5.09 -7.51  2.40 -1.42  4.71  3.11 -1.69 >
INFO: ngram_search_fwdtree.c(1550):      536 words recognized (5/fr)
INFO: ngram_search_fwdtree.c(1552):    21161 senones evaluated (196/fr)
INFO: ngram_search_fwdtree.c(1556):    11318 channels searched (104/fr), 1225 1st, 8541 last
INFO: ngram_search_fwdtree.c(1559):      706 words for which last channels evaluated (6/fr)
INFO: ngram_search_fwdtree.c(1561):      350 candidate words for entering last phone (3/fr)
INFO: ngram_search_fwdtree.c(1564): fwdtree 1.33 CPU 1.231 xRT
INFO: ngram_search_fwdtree.c(1567): fwdtree 7.24 wall 6.703 xRT



INFO: continuous.c(252): Ready....
INFO: continuous.c(261): Listening...
INFO: cmn_live.c(120): Update from < 41.00 -5.29 -0.12  5.09  2.48 -4.07 -1.37 -1.78 -5.08 -2.05 -6.45 -1.42  1.17 >
INFO: cmn_live.c(138): Update to   < 37.15 11.76 -7.41  2.44 -1.18  5.37  6.10 -10.68 -0.06 13.69 -5.38  2.90  4.92 >
INFO: ngram_search_fwdtree.c(1550):      865 words recognized (6/fr)
INFO: ngram_search_fwdtree.c(1552):    33121 senones evaluated (219/fr)
INFO: ngram_search_fwdtree.c(1556):    17572 channels searched (116/fr), 1998 1st, 13222 last
INFO: ngram_search_fwdtree.c(1559):     1120 words for which last channels evaluated (7/fr)
INFO: ngram_search_fwdtree.c(1561):      460 candidate words for entering last phone (3/fr)
INFO: ngram_search_fwdtree.c(1564): fwdtree 1.41 CPU 0.934 xRT
INFO: ngram_search_fwdtree.c(1567): fwdtree 6.52 wall 4.317 xRT
INFO: ngram_search_fwdflat.c(302): Utterance vocabulary contains 12 words
INFO: ngram_search_fwdflat.c(948):      716 words recognized (5/fr)
INFO: ngram_search_fwdflat.c(950):    36113 senones evaluated (239/fr)
INFO: ngram_search_fwdflat.c(952):    24433 channels searched (161/fr)
INFO: ngram_search_fwdflat.c(954):     1597 words searched (10/fr)
INFO: ngram_search_fwdflat.c(957):      726 word transitions (4/fr)
INFO: ngram_search_fwdflat.c(960): fwdflat 0.59 CPU 0.391 xRT
INFO: ngram_search_fwdflat.c(963): fwdflat 0.59 wall 0.390 xRT
INFO: ngram_search.c(1250): lattice start node <s>.0 end node </s>.135
INFO: ngram_search.c(1276): Eliminated 0 nodes before end node
INFO: ngram_search.c(1381): Lattice has 121 nodes, 213 links
INFO: ps_lattice.c(1380): Bestpath score: -4428
INFO: ps_lattice.c(1384): Normalizer P(O) = alpha(</s>:135:149) = -232619
INFO: ps_lattice.c(1441): Joint P(O,S) = -265656 P(S|O) = -33037
INFO: ngram_search.c(872): bestpath 0.00 CPU 0.000 xRT
INFO: ngram_search.c(875): bestpath 0.00 wall 0.001 xRT
SHUTDOWN



startup logs : 



INFO: pocketsphinx.c(152): Parsed model-specific feature parameters from /usr/local/share/pocketsphinx/model/en-us/en-us/feat.params
Current configuration:
[NAME]                  [DEFLT]         [VALUE]
-agc                    none            none
-agcthresh              2.0             2.000000e+00
-allphone
-allphone_ci            yes             yes
-alpha                  0.97            9.700000e-01
-ascale                 20.0            2.000000e+01
-aw                     1               1
-backtrace              no              no
-beam                   1e-48           1.000000e-48
-bestpath               yes             yes
-bestpathlw             9.5             9.500000e+00
-ceplen                 13              13
-cmn                    live            batch
-cmninit                40,3,-1         41.00,-5.29,-0.12,5.09,2.48,-4.07,-1.37,-1.78,-5.08,-2.05,-6.45,-1.42,1.17
-compallsen             no              no
-debug                                  0
-dict                                   6610.dic
-dictcase               no              no
-dither                 no              no
-doublebw               no              no
-ds                     1               1
-fdict
-feat                   1s_c_d_dd       1s_c_d_dd
-featparams
-fillprob               1e-8            1.000000e-08
-frate                  100             100
-fsg
-fsgusealtpron          yes             yes
-fsgusefiller           yes             yes
-fwdflat                yes             yes
-fwdflatbeam            1e-64           1.000000e-64
-fwdflatefwid           4               4
-fwdflatlw              8.5             8.500000e+00
-fwdflatsfwin           25              25
-fwdflatwbeam           7e-29           7.000000e-29
-fwdtree                yes             yes
-hmm                                    /usr/local/share/pocketsphinx/model/en-us/en-us
-input_endian           little          little
-jsgf
-keyphrase
-kws
-kws_delay              10              10
-kws_plp                1e-1            1.000000e-01
-kws_threshold          1e-30           1.000000e-30
-latsize                5000            5000
-lda
-ldadim                 0               0
-lifter                 0               22
-lm                                     6610.lm
-lmctl
-lmname
-logbase                1.0001          1.000100e+00
-logfn
-logspec                no              no
-lowerf                 133.33334       1.300000e+02
-lpbeam                 1e-40           1.000000e-40
-lponlybeam             7e-29           7.000000e-29
-lw                     6.5             6.500000e+00
-maxhmmpf               30000           30000
-maxwpf                 -1              -1
-mdef
-mean
-mfclogdir
-min_endfr              0               0
-mixw
-mixwfloor              0.0000001       1.000000e-07
-mllr
-mmap                   yes             yes
-ncep                   13              13
-nfft                   512             512
-nfilt                  40              25
-nwpen                  1.0             1.000000e+00
-pbeam                  1e-48           1.000000e-48
-pip                    1.0             1.000000e+00
-pl_beam                1e-10           1.000000e-10
-pl_pbeam               1e-10           1.000000e-10
-pl_pip                 1.0             1.000000e+00
-pl_weight              3.0             3.000000e+00
-pl_window              5               5
-rawlogdir
-remove_dc              no              no
-remove_noise           yes             yes
-remove_silence         yes             yes
-round_filters          yes             yes
-samprate               16000           1.600000e+04
-seed                   -1              -1
-sendump
-senlogdir
-senmgau
-silprob                0.005           5.000000e-03
-smoothspec             no              no
-svspec                                 0-12/13-25/26-38
-tmat
-tmatfloor              0.0001          1.000000e-04
-topn                   4               4
-topn_beam              0               0
-toprule
-transform              legacy          dct
-unit_area              yes             yes
-upperf                 6855.4976       6.800000e+03
-uw                     1.0             1.000000e+00
-vad_postspeech         50              50
-vad_prespeech          20              20
-vad_startspeech        10              10
-vad_threshold          3.0             3.000000e+00
-var
-varfloor               0.0001          1.000000e-04
-varnorm                no              no
-verbose                no              no
-warp_params
-warp_type              inverse_linear  inverse_linear
-wbeam                  7e-29           7.000000e-29
-wip                    0.65            6.500000e-01
-wlen                   0.025625        2.562500e-02

INFO: feat.c(715): Initializing feature stream to type: '1s_c_d_dd', ceplen=13, CMN='batch', VARNORM='no', AGC='none'
INFO: acmod.c(162): Using subvector specification 0-12/13-25/26-38
INFO: mdef.c(518): Reading model definition: /usr/local/share/pocketsphinx/model/en-us/en-us/mdef
INFO: mdef.c(531): Found byte-order mark BMDF, assuming this is a binary mdef file
INFO: bin_mdef.c(336): Reading binary model definition: /usr/local/share/pocketsphinx/model/en-us/en-us/mdef
INFO: bin_mdef.c(516): 42 CI-phone, 137053 CD-phone, 3 emitstate/phone, 126 CI-sen, 5126 Sen, 29324 Sen-Seq
INFO: tmat.c(149): Reading HMM transition probability matrices: /usr/local/share/pocketsphinx/model/en-us/en-us/transition_matrices
INFO: acmod.c(113): Attempting to use PTM computation module
INFO: ms_gauden.c(127): Reading mixture gaussian parameter: /usr/local/share/pocketsphinx/model/en-us/en-us/means
INFO: ms_gauden.c(242): 42 codebook, 3 feature, size:
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(127): Reading mixture gaussian parameter: /usr/local/share/pocketsphinx/model/en-us/en-us/variances
INFO: ms_gauden.c(242): 42 codebook, 3 feature, size:
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(244):  128x13
INFO: ms_gauden.c(304): 222 variance values floored
INFO: ptm_mgau.c(476): Loading senones from dump file /usr/local/share/pocketsphinx/model/en-us/en-us/sendump
INFO: ptm_mgau.c(500): BEGIN FILE FORMAT DESCRIPTION
INFO: ptm_mgau.c(563): Rows: 128, Columns: 5126
INFO: ptm_mgau.c(595): Using memory-mapped I/O for senones
INFO: ptm_mgau.c(838): Maximum top-N: 4
INFO: phone_loop_search.c(114): State beam -225 Phone exit beam -225 Insertion penalty 0
INFO: dict.c(320): Allocating 4118 * 20 bytes (80 KiB) for word entries
INFO: dict.c(333): Reading main dictionary: 6610.dic
INFO: dict.c(213): Dictionary size 17, allocated 0 KiB for strings, 0 KiB for phones
INFO: dict.c(336): 17 words read
INFO: dict.c(358): Reading filler dictionary: /usr/local/share/pocketsphinx/model/en-us/en-us/noisedict
INFO: dict.c(213): Dictionary size 22, allocated 0 KiB for strings, 0 KiB for phones
INFO: dict.c(361): 5 words read
INFO: dict2pid.c(396): Building PID tables for dictionary
INFO: dict2pid.c(406): Allocating 42^3 * 2 bytes (144 KiB) for word-initial triphones
INFO: dict2pid.c(132): Allocated 21336 bytes (20 KiB) for word-final triphones
INFO: dict2pid.c(196): Allocated 21336 bytes (20 KiB) for single-phone word triphones
INFO: ngram_model_trie.c(354): Trying to read LM in trie binary format
INFO: ngram_model_trie.c(365): Header doesn''t match
INFO: ngram_model_trie.c(177): Trying to read LM in arpa format
INFO: ngram_model_trie.c(193): LM of order 3
INFO: ngram_model_trie.c(195): #1-grams: 16
INFO: ngram_model_trie.c(195): #2-grams: 20
INFO: ngram_model_trie.c(195): #3-grams: 15
INFO: lm_trie.c(474): Training quantizer
INFO: lm_trie.c(482): Building LM trie
INFO: ngram_search_fwdtree.c(74): Initializing search tree
INFO: ngram_search_fwdtree.c(101): 16 unique initial diphones
INFO: ngram_search_fwdtree.c(186): Creating search channels
INFO: ngram_search_fwdtree.c(323): Max nonroot chan increased to 168
INFO: ngram_search_fwdtree.c(333): Created 16 root, 40 non-root channels, 5 single-phone words
INFO: ngram_search_fwdflat.c(157): fwdflat: min_ef_width = 4, max_sf_win = 25
INFO: continuous.c(307): pocketsphinx_continuous COMPILED ON: Mar  2 2017, AT: 23:16:06

INFO: continuous.c(252): Ready....



```


#### Params pocketsphinx  
```
  /usr/local/share/pocketsphinx/model/en-us/cmudict-en-us.dict    
-dict                                   /usr/local/share/pocketsphinx/model/en-us/cmudict-en-us.dict
-hmm                                    /usr/local/share/pocketsphinx/model/en-us/en-us
-lm                                     /usr/local/share/pocketsphinx/model/en-us/en-us.lm.bin
INFO: ms_gauden.c(127): Reading mixture gaussian parameter: /usr/local/share/pocketsphinx/model/en-us/en-us/means
INFO: ms_gauden.c(127): Reading mixture gaussian parameter: /usr/local/share/pocketsphinx/model/en-us/en-us/variances
INFO: ptm_mgau.c(476): Loading senones from dump file /usr/local/share/pocketsphinx/model/en-us/en-us/sendump
INFO: dict.c(358): Reading filler dictionary: /usr/local/share/pocketsphinx/model/en-us/en-us/noisedict

format :  WAV 16kHz 16-bit mono before decoding. 


```




#### Resultat performance Orange PI zero  
```
   Utterances=11
   CpuTime=146.77 seconds
   CPU xRealTime=3.793 or 379.3% of one core
   Actual Speech=38.695 seconds
   Utterances=146.99 seconds total
   26% of utterances were speech
```

#### Resultat performance PI3 
```
  Utterances=15
CpuTime=90.75 seconds
CPU xRealTime=2.168 or 216.8% of one core
Actual Speech=41.8589 seconds
Utterances=90.95 seconds total
46% of utterances were speech
```

#### Resultat performance PI B+  
```
Utterances=15
CpuTime=219.06 seconds
CPU xRealTime=5.234 or 523.4% of one core
Actual Speech=41.8533 seconds
Utterances=230.94 seconds total
18% of utterances were speech
```


#### test avec SpeakPython 
```
1-"erreur :
INFO: fsg_lextree.c(108): Allocated 35394 bytes (34 KiB) for left and right context phones
INFO: fsg_lextree.c(253): 3989 HMM nodes in lextree (3593 leaves)
INFO: fsg_lextree.c(255): Allocated 430812 bytes (420 KiB) for all lextree nodes
INFO: fsg_lextree.c(258): Allocated 388044 bytes (378 KiB) for lextree leafnodes
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started


solution possible 1 : https://bbs.archlinux.org/viewtopic.php?id=147527     
solution possible 2 : http://raspberrypi.stackexchange.com/questions/639/how-to-get-pulseaudio-running 

aide sur PulseAudio : https://wiki.archlinux.org/index.php/PulseAudio    
aide pulseaudio sur debian : https://wiki.debian.org/PulseAudio      
aide, comment lancer pulseaudio : https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/Running/       
aide, jack_control : http://forum.renoise.com/index.php/topic/41843-linux-howto-pulseaudio-jack-server/      


etat de pulseaudio : 
| => sudo systemctl status pulseaudio
[sudo] password for chip:
? pulseaudio.service
   Loaded: not-found (Reason: No such file or directory)
   Active: inactive (dead)

2- erreur 2: 

ad_oss.c(115): Failed to open audio device(/dev/dsp): No such file or directory  
probleme similaire: https://sourceforge.net/p/cmusphinx/discussion/help/thread/7854934d/     

verifier dans /usr/share/alsa/alsa.conf   ->  https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=136974    

solution 1 : http://cmusphinx.sourceforge.net/wiki/faq#qfailed_to_open_audio_device_dev_dsp_no_such_file_or_directory    
on fait : sudo apt-get install libasound2-dev 


solution 2 : https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=124016&p=857433&hilit=alsa#p857433     
on change ~/.asoundrc comme suit : 
        pcm.!default plughw:Device    
        ctl.!default plughw:Device      

lspci -v | grep HCI
modprobe snd_usb_audio

amixer cset numid=3 2
sudo raspi-config
installer jackd : 'sudo apt-get install jackd2'  
lancer jack-server :   jackd -d alsa 
jackd -R -d alsa -d hw:0,3   ->  http://askubuntu.com/questions/320946/jackd-does-not-work-aplay-l-shows-two-instances-of-the-same-card-ubuntu-13-04      
jackd -R -d alsa -d hw:CARD,DEVICE // voir avec 'arecord -l' ou 'aplay -l' 

| => cat /etc/modprobe.d/alsa-base.conf
options snd-usb-audio index=1



http://wiki.linuxaudio.org/wiki/raspberrypi  // parle de jackd et plusieurs tweeks 
https://www.raspberrypi.org/forums/viewtopic.php?f=38&t=54405
une piste lie a PyAudio :  http://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time    
une autre piste : http://stackoverflow.com/questions/31332663/raspberry-pi-radio-script-stopped-working-jack-server-is-not-running-or-cannot 
essayer alsa reset 'alsactl  init' -> https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=20923



3- error jackd server 

 | => jackd -R -d alsa -d hw:2,0
jackdmp 1.9.10
Copyright 2001-2005 Paul Davis and others.
Copyright 2004-2014 Grame.
jackdmp comes with ABSOLUTELY NO WARRANTY
This is free software, and you are welcome to redistribute it
under certain conditions; see the file COPYING for details
JACK server starting in realtime mode with priority 10
self-connect-mode is "Don't restrict self connect requests"
Cannot lock down 82278944 byte memory area (Cannot allocate memory)
audio_reservation_init
dbus_bus_request_name() failed. (1)
Failed to acquire device name : Audio2 error : Connection ":1.12" is not allowed to own the service "org.freedesktop.ReserveDevice1.Audio2" due to security policies in the configuration file
Audio device hw:2,0 cannot be acquired...
Cannot initialize driver
JackServer::Open failed with -1
Failed to open server


solution 1 : export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/dbus/system_bus_socket   -> https://linuxmusicians.com/viewtopic.php?t=12821     
solution 2: https://www.raspberrypi.org/forums/viewtopic.php?t=57025  



 If you want to run jackd with realtime priorities, the user starting jackd needs realtime permissions. Accept this option to create the file              ¦
 ¦ /etc/security/limits.d/audio.conf, granting realtime priority and memlock privileges to the audio group.                                                  ¦
 ¦                                                                                                                                                           ¦
 ¦ Running jackd with realtime priority minimizes latency, but may lead to complete system lock-ups by requesting all the available physical system memory,  ¦
 ¦ which is unacceptable in multi-user environments.                                                                                                         ¦
 ¦                                                                                                                                                           ¦
 ¦ Enable realtime process priority?


 Pour le message "Cannot lock down 82278944 byte memory area (Cannot allocate memory)" 
  On change la taille a 300 MB (300000000) dans  /etc/security/limits.d/audio.conf
 
  
4- erreur en lancant l-app 'python mainHouseCommands.py'
-warp_params
-warp_type      inverse_linear  inverse_linear
-wbeam          7e-29           7.000000e-29
-wip            0.65            6.500000e-01
-wlen           0.025625        2.562500e-02

INFO: feat.c(713): Initializing feature stream to type: '1s_c_d_dd', ceplen=13, CMN='prior', VARNO
RM='no', AGC='none'
INFO: cmn.c(142): mean[0]= 12.00, mean[1..12]= 0.0
ERROR: "acmod.c", line 85: Acoustic model definition is not specified neither with -mdef option no
r with -hmm

(mainHouseCommands.py:965): GStreamer-CRITICAL **: range start is not smaller than end for `GstInt
Range'
INFO: feat.c(713): Initializing feature stream to type: '1s_c_d_dd', ceplen=13, CMN='prior', VARNO
RM='no', AGC='none'
INFO: cmn.c(142): mean[0]= 12.00, mean[1..12]= 0.0
ERROR: "acmod.c", line 85: Acoustic model definition is not specified neither with -mdef option no
r with -hmm
Segmentation fault'
solution :  - il faut cree an lien  symbolique dans /usr/share/ 
              'sudo ln -s /usr/local/share/pocketsphinx/ pocketsphinx'
            - copier le dossier  hub4wsj_sc_8k/ comme suit 
                'sudo cp -r hub4wsj_sc_8k/ /usr/share/pocketsphinx/model/hmm/en_US/' 
             

5- erreur en lancant 'pocketsphinx_continuous' :  
Error opening audio device (null) for capture: Connection refused
FATAL: "continuous.c", line 239: Failed to open audio device

solution 1 : https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=37262   
on desinstall pulse-audio :
		apt-get --purge remove libpulse-dev 



solution 2 : https://www.raspberrypi.org/forums/viewtopic.php?t=57025

```











