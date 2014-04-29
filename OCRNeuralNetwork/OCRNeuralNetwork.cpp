#include "stdafx.h"
#include <stdio.h>      // defines FILENAME_MAX
#include <stdlib.h>     // srand, rand
#include <direct.h>     // _getcwd
#include <time.h>       // time
#include <string.h>
#include <fstream>

#include "CvNeuralNetwork.h"
#include "CppTools.h"

using namespace cv;
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	// Initialize random seed
	srand(time(NULL));

	// Get current directory
	char currentPath[FILENAME_MAX];
	_getcwd(currentPath, sizeof(currentPath));
	currentPath[sizeof(currentPath)-1] = '\0';

	// Create dataset path with current directory
	string datasetPath = string(currentPath) + "\\..\\Dataset";

	if (!CppTools::fileExists(datasetPath))
	{
		cout << "Dataset file path not found." << endl;
		cout << "(" << datasetPath << ")" << endl;

		system("PAUSE");
		return 0;
	}
	
	string trainingPath = datasetPath + "\\trainingset.txt";
	string testPath = datasetPath + "\\testset.txt";
	string networkPath = datasetPath + "\\network.xml";

	if (!CppTools::fileExists(trainingPath))
	{
		cout << "Writing the training set ..." << endl;
		CvTools::writeDataset(datasetPath, 305, datasetPath + "\\trainingset.txt");
	}
	
	if (!CppTools::fileExists(testPath))
	{
		cout << "Writing the test set ..." << endl;
		CvTools::writeDataset(datasetPath, 130, datasetPath + "\\testset.txt");
	}

	CvNeuralNetwork neuralNetwork(datasetPath, trainingPath, testPath, networkPath);

	for (int charIndex = 1; charIndex < 11; ++charIndex)
	{
		int sampleGroupID = rand() % 62 + 1;
		int sampleID = rand() % 1016 + 1;
		string filename = datasetPath + "\\English\\Fnt\\Sample" + CvTools::intToString(sampleGroupID) + "\\" + CvTools::intToString(sampleID) + ".png";

		cout << "-------------------- " << charIndex << " --------------------" << endl << endl;

		if (CppTools::fileExists(filename))
		{
			int maxIndex = neuralNetwork.predictClass(filename);
			
			cout << "Group " << sampleGroupID << " -> Sample " << sampleID << endl;
			cout << "Predicted class:" << maxIndex << endl << endl;
		}
		else
		{
			cout << "Test image not found." << endl;
			cout << filename << endl;
		}
	}

	system("PAUSE");
	return 0;
}

