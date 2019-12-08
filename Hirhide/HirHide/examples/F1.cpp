#include <cstdio>
#include <iostream>
#include "../Graph.h"

#include "../os.h"
#include "../Config.h"

using std::cout;
using std::endl;

#include <vector>
#include <string>
using std::vector;
using std::string;

#include <string.h>

extern Config hicode_config;

void showVector(vector<int> & v, string name = "vector", int id = 0)
{
	cout << name << " " << id << " (size=" << v.size() << ") : " << endl;
	//for (size_t i = 0; i < v.size(); ++i)
		//cout << v[i] << " ";
	//cout << endl;
}

bool fileExists(string filename)
{
	bool b;
	FILE * f = fopen(filename.c_str(), "r");
	if (f)
	{
		b = true;
		fclose(f);
	}
	else
		b = false;



	return b;
}

int main_F1(int argc, char *argv[])
{
	string path = "F:/BioHICODE/SC_test/";
	string detected_path = "F:/BioHICODE/SC_test/detected4/";
	string truth_path = "F:/BioHICODE/SC_test/";
	string output_path = "F:/BioHICODE/SC_test/Output2/";
	string baseline_path = "F:/BioHICODE/SC_test/baseline/";

	os::mkdir(output_path);

	Graph g;
	g.load(path +"graph");

	FILE * fp;
	FILE * fp_read;

	//基本情况
	//Detected                                *********** need to be changed ********
	vector<string> d_files;

	for (int i = 1; i <= 4; ++i)  //Layer*********** need to be changed ********
	{
		for (int j = 1; j <= 4; ++j)  //Level*********** need to be changed ********
		{
			char buff[256];
			string s;
			sprintf(buff, "Layer%d_Level%d.gen", i, j);
			//sprintf(buff, "Level%d.gen",  j);
			
			printf("%s\n", buff);
			s = buff;
			d_files.push_back(s);
		}
	}


	vector<string> baseline_files;
	baseline_files.push_back("mod.gen");
	baseline_files.push_back("mod.gen_level1");
	baseline_files.push_back("mod.gen_level2");
	//baseline_files.push_back("mod.gen_level3");
	baseline_files.push_back("Infomap.gen");
	baseline_files.push_back("CFinder.gen");
	baseline_files.push_back("LC.gen");
	baseline_files.push_back("OSLOM.gen");
	baseline_files.push_back("OSLOM.gen_level1");
	baseline_files.push_back("OSLOM.gen_level2");
	baseline_files.push_back("OSLOM.gen_level3");
	

	vector<string> t_files;
	for (int i = 0; i <= 0; ++i)
	{
		char buff[256];
		string s;
		sprintf(buff, "truth_id.gen", i);
		//sprintf(buff, "level_%d.gen", i);
		s = buff;
		t_files.push_back(s);
	}
	//t_files.push_back("detected.gen");

	Communities truth_all;
	Communities detected_layer1_all;
	Communities detected_layer2_all;

	string filename;

	//社团基本信息
	filename = output_path + "detected_community.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "detected, #community, average size, Q\n");
		for (int i = 0; i < d_files.size(); ++i)
		{
			string path = detected_path + d_files[i];
			Communities d;
			d.load(path.c_str());
			double Q = g.calcModularity(d);

			fprintf(fp, "%s,%d,%.0lf,%lf\n", d_files[i].c_str(), d.size(), d.averageSize(), Q);
			printf("%s,%d,%.0lf,%lf\n", d_files[i].c_str(), d.size(), d.averageSize(), Q);

		}
		fclose(fp);
	}
	else
		printf("%s exists\n", filename.c_str());
	
	filename = output_path + "baseline_community.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "detected, #community, average size, Q\n");
		for (int i = 0; i < baseline_files.size(); ++i)
		{
			string path = baseline_path + baseline_files[i];
			Communities d;
			d.load(path.c_str());
			double Q = g.calcModularity(d);

			fprintf(fp, "%s,%d,%.0lf,%lf\n", baseline_files[i].c_str(), d.size(), d.averageSize(), Q);
		}
		fclose(fp);
	}
	else
		printf("%s exists\n", filename.c_str());
	
	filename = output_path + "truth_community.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "truth, #community, average size, Q\n");
		for (int i = 0; i < t_files.size(); ++i)
		{
			string path = truth_path + t_files[i];
			Communities t;
			t.load(path.c_str());
			double Q = g.calcModularity(t);

			fprintf(fp, "%s,%d,%.0lf,%lf\n", t_files[i].c_str(), t.size(), t.averageSize(), Q);
		}
		fclose(fp);
	}
	else
		printf("%s exists\n", filename.c_str());
	

	

	//detected和truth 分层对比
	filename = output_path + "detected_vs_truth_lavel.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "detected, truth, truth average f1, detected average f1, truth weighted f1, detected weighted f1\n");
		for (int i = 0; i < d_files.size(); ++i)
		{
			string path = detected_path + d_files[i];
			Communities d;
			d.load(path.c_str());

			for (int j = 0; j < t_files.size(); ++j)
			{
				string path = truth_path + t_files[j];
				Communities t;
				t.load(path.c_str());

				printf("%d vs %d\n", i, j);

				double t_f1, d_f1, t_wf1, d_wf1;
				t_f1 = Communities::f1(t, d);
				d_f1 = Communities::f1(d, t);
				t_wf1 = Communities::wf1(t, d);
				d_wf1 = Communities::wf1(d, t);
				fprintf(fp, "%s,%s,%lf,%lf,%lf,%lf\n", d_files[i].c_str(), t_files[j].c_str(), t_f1, d_f1, t_wf1, d_wf1);
			}
		}
		fclose(fp);
	}
	else
		printf("%s exists\n", filename.c_str());
	

	//baseline对比truth 分层对比
	filename = output_path + "baseline_vs_truth_level.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "detected, truth, truth average f1, detected average f1, truth weighted f1, detected weighted f1\n");
		for (int i = 0; i < baseline_files.size(); ++i)
		{
			string path = baseline_path + baseline_files[i];
			Communities d;
			d.load(path.c_str());

			for (int j = 0; j < t_files.size(); ++j)
			{
				string path = truth_path + t_files[j];
				Communities t;
				t.load(path.c_str());

				printf("%d vs %d\n", i, j);

				double t_f1, d_f1, t_wf1, d_wf1;
				t_f1 = Communities::f1(t, d);
				d_f1 = Communities::f1(d, t);
				t_wf1 = Communities::wf1(t, d);
				d_wf1 = Communities::wf1(d, t);
				fprintf(fp, "%s,%s,%lf,%lf,%lf,%lf\n", baseline_files[i].c_str(), t_files[j].c_str(), t_f1, d_f1, t_wf1, d_wf1);
			}
		}
		fclose(fp);
	}
	else
		printf("%s exists\n", filename.c_str());


	//truth modularity
	//Communities detected;
	//detected.load("F:/Bio/0420/output/hicode_mod_ReduceWeight_2layers_ori_sub/all.gen");
	//detected.calcModularity(g);

	filename = output_path + "community_truth_detected.csv";
	if (!fileExists(filename))
	{
		fp = fopen(filename.c_str(), "w");
		fprintf(fp, "level, #,size,inter edges, outer edges, modularity\n");
		for (int i = 0; i < t_files.size(); ++i)
		{
			string path = truth_path + t_files[i];
			Communities t;
			t.load(path.c_str());
			t.calcModularity(g);

			for (int j = 0; j < t.size(); ++j)
			{
				printf("%d\n", j);
				fprintf(fp, "%d,%d,%d,%lf,%lf,%lf\n", i, j, t.comms[j].size(), 
					t.comm_inter_edge_num[j], t.comm_out_edge_num[j],t.getCommQ(j));
			}
		}
		fclose(fp);
		
		
	}
	else
		printf("%s exists\n", filename.c_str());
	
	
	//从Detected里面找truth最像的
	for (int j = 0; j < t_files.size(); ++j)
	{
		string path = truth_path + t_files[j];
		Communities t;
		t.load(path.c_str());

		filename = output_path + t_files[j] + "_vs_detected.csv";
		if (!fileExists(filename))
		{
			fp = fopen(filename.c_str(), "w");
			fprintf(fp, "truth");
			for (int i = 0; i < t.size(); ++i)
			{
				fprintf(fp, ",%d", i);
			}
			fprintf(fp, "\n");
			for (int i = 0; i < baseline_files.size(); ++i)
			{
				string path = baseline_path + baseline_files[i];
				Communities d;
				d.load(path.c_str());
				fprintf(fp, "%s", baseline_files[i].c_str());
				for (int k = 0; k < t.size(); ++k)
				{
					pair<double, int> res;
					res = Communities::f1(t.comms[k], d);
					fprintf(fp, ",%lf", res.first);
				}
				fprintf(fp, "\n");
			}
			for (int i = 0; i < d_files.size(); ++i)
			{
				string path = detected_path + d_files[i];
				Communities d;
				d.load(path.c_str());
				fprintf(fp, "%s", d_files[i].c_str());
				for (int k = 0; k < t.size(); ++k)
				{
					pair<double, int> res;
					res = Communities::f1(t.comms[k], d);
					fprintf(fp, ",%lf", res.first);
				}
				fprintf(fp, "\n");
			}
			fclose(fp);
		}
		else
			printf("%s exists\n", filename.c_str());
	}


	return 0;
}