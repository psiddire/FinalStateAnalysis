'''                                                                                                                                                                                                                                                                         IInterface for DY pT correction
===================================================
Author: Prasanna Kumar Siddireddy
'''

from correctionloader import CorrectionLoader
import os
import ROOT 

def make_DYreweight_2018():
    return DYCorrection(
        os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/zpt_weights_2018.root'),
        "zptmass_histo"   
    )

def make_DYreweight_2017():
    return DYCorrection(
        os.path.join(os.environ['fsa'], 'TagAndProbe/data/2017/zptm_weights_2017_kit.root'),
        "zptmass_histo"
    )

def make_DYreweight_2016():
    return DYCorrection(
        os.path.join(os.environ['fsa'], 'TagAndProbe/data/2016/zpt_weights_2016_BtoH.root'),
        "zptmass_histo"   
    )

class DYCorrection(object):
    def __init__(self, file, mass_pt):
        ROOT.TH1.AddDirectory(False)
        self.filename = file
        self.file = ROOT.TFile.Open(file)
        self.histopath = mass_pt
        self.correct_by_mass_pt = {}
        self.key = self.file.Get(self.histopath)
    def __call__(self, mass, pt):
        self.correct_by_mass_pt = self.key.GetBinContent(self.key.FindFixBin(mass, pt))
        self.error_by_mass_pt = self.key.GetBinError(self.key.FindFixBin(mass, pt))
        return self.correct_by_mass_pt

