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

Features
--------

* Task

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


Troubleshooting
---------------

Wrong pre-commit with pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the next:

.. code:: bash

    pyenv shell {{ cookiecutter.python_version }}

Team
----

+---------------+
| |{{cookiecutter.author_name}}|  |
+---------------+
| `{{cookiecutter.author_name}}`_ |
+---------------+

License
-------

MIT

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
------------

Contributions are welcome!

Review the `CONTRIBUTING`_ for details on how to:

* Submit issues
* Submit pull requests

Versioning
----------

Releases are managed using {{ cookiecutter.repository }} release feature.
We use [Semantic Versioning](http://semver.org) for all
the releases. Every change made to the code base will be referred to in the release notes (except for
cleanups and refactorings).

Credits
-------

-  `CONTRIBUTORS`_

|linkedin| |beacon| |made|

Made with :coffee: and :pizza: by `{{cookiecutter.author_name}}`_ and `{{cookiecutter.company_name}}`_.

.. Links
.. _`CHANGELOG`: CHANGELOG.rst
.. _`CONTRIBUTORS`: docs/source/AUTHORS.rst
.. _`CONTRIBUTING`: docs/source/CONTRIBUTING.rst
.. _`LICENSE`: LICENSE

.. _`{{cookiecutter.company_name}}`: {{cookiecutter.repository_domain}}/{{cookiecutter.company_repository_username}}
.. _`{{cookiecutter.author_name}}`: {{cookiecutter.repository_domain}}/{{cookiecutter.author_repository_username}}

.. |Build Status| image:: https://travis-ci.org/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}.svg
    :target: https://travis-ci.org/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}
.. |GitHub issues| image:: https://img.shields.io/github/issues/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}.svg
    :target: {{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}/issues
.. |GitHub license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
    :target: LICENSE

.. Team:
.. |{{cookiecutter.author_name}}| image:: {{cookiecutter.repository_domain}}/{{cookiecutter.author_repository_username}}.png?size=100
    :target: {{cookiecutter.repository_domain}}/{{cookiecutter.author_repository_username}}

.. Footer:

.. |linkedin| image:: http://www.linkedin.com/img/webpromo/btn_liprofile_blue_80x15.png
    :target: {{cookiecutter.author_linkedin}}
.. |beacon| image:: https://ga-beacon.appspot.com/UA-65019326-1/github.com/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}/readme
    :target: {{cookiecutter.repository_domain}}/{{cookiecutter.repository_owner}}/{{cookiecutter.repository_name}}
.. |made| image:: https://img.shields.io/badge/Made%20with-Zsh-1f425f.svg
    :target: http://www.zsh.org

.. dependences
.. _`Pyenv`: https://github.com/pyenv/pyenv
.. _`Docker`: https://www.docker.com/
.. _`Tfenv`: https://github.com/tfutils/tfenv
.. _`Terragrunt`: https://github.com/gruntwork-io/terragrunt
