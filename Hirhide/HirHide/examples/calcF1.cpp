#include <cstdio>
#include <iostream>
#include "../Graph.h"

#include "../os.h"

using std::cout;
using std::endl;

#include "../Config.h"

extern Config hicode_config;

int main_Facebook_f1(int argc, char *argv[])
{


	string graph_path;
	
	graph_path = "F:/HICODE_SUB/BisheDataAchieve/UCSC/";
	string detected_path_s = "hicode/";
	string truth_path_s = "truth/";

	Graph g;
	g.load(graph_path + "graph");

	FILE * fp = fopen((graph_path + detected_path_s + "detected_files.txt").c_str(), "r");
	if (!fp)
		printf("fopen detected_files.txt failed");
	vector<string> detected_path;
	vector<Communities> detected;
	char buff[1024];
	while (!feof(fp))
	{
		fgets(buff, 1000, fp);
		string sfn = buff;
		if (sfn.size() > 1 && sfn[sfn.size() - 1] == '\n') sfn = sfn.substr(0, sfn.size() - 1);
		detected_path.push_back(sfn);

		Communities cs;
		cs.load(graph_path + detected_path_s + sfn);
		//cs.print();
		detected.push_back(cs);
	}
	fclose(fp);

	fp = fopen((graph_path + truth_path_s + "truth_files.txt").c_str(), "r");
	if (!fp)
		printf("fopen truth_files.txt failed");
	vector<string> truth_path;
	vector<Communities> truth;
	while (!feof(fp))
	{
		fgets(buff, 1000, fp);
		string sfn = buff;
		if (sfn.size() > 1 && sfn[sfn.size() - 1] == '\n') sfn = sfn.substr(0, sfn.size() - 1);
		truth_path.push_back(sfn);

		Communities cs;
		cs.load(graph_path + truth_path_s + sfn);

		//cs.print();
		truth.push_back(cs);
	}
	fclose(fp);

	//showVector(truth_path);



	string outdir = "statistic/";
	os::mkdir(outdir);

	fp = fopen((outdir + "modularity.csv").c_str(), "w");
	fprintf(fp, "truth,#comm,avgSize,modularity\n");



	for (int i = 0; i < truth.size(); ++i)
	{
		printf("process truth %d..\n", i);

		fprintf(fp, "%s,", truth_path[i].c_str());
		fprintf(fp, "%d,", truth[i].size());
		fprintf(fp, "%.0lf,", truth[i].averageSize());

		double m = g.calcModularity(truth[i]);
		fprintf(fp, "%lf\n", m);
		
	}
	fclose(fp);



	fp = fopen((outdir + "f1.csv").c_str(), "w");
	fprintf(fp, "truth");
	for (int truth_i = 0; truth_i < detected.size(); ++truth_i)
	{


		string tpath = detected_path[truth_i];

		fprintf(fp, ",%s", tpath.c_str());
	}

	fprintf(fp, "\n");
	for (int i = 0; i < truth.size(); ++i)
	{
		printf("process truth %d..\n", i);
		
		fprintf(fp, "%s", truth_path[i].c_str());
		fprintf(fp, "(%d)", truth[i].size());
		for (int j = 0; j < detected.size(); ++j)
		{
			//printf("process truth %d..\n", j);

			double wf1 = Communities::F1_unweighted(truth[i], detected[j]);
			fprintf(fp, ",%lf", wf1);
		}
		fprintf(fp, "\n");	

	}
	fclose(fp);


	
	

	os::moveDir(outdir, graph_path);

	printf("------------\ndone\n");
	return 0;
}