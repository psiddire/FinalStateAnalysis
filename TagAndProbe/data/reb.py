import ROOT

f = ROOT.TFile.Open("pileupVBFHEM.root")

t = f.Get('pileup')

f1 = ROOT.TFile("hist.root","RECREATE")

xbins = []

for i in range(81):
    xbins.append(float(i))

print(xbins)

t.Rebin(80, 'pileup')

f1.cd()

t.Write()
