import os
import re
import ROOT
from graphReader import GraphReaderTrackingEta
from correctionloader import CorrectionLoader

_DATA_DIR = os.path.join(os.environ['CMSSW_BASE'], 'src',
                         "FinalStateAnalysis", "TagAndProbe", "data")

_DATA_FILES = {
    '2017ReReco' : {
        'IDnoIsoWP90' : os.path.join(_DATA_DIR, 'gammaEffi.txt_EGM2D_runBCDEF_passingMVA94Xwp90noiso.root'),
        'IDIsoWP90'   : os.path.join(_DATA_DIR, 'gammaEffi.txt_EGM2D_runBCDEF_passingMVA94Xwp90iso.root'),
        'IDnoIsoWP80' : os.path.join(_DATA_DIR, 'gammaEffi.txt_EGM2D_runBCDEF_passingMVA94Xwp80noiso.root'),
        'IDIsoWP80'   : os.path.join(_DATA_DIR, 'gammaEffi.txt_EGM2D_runBCDEF_passingMVA94Xwp80iso.root'),
        'Reco'        : os.path.join(_DATA_DIR, 'egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root'),
        },
    }


def make_electron_pog_IDnoIsoWP90_2017ReReco():
    return ElectronPOGCorrection2D_ReReco(
        _DATA_FILES['2017ReReco']['IDnoIsoWP90'],
        "EGamma_SF2D"
    )

def make_electron_pog_IDIsoWP90_2017ReReco():
    return ElectronPOGCorrection2D_ReReco(
        _DATA_FILES['2017ReReco']['IDIsoWP90'],
        "EGamma_SF2D"
    )

def make_electron_pog_IDnoIsoWP80_2017ReReco():
    return ElectronPOGCorrection2D_ReReco(
        _DATA_FILES['2017ReReco']['IDnoIsoWP80'],
        "EGamma_SF2D"
    )

def make_electron_pog_IDIsoWP80_2017ReReco():
    return ElectronPOGCorrection2D_ReReco(
        _DATA_FILES['2017ReReco']['IDIsoWP80'],
        "EGamma_SF2D"
    )

def make_electron_pog_Reco_2017ReReco():
    return ElectronPOGCorrection2D_ReReco(
        _DATA_FILES['2017ReReco']['Reco'],
        "EGamma_SF2D"
    )


class ElectronPOGCorrection2D_ReReco(object):

    def __init__(self, file, pt_abseta):
        self.filename = file
        self.file = ROOT.TFile.Open(file)
        self.histopath = pt_abseta
        self.correct_by_pt_abseta = {}
        self.key = self.file.Get(self.histopath)
      
    def __call__(self, pt, eta):
        if pt >= 499.: pt = 499.
        if pt < 20. : pt = 20.
        self.correct_by_pt_abseta = self.key.GetBinContent(self.key.FindFixBin(eta, pt))

        return self.correct_by_pt_abseta


if __name__ == "__main__":
    make_electron_pog_IDnoIsoWP90_2017ReReco()
    make_electron_pog_IDIsoWP90_2017ReReco()
    make_electron_pog_IDnoIsoWP80_2017ReReco()
    make_electron_pog_IDIsoWP80_2017ReReco()
    make_electron_pog_Reco_2017ReReco()
