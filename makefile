install:
	#pip install python-telegram-bot
	#snap install heroku --classic
	python ravegen/generateAp.py
	cp rave_compl.bash ravegen/
	mkdir -p /lib/python2.7/site-packages/ravegen
	cp -R ravegen/* /lib/python2.7/site-packages/ravegen
	python -m compileall /lib/python2.7/site-packages/ravegen
	rm -f /bin/ravegen
	chmod  +x /lib/python2.7/site-packages/ravegen/ravegen
	ln -s /lib/python2.7/site-packages/ravegen/ravegen /bin/ravegen
	cp /lib/python2.7/site-packages/ravegen/rave_compl.bash /etc/bash_completion.d/

build:
	python -m compileall ravegen/
	python ravegen/generateAp.py
	cp rave_compl.bash ravegen/
	cp LICENSE ravegen/
	python setup.py bdist_wheel

upload:
	python -m twine upload dist/*

clean:
	rm -Rf ravegen/*.pyc
	rm -Rf ravegen/ConsoleEngine/*.pyc
	rm -Rf ravegen/DeployEngine/*.pyc
	rm -Rf ravegen/RaveEngine/*.pyc
	rm -Rf ravegen/Utils/*.pyc
	rm -Rf build/
	rm -Rf dist/
	rm -Rf ravegen_dev.egg-info
	rm -f rave_compl.bash
	rm -f ravegen/rave_compl.bash
	rm -f ravegen/LICENSE
	