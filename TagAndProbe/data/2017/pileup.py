import ROOT

f = ROOT.TFile.Open("pileupWG.root")

t = f.Get('pileup/pileup')

f1 = ROOT.TFile("hist.root","RECREATE")

f1.cd()

t.Write()
