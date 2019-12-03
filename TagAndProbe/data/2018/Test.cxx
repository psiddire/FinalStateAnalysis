#include "TFile.h"
#include "TString.h"

//double ();

double QCDEstimation(TString& file, int jets, double dR, double Electron_pt, double Muon_pt){

  std::cout << dR << std::endl;

  TFile f(file);
  RooWorkspace* w = (RooWorkspace*)f.Get("w");
  w->var("njets")->setVal(jets);
  w->var("dR")->setVal(dR);
  w->var("e_pt")->setVal(Electron_pt);
  w->var("m_pt")->setVal(Muon_pt);

  double factor_bin =  w->function("em_qcd_osss_binned")->getVal();
  double factor_uncert = w->function("em_qcd_extrap_uncert")->getVal();

  double osss = factor_bin * factor_uncert;

  //float osss = w->function("em_qcd_osss_binned").getVal()*w->funtion("em_qcd_extrap_uncert").getVal();
  //std::cout << "OSSS Value " << osss << std::endl;

  return osss;
  f.Close();
}


void Test(){

  TString file("htt_scalefactors_legacy_2018.root");
  double osss = QCDEstimation(file, 0, 1.0, 100.0, 100.0);
  std::cout << osss << std::endl;
 
}
