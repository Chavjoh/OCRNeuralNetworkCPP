#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------#
# Count the number of sample for each group                                    #
# ============================================================================ #
# Developer:    Chavaillaz Johan                                               #
# Filename:     DatasetCount.py                                                #
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

import os

#------------------------------------------------------------------------------#
#                                                                              #
#                             UTILITIES FUNCTIONS                              #
#                                                                              #
#------------------------------------------------------------------------------#

def fcount(path):
	""" Counts the number of files in a directory """
	count = 0
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			count += 1

	return count
	
#------------------------------------------------------------------------------#
#                                                                              #
#                                     MAIN                                     #
#                                                                              #
#------------------------------------------------------------------------------#

if __name__ == '__main__':

	baseFolder = 'Dataset/English/Fnt/'
	totalCount = 0

	for folder in os.listdir(baseFolder):
		currentCount = fcount(baseFolder + folder)
		totalCount += currentCount
		print(baseFolder + folder + " -> " + str(currentCount))
		
	print("----------------------------------------")
	print("Total : " + str(totalCount))
	print("----------------------------------------")
	