#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------#
# Dataset download and installation in current directory                       #
# ============================================================================ #
# Developer:    Chavaillaz Johan                                               #
# Filename:     DatasetInstallation.py                                         #
# Version:      1.0                                                            #
#                                                                              #
# Licensed to the Apache Software Foundation (ASF) under one                   #
# or more contributor license agreements. See the NOTICE file                  #
# distributed with this work for additional information                        #
# regarding copyright ownership. The ASF licenses this file                    #
# to you under the Apache License, Version 2.0 (the                            #
# "License"); you may not use this file except in compliance                   #
# with the License. You may obtain a copy of the License at                    #
#                                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                              #
# Unless required by applicable law or agreed to in writing,                   #
# software distributed under the License is distributed on an                  #
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY                       #
# KIND, either express or implied. See the License for the                     #
# specific language governing permissions and limitations                      #
# under the License.                                                           #
#                                                                              #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                                                                              #
#                               LIBRARIES IMPORT                               #
#                                                                              #
#------------------------------------------------------------------------------#

import os, sys
import tarfile
import argparse
import urllib.request
import shutil
import glob

#------------------------------------------------------------------------------#
#                                                                              #
#                             UTILITIES FUNCTIONS                              #
#                                                                              #
#------------------------------------------------------------------------------#

def downloadBinary(url, destination):
	with urllib.request.urlopen(url) as download:  
		file = open(destination, 'wb')
		file.write(download.read())
		file.close()

def untar(path, extract_path):
	tar = tarfile.open(path, 'r')
	for item in tar:
		tar.extract(item, extract_path)
		if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
			extract(item.name, "./" + item.name[:item.name.rfind('/')])

def renameIncremental(dir, pattern):
	i = 0
	for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
		i += 1
		# Get title and extension of the current file
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		# Rename current file
		os.rename(pathAndFilename, os.path.join(dir, str(i) + ext))

#------------------------------------------------------------------------------#
#                                                                              #
#                                     MAIN                                     #
#                                                                              #
#------------------------------------------------------------------------------#

if __name__ == '__main__':

	# Create argument parser to help user
	parser = argparse.ArgumentParser(
		description='Dataset installation used to train neural network for optical character recognition.'
	)

	# Show help if one of the arguments is missing
	if len(sys.argv) != 1:
		parser.print_help()
		sys.exit()
	
	# Installer configuration
	datasetPath = r'Dataset/' 
	datasetFile = r'Chars74k.tgz'
	
	# Delete dataset folder
	if os.path.exists(datasetPath):
		print("Deleting old dataset ...")
		shutil.rmtree('Dataset')
	
	# Create dataset folder
	os.makedirs(datasetPath)
	
	# Download dataset file
	print("Downloading dataset ...")
	downloadBinary('http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishFnt.tgz', datasetPath + datasetFile)
	
	# Untar dataset file
	print("Untaring dataset ...")
	untar(datasetPath + datasetFile, datasetPath)
	
	# Rename dataset file for each 62 datasets [1, 62]
	print("Preparing dataset ...")
	for i in range(1, 63):
	
		# Folder that contains samples
		sampleFolder = datasetPath + "English/Fnt/Sample"

		# Default folder name of the dataset
		folderPath = sampleFolder + str(i).zfill(3);
		
		# Rename each file in the folder to be accessed more easily
		renameIncremental(folderPath, r'*.png')
		
		# Rename folder to be accessed more easily
		os.rename(folderPath, sampleFolder + str(i));
	
	print("Dataset successfully installed !")
	