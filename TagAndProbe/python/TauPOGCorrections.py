'''
Interface to official corrections from the Tau POG
===================================================
Adapted from MuonPOGcorrections.py
Author: Prasanna Kumar Siddireddy
https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPOG
'''

import os
import re
import ROOT
from graphReader import GraphReaderFES

# Fake Energy Scale
Tau_FES_2018 = GraphReaderFES(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2018/TauFES_eta-dm_DeepTau2017v2p1VSe_2018ReReco.root'))

Tau_FES_2017 = GraphReaderFES(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2017/TauFES_eta-dm_DeepTau2017v2p1VSe_2017ReReco.root'))

Tau_FES_2016 = GraphReaderFES(os.path.join(os.environ['fsa'], 'TagAndProbe/data/2016/TauFES_eta-dm_DeepTau2017v2p1VSe_2016Legacy.root'))

# Data Directories
_DATA_DIR_2018 = os.path.join(os.environ['CMSSW_BASE'], 'src',
                              "FinalStateAnalysis", "TagAndProbe", "data", "2018")

_DATA_DIR_2017 = os.path.join(os.environ['CMSSW_BASE'], 'src',
                              "FinalStateAnalysis", "TagAndProbe", "data", "2017")

_DATA_DIR_2016 = os.path.join(os.environ['CMSSW_BASE'], 'src',
                              "FinalStateAnalysis", "TagAndProbe", "data", "2016")

# Data Files
_DATA_FILES = {
    '2018' : {
        'tauvse'        : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_DeepTau2017v2p1VSe_2018ReReco.root'),
        'antiele'       : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_antiEleMVA6_2018ReReco.root'),
        'tauvsmu'       : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_DeepTau2017v2p1VSmu_2018ReReco.root'),
        'antimu'        : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_antiMu3_2018ReReco.root'),
        'tauvsjet'      : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2018ReReco.root'),
        'tauvsjetEMB'   : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2018ReReco_EMB.root'),
        'mva'           : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_MVAoldDM2017v2_2018ReReco.root'),
        'tauvsjetdm'    : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2018ReReco.root'),
        'tauvsjetdmEMB' : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2018ReReco_EMB.root'),
        'mvadm'         : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_MVAoldDM2017v2_2018ReReco.root'),
        'es'            : os.path.join(_DATA_DIR_2017, 'TauES_dm_MVAoldDM2017v2_2018ReReco.root'),
    },
    '2017' : {
        'tauvse'        : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_DeepTau2017v2p1VSe_2017ReReco.root'),
        'antiele'       : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_antiEleMVA6_2017ReReco.root'),
        'tauvsmu'       : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_DeepTau2017v2p1VSmu_2017ReReco.root'),
        'antimu'        : os.path.join(_DATA_DIR_2017, 'TauID_SF_eta_antiMu3_2017ReReco.root'),
        'tauvsjet'      : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2017ReReco.root'),
        'tauvsjetEMB'   : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2017ReReco_EMB.root'),
        'mva'           : os.path.join(_DATA_DIR_2017, 'TauID_SF_pt_MVAoldDM2017v2_2017ReReco.root'),
        'tauvsjetdm'    : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root'),
        'tauvsjetdmEMB' : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root'),
        'mvadm'         : os.path.join(_DATA_DIR_2017, 'TauID_SF_dm_MVAoldDM2017v2_2017ReReco.root'),
        'es'            : os.path.join(_DATA_DIR_2017, 'TauES_dm_MVAoldDM2017v2_2017ReReco.root'),
    },
    '2016' : {
        'tauvse'        : os.path.join(_DATA_DIR_2016, 'TauID_SF_eta_DeepTau2017v2p1VSe_2016Legacy.root'),
        'antiele'       : os.path.join(_DATA_DIR_2016, 'TauID_SF_eta_antiEleMVA6_2016Legacy.root'),
        'tauvsmu'       : os.path.join(_DATA_DIR_2016, 'TauID_SF_eta_DeepTau2017v2p1VSmu_2016Legacy.root'),
        'antimu'        : os.path.join(_DATA_DIR_2016, 'TauID_SF_eta_antiMu3_2016Legacy.root'),
        'tauvsjet'      : os.path.join(_DATA_DIR_2016, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2016Legacy.root'),
        'tauvsjetEMB'   : os.path.join(_DATA_DIR_2016, 'TauID_SF_pt_DeepTau2017v2p1VSjet_2016Legacy_EMB.root'),
        'mva'           : os.path.join(_DATA_DIR_2016, 'TauID_SF_pt_MVAoldDM2017v2_2016Legacy.root'),
        'tauvsjetdm'    : os.path.join(_DATA_DIR_2016, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2016Legacy.root'),
        'tauvsjetdmEMB' : os.path.join(_DATA_DIR_2016, 'TauID_SF_dm_DeepTau2017v2p1VSjet_2016Legacy_EMB.root'),
        'mvadm'         : os.path.join(_DATA_DIR_2016, 'TauID_SF_dm_MVAoldDM2017v2_2016Legacy.root'),
        'es'            : os.path.join(_DATA_DIR_2016, 'TauES_dm_MVAoldDM2017v2_2016Legacy.root'),
    }
}

# 2018
def make_tau_pog_DeepTauVSe_2018(WP):
    return AgainstCorrection(
        _DATA_FILES['2018']['tauvse'], WP
    )
def make_tau_pog_againstElectron_2018(WP):
    return AgainstCorrection(
        _DATA_FILES['2018']['antiele'], WP
    )
def make_tau_pog_DeepTauVSmu_2018(WP):
    return AgainstCorrection(
        _DATA_FILES['2018']['tauvsmu'], WP
    )
def make_tau_pog_againstMuon_2018(WP):
    return AgainstCorrection(
        _DATA_FILES['2018']['antimu'], WP
    )
def make_tau_pog_DeepTauVSjet_2018(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2018']['tauvsjet'], WP
    )
def make_tau_pog_DeepTauVSjet_EMB_2018(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2018']['tauvsjetEMB'], WP
    )
def make_tau_pog_MVA_2018(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2018']['mva'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_2018(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2018']['tauvsjetdm'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_EMB_2018(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2018']['tauvsjetdmEMB'], WP
    )
def make_tau_pog_MVA_dm_2018(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2018']['mvadm'], WP
    )
def make_tau_pog_ES_2018():
    return ESCorrection(
        _DATA_FILES['2018']['es']
    )
# 2017
def make_tau_pog_DeepTauVSe_2017(WP):
    return AgainstCorrection(
        _DATA_FILES['2017']['tauvse'], WP
    )
def make_tau_pog_againstElectron_2017(WP):
    return AgainstCorrection(
        _DATA_FILES['2017']['antiele'], WP
    )
def make_tau_pog_DeepTauVSmu_2017(WP):
    return AgainstCorrection(
        _DATA_FILES['2017']['tauvsmu'], WP
    )
def make_tau_pog_againstMuon_2017(WP):
    return AgainstCorrection(
        _DATA_FILES['2017']['antimu'], WP
    )
def make_tau_pog_DeepTauVSjet_2017(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2017']['tauvsjet'], WP
    )
def make_tau_pog_DeepTauVSjet_EMB_2017(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2017']['tauvsjetEMB'], WP
    )
def make_tau_pog_MVA_2017(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2017']['mva'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_2017(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2017']['tauvsjetdm'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_EMB_2017(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2017']['tauvsjetdmEMB'], WP
    )
def make_tau_pog_MVA_dm_2017(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2017']['mvadm'], WP
    )
def make_tau_pog_ES_2017():
    return ESCorrection(
        _DATA_FILES['2017']['es']
    )
# 2016
def make_tau_pog_DeepTauVSe_2016(WP):
    return AgainstCorrection(
        _DATA_FILES['2016']['tauvse'], WP
    )
def make_tau_pog_againstElectron_2016(WP):
    return AgainstCorrection(
        _DATA_FILES['2016']['antiele'], WP
    )
def make_tau_pog_DeepTauVSmu_2016(WP):
    return AgainstCorrection(
        _DATA_FILES['2016']['tauvsmu'], WP
    )
def make_tau_pog_againstMuon_2016(WP):
    return AgainstCorrection(
        _DATA_FILES['2016']['antimu'], WP
    )
def make_tau_pog_DeepTauVSjet_2016(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2016']['tauvsjet'], WP
    )
def make_tau_pog_DeepTauVSjet_EMB_2016(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2016']['tauvsjetEMB'], WP
    )
def make_tau_pog_MVA_2016(WP):
    return AgainstJetCorrection(
        _DATA_FILES['2016']['mva'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_2016(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2016']['tauvsjetdm'], WP
    )
def make_tau_pog_DeepTauVSjet_dm_EMB_2016(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2016']['tauvsjetdmEMB'], WP
    )
def make_tau_pog_MVA_dm_2016(WP):
    return AgainstJetCorrectionDM(
        _DATA_FILES['2016']['mvadm'], WP
    )
def make_tau_pog_ES_2016():
    return ESCorrection(
        _DATA_FILES['2016']['es']
    )

# Class ID
class AgainstCorrection(object):
    def __init__(self, file, WP):
        self.file = ROOT.TFile.Open(file)
        self.key = self.file.Get(WP)
    def __call__(self, eta):
        self.out = self.key.GetBinContent(self.key.FindFixBin(abs(eta)))
        self.out_up = self.key.GetBinContent(self.key.FindFixBin(abs(eta))) + self.key.GetBinErrorUp(self.key.FindFixBin(abs(eta)))
        self.out_down = self.key.GetBinContent(self.key.FindFixBin(abs(eta))) - self.key.GetBinErrorLow(self.key.FindFixBin(abs(eta)))
        return (self.out, self.out_up, self.out_down)

class AgainstJetCorrection(object):
    def __init__(self, file, WP):
        self.file = ROOT.TFile.Open(file)
        self.key1 = self.file.Get(WP+'_cent')
        self.key2 = self.file.Get(WP+'_up')
        self.key3 = self.file.Get(WP+'_down')
    def __call__(self, pt):
        return (self.key1.Eval(pt), self.key2.Eval(pt), self.key3.Eval(pt))

class AgainstJetCorrectionDM(object):
    def __init__(self, file, WP):
        self.file = ROOT.TFile.Open(file)
        self.key = self.file.Get(WP)
    def __call__(self, dm):
        self.out = self.key.GetBinContent(self.key.FindFixBin(dm))
        self.out_up = self.key.GetBinContent(self.key.FindFixBin(dm)) + self.key.GetBinErrorUp(self.key.FindFixBin(dm))
        self.out_down = self.key.GetBinContent(self.key.FindFixBin(dm)) - self.key.GetBinErrorLow(self.key.FindFixBin(dm))
        return (self.out, self.out_up, self.out_down)

class ESCorrection(object):
    def __init__(self, file):
        self.file = ROOT.TFile.Open(file)
        self.key = self.file.Get('tes')
    def __call__(self, dm):
        self.out = self.key.GetBinContent(self.key.FindFixBin(dm))
        self.out_up = self.key.GetBinContent(self.key.FindFixBin(dm)) + self.key.GetBinErrorUp(self.key.FindFixBin(dm))
        self.out_down = self.key.GetBinContent(self.key.FindFixBin(dm)) - self.key.GetBinErrorLow(self.key.FindFixBin(dm))
        return (self.out, self.out_up, self.out_down)

# Functions
if __name__ == "__main__":
    make_tau_pog_DeepTauVSe_2018()
    make_tau_pog_againstElectron_2018()
    make_tau_pog_DeepTauVSmu_2018()
    make_tau_pog_againstMuon_2018()
    make_tau_pog_DeepTauVSjet_2018()
    make_tau_pog_DeepTauVSjet_EMB_2018()
    make_tau_pog_MVA_2018()
    make_tau_pog_DeepTauVSjet_dm_2018()
    make_tau_pog_DeepTauVSjet_dm_EMB_2018()
    make_tau_pog_MVA_dm_2018()
    make_tau_pog_ES_2018()
    make_tau_pog_DeepTauVSe_2017()
    make_tau_pog_againstElectron_2017()
    make_tau_pog_DeepTauVSmu_2017()
    make_tau_pog_againstMuon_2017()
    make_tau_pog_DeepTauVSjet_2017()
    make_tau_pog_DeepTauVSjet_EMB_2017()
    make_tau_pog_MVA_2017()
    make_tau_pog_DeepTauVSjet_dm_2017()
    make_tau_pog_DeepTauVSjet_dm_EMB_2017()
    make_tau_pog_MVA_dm_2017()
    make_tau_pog_ES_2017()
    make_tau_pog_DeepTauVSe_2016()
    make_tau_pog_againstElectron_2016()
    make_tau_pog_DeepTauVSmu_2016()
    make_tau_pog_againstMuon_2016()
    make_tau_pog_DeepTauVSjet_2016()
    make_tau_pog_DeepTauVSjet_EMB_2016()
    make_tau_pog_MVA_2016()
    make_tau_pog_DeepTauVSjet_dm_2016()
    make_tau_pog_DeepTauVSjet_dm_EMB_2016()
    make_tau_pog_MVA_dm_2016()
    make_tau_pog_ES_2016()
