#apt-get install python-telegram-bot
#sudo snap install heroku --classic

mkdir -p /opt/ravegen
cp -R src/* /opt/ravegen
chmod  +x /opt/ravegen/main.py
rm -f /opt/ravegen/Utils/sadD.py
touch /opt/ravegen/Utils/sadD.py
echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \"/opt/ravegen/ConsoleEngine/commands\"" > /opt/ravegen/Utils/sadD.py
rm -f /bin/ravegen
ln -s /opt/ravegen/main.py /bin/ravegen

