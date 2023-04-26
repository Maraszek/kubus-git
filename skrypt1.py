# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:44:49 2023

@author: Martyna
"""
import argparse
import numpy as np
from transformacje import Transformacje


def main():
    elipsoida_grs80 = Transformacje(model="grs80")

    parser = argparse.ArgumentParser(description="Program do transformacji współrzędnych.")
    parser.add_argument("--input", help="ścieżka do pliku wejściowego z danymi")
    parser.add_argument("--output", help="ścieżka do pliku wyjściowego z wynikami")

    args = parser.parse_args()

    if args.input and args.output:
        input_data = np.genfromtxt(args.input, delimiter=',', skip_header=4)
        output_path = args.output

        w, k = np.shape(input_data)

        fi_lam_h = np.zeros((w, k))
        XYZ = np.zeros((w, k))
        XY_00 = np.zeros((w, 2))
        XY_92 = np.zeros((w, 2))
        n_e_u = np.zeros((w, k))

        tablica_wynikow = np.zeros((w, 10))
