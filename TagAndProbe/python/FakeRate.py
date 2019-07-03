import os
import re
import ROOT
from graphReader import GraphReaderTrackingEta
from correctionloader import CorrectionLoader

_DATA_DIR = os.path.join(os.environ['CMSSW_BASE'], 'src',
                         "FinalStateAnalysis", "TagAndProbe", "data")

_DATA_FILES = {
    'Tau' : {
        'frEBDM0'   : os.path.join(_DATA_DIR, 'frEBDM0.root'),
        'frEBDM1'   : os.path.join(_DATA_DIR, 'frEBDM1.root'),
        'frEBDM10'   : os.path.join(_DATA_DIR, 'frEBDM10.root'),
        'frEEDM0'   : os.path.join(_DATA_DIR, 'frEBDM0.root'),
        'frEEDM1'   : os.path.join(_DATA_DIR, 'frEEDM1.root'),
        'frEEDM10'   : os.path.join(_DATA_DIR, 'frEEDM10.root')
        },
    'Muon' : {
        'frMuon'   : os.path.join(_DATA_DIR, 'frMuonPt.root')
        },
    'Electron' : {                                                                                                                                                                                                                                                  
        'frElectron' : os.path.join(_DATA_DIR, 'frElectronPt.root')                                                                                                                                                                       
        },
    }


def FakeRateWeight():
    return FakeRateWeight_ReReco(
        _DATA_FILES['Tau'],
        "fakerate"
    )


def FakeRateMuonWeight():
    return FakeRateMuonWeight_ReReco(
        _DATA_FILES['Muon'],
        "fakerate"
    )


def FakeRateElectronWeight():                                                                                                                                                                                                                               
    return FakeRateElectronWeight_ReReco(                                                                                                                                                                                                                
        _DATA_FILES['Electron'],                                                                                                                                                                                                                             
        "fakerate"                                                                                                                                                                                                                                                            
    ) 

class FakeRateWeight_ReReco(object):

    def __init__(self, files, frHisto):
        self.histopath = frHisto

        self.filenameEBDM0 = files['frEBDM0']
        self.fileEBDM0 = ROOT.TFile.Open(self.filenameEBDM0)
        self.keyEBDM0 = self.fileEBDM0.Get(self.histopath)

        self.filenameEBDM1 = files['frEBDM1']
        self.fileEBDM1 = ROOT.TFile.Open(self.filenameEBDM1)
        self.keyEBDM1 = self.fileEBDM1.Get(self.histopath)

        self.filenameEBDM10 = files['frEBDM10']
        self.fileEBDM10 = ROOT.TFile.Open(self.filenameEBDM10)
        self.keyEBDM10 = self.fileEBDM10.Get(self.histopath)

        self.filenameEEDM0 = files['frEEDM0']
        self.fileEEDM0 = ROOT.TFile.Open(self.filenameEEDM0)
        self.keyEEDM0 = self.fileEEDM0.Get(self.histopath)

        self.filenameEEDM1 = files['frEEDM1']
        self.fileEEDM1 = ROOT.TFile.Open(self.filenameEEDM1)
        self.keyEEDM1 = self.fileEEDM1.Get(self.histopath)

        self.filenameEEDM10 = files['frEEDM10']
        self.fileEEDM10 = ROOT.TFile.Open(self.filenameEEDM10)
        self.keyEEDM10 = self.fileEEDM10.Get(self.histopath)
      
    def __call__(self, pt, eta, DM, shift=''):
        f = {'' : 1}
        if pt < 30:
            bin = 1
        elif pt < 40:
            bin = 2
        elif pt < 50:
            bin = 3
        elif pt < 60:
            bin = 4
        elif pt < 70:
            bin = 5 
        elif pt < 90:
            bin = 6 
        elif pt < 120:
            bin = 7
        elif pt < 150:
            bin = 8
        else:
            bin = 9
        if abs(eta) < 1.5:
            if DM == 0:
                f = {'': self.keyEBDM0.GetEfficiency(bin),
                     'frUp': self.keyEBDM0.GetEfficiency(bin) + self.keyEBDM0.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEBDM0.GetEfficiency(bin) - self.keyEBDM0.GetEfficiencyErrorLow(bin)}
            elif DM == 1:
                f = {'': self.keyEBDM1.GetEfficiency(bin),
                     'frUp': self.keyEBDM1.GetEfficiency(bin) + self.keyEBDM1.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEBDM1.GetEfficiency(bin) - self.keyEBDM1.GetEfficiencyErrorLow(bin)}
            elif DM == 10:
                f = {'': self.keyEBDM10.GetEfficiency(bin),
                     'frUp': self.keyEBDM10.GetEfficiency(bin) + self.keyEBDM10.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEBDM10.GetEfficiency(bin) - self.keyEBDM10.GetEfficiencyErrorLow(bin)}
        else:
            if DM == 0:
                f = {'': self.keyEEDM0.GetEfficiency(bin),
                     'frUp': self.keyEEDM0.GetEfficiency(bin) + self.keyEEDM0.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEEDM0.GetEfficiency(bin) - self.keyEEDM0.GetEfficiencyErrorLow(bin)}
            elif DM == 1:
                f = {'': self.keyEEDM1.GetEfficiency(bin),
                     'frUp': self.keyEEDM1.GetEfficiency(bin) + self.keyEEDM1.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEEDM1.GetEfficiency(bin) - self.keyEEDM1.GetEfficiencyErrorLow(bin)}
            elif DM == 10:
                f = {'': self.keyEEDM10.GetEfficiency(bin),
                     'frUp': self.keyEEDM10.GetEfficiency(bin) + self.keyEEDM10.GetEfficiencyErrorUp(bin),
                     'frDown': self.keyEEDM10.GetEfficiency(bin) - self.keyEEDM10.GetEfficiencyErrorLow(bin)}
        if f[shift] >= 1 or f[shift] < 0:
            return 0
        return f[shift]/(1-f[shift])


class FakeRateMuonWeight_ReReco(object):

    def __init__(self, files, frHisto):
        self.filename = files['frMuon']
        self.file = ROOT.TFile.Open(self.filename)
        self.histopath = frHisto
        self.key = self.file.Get(self.histopath)

    def __call__(self, pt, shift=''):
        if pt < 10:
            bin = 1
        elif pt < 20:
            bin = 2
        elif pt < 30:
            bin = 3
        elif pt < 40:
            bin = 4
        elif pt < 50:
            bin = 5
        elif pt < 60:
            bin = 6
        else:
            bin = 1
        f = {'': self.key.GetEfficiency(bin),
             'frUp': self.key.GetEfficiency(bin) + self.key.GetEfficiencyErrorUp(bin),
             'frDown': self.key.GetEfficiency(bin) - self.key.GetEfficiencyErrorLow(bin)}
        if (f[shift] >= 1 or f[shift] < 0) or (f[''] >= 1 or f[''] < 0):
            return 0
        return (f[shift]/(1-f[shift]))


class FakeRateElectronWeight_ReReco(object):                                                                                                                                                                                                                        

    def __init__(self, files, frHisto):
        self.filename = files['frElectron']                                                                                                                                                                                                            
        self.file = ROOT.TFile.Open(self.filename)
        self.histopath = frHisto
        self.key = self.file.Get(self.histopath)
        
    def __call__(self, pt, shift=''):
        if pt < 30:
            bin = 1
        elif pt < 60:
            bin = 2
        elif pt < 90:
            bin = 3
        elif pt < 120:                                                                                                                                                                                                                                                 
            bin = 4
        else:
            bin = 5
        f = {'': self.key.GetEfficiency(bin),
             'frUp': self.key.GetEfficiency(bin) + self.key.GetEfficiencyErrorUp(bin),
             'frDown': self.key.GetEfficiency(bin) - self.key.GetEfficiencyErrorLow(bin)}

        if f[shift] >= 1 or f[shift] < 0:
            return 0
        return (f[shift]/(1-f[shift]))  


if __name__ == "__main__":
    FakeRateWeight()
    FakeRateMuonWeight()
    FakeRateElectronWeight()
