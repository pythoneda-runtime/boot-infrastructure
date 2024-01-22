# vim: set fileencoding=utf-8
"""
pythoneda/runtime/boot/infrastructure/dbus/boot_dbus_signal_listener.py

This file defines the BootDbusSignalListener class.

Copyright (C) 2023-today boot's pythoneda-runtime/boot-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import BusType, Message
from pythoneda.runtime.boot.events.lifecycle import BootRequested
from pythoneda.runtime.boot.events.lifecycle.infrastructure.dbus import (
    DbusBootRequested,
)
from pythoneda.shared.infrastructure.dbus import DbusSignalListener
from typing import Dict


class BootDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to Boot-relevant d-bus signals.

    Class name: BootDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to Boot.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Receives relevant domain events.
        - pythoneda.runtime.boot.events.lifecycle.infrastructure.dbus.DbusBootRequested
    """

    def __init__(self):
        """
        Creates a new BootDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(BootRequested)
        result[key] = [DbusBootRequested, BusType.SYSTEM]
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
