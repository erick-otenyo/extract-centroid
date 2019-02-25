# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExtractCentroid
                                 A QGIS plugin
 This plugin extracts centroid from vector polygon data
                             -------------------
        begin                : 2019-02-25
        copyright            : (C) 2019 by Erick Otenyo
        email                : otenyo.erick@gmail.com
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
    """Load ExtractCentroid class from file ExtractCentroid.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .extract_centroid import ExtractCentroid
    return ExtractCentroid(iface)
