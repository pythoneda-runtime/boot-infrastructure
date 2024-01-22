# vim: set fileencoding=utf-8
"""
pythoneda/runtime/boot/infrastructure/cli/def_url_cli.py

This file defines the DefUrlCli class.

Copyright (C) 2024-today rydnr's https://github.com/pythoneda-runtime/boot-infrastructure

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
from argparse import ArgumentParser
from pythoneda.shared import PrimaryPort
from pythoneda.shared.application import PythonEDA
from pythoneda.shared.infrastructure.cli import CliHandler


class DefUrlCli(CliHandler, PrimaryPort):

    """
    A PrimaryPort used to gather information about the url of a definition repository.

    Class name: DefUrlCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the url of a definition repository.

    Collaborators:
        - pythoneda.runtime.boot.application.BootApp: They are notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new DefUrlCli instance.
        """
        super().__init__("Provide the url of the definition repository")

    @classmethod
    def priority(cls) -> int:
        """
        Retrieves the priority of this port.
        :return: The priority.
        :rtype: int
        """
        return 90

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return True

    def add_arguments(self, parser: ArgumentParser):
        """
        Defines the specific CLI arguments.
        :param parser: The parser.
        :type parser: argparse.ArgumentParser
        """
        parser.add_argument(
            "-d",
            "--def-url",
            required=True,
            help="The url of the definition repository",
        )

    async def handle(self, app: PythonEDA, args):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :param args: The CLI args.
        :type args: argparse.args
        """
        await app.accept_definition_url(args.def_url)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
