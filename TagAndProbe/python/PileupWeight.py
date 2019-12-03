'''
Takes as input a MC tag and pileup distributions (generated by pileupCalc.py [1])
Author: Prasanna Kumar Siddireddy
https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData
'''

from FinalStateAnalysis.Utilities.FileInPath import FileInPath
import ROOT

class PileupWeight(object):
    def __init__(self, mctag, year, *datafiles):

        if year=='2016':
            pu_file = FileInPath("FinalStateAnalysis/TagAndProbe/data/2016/Pileup.root").full_path()
        elif year=='2017':
            pu_file = FileInPath("FinalStateAnalysis/TagAndProbe/data/2017/Pileup.root").full_path()
        elif year=='2018':
            pu_file = FileInPath("FinalStateAnalysis/TagAndProbe/data/2018/Pileup.root").full_path()

        ROOT.TH1.AddDirectory(False)
        self.mc = None
        self.data = None
        
        for filename in datafiles:
            file = ROOT.TFile.Open(filename)
            pu = file.Get('pileup')
            if self.data is None:
                self.data = pu.Clone()
                self.data.SetDirectory(0)
            else:
                self.data.Add(pu)
            file.Close()
        self.data.Scale(1./self.data.Integral())

        mc_file = ROOT.TFile.Open(pu_file)
        if not mc_file:
            raise IOError("Can't open PU MC file")
        mc_base = mc_file.Get(mctag)
        self.mc = mc_base.Clone()
        self.mc.SetName('pileup_mc')
        
        # Make sure bins are consistent
        if not ROOT.TEfficiency.CheckBinning(self.mc, self.data):
            error = "Data and MC PU histograms do not have the same binning!\n"
            def print_bins(tag, x):
                return "%s: (%i, %0.1f, %0.1f)" % (
                    tag, x.GetNbinsX(), x.GetXaxis().GetXmin(),
                    x.GetXaxis().GetXmax())
            error += print_bins(mctag, self.mc)
            error += "\n"
            error += print_bins('data', self.data)
            raise ValueError(error)
       # Normalize MC
        self.mc.Scale(1./self.mc.Integral())
        ROOT.TH1.AddDirectory(True)
        
    def __call__(self, ntruepu):
        '''
        Get the PU weight given the true number of interactions
        '''
        bin = self.data.FindBin(ntruepu)
        data = self.data.GetBinContent(bin)
        mc = self.mc.GetBinContent(bin)
        if mc:
            return data/mc
        else:
            return 1.0

