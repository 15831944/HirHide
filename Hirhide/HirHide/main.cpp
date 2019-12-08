#include <map>
#include "Graph.h"
#include "Config.h"

map<string, string> Graph::config;

int main_hicode(int argc, char *argv[]);
int main_F1(int argc, char *argv[]);
int main_f1fj(int argc, char *argv[]);
int main_Facebook_f1(int argc, char *argv[]);
int run_main(int argc, char *argv[]);
int test_main(int argc, char *argv[]);

Config hicode_config;

int main(int argc, char *argv[])
{
	Graph::loadConfig(ALG_CONFIG_PATH);
	hicode_config.updateConfig("../../hicode_default.config");


	


	//return run_main(argc, argv);
	return main_hicode(argc, argv);
	//return main_F1(argc, argv);
	//return main_f1fj(argc, argv);
	//return main_Facebook_f1(argc, argv);
	//return test_main(argc, argv);      //*********** need to be changed ********


}