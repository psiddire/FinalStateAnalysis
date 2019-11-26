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

el_Ele24_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/Electron_Run2018_Ele24.root'))
el_Ele32orEle35_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/Electron_Run2018_Ele32orEle35.root'))
el_Ele35_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/Electron_Run2018_Ele35.root'))
el_IdIso_2018 = GraphReaderEleSF(os.path.join(os.environ['fsa'], 'TagAndProbe/data/Electron_Run2018_IdIso.root'))

_DATA_DIR = os.path.join(os.environ['CMSSW_BASE'], 'src',
                         "FinalStateAnalysis", "TagAndProbe", "data")

_DATA_FILES = {
    '2018' : {
        'ID'   : os.path.join(_DATA_DIR, 'egammaEffi.txt_EGM2D_updatedAll_2018.root')
    }
}

def make_egamma_pog_electronID_2018():
    return EGammaPOGCorrection(
        _DATA_FILES['2018']['ID'],    
        "EGamma_SF2D"
    )


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
