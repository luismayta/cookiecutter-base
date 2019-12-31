{{ cookiecutter.repository_name }}
==================================

{{ cookiecutter.project_description }}

:Version: {{cookiecutter.version}}
:Web: {{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}
:Download: {{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}
:Source: {{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}
:Keywords: {{cookiecutter.repository_name}}

.. contents:: Table of Contents:
    :local:


License
-------

The code in this repository is licensed under the GPL unless
otherwise noted.

Please see LICENSE_ for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute` CONTRIBUTING_ for details.

Issue report template should be automatically applied if you are sending it from bitbucket UI as well; otherwise you
can find it at `ISSUE_TEMPLATE.md <{{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}/blob/master/.jira/issue_templates/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@luismayta.com.

Requirements
------------

This is a list of applications that need to be installed previously to
enjoy all the goodies of this configuration:

- `Pyenv`_
- `Docker`_
- `Tfenv`_
- `Terragrunt`_


Quickstart
----------

Project Start
^^^^^^^^^^^^^

.. code:: bash

    $ make environment
    $ make setup
    $ make yarn.install

Start Application
^^^^^^^^^^^^^^^^^

.. code:: bash

    $ make yarn.start

Troubleshooting
---------------

Wrong pre-commit with pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the next:

.. code:: bash

    pyenv shell {{ cookiecutter.python_version }}


License
=======

MIT

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
============

Please see `CONTRIBUTING`_ for details.


Versioning
----------

Releases are managed using {{ cookiecutter.repository }} release feature.
We use [Semantic Versioning](http://semver.org) for all
the releases. Every change made to the code base will be referred to in the release notes (except for
cleanups and refactorings).

Credits
-------

-  `CONTRIBUTORS`_

Made with :heart: :coffee: and :pizza: by `luismayta`_.

.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
    :target: LICENSE
    :alt: License

.. Links
.. _`CHANGELOG`: CHANGELOG.rst
.. _`CONTRIBUTORS`: docs/source/AUTHORS.rst
.. _`CONTRIBUTING`: docs/source/CONTRIBUTING.rst
.. _`LICENSE`: LICENSE


.. _`luismayta`: https://github.com/luismayta

.. dependences
.. _`Pyenv`: https://github.com/pyenv/pyenv
.. _`Docker`: https://www.docker.com/
.. _`Tfenv`: https://github.com/tfutils/tfenv
.. _`Terragrunt`: https://github.com/gruntwork-io/terragrunt
