'''
Interface to official corrections from the EGamma  POG
===================================================
Adapted from MuonPOGcorrections.py
Author: Prasanna Kumar Siddireddy
https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPOG
'''

import os
import re
import ROOT
from graphReader import GraphReaderEleSF

# Trigger and ID
el_Ele24_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/Electron_Run2018_Ele24.root'))
el_Ele32orEle35_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/Electron_Run2018_Ele32orEle35.root'))
el_Ele35_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/Electron_Run2018_Ele35.root'))
el_IdIso_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/Electron_Run2018_IdIso.root'))

el_Ele25_2016 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2016/Electron_Run2016_legacy_Ele25.root'))
el_IdIso_2016 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2016/Electron_Run2016_legacy_IdIso.root'))

# Data Directories
_DATA_DIR_2018 = os.path.join(os.environ['CMSSW_BASE'], 'src',
                              "FinalStateAnalysis", "TagAndProbe", "data", "2018")

_DATA_DIR_2016 = os.path.join(os.environ['CMSSW_BASE'], 'src',
                              "FinalStateAnalysis", "TagAndProbe", "data", "2016")

# Data Files
_DATA_FILES = {
    '2018' : {
        'ID'   : os.path.join(_DATA_DIR_2018, 'egammaEffi.txt_EGM2D_updatedAll_2018.root')
    },
    '2016' : {
        'ID80'   : os.path.join(_DATA_DIR_2016, '2016LegacyReReco_ElectronMVA80_Fall17V2.root'),
        'ID80noiso'   : os.path.join(_DATA_DIR_2016, '2016LegacyReReco_ElectronMVA80noiso_Fall17V2.root'),
        'ID90'   : os.path.join(_DATA_DIR_2016, '2016LegacyReReco_ElectronMVA90_Fall17V2.root'),
        'ID90noiso'   : os.path.join(_DATA_DIR_2016, '2016LegacyReReco_ElectronMVA90noiso_Fall17V2.root')
    }
}

# 2018
def make_egamma_pog_electronID_2018():
    return EGammaPOGCorrection(
        _DATA_FILES['2018']['ID'],    
        "EGamma_SF2D"
    )

# 2016
def make_egamma_pog_electronID80_2016():
    return EGammaPOGCorrection(
        _DATA_FILES['2016']['ID80'],    
        "EGamma_SF2D"
    )

def make_egamma_pog_electronID80noiso_2016():
    return EGammaPOGCorrection(
        _DATA_FILES['2016']['ID80noiso'],    
        "EGamma_SF2D"
    )

def make_egamma_pog_electronID90_2016():
    return EGammaPOGCorrection(
        _DATA_FILES['2016']['ID90'],    
        "EGamma_SF2D"
    )

def make_egamma_pog_electronID90noiso_2016():
    return EGammaPOGCorrection(
        _DATA_FILES['2016']['ID90noiso'],    
        "EGamma_SF2D"
    )

# Class ID
class EGammaPOGCorrection(object):

    def __init__(self, file, eta_pt):
        self.filename = file
        self.file = ROOT.TFile.Open(file)
        self.histopath = eta_pt
        self.correct_by_eta_pt = {}
        self.key = self.file.Get(self.histopath)

    def __call__(self, eta, pt):
        if pt >= 500: pt = 500.
        self.correct_by_eta_pt = self.key.GetBinContent(self.key.FindFixBin(eta, pt))
        return self.correct_by_eta_pt

# Functions
if __name__ == "__main__":
    make_egamma_pog_electronID_2018()
    make_egamma_pog_electronID80_2016()
    make_egamma_pog_electronID80noiso_2016()
    make_egamma_pog_electronID90_2016()
    make_egamma_pog_electronID90noiso_2016()
