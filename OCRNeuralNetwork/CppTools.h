#pragma once

#include <fstream>

using namespace std;

class CppTools
{
public:
	static bool fileExists(const string& name);

private:
	CppTools();
	~CppTools();
};

