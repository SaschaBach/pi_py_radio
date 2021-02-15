# Fuer den Mac
# Homebrew 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# python 
brew install python
# VLC
brew install vlc
# GIT
brew install git
# Um das Entwicklungsverzeichnis auf dem Pi innerhalb der lokalen Maschine zu mounten
sshfs pi@192.168.2.114:/home/pi/Desktop/pi_py_radio ~/Desktop/pi_py_radio_pi

# Fuer den Pi
# VLC
apt-get install vlc
# GIT
apt-get install git

# Fuer beide
# Um VLC zu starten muss erst die python lib für VLC installiert werden
pip install python-vlc

# Git Commands
git init
git config --global user.name "SaschaBach"
git config --global user.email "sascha.bach@googlemail.com"
git config --global init.defaultBranch master
git remote add origin https://github.com/SaschaBach/pi_py_radio.git
git fetch
git checkout main
git add --all
git commit -m "bissl huebsch gemacht"
git push -u origin main