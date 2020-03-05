'''

Ntuple branch template sets for event level quantities

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

'''

import FWCore.ParameterSet.Config as cms
from FinalStateAnalysis.Utilities.cfgtools import PSet

# Vetos on extra stuff in the event
num = PSet(
    evt=cms.vstring('evt.eventDouble', 'l'), # use unsigned long long branch
    lumi=cms.vstring('evt.evtId.luminosityBlock', 'I'),  # use int branch
    run=cms.vstring('evt.evtId.run', 'I'),  # use int branch
    isdata=cms.vstring('evt.isRealData', 'I'),
    isembed=cms.vstring('evt.isEmbeddedSample', 'I'),
)

pileup = PSet(
    rho='evt.rho',
    #nvtx='evt.recoVertices.size',
    nvtx='evt.numberVertices',
    # Number of true PU events
    nTruePU='? evt.puInfo.size > 0 ? evt.puInfo[1].getTrueNumInteractions :-1',
)

pv_info = PSet(
    pvX='? evt.pv.isNonnull() ? evt.pv.x : -999',
    pvY='? evt.pv.isNonnull() ? evt.pv.y : -999',
    pvZ='? evt.pv.isNonnull() ? evt.pv.z : -999',
    pvDX='? evt.pv.isNonnull() ? evt.pv.xError : -999',
    pvDY='? evt.pv.isNonnull() ? evt.pv.yError : -999',
    pvDZ='? evt.pv.isNonnull() ? evt.pv.zError : -999',
    pvChi2='? evt.pv.isNonnull() ? evt.pv.chi2 : -999',
    pvndof='? evt.pv.isNonnull() ? evt.pv.ndof : -999',
    pvNormChi2='? evt.pv.isNonnull() ? evt.pv.normalizedChi2 : -999',
    pvIsValid=cms.vstring('? evt.pv.isNonnull() ? evt.pv.isValid : 0', 'I'),
    pvIsFake=cms.vstring('? evt.pv.isNonnull() ? evt.pv.isFake : 1', 'I'),
    pvRho = 'evt.pv.position.Rho',
)

met = PSet(
    #mvaMetEt       = 'evt.met("mvamet").et',
    #mvaMetPhi      = 'evt.met("mvamet").phi',
    #mvaMetCov00    = 'evt.met("mvamet").getSignificanceMatrix[0][0]',
    #mvaMetCov01    = 'evt.met("mvamet").getSignificanceMatrix[0][1]',
    #mvaMetCov10    = 'evt.met("mvamet").getSignificanceMatrix[1][0]',
    #mvaMetCov11    = 'evt.met("mvamet").getSignificanceMatrix[1][1]',
    type1_pfMetEt  = 'evt.met("pfmet").pt', 
    type1_pfMetPhi = 'evt.met("pfmet").phi',
    puppiMetEt  = 'evt.met("puppimet").pt',
    puppiMetPhi = 'evt.met("puppimet").phi',
    
    recoilDaught='getDaughtersRecoil().R()',
    recoilWithMet='getDaughtersRecoilWithMet().R()',
)

# these things break if you pass a shifted met to fsa
shiftedMet = PSet(

    type1_pfMet_shiftedPt_JERUp                 = 'evt.metShift("pfmet","pt","jer+")',
    type1_pfMet_shiftedPhi_JERUp                = 'evt.metShift("pfmet","phi","jer+")',
    type1_pfMet_shiftedPt_JERDown               = 'evt.metShift("pfmet","pt","jer-")',
    type1_pfMet_shiftedPhi_JERDown              = 'evt.metShift("pfmet","phi","jer-")',

    type1_pfMet_shiftedPt_JetTotalUp            = 'evt.metShift("pfmet","pt","jesTotal+")',
    type1_pfMet_shiftedPt_JetTotalDown          = 'evt.metShift("pfmet","pt","jesTotal-")',
    type1_pfMet_shiftedPt_JetEC2Up              = 'evt.metShift("pfmet","pt","jesEC2+")',
    type1_pfMet_shiftedPt_JetEC2Down            = 'evt.metShift("pfmet","pt","jesEC2-")',
    type1_pfMet_shiftedPt_JetAbsoluteUp         = 'evt.metShift("pfmet","pt","jesAbsolute+")',
    type1_pfMet_shiftedPt_JetAbsoluteDown       = 'evt.metShift("pfmet","pt","jesAbsolute-")',
    type1_pfMet_shiftedPt_JetAbsoluteyearUp     = 'evt.metShift("pfmet","pt","jesAbsoluteyear+")',
    type1_pfMet_shiftedPt_JetAbsoluteyearDown   = 'evt.metShift("pfmet","pt","jesAbsoluteyear-")',
    type1_pfMet_shiftedPt_JetFlavorQCDUp        = 'evt.metShift("pfmet","pt","jesFlavorQCD+")',
    type1_pfMet_shiftedPt_JetFlavorQCDDown      = 'evt.metShift("pfmet","pt","jesFlavorQCD-")',
    type1_pfMet_shiftedPt_JetBBEC1Up            = 'evt.metShift("pfmet","pt","jesBBEC1+")',
    type1_pfMet_shiftedPt_JetBBEC1Down          = 'evt.metShift("pfmet","pt","jesBBEC1-")',
    type1_pfMet_shiftedPt_JetHFUp               = 'evt.metShift("pfmet","pt","jesHF+")',
    type1_pfMet_shiftedPt_JetHFDown             = 'evt.metShift("pfmet","pt","jesHF-")',
    type1_pfMet_shiftedPt_JetBBEC1yearUp        = 'evt.metShift("pfmet","pt","jesBBEC1year+")',
    type1_pfMet_shiftedPt_JetBBEC1yearDown      = 'evt.metShift("pfmet","pt","jesBBEC1year-")',
    type1_pfMet_shiftedPt_JetEC2yearUp          = 'evt.metShift("pfmet","pt","jesEC2year+")',
    type1_pfMet_shiftedPt_JetEC2yearDown        = 'evt.metShift("pfmet","pt","jesEC2year-")',
    type1_pfMet_shiftedPt_JetHFyearUp           = 'evt.metShift("pfmet","pt","jesHFyear+")',
    type1_pfMet_shiftedPt_JetHFyearDown         = 'evt.metShift("pfmet","pt","jesHFyear-")',
    type1_pfMet_shiftedPt_JetRelativeBalUp      = 'evt.metShift("pfmet","pt","jesRelativeBal+")',
    type1_pfMet_shiftedPt_JetRelativeBalDown    = 'evt.metShift("pfmet","pt","jesRelativeBal-")',
    type1_pfMet_shiftedPt_JetRelativeSampleUp   = 'evt.metShift("pfmet","pt","jesRelativeSample+")',
    type1_pfMet_shiftedPt_JetRelativeSampleDown = 'evt.metShift("pfmet","pt","jesRelativeSample-")',
    type1_pfMet_shiftedPhi_JetTotalUp           = 'evt.metShift("pfmet","phi","jesTotal+")',
    type1_pfMet_shiftedPhi_JetTotalDown         = 'evt.metShift("pfmet","phi","jesTotal-")',
    type1_pfMet_shiftedPhi_JetEC2Up             = 'evt.metShift("pfmet","phi","jesEC2+")',
    type1_pfMet_shiftedPhi_JetEC2Down           = 'evt.metShift("pfmet","phi","jesEC2-")',
    type1_pfMet_shiftedPhi_JetAbsoluteUp        = 'evt.metShift("pfmet","phi","jesAbsolute+")',
    type1_pfMet_shiftedPhi_JetAbsoluteDown      = 'evt.metShift("pfmet","phi","jesAbsolute-")',
    type1_pfMet_shiftedPhi_JetAbsoluteyearUp    = 'evt.metShift("pfmet","phi","jesAbsoluteyear+")',
    type1_pfMet_shiftedPhi_JetAbsoluteyearDown  = 'evt.metShift("pfmet","phi","jesAbsoluteyear-")',
    type1_pfMet_shiftedPhi_JetFlavorQCDUp       = 'evt.metShift("pfmet","phi","jesFlavorQCD+")',
    type1_pfMet_shiftedPhi_JetFlavorQCDDown     = 'evt.metShift("pfmet","phi","jesFlavorQCD-")',
    type1_pfMet_shiftedPhi_JetBBEC1Up           = 'evt.metShift("pfmet","phi","jesBBEC1+")',
    type1_pfMet_shiftedPhi_JetBBEC1Down         = 'evt.metShift("pfmet","phi","jesBBEC1-")',
    type1_pfMet_shiftedPhi_JetHFUp              = 'evt.metShift("pfmet","phi","jesHF+")',
    type1_pfMet_shiftedPhi_JetHFDown            = 'evt.metShift("pfmet","phi","jesHF-")',
    type1_pfMet_shiftedPhi_JetBBEC1yearUp       = 'evt.metShift("pfmet","phi","jesBBEC1year+")',
    type1_pfMet_shiftedPhi_JetBBEC1yearDown     = 'evt.metShift("pfmet","phi","jesBBEC1year-")',
    type1_pfMet_shiftedPhi_JetEC2yearUp         = 'evt.metShift("pfmet","phi","jesEC2year+")',
    type1_pfMet_shiftedPhi_JetEC2yearDown       = 'evt.metShift("pfmet","phi","jesEC2year-")',
    type1_pfMet_shiftedPhi_JetHFyearUp          = 'evt.metShift("pfmet","phi","jesHFyear+")',
    type1_pfMet_shiftedPhi_JetHFyearDown        = 'evt.metShift("pfmet","phi","jesHFyear-")',
    type1_pfMet_shiftedPhi_JetRelativeBalUp     = 'evt.metShift("pfmet","phi","jesRelativeBal+")',
    type1_pfMet_shiftedPhi_JetRelativeBalDown   = 'evt.metShift("pfmet","phi","jesRelativeBal-")',
    type1_pfMet_shiftedPhi_JetRelativeSampleUp  = 'evt.metShift("pfmet","phi","jesRelativeSample+")',
    type1_pfMet_shiftedPhi_JetRelativeSampleDown= 'evt.metShift("pfmet","phi","jesRelativeSample-")',

    type1_pfMet_shiftedPt_UesHCALUp             = 'evt.metShift("pfmet","pt","metSystUesHCAL+")',
    type1_pfMet_shiftedPt_UesHCALDown           = 'evt.metShift("pfmet","pt","metSystUesHCAL-")',
    type1_pfMet_shiftedPt_UesHFUp               = 'evt.metShift("pfmet","pt","metSystUesHF+")',
    type1_pfMet_shiftedPt_UesHFDown             = 'evt.metShift("pfmet","pt","metSystUesHF-")',
    type1_pfMet_shiftedPt_UesECALUp             = 'evt.metShift("pfmet","pt","metSystUesECAL+")',
    type1_pfMet_shiftedPt_UesECALDown           = 'evt.metShift("pfmet","pt","metSystUesECAL-")',
    type1_pfMet_shiftedPt_UesCHARGEDUp          = 'evt.metShift("pfmet","pt","metSystUesCHARGED+")',
    type1_pfMet_shiftedPt_UesCHARGEDDown        = 'evt.metShift("pfmet","pt","metSystUesCHARGED-")',

    type1_pfMet_shiftedPhi_UesHCALUp            = 'evt.metShift("pfmet","phi","metSystUesHCAL+")',
    type1_pfMet_shiftedPhi_UesHCALDown          = 'evt.metShift("pfmet","phi","metSystUesHCAL-")',
    type1_pfMet_shiftedPhi_UesHFUp              = 'evt.metShift("pfmet","phi","metSystUesHF+")',
    type1_pfMet_shiftedPhi_UesHFDown            = 'evt.metShift("pfmet","phi","metSystUesHF-")',
    type1_pfMet_shiftedPhi_UesECALUp            = 'evt.metShift("pfmet","phi","metSystUesECAL+")',
    type1_pfMet_shiftedPhi_UesECALDown          = 'evt.metShift("pfmet","phi","metSystUesECAL-")',
    type1_pfMet_shiftedPhi_UesCHARGEDUp         = 'evt.metShift("pfmet","phi","metSystUesCHARGED+")',
    type1_pfMet_shiftedPhi_UesCHARGEDDown       = 'evt.metShift("pfmet","phi","metSystUesCHARGED-")',

    #raw_pfMetEt    = 'evt.met("pfmet").uncorPt',
    #raw_pfMetPhi   = 'evt.met("pfmet").uncorPhi',

    # new systematics
    type1_pfMet_shiftedPt_JetResUp              = 'evt.metShift("pfmet","pt","jres+")',
    type1_pfMet_shiftedPt_JetResDown            = 'evt.metShift("pfmet","pt","jres-")',
    type1_pfMet_shiftedPhi_JetResUp             = 'evt.metShift("pfmet","phi","jres+")',
    type1_pfMet_shiftedPhi_JetResDown           = 'evt.metShift("pfmet","phi","jres-")',

    type1_pfMet_shiftedPt_JetEnUp               = 'evt.metShift("pfmet","pt","jes+")',
    type1_pfMet_shiftedPt_JetEnDown             = 'evt.metShift("pfmet","pt","jes-")',
    type1_pfMet_shiftedPhi_JetEnUp              = 'evt.metShift("pfmet","phi","jes+")',
    type1_pfMet_shiftedPhi_JetEnDown            = 'evt.metShift("pfmet","phi","jes-")',

    type1_pfMet_shiftedPhi_UnclusteredEnDown    = 'evt.metShift("pfmet","phi","ues-")',
    type1_pfMet_shiftedPhi_UnclusteredEnUp      = 'evt.metShift("pfmet","phi","ues+")',
    type1_pfMet_shiftedPt_UnclusteredEnDown     = 'evt.metShift("pfmet","pt","ues-")',
    type1_pfMet_shiftedPt_UnclusteredEnUp       = 'evt.metShift("pfmet","pt","ues+")',

)

metShiftsForFullJES = PSet(
    type1_pfMet_shiftedPt_JetResUp              = 'evt.metShift("pfmet","pt","jres+")',
    type1_pfMet_shiftedPt_JetResDown            = 'evt.metShift("pfmet","pt","jres-")',
    type1_pfMet_shiftedPhi_JetResUp             = 'evt.metShift("pfmet","phi","jres+")',
    type1_pfMet_shiftedPhi_JetResDown           = 'evt.metShift("pfmet","phi","jres-")',

    type1_pfMet_shiftedPt_JetEnUp               = 'evt.metShift("pfmet","pt","jes+")',
    type1_pfMet_shiftedPt_JetEnDown             = 'evt.metShift("pfmet","pt","jes-")',
    type1_pfMet_shiftedPhi_JetEnUp              = 'evt.metShift("pfmet","phi","jes+")',
    type1_pfMet_shiftedPhi_JetEnDown            = 'evt.metShift("pfmet","phi","jes-")',

    type1_pfMet_shiftedPhi_UnclusteredEnDown    = 'evt.metShift("pfmet","phi","ues-")',
    type1_pfMet_shiftedPhi_UnclusteredEnUp      = 'evt.metShift("pfmet","phi","ues+")',
    type1_pfMet_shiftedPt_UnclusteredEnDown     = 'evt.metShift("pfmet","pt","ues-")',
    type1_pfMet_shiftedPt_UnclusteredEnUp       = 'evt.metShift("pfmet","pt","ues+")',
)

gen = PSet(
    # Process ID used to simulate in Pythia
    processID='evt.genEventInfo.signalProcessID',
    isZtautau='evt.findDecay(23,15)',
    isGtautau='evt.findDecay(22,15)',
    isWtaunu='evt.findDecay(24,15)',
    isWmunu='evt.findDecay(24,13)',
    isWenu='evt.findDecay(24,11)',
    isZmumu='evt.findDecay(23,13)',
    isZee='evt.findDecay(23,11)',

    genHTT='evt.genHTT',
    NUP='evt.lesHouches.NUP',
    EmbPtWeight='evt.generatorFilter.filterEfficiency',
    GenWeight='? evt.genEventInfo.weights().size>0 ? evt.genEventInfo.weights()[0] : 0',
)

tauSpinner = PSet(
    tauSpinnerWeight = 'evt.weight("tauSpinnerWeight")'
)


