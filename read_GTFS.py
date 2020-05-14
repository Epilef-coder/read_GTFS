import zipfile
import errno
import os
from os import listdir
from os.path import isfile
from os import remove
import shutil
import pandas as pd
from collections import defaultdict


# Recibimos ruta de GTFS para su lectura
class read_GTFS:

    # inicializamos variables globales
    def __init__(self, path):
        # path\to\GTFS.zip
        self.path = path
        self.dir = self.path[:self.path.rfind("\\")]
        self.name = self.path[self.path.rfind("\\") + 1:]
        self.dir_out = self.dir + "\\" + self.name[:self.name.rfind(".zip")]

        # contiene los nombres de los archivos que un GTFS puede tener
        self.arch_gtfs = []
        self.arch_gtfs.append("agency.txt")
        self.arch_gtfs.append("stops.txt")
        self.arch_gtfs.append("routes.txt")
        self.arch_gtfs.append("trips.txt")
        self.arch_gtfs.append("stop_times.txt")
        self.arch_gtfs.append("calendar.txt")
        self.arch_gtfs.append("calendar_dates.txt")
        self.arch_gtfs.append("fare_attributes.txt")
        self.arch_gtfs.append("fare_rules.txt")
        self.arch_gtfs.append("shapes.txt")
        self.arch_gtfs.append("frequencies.txt")
        self.arch_gtfs.append("transfers.txt")
        self.arch_gtfs.append("pathways.txt")
        self.arch_gtfs.append("level.txt")
        self.arch_gtfs.append("feed_info.txt")
        self.arch_gtfs.append("translations.txt")
        self.arch_gtfs.append("attributions.txt")

    def print_path(self):
        print(self.path)

    def print_dir(self):
        print(self.dir)

    def print_name(self):
        print(self.name)

    def print_dir_out(self):
        print(self.dir_out)

    # verifica si un archivo es txt
    @staticmethod
    def txt(arch):
        return arch.endswith('.txt')

    # verifica si un archivo es zip
    @staticmethod
    def zip(arch):
        return arch.endswith('.zip')

    # descomprimimos GTFS
    def decompress(self):
        # extraemos archivos de gtfs.zip input
        z = zipfile.ZipFile(self.path)
        # intentamos crear directorio de salida si no existe
        try:
            os.mkdir(self.dir_out)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        z.extractall(self.dir_out)
        z.close()

    # reconocemos archivos descomprimidos
    def list_arch(self):
        directory = self.dir_out + "\\"
        arch = [obj for obj in listdir(directory) if isfile(directory + obj)]
        print(arch)
        return arch

    # eliminamos archivos txt
    def clean_txt(self):
        arch = self.list_arch()
        for a in arch:
            if self.txt(a):
                remove(self.dir_out + "\\" + a)

    # limpiamos directorio
    def clean_dir(self):
        directory = self.dir_out.replace("\\", "\\\\")
        try:
            shutil.rmtree(directory)
        except OSError as e:
            print(e)

    # funcion principal
    def read_gtfs_with_df(self):
        # diccionario de nombre de archivos y su dataframe
        dic_gtfs = defaultdict(None)
        # descomprimimos el gtfs
        self.decompress()
        # reconocemos archivos
        arch = self.list_arch()
        print("")
        print("{} archivos en GTFS.zip: {}".format(len(arch), arch))
        # reconocemos archivos del gtfs
        ingtfs = []
        # reconocemos archivos no gtfs
        outgtfs = []
        # para cada archivo creamos dataframe
        for a in arch:
            name = a
            if name in self.arch_gtfs:
                ingtfs.append(name)
                df = pd.read_csv(self.dir_out + "\\" + name, sep=",")
                dic_gtfs[name] = df
            else:
                outgtfs.append(name)
                df = pd.read_csv(self.dir_out + "\\" + name, sep=",")
                dic_gtfs[name] = df
        # print archivos del GTFS
        print("{} archivos correspondiente a GTFS: {}".format(len(ingtfs), ingtfs))
        # print archivos no GTFS
        print("{} archivos no correspondiente a GTFS: {}".format(len(outgtfs), outgtfs))
        # limpiamos directorio
        self.clean_dir()
        # return
        return dic_gtfs
