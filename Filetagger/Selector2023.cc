#include<string>
#include<iostream>
#include<fstream>
#include<TFile.h>
#include<TTree.h>
#include<TH1D.h>

using namespace std;

void Mixed_Analysis(string inputFile,string outputFile){
 TFile *fin = TFile::Open(inputFile.c_str());
cout<<"file retrieved"<<endl;
 TTree *tin = static_cast<TTree *>(fin->Get("Runs"));
cout<<"tree retrieved"<<endl;
 TH1D *htemp = new TH1D("htemp","runNumber",50,369925,369975);
 int n=tin->Draw("RunAuxiliary.id_.run_","","goff");
cout<<"debbug"<<endl;
 double av=htemp->GetMean();
cout<<"run number retrieved"<<endl;
 

 TTree *tin2 = static_cast<TTree *>(fin->Get("LuminosityBlocks"));
 int nlumi=tin2->GetEntries();
 TH1D *htemp2 = new TH1D("htemp2","lumiNumber",10000,0,10000);
 tin2->Draw("LuminosityBlockAuxiliary.id_.luminosityBlock_>>htemp2","","goff");

 cout<<"Number of runs in this file "<<n<<endl;
 cout<<"Average "<<av <<endl;
 if(abs(av-369956)<0.5){
  bool safe=false;
  if((htemp2->Integral(0,235)<0.1) && (htemp2->Integral(710,10000)<0.1)) safe=true;
  if(!safe) {cout<<"Discard file because lower integral is "<<htemp2->Integral(0,235) <<" and upper is"<<  htemp2->Integral(710,10000)<<endl;}
  else{
 	cout<<"File Saved!"<<endl;
  	ofstream write (outputFile, std::ofstream::app);
  	write<<inputFile<<endl;
  	write.close();
   }
 }
 else{cout<<"Discard file"<<endl;}
 delete htemp2;
}

int main(int argc, char **argv){
    string inputFile = argv[1];
    string outputFile = argv[2];

    cout<<"Scanning "<<inputFile<<endl;

    Mixed_Analysis(inputFile, outputFile);

    return 0;
}
