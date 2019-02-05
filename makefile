install:
	pip install python-telegram-bot
	snap install heroku --classic
	python src/generateAp.py
	mkdir -p /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen
	cp -R src/* /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen
	rm -f /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen/Utils/sadD.py
	touch /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen/Utils/sadD.py
	echo "_CONSOLE_ENGINE_COMMANDS_FILE_PATH = \"/opt/ravegen/ConsoleEngine/commands\"" > /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen/Utils/sadD.py
	python -m compileall /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen
	rm -f /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/bin/ravegen
	chmod  +x /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/opt/ravegen/main.py
	ln -s /opt/ravegen/main.py /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/bin/ravegen
	cp rave_compl.bash /home/xnpiochv/rpmbuild/BUILDROOT/ravegen-0.1.0-1.x86_64/etc/bash_completion.d/

clean:
	rm -Rf src/*.pyc
	rm -Rf src/ConsoleEngine/*.pyc
	rm -Rf src/DeployEngine/*.pyc
	rm -Rf src/RaveEngine/*.pyc
	rm -Rf src/Utils/*.pyc
	