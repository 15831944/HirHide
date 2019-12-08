#include <cstdio>
#include <iostream>
#include "../Graph.h"
#include "../Config.h"


using std::cout;
using std::endl;


extern Config hicode_config;



#include "../os.h"

int test_main(int argc, char *argv[])
{
	


	string graph_path = "F:/BioHICODE/test/";
	hicode_config.updateConfig(graph_path + "hicode_default.config");



	Graph g;
	g.load(graph_path + "graph");
	g.setWeighted(true);


	g.print();

	//return 0;

	Communities layer1;
	
	layer1 = g.runMod();
	double Q = layer1.calcModularity(g);
	layer1.print();

	Graph g1;
	g1 = g.reduceWeight(layer1);

	g1.print();

	Communities layer2=g1.runMod();
	Q = layer2.calcModularity(g);
	layer2.print(true);



	printf("------------\ndone\n");
	return 0;
}