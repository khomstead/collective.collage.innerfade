Overview
========

collective.collage.innerfade allows an ATFolder type to be viewed using the innerfade jQuery plugin.

Compatibility
-------------

* Software was created and tested on Plone 4

Status
------

Stable; almost in production :)

Usage
-----

Use buildout, or a similar method to install collective.collage.innerfade and then (re)start your Plone instance. The zcml configuration will automatically get picked up and register the additional view for your Collage content. Note that you also need ``collective.js.innerfade`` for this module to function properly.

#. Create a Collage.
#. Add rows and columns.
#. Add a Folder to your Collage, either actual content or an alias. 
#. In the *Compose* page for the Collage, click the *Layout* link of the Folder you just created.
#. Select *Innerfade View*

Obviously, the innerfade view will only be useful when it contains Image and Link instances.

Development
-----------

Please report issues to `Wietze Helmantel (main developer) <helmantel@gw20e.com>`_

Sponsors
--------

Work on this product has been sponsored by Milieudefensie (http://www.milieudefensie.nl)
