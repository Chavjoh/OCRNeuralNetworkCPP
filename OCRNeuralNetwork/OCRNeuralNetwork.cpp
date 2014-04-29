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

	// Define dataset path (WARNING : Only available if executed in Visual Studio)
	string datasetPath = string(currentPath) + "\\..\\Dataset";

	// If dataset folder doesn't exist, ask user to run install script
	if (!CppTools::fileExists(datasetPath))
	{
		cout << "Dataset file path not found." << endl;
		cout << "Please install dataset with DatasetInstallation python script." << endl;

		system("PAUSE");
		return 0;
	}
	
	// Define training/testing computed file path and neural network parameters file path
	string trainingPath = datasetPath + "\\trainingset.txt";
	string testPath = datasetPath + "\\testset.txt";
	string networkPath = datasetPath + "\\network.xml";

	// Create computed training file if not exists
	if (!CppTools::fileExists(trainingPath))
	{
		cout << "Writing the training set ..." << endl;
		CvTools::writeDataset(datasetPath, 305, datasetPath + "\\trainingset.txt");
	}
	
	// Create computed testing file if not exists
	if (!CppTools::fileExists(testPath))
	{
		cout << "Writing the test set ..." << endl;
		CvTools::writeDataset(datasetPath, 130, datasetPath + "\\testset.txt");
	}

	// Create neural network for optical character recognition
	CvNeuralNetwork neuralNetwork(datasetPath, trainingPath, testPath, networkPath);

	// Make some random tests
	for (int charIndex = 1; charIndex < 11; ++charIndex)
	{
		// Select random file in a random group
		int sampleGroupID = rand() % 10 + 1;//rand() % 62 + 1;
		int sampleID = rand() % 1016 + 1;

		// Define file path
		string filename = datasetPath + "\\English\\Fnt\\Sample" + CvTools::intToString(sampleGroupID) + "\\" + CvTools::intToString(sampleID) + ".png";

		cout << "----------------------------------------" << endl << endl;

		if (CppTools::fileExists(filename))
		{
			int maxIndex = neuralNetwork.predictClass(filename);
			
			cout << "Group " << (sampleGroupID - 1) << " -> Sample " << sampleID << endl;
			cout << "Predicted class -> " << maxIndex << endl << endl;
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

