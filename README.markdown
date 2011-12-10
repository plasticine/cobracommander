# Cobra Commander

In your codebase building your builds.


## What is Cobracommander?

Cobracommander is a CI tool written in python. Cobracommander is made up of 3 components; Cobracommander, Henchman & Minion(s) — detailed below;

### Cobracommander

Cobracommander itself is just a django application. Its purpose is to act as a UI for controlling and administering projects and their associated build targets, and builds.

Cobracommander communicates with Henchman (who actually does all the hard work) via basic HTTP POST requests and Cobracommander templates also set up Websocket (Socket.IO) connections to Henchman to steam down build progress logs and build queue status, etc.

### Henchman

Henchman is a separate, lightweight, server that provides HTTP and Socket.IO interfaces for communication. Henchman is responsible for managing the state of the build-queue and the Minions in it. Henchman provides HTTP interfaces for Cobracommander to start/stop/etc builds.

### Minion(s)

A Minion is basically an instance of a build for your project — either scheduled, or in-progress — in the Henchman build-queue.

Minions are responsible for the setting up, reading the project Snakefile, running, and collection of output from a build. They also handle any cleanup and reporting required to finish off their build.

### Snakefile

A Cobracommander `snakefile` contains the steps to tell Cobracommander, and the Minion assigned to building your project how your project should be built.

Snakefiles should output, or contain a JSON.

At its simplest a Snakefile can just contain a JSON object listing the steps (commands, executed serially) required to complete a build of your project.

To use Cobracommander you need to add a Snakefile (`snakefile`) to the root of your project. Needless to say; it should be under version control.


## Developing

### Requirements

- python ~2.7
- django 1.3
- python requirements; see `requirements.pip`.

#### Extras:

- postgres, coffeescript & scss


### Getting up and running for development

Install stuff:

    brew install python postgres

Set up the virtual environment for development:

    mkvirtualenv --no-site-packages --distribute cobracommander
    cdvirtualenv
    echo "export DJANGO_SETTINGS_MODULE='settings.development'" > bin/postactivate
    echo "export PYTHONPATH='`pwd`/project/cobracommander'" >> bin/postactivate
    echo "unset DJANGO_SETTINGS_MODULE" > bin/depostactivate

Get the code, install requirements, set up DB, etc...

    git clone git://github.com/plasticine/cobracommander.git project/cobracommander
    cd project/cobracommander
    pip install -r REQUIREMENTS
    createdb cobracommander_development
    django-admin.py syncdb
    django-admin.py migrate


__Boom.__
