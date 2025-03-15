import math
import openmc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Iterable

def get_exp_cllif_density(temp, LiCl_frac=0.695):
    """Calculates density of ClLiF [g/cc] from temperature in Celsius
    and molar concentration of LiCl. Valid for 660 C - 1000 C.
    Source:
    G. J. Janz, R. P. T. Tomkins, C. B. Allen;
    Molten Salts: Volume 4, Part 4
    Mixed Halide Melts Electrical Conductance, Density, Viscosity, and Surface Tension Data.
    J. Phys. Chem. Ref. Data 1 January 1979; 8 (1): 125–302.
    https://doi.org/10.1063/1.555590
    """
    temp = temp + 273.15  # Convert temperature from Celsius to Kelvin
    C = LiCl_frac * 100  # Convert molar concentration to molar percent

    a = 2.25621
    b = -8.20475e-3
    c = -4.09235e-4
    d = 6.37250e-5
    e = -2.52846e-7
    f = 8.73570e-9
    g = -5.11184e-10

    rho = a + b * C + c * temp + d * C**2 + e * C**3 + f * temp * C**2 + g * C * temp**2

    return rho


def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def calculate_circle_surface(radius):
    area = math.pi * radius**2
    return area

def rescale_to_lethargy(df: pd.DataFrame, normalize_over: Iterable = None) -> pd.DataFrame:
    """Rescale the mean and std. dev. of a DataFrame to lethargy values.
    Useful when it comes to plot a particle energy spectrum in lethargy scale.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing an energy spectrum tally. it needs to contain
        'mean' and 'std. dev.' columns, as well as 'energy low [eV]' and 
        'energy high [eV]' columns.
    normalize_over : Iterable, optional
        Some openmc tallies (e.g. cell tally, surface tally) need to be normalized 
        by their filter dimension (e.g cell volume, surface area), by default None

    Returns
    -------
    pd.DataFrame
        DataFrame with the mean and std. dev. rescaled to lethargy values.
    """
    # Copy the DataFrame to avoid modifying the original
    df_lethargy = df.copy()

    # Calculate the lethargy of the energy bins
    lethargy = np.log(
        df_lethargy['energy high [eV]'] / df_lethargy['energy low [eV]'])
    
    # normalize tally over tally filter dimension (e.g. cell volume, surface area etc.)
    if normalize_over is not None:
        df_lethargy['mean'] = df_lethargy['mean'] / normalize_over
        df_lethargy['std. dev.'] = df_lethargy['std. dev.'] / normalize_over

    # Rescale the mean and std. dev. to lethargy
    df_lethargy['mean'] = df_lethargy['mean'] / lethargy
    df_lethargy['std. dev.'] = df_lethargy['std. dev.'] / lethargy

    return df_lethargy

def plot_results(df, ylabel, label, color):
        
    figsize = (10, 5)
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=figsize, constrained_layout=True)
    
    ax[0].set_xscale('log')
    ax[1].set_xscale('linear')
    
    for i in range(2):
        ax[i].set_yscale('log')
        ax[i].tick_params(axis='both', which='both', direction='in', labelsize=12)
        ax[i].set_xlabel('Energy (eV)', fontsize=12)
    
    ax[0].set_ylabel(ylabel, fontsize=12)
    
    ax[0].annotate("Log scale on x", [0.05, 0.01], xycoords='axes fraction',
                    horizontalalignment='left', verticalalignment='bottom', fontsize=12)
    ax[1].annotate("Lin scale on x", [0.05, 0.01], xycoords='axes fraction',
                    horizontalalignment='left', verticalalignment='bottom', fontsize=12)
    
    # Plot
        
    ax[0].step(df['energy low [eV]'], df["mean"], linestyle='-', label=label, color=color)
    ax[0].fill_between(df['energy low [eV]'], df["mean"] - df["std. dev."], df["mean"] + df["std. dev."], color='gray', step='pre', alpha=0.5)

    ax[1].step(df['energy low [eV]'], df["mean"], linestyle='-', label=label, color=color)
    ax[1].fill_between(df['energy low [eV]'], df["mean"] - df["std. dev."], df["mean"] + df["std. dev."], color='gray', step='pre', alpha=0.5)

    ax[0].legend()
    
    plt.show()