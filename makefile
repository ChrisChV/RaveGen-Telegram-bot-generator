#InstallationPath = /usr/local/lib/python2.7/dist-packages##ubuntu
InstallationPath = /lib/python2.7/site-packages##fedora

install:
	#pip install python-telegram-bot
	#snap install heroku --classic
	python ravegen/generateAp.py
	cp rave_compl.bash ravegen/
	cat setup.py | grep version > ravegen/version
	sudo mkdir -p $(InstallationPath)/ravegen
	sudo cp -R ravegen/* $(InstallationPath)/ravegen
	sudo python -m compileall $(InstallationPath)/ravegen
	sudo rm -f /bin/ravegen
	sudo chmod  +x $(InstallationPath)/ravegen/ravegen
	sudo ln -s $(InstallationPath)/ravegen/ravegen /bin/ravegen
	sudo cp $(InstallationPath)/ravegen/rave_compl.bash /etc/bash_completion.d/
	mkdir -p ~/.ravegen
	echo '$(InstallationPath)' > ~/.ravegen/installationPath
	make clean

build:
	python -m compileall ravegen/
	python ravegen/generateAp.py
	cp rave_compl.bash ravegen/
	cp LICENSE ravegen/
	cat setup.py | grep version= > ravegen/version
	python setup.py bdist_wheel
	


clean:
	rm -Rf ravegen/*.pyc
	rm -Rf ravegen/ConsoleEngine/*.pyc
	rm -Rf ravegen/DeployEngine/*.pyc
	rm -Rf ravegen/RaveEngine/*.pyc
	rm -Rf ravegen/Utils/*.pyc
	rm -Rf ravegen/Decorators/*.pyc
	rm -Rf build/
	rm -Rf dist/
	rm -Rf ravegen_dev.egg-info
	rm -Rf ravegen.egg-info
	rm -f rave_compl.bash
	rm -f ravegen/rave_compl.bash
	rm -f ravegen/LICENSE
	rm -f ravegen/version
	
