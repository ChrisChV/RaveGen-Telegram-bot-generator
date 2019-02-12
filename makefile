install:
	#pip install python-telegram-bot
	#snap install heroku --classic
	mkdir -p /opt/ravegen
	cp -R src/* /opt/ravegen
	rm -f /opt/ravegen/Utils/sadD.py
	touch /opt/ravegen/Utils/sadD.py
	echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \"/opt/ravegen/ConsoleEngine/commands\"" > /opt/ravegen/Utils/sadD.py
	python -m compileall /opt/ravegen
	python /opt/ravegen/generateAp.py
	rm -f /bin/ravegen
	chmod  +x /opt/ravegen/main.py
	ln -s /opt/ravegen/main.py /bin/ravegen
	cp /opt/ravegen/rave_compl.bash /etc/bash_completion.d/
	rm -Rf /lib/python2.7/site-packages/ravegen
	cp -R /opt/ravegen /lib/python2.7/site-packages/

clean:
	rm -Rf ravegen/*.pyc
	rm -Rf ravegen/ConsoleEngine/*.pyc
	rm -Rf ravegen/DeployEngine/*.pyc
	rm -Rf ravegen/RaveEngine/*.pyc
	rm -Rf ravegen/Utils/*.pyc
	rm -Rf build/
	rm -Rf dist/
	rm -Rf ravegen_dev.egg-info
	