#include <cstdio>
#include <iostream>
#include "../Graph.h"

#include "../os.h"

using std::cout;
using std::endl;

#include "../Config.h"
extern Config hicode_config;




int main_f1fj(int argc, char *argv[])
{
	if (argc != 5)
	{
		printf("ustage: f1fj graph detected.gen truth.gen outdir\n");
		//return 0;
	}
	Communities detected;
	Communities truth;

	Graph g;
	if (argc > 1)
		g.load(argv[1]);
	else
		g.load("F:/HICODE_SUB/0426new/graph");
	if (argc > 2)
		detected.load(argv[2]);
	else
		detected.load("F:/HICODE_SUB/0426new/L11.txt");

	if (argc > 3)
		truth.load(argv[3]);
	else
		truth.load("F:/HICODE_SUB/0426new/hicode_mod_ReduceWeight_2layers/maxOriginlayer1.gen");

	string outdir;
	if (argc > 4)
		outdir = argv[4];
	else
		outdir = "f1fj_output/";

	os::mkdir(outdir);

	double f1_unweighted = Communities::F1_unweighted(detected, truth);
	double f1_weighted = Communities::F1_weighted(detected, truth);

	double jaccard_f1_unweighted = Communities::Jaccard_F1_unweighted(detected, truth);
	double jaccard_f1_weighted = Communities::Jaccard_F1_weighted(detected, truth);

	double f1_precision_unweighted = Communities::f1(detected, truth);
	double f1_recall_unweighted = Communities::f1(detected, truth);

	double f1_precision_weighted = Communities::wf1(detected, truth);
	double f1_recall_weighted = Communities::wf1(detected, truth);

	printf("F1 = %lf, wF1 = %lf\n", f1_unweighted, f1_weighted);

	printf("JF1 = %lf, wJF1 = %lf\n", jaccard_f1_unweighted, jaccard_f1_weighted);

	printf("F1_precision = %lf, wF1_precision = %lf\n", f1_precision_unweighted, f1_recall_unweighted);

	printf("F1_recall = %lf, wF1_recall = %lf\n", f1_precision_weighted, f1_recall_weighted);


	
	return 0;
}