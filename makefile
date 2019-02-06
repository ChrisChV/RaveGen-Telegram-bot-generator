install:
	pip install python-telegram-bot
	snap install heroku --classic
	mkdir -p $(DESTDIR)/opt/ravegen
	cp -R src/* $(DESTDIR)/opt/ravegen
	rm -f $(DESTDIR)/opt/ravegen/Utils/sadD.py
	touch $(DESTDIR)/opt/ravegen/Utils/sadD.py
	echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \""$(DESTDIR)"/opt/ravegen/ConsoleEngine/commands\"" > $(DESTDIR)/opt/ravegen/Utils/sadD.py
	python -m compileall $(DESTDIR)/opt/ravegen
	python $(DESTDIR)/opt/ravegen/generateAp.py
	rm -f $(DESTDIR)/opt/ravegen/Utils/sadD.py
	touch $(DESTDIR)/opt/ravegen/Utils/sadD.py
	echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \"/opt/ravegen/ConsoleEngine/commands\"" > $(DESTDIR)/opt/ravegen/Utils/sadD.py
	rm -f $(DESTDIR)/bin/ravegen
	chmod  +x $(DESTDIR)/opt/ravegen/main.py
	ln -s /opt/ravegen/main.py $(DESTDIR)/bin/ravegen
	cp rave_compl.bash $(DESTDIR)/etc/bash_completion.d/

clean:
	rm -Rf src/*.pyc
	rm -Rf src/ConsoleEngine/*.pyc
	rm -Rf src/DeployEngine/*.pyc
	rm -Rf src/RaveEngine/*.pyc
	rm -Rf src/Utils/*.pyc
	
