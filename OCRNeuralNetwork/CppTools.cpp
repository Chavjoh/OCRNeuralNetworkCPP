#include "stdafx.h"
#include "CppTools.h"

#include <sys/stat.h>

using namespace std;

CppTools::CppTools()
{
	// Nothing
}

CppTools::~CppTools()
{
	// Nothing
}

bool CppTools::fileExists(const string& name) 
{
	// Fatest way to check if a file exists
	// http://stackoverflow.com/questions/12774207/fastest-way-to-check-if-a-file-exist-using-standard-c-c11-c

	struct stat buffer;
	return (stat(name.c_str(), &buffer) == 0);
}
