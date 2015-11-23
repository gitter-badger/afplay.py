	
Install
'''''''

github.com_: :code:`pip install git+git://github.com/b'russianidiot'/afplay.py.git`

pypi.python.org_: :code:`pip install afplay`

download_: :code:`python setup.py install` or :code:`setup/.setup.py develop.command`

.. _github.com: http://github.com/b'russianidiot'/afplay.py
.. _pypi.python.org: https://pypi.python.org/pypi/afplay
.. _download: https://github.com/b'russianidiot'/afplay.py/archive/master.zip

	

**Platforms**: OSX

	

	

Usage 
'''''
.. code-block::

	from afplay import *

	afplay() # default sound, /System/Library/Sounds/Glass.aiff
	afplay("path/to/custom/sound.aiff")

------------

**Tested**: python 2.6, 2.7, 3+

**Bug Tracker**: `github.com/b'russianidiot'/afplay.py/issues`__

__ https://github.com/b'russianidiot'/afplay.py/issues