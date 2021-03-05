# Mac
# Homebrew 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# python 
brew install python
# VLC
brew install vlc
# GIT
brew install git
# to mount the code folder of the pi at the mac
sshfs pi@192.168.2.114:/home/pi/Desktop/pi_py_radio ~/Desktop/pi_py_radio_pi
umount -f ~/Desktop/pi_py_radio_pi
# Redis
brew install redis
brew services start redis
brew services stop redis
redis-cli ping
redis-cli monitor

# Pi
# VLC
apt-get install vlc
# GIT
apt-get install git
# Redis
apt-get install redis
systemctl status redis
redis-cli ping
redis-cli monitor
# SpiDev Bib to process analog signals.  
wget https://github.com/doceme/py-spidev/archive/master.zip 
unzip master.zip
cd py-spidev-master
sudo python setup.py install

# For both (As root if you want to start the script later via cron)
pip3 install python-vlc
pip3 install coloredlogs
pip3 install redis
pip3 install termcolor

# Git Commands
git init
git config --global user.name "SaschaBach"
git config --global user.email "sascha.bach@googlemail.com"
git config --global init.defaultBranch master
git config --global core.excludesFile *.log
git remote add origin https://github.com/SaschaBach/pi_py_radio.git
git fetch
git checkout main
git add --all
git commit -m "bissl huebsch gemacht"
git push -u origin main
git pull