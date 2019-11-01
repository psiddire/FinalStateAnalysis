'''
Interface to official corrections from the muon POG
===================================================
Author: Prasanna Kumar Siddireddy
https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffs2018
'''

import os
import re
import ROOT
from graphReader import GraphReaderTrackingEta
from correctionloader import CorrectionLoader

# Update when 2018 tracking numbers are available
mu_trackingEta_2018 = GraphReaderTrackingEta(
    os.path.join(os.environ['fsa'], 'TagAndProbe/data/fits.root'),'ratio_eff_eta3_dr030e030_corr'
)

_DATA_DIR = os.path.join(os.environ['CMSSW_BASE'], 'src',
                         "FinalStateAnalysis", "TagAndProbe", "data")

_DATA_FILES = {
    '2018' : {
        'ID'     : os.path.join(_DATA_DIR, 'RunABCD_SF_ID.root'),
        'Iso'    : os.path.join(_DATA_DIR, 'RunABCD_SF_ISO.root'),
        'Trigger': [os.path.join(_DATA_DIR, 'EfficienciesAndSF_2018Data_BeforeMuonHLTUpdate.root'),
                    os.path.join(_DATA_DIR, 'EfficienciesAndSF_2018Data_AfterMuonHLTUpdate.root')]
    }
}

def make_muon_pog_PFTight_2018():
    return MuonPOGCorrectionID2D(
        _DATA_FILES['2018']['ID'],
        "NUM_TightID_DEN_TrackerMuons_pt_abseta"
    )

def make_muon_pog_PFMedium_2018():
    return MuonPOGCorrectionID2D(
        _DATA_FILES['2018']['ID'],
        "NUM_MediumID_DEN_TrackerMuons_pt_abseta"
    )

def make_muon_pog_PFLoose_2018():
    return MuonPOGCorrectionID2D(
        _DATA_FILES['2018']['ID'],
        "NUM_LooseID_DEN_TrackerMuons_pt_abseta"
    )

def make_muon_pog_TightIso_2018(MuonID):
    return MuonPOGCorrectionTightIso2D(
        _DATA_FILES['2018']['Iso'],
        MuonID,
        ["NUM_TightRelIso_DEN_MediumID_pt_abseta",
        "NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta"]
    )

def make_muon_pog_LooseIso_2018(MuonID):
    return MuonPOGCorrectionLooseIso2D(
        _DATA_FILES['2018']['Iso'],
        MuonID,
        ["NUM_LooseRelIso_DEN_LooseID_pt_abseta",
        "NUM_LooseRelIso_DEN_MediumID_pt_abseta",
        "NUM_LooseRelIso_DEN_TightIDandIPCut_pt_abseta"]
    )

def make_muon_pog_IsoMu24_2018():
    ''' trigger efficiencies in DATA; weigthed by lumi for two sets available , viz Run 316361 (8950.878 /pb) and Run 316361 (50811.128 /pb); more info in MUON POG twiki '''
    return MuonPOGCorrectionTrig2D_weighted(
            _DATA_FILES['2018']['Trigger'],
            ["IsoMu24_PtEtaBins/pt_abseta_ratio", "IsoMu24_PtEtaBins/pt_abseta_ratio"], 8950.878, 50811.128
        )

class MuonPOGCorrectionID2D(object):

    def __init__(self, file, pt_abseta):
        self.file = ROOT.TFile.Open(file)
        self.histopath = pt_abseta
        self.correct_by_pt_abseta = {}
        self.key = self.file.Get(self.histopath)

    def __call__(self, pt, eta):
        if pt >= 120: pt = 115.
        self.correct_by_pt_abseta = self.key.GetBinContent(self.key.FindFixBin(pt, eta))
        return self.correct_by_pt_abseta


class MuonPOGCorrectionLooseIso2D(object):

    def __init__(self, file, MuonID, pt_abseta):
        self.file = ROOT.TFile.Open(file)
        if MuonID=='Tight':
            self.histopath = pt_abseta[2]
        if MuonID=='Medium':
            self.histopath = pt_abseta[1]
        if MuonID=='Loose':
            self.histopath = pt_abseta[0]
        self.correct_by_pt_abseta = {}
        self.key = self.file.Get(self.histopath)

    def __call__(self, pt, eta):
        if pt >= 119.: pt = 119.
        self.correct_by_pt_abseta = self.key.GetBinContent(self.key.FindFixBin(pt, eta))
        return self.correct_by_pt_abseta


class MuonPOGCorrectionTightIso2D(object):

    def __init__(self, file, MuonID, pt_abseta):
        self.file = ROOT.TFile.Open(file)
        if MuonID=='Tight':
            self.histopath = pt_abseta[1]
        if MuonID=='Medium':
            self.histopath = pt_abseta[0]
        self.correct_by_pt_abseta = {}
        self.key = self.file.Get(self.histopath)

    def __call__(self, pt, eta):
        if pt >= 119.: pt = 119.
        self.correct_by_pt_abseta = self.key.GetBinContent(self.key.FindFixBin(pt, eta))
        return self.correct_by_pt_abseta


class MuonPOGCorrectionTrig2D_weighted(object):

    def __init__(self, file, pt_abseta, lumi1, lumi2):
        self.file1 = ROOT.TFile.Open(file[0])
        self.file2 = ROOT.TFile.Open(file[1])
        self.lumi1 = lumi1
        self.lumi2 = lumi2
        self.histopath1 = pt_abseta[0]
        self.histopath2 = pt_abseta[1]
        self.correct_by_pt_abseta1 = {}
        self.correct_by_pt_abseta2 = {}
        self.correct_by_pt_abseta_weighted = {}
        self.key1 = self.file1.Get(self.histopath1)
        self.key2 = self.file2.Get(self.histopath2)

    def __call__(self, pt, eta):
        if pt >= 1200: pt = 1000.
        self.correct_by_pt_abseta1 = self.key1.GetBinContent(self.key1.FindFixBin(pt, eta))
        self.correct_by_pt_abseta2 = self.key2.GetBinContent(self.key2.FindFixBin(pt, eta))
        self.correct_by_pt_abseta_weighted = (self.lumi1 * self.correct_by_pt_abseta1 + self.lumi2 * self.correct_by_pt_abseta2)/(self.lumi1 + self.lumi2)
        return self.correct_by_pt_abseta_weighted


if __name__ == "__main__":
    make_muon_pog_PFTight_2018()
    make_muon_pog_PFMedium_2018()
    make_muon_pog_PFLoose_2018()
    make_muon_pog_TightIso_2018()
    make_muon_pog_LooseIso_2018()
    make_muon_pog_IsoMu24_2018()
