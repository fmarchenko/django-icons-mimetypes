Mimetypes Icons
===============

The collection of mimetypes icons from the `Tango Icon Library`_ project, and a template tag to include them.

.. _`Tango Icon Library`: http://tango.freedesktop.org/Tango_Icon_Library

Usage
-----

In your settings::

    INSTALLED_APPS = (
        ...
        'icons_mimetypes',
    )

Then in your templates::

    {% load mimetypes %}

    <img src="{% icon "image/jpeg" %}">

    <img src="{% icon "image/jpeg" "32x32" %}">

    <img src="{% icon "image/jpeg" size %}">

    <img src="{% icon mimetype %}">

    <a style="background-image: url({% icon mimetype "16x16" %})">

    <img src="{% icon mimetype size %}">

    {% icon "application/pdf" as pdf_icon %}

    {% icon "application/pdf" "48x48" as pdf_icon %}

    {% icon "application/pdf" size as pdf_icon %}

    {% icon mimetype as pdf_icon %}

    {% icon mimetype "32x32" as pdf_icon %}

    {% icon mimetype size as pdf_icon %}

Or obviously you can directly link to the files in the ``static`` directory,
e.g. if you want to reference them in a static CSS.

Tests
-----

A minimal Django project is shipped to run the test suite. Try ``make coverage`` (100% at the time of this writing).

License
-------

The code is copyright Bors Ltd and published under the GNU General Public License version 3.

The icons are placed in the public domain, see ``Tango`` for details.
