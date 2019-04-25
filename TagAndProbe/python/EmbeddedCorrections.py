import os
import re
import ROOT
from graphReader import GraphReaderTrackingEta
from correctionloader import CorrectionLoader

_DATA_DIR = os.path.join(os.environ['CMSSW_BASE'], 'src',
                         "FinalStateAnalysis", "TagAndProbe", "data")

_DATA_FILES = {
    '2017ReReco' : {
        'DataTrg': os.path.join(_DATA_DIR, 'ZmmTP_Data_Fits_Trg_IsoMu27_pt_eta_bins.root'),
        'EmbTrg': os.path.join(_DATA_DIR, 'ZmmTP_Embedding_Fits_Trg_IsoMu27_pt_eta_bins.root'),
        'DataID': os.path.join(_DATA_DIR, 'ZmmTP_Data_Fits_ID_pt_eta_bins.root'),
        'EmbID': os.path.join(_DATA_DIR, 'ZmmTP_Embedding_Fits_ID_pt_eta_bins.root'),
        'DataIso': os.path.join(_DATA_DIR, 'ZmmTP_Data_Fits_Iso_pt_eta_bins.root'),
        'EmbIso': os.path.join(_DATA_DIR, 'ZmmTP_Embedding_Fits_Iso_pt_eta_bins.root'),
        },
    }


def embed_IsoMu27_2017ReReco():
    return EmbedCorrection_ReReco(
        _DATA_FILES['2017ReReco']['DataTrg'],
        _DATA_FILES['2017ReReco']['EmbTrg'],
        "Trg_IsoMu27_pt_eta_bins"
    )

def embed_ID_2017ReReco():
    return EmbedCorrection_ReReco(
        _DATA_FILES['2017ReReco']['DataID'],
        _DATA_FILES['2017ReReco']['EmbID'],
        "ID_pt_eta_bins"
    )

def embed_Iso_2017ReReco():
    return EmbedCorrection_ReReco(
        _DATA_FILES['2017ReReco']['DataIso'],
        _DATA_FILES['2017ReReco']['EmbIso'],
        "Iso_pt_eta_bins"
    )


class EmbedCorrection_ReReco(object):

    def __init__(self, file1, file2, pt_abseta):
        self.file1 = ROOT.TFile.Open(file1)
        self.file2 = ROOT.TFile.Open(file2)
        self.histopath = pt_abseta
        self.correct_by_pt_abseta = {}
        self.key1 = self.file1.Get(self.histopath)
        self.key2 = self.file2.Get(self.histopath)
      
    def __call__(self, pt, eta):
        if pt >= 999.: pt = 999.
        if pt < 20. : pt = 20.
        self.data_pt_abseta = self.key1.GetBinContent(self.key1.FindFixBin(pt, eta))
        self.embed_pt_abseta = self.key2.GetBinContent(self.key2.FindFixBin(pt, eta))
        if self.embed_pt_abseta <= 0:
            self.correct_by_pt_abseta = 0
        else:
            self.correct_by_pt_abseta = self.data_pt_abseta/self.embed_pt_abseta
        return self.correct_by_pt_abseta


if __name__ == "__main__":
    embed_IsoMu27_2017ReReco()
    embed_ID_2017ReReco()
    embed_Iso_2017ReReco()

