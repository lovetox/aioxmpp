########################################################################
# File name: __init__.py
# This file is part of: aioxmpp
#
# LICENSE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
########################################################################
"""
:mod:`~aioxmpp.misc` -- Miscellaneous XSOs
##########################################

This subpackage bundles XSO definitions for several XEPs. They do not get their
own subpackage because they often only define one or two XSOs without any logic
involved. The XSOs are often intended for re-use by other protocols.


Out of Band Data (:xep:`66`)
============================

.. autoclass:: OOBExtension

.. attribute:: aioxmpp.Message.xep0066_oob


Delayed Delivery (:xep:`203`)
=============================

.. autoclass:: Delay()

.. attribute:: aioxmpp.Message.xep0203_delay

   A :class:`Delay` instance which indicates that the message has been
   delivered with delay.


Stanza Forwarding (:xep:`297`)
==============================

.. autoclass:: Forwarded()


Chat Markers (:xep:`333`)
=========================

.. autoclass:: ReceivedMarker

.. autoclass:: DisplayedMarker

.. autoclass:: AcknowledgedMarker

.. attribute:: aioxmpp.Message.xep0333_marker


JSON Containers (:xep:`335`)
============================

:xep:`335` defines a standard way to transport JSON data in XMPP. The
:class:`JSONContainer` is an XSO class which represents the ``<json/>`` element
specified in :xep:`335`.

:mod:`aioxmpp` also provides an :class:`~aioxmpp.xso.AbstractElementType`
called :class:`JSONContainerType` which can be used to extract JSON data from
an element using the :class:`JSONContainer` format.

.. autoclass:: JSONContainer

.. autoclass:: JSONContainerType


Pre-Authenticated Roster Subcription (:xep:`379`)
=================================================

.. autoclass:: Preauth

.. attribute:: aioxmpp.Presence.xep0379_preauth

   The pre-auth element associate with a subscription request.

"""

from .delay import Delay  # NOQA: F401
from .forwarding import Forwarded  # NOQA: F401
from .oob import OOBExtension  # NOQA: F401
from .markers import (  # NOQA: F401
    ReceivedMarker,
    DisplayedMarker,
    AcknowledgedMarker,
)
from .json import JSONContainer, JSONContainerType  # NOQA: F401
from .pars import Preauth  # NOQA: F401
