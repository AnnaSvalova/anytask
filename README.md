Anytask [![Build Status](https://travis-ci.com/hariton27sy/anytask.svg?branch=update_django_1.7)](https://travis-ci.org/hariton27sy/anytask)
=======


local install
-------------

Development installation commands:

    # ... clone ...
    # ... cd ...
    git submodule init
    git submodule update
    virtualenv .env
    . .env/bin/activate
    pip install pip>=10 setuptools>=30 --upgrade
    pip install -r requirements_local.txt
    python setup.py develop
    ./anytask/manage.py  # test it  # TODO: make a setup entry point
    ./anytask/manage.py syncdb --migrate --noinput
    ./anytask/manage.py runserver 127.0.0.1:8019 -v 3 --traceback
