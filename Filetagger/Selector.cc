#include<string>
#include<iostream>
#include<fstream>
#include<TFile.h>
#include<TTree.h>
#include<TH1D.h>

using namespace std;

void Mixed_Analysis(string inputFile,string outputFile){
 TFile *fin = TFile::Open(inputFile.c_str());
 TTree *tin = static_cast<TTree *>(fin->Get("Runs"));
 TH1D *htemp = new TH1D("htemp","runNumber",500,355500,356000);
 int n=tin->Draw("RunAuxiliary.id_.run_","","goff");
 cout<<"Number of runs in this file "<<n<<endl;
 double av=htemp->GetMean();
 cout<<"Average "<<av <<endl;
 if(abs(av-355933)<1||abs(av-355942)<1){
  cout<<"File Saved!"<<endl;
  ofstream write (outputFile, std::ofstream::app);
  write<<inputFile<<endl;
  write.close();
 }
 else{cout<<"Discard file"<<endl;}
 delete htemp;
}

int main(int argc, char **argv){
    string inputFile = argv[1];
    string outputFile = argv[2];

    cout<<"Scanning "<<inputFile<<endl;

    Mixed_Analysis(inputFile, outputFile);

    return 0;
}
