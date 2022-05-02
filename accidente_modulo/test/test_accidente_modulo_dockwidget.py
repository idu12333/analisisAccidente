# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'idu12333@usal.es'
__date__ = '2022-04-23'
__copyright__ = 'Copyright 2022, Francisco Javier Holguera Illera'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from accidente_modulo_dockwidget import AccidenteDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class AccidenteDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = AccidenteDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(AccidenteDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

