"""
This file contains the eGo functions for studies on storages.
"""

__copyright__ = ("Europa-Universität Flensburg, "
                 "Centre for Sustainable Energy Systems")
__license__ = "GNU Affero General Public License Version 3 (AGPL-3.0)"
__author__ = "wolf_bunke,maltesc"

import io
import os
import logging
logger = logging.getLogger('ego')

if not 'READTHEDOCS' in os.environ:
    import pandas as pd
    import numpy as np


def total_storage_charges(network):
    """
    Sum up the pysical storage values of the total scenario based on
    eTraGo results.

    Parameters
    ----------
    network : eTraGo Network based on pypsa.network
        PyPSA Network object modified by eTraGo

    plot (bool):
        Use plot function


    Returns
    -------

    results : pandas.DataFrame
        Return ...

    Notes
    -----
    charge :
         Quantity of charged Energy in MWh over scenario time steps

    discharge :
        Quantity of discharged Energy in MWh over scenario time steps

    count :
        Number of storage units

    p_nom_o_sum:
        Sum of optimal installed power capacity
    """

    charge = network.storage_units_t.p[network.storage_units_t.
                                       p[network.storage_units[network.storage_units.
                                                               p_nom_opt > 0].index].values > 0.].\
        groupby(network.storage_units.carrier, axis=1).sum().sum()

    discharge = network.storage_units_t.p[network.storage_units_t.
                                          p[network.storage_units[network.storage_units.
                                                                  p_nom_opt > 0].index].values < 0.].\
        groupby(network.storage_units.carrier, axis=1).sum().sum()

    count = network.storage_units.bus[network.storage_units.p_nom_opt > 0].\
        groupby(network.storage_units.carrier, axis=0).count()

    p_nom_sum = network.storage_units.p_nom.groupby(network.storage_units.
                                                    carrier, axis=0).sum()

    p_nom_o_sum = network.storage_units.p_nom_opt.groupby(network.storage_units.
                                                          carrier, axis=0).sum()
    p_nom_o = p_nom_sum - p_nom_o_sum  # Zubau

    results = pd.concat([charge.rename('charge'), discharge.rename('discharge'),
                         p_nom_sum, count.rename('total_units'), p_nom_o
                         .rename('extension'), ], axis=1, join='outer')

    return results


def etrago_storages(network):
    """Function for storage and grid expantion costs of eTraGo.

    Parameters
    ----------

    network : eTraGo Network
        eTraGo Network Class based on PyPSA

    Returns
    -------
    storages : pandas.DataFrame
        DataFrame with cumulated results of storages

    """
    # Charge / discharge (MWh) and installed capacity MW
    storages = total_storage_charges(network=network)

    return storages