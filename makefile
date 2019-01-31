install:
	mkdir -p /opt/ravegen
	cp -R src/* /opt/ravegen
	rm -f /opt/ravegen/Utils/sadD.py
	touch /opt/ravegen/Utils/sadD.py
	echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \"/opt/ravegen/ConsoleEngine/commands\"" > /opt/ravegen/Utils/sadD.py
	python -m compileall /opt/ravegen
	rm -f /bin/ravegen
	chmod  +x /opt/ravegen/main.py
	ln -s /opt/ravegen/main.py /bin/ravegen


clean:
	rm -Rf src/*.pyc
	rm -Rf src/ConsoleEngine/*.pyc
	rm -Rf src/DeployEngine/*.pyc
	rm -Rf src/RaveEngine/*.pyc
	rm -Rf src/Utils/*.pyc
	