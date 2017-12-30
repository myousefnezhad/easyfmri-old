easy fMRI project (V1.7B1000 beta)
===============



### Introduction


easy fMRI is a open source toolbox for the Human Brain Mapping and Decoding. This project is developing by Muhammad Yousefnezhad, iBRAIN Group, Nanjing University of Aeronautics and Astronautics, China. The project website is https://easyfmri.sourceforge.io/


### How install easy fMRI


You need following Software:

-FSL Version=5.0.10 or above

-AFNI Version=17.3.06 or above

-Python Version=3.6.2 or above

-OS= Mac or Linux



# STEP(A). Copy Files

1. Download the last version of easy fMRI file (a zip file, e.g. easyfmri.zip) and copy it to your home directory.

2. Extract easy fMRI files and folders:

```
unzip easyfmri.zip
```

3. Rename the extracted folder to the default folder of easy fMRI. NOTE: The default folder will be hidden!

```
mv easyfmri .easyfmri
```


4. copy running file to /usr/bin/local

```
sudo cp ~/.easyfmri/_Script/ezfmri  /usr/local/bin/
```

5. Environment Variable (see example at the end)



# STEP(B). Python 3.6.2 or above

1. Download (https://anaconda.org/anaconda/python) and Install Python3 by using Anaconda3

For Linux:

```
sudo sh Anaconda3-<version>-Linux<platform>.sh
```

For Mac: Click pkg file and continue installation.

2. Install all packages in ~/.easyfmri/PyPackage directory

```
cd ~/.easyfmri/PyPackage
sudo pip install *
```

3. Environment Variable (see example at the end)



# STEP(C). Install FSL 5.0.10 or above

1. Register from https://fsl.fmrib.ox.ac.uk/fsl/fslwiki

2. Download fslinstaller.py

3. Run following for downloading installaion file (Mac: fsl-<version>-macOS_64.tar.gz or Linux: fsl-<version>-centos7_64.tar.gz)

```
python2 fslinstaller.py -o
md5sum fsl-5.x.x-centosY_64.tar.gz
```


4. Install downloaded file:

```
python2 fslinstaller.py -f <downloaded file, e.g. fsl-5.x.x-centosY_64.tar.gz> -M
```

5. Environment Variable (see example at the end)



# STEP(D). Install AFNI 17.3.06 or above

1. Download AFNI (https://afni.nimh.nih.gov/)

2. Extract AFNI to ~/abin

3. Environment Variable (see example at the end)



# STEP(E). Update Environment Variable

1. See the example bellow

2. After restarting your computer, run easyfmri:

```
ezfmri
```


### How upgrade easy fMRI

For updating a new version, just replace the old files by the extracted new files

Note: default directory for easy fMRI is a hidden folder in ~/.easyfmri




### Environment Variable (Example)

Copy following to in .profile or .bashrc and restart your computer


```
# Easy fMRI
export EASYFMRI="$HOME/.easyfmri"         # This is the default directory of easy fMRI
export PATH="/usr/local/bin:$PATH"        # This is for binary file for running "ezfmri" command

# Python
export PATH="$HOME/anaconda3/bin:$PATH"   # This must be matched by your anaconda installation directory
alias python3="python3 -m IPython"

#FSL
export FSLDIR="/usr/local/fsl"            # This must be matched by FSL installation directory
. ${FSLDIR}/etc/fslconf/fsl.sh
export PATH="$FSLDIR/bin:$PATH"

# AFNI
export PATH="$HOME/abin:/usr/lib/lightdm/lightdm:$PATH" # This must be matched by AFNI installation directory
```

NOTE: We also provide another example of Environment Variables in ~/.easyfmri/Script/linuxshell.tar.gz
