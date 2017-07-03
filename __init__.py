# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LocationGenerator
                                 A QGIS plugin
 Generates potential beaver dam locations based on beaver dam capacity estimates from the Beaver Restoration Assessment Tool
                             -------------------
        begin                : 2017-07-03
        copyright            : (C) 2017 by Konrad Hafen
        email                : k.hafen@aggiemail.usu.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LocationGenerator class from file LocationGenerator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bd_location_generator import LocationGenerator
    return LocationGenerator(iface)
