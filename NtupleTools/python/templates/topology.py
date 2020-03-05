
'''

Ntuple branch template sets for topological variables (MT, etc)

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

mtToMET = PSet()

shiftedMtToMET = PSet()

# Variables based on pairs of objects
pairs = PSet(
    object1_object2_Mass = 'subcand({object1_idx}, {object2_idx}).get.mass',
    #object1_object2_Mt = 'subcand({object1_idx}, {object2_idx}).get.mt',
    #object1_object2_Pt = 'subcand({object1_idx}, {object2_idx}).get.pt',
    #object1_object2_Eta = 'subcand({object1_idx}, {object2_idx}).get.eta',
    #object1_object2_Phi = 'subcand({object1_idx}, {object2_idx}).get.phi',
    object1_object2_DR = 'dR({object1_idx}, {object2_idx})',
    #object1_object2_DPhi = 'dPhi({object1_idx}, {object2_idx})',
    #object1_object2_SS = 'likeSigned({object1_idx}, {object2_idx})',
    object1_object2_PZeta = 'pZeta({object1_idx}, {object2_idx})',
    object1_object2_PZetaVis = 'pZetaVis({object1_idx}, {object2_idx})',
    #object1_object2_CosThetaStar = 'abs(subcand({object1_idx}, {object2_idx}).get.daughterCosThetaStar(0))',

    ##Pairs + MET
    #object1_object2_ToMETDPhi_Ty1 = 'twoParticleDeltaPhiToMEt({object1_idx}, {object2_idx}, "type1")',
)

svfit = PSet(
    #object1_object2_SVfitMass = 'SVfit({object1_idx},{object2_idx}).at(0)',
    #object1_object2_SVfitPt = 'SVfit({object1_idx},{object2_idx}).at(1)',
    #object1_object2_SVfitEta = 'SVfit({object1_idx},{object2_idx}).at(2)',
    #object1_object2_SVfitPhi = 'SVfit({object1_idx},{object2_idx}).at(3)',
    #object1_object2_SVfitMET = 'SVfit({object1_idx},{object2_idx}).at(4)',
)

finalstate = PSet(
    LT = 'ht',
    charge = 'charge',
    Pt = 'pt',
    Eta = 'eta',
    Phi = 'phi',
    Mass = 'mass',
    Mt = 'mt',
    Ht = 'jetHt("pt>30 && abs(eta)<2.5")',
    MassError = '? hasUserFloat("cand_dM") ? userFloat("cand_dM") : -999',
    MassErrord1 = '? hasUserFloat("cand_dM_0") ? userFloat("cand_dM_0") : -999',
    MassErrord2 = '? hasUserFloat("cand_dM_1") ? userFloat("cand_dM_1") : -999',
    MassErrord3 = '? hasUserFloat("cand_dM_2") ? userFloat("cand_dM_2") : -999',
    MassErrord4 = '? hasUserFloat("cand_dM_3") ? userFloat("cand_dM_3") : -999',
)


vbf = PSet(
    vbfNJets20 = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).nJets',
    vbfNJets30 = 'vbfVariables("pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).nJets',
    vbfJetVeto30 = 'vbfVariables("pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).jets30',
    vbfJetVeto20 = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).jets20',
    vbfMass = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).mass',
    vbfMassWoNoisyJets = 'vbfVariables("(pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).mass',
    vbfDeta = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).deta',
    vbfj1eta = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).eta1',
    vbfj2eta = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).eta2',
    vbfj1pt = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).pt1',
    vbfj2pt = 'vbfVariables("pt > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | pt>50)", 0.5).pt2',
)


extraJet = PSet(
    objectPt = '? evt.jets.size()>{object_idx} ? {object}.pt() : -999',
    objectPtJESTotal_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesTotal+\').pt() : -999',
    objectPtJESTotal_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesTotal-\').pt() : -999',
    objectPtJESEta0to5_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta0to5+\').pt() : -999',
    objectPtJESEta0to5_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta0to5-\').pt() : -999',
    objectPtJESEta0to3_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta0to3+\').pt() : -999',
    objectPtJESEta0to3_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta0to3-\').pt() : -999',
    objectPtJESEta3to5_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta3to5+\').pt() : -999',
    objectPtJESEta3to5_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesEta3to5-\').pt() : -999',
    objectPtJESRelativeSample_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesRelativeSample+\').pt() : -999',
    objectPtJESRelativeSample_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesRelativeSample-\').pt() : -999',
    objectPtJESRelativeBal_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesRelativeBal+\').pt() : -999',
    objectPtJESRelativeBal_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesRelativeBal-\').pt() : -999',
    objectPtJESClosure_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesClosure+\').pt() : -999',
    objectPtJESClosure_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesClosure-\').pt() : -999',
    objectPtJESClosureNew_Up = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesClosureNew+\').pt() : -999',
    objectPtJESClosureNew_Down = '? evt.jets.size()>{object_idx} ? {object}.userCand(\'jesClosureNew-\').pt() : -999',
    objectEta = '? evt.jets.size()>{object_idx} ? {object}.eta() : -999',
    objectPhi = '? evt.jets.size()>{object_idx} ? {object}.phi() : -999',
    objectIDTight = '? evt.jets.size()>{object_idx} ? {object}.userFloat("idTight") : -999',
    objectIDTightLepVeto = '? evt.jets.size()>{object_idx} ? {object}.userFloat("idTightLepVeto") : -999',
    objectIDLoose = '? evt.jets.size()>{object_idx} ? {object}.userFloat("idLoose") : -999',
    objectPUMVA = '? evt.jets.size()>{object_idx} & {object}.pt()>20 & abs({object}.eta())<2.5 ? {object}.userFloat("pileupJetId:fullDiscriminant") : -999',
    objectBJetCISV = '? evt.jets.size()>{object_idx} & {object}.pt()>20 & abs({object}.eta())<2.5 ? {object}.bDiscriminator(\'pfCombinedInclusiveSecondaryVertexV2BJetTags\') : -999',
)


# Temporary variables for JES study
fullJES = PSet(

    vbfMassWoNoisyJets_JERUp = 'vbfVariables("(userCand(\'jer+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JERDown = 'vbfVariables("(userCand(\'jer-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JERUp = 'vetoJets(0.5, "(userCand(\'jer+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JERDown = 'vetoJets(0.5, "(userCand(\'jer-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt > 50)").size()',

    vbfMassWoNoisyJets_JetTotalUp = 'vbfVariables("(userCand(\'jesTotal+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesTotal+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesTotal+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetTotalDown = 'vbfVariables("(userCand(\'jesTotal-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesTotal-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesTotal-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetTotalUp = 'vetoJets(0.5, "(userCand(\'jesTotal+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesTotal+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesTotal+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetTotalDown = 'vetoJets(0.5, "(userCand(\'jesTotal-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesTotal-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesTotal-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetAbsoluteUp = 'vbfVariables("(userCand(\'jesAbsolute+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsolute+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsolute+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetAbsoluteDown = 'vbfVariables("(userCand(\'jesAbsolute-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsolute-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsolute-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetAbsoluteUp = 'vetoJets(0.5, "(userCand(\'jesAbsolute+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsolute+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsolute+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetAbsoluteDown = 'vetoJets(0.5, "(userCand(\'jesAbsolute-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsolute-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsolute-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetAbsoluteyearUp = 'vbfVariables("(userCand(\'jesAbsoluteyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsoluteyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsoluteyear+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetAbsoluteyearDown = 'vbfVariables("(userCand(\'jesAbsoluteyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsoluteyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsoluteyear-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetAbsoluteyearUp = 'vetoJets(0.5, "(userCand(\'jesAbsoluteyear+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsoluteyear+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsoluteyear+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetAbsoluteyearDown = 'vetoJets(0.5, "(userCand(\'jesAbsoluteyear-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesAbsoluteyear-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesAbsoluteyear-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetBBEC1Up = 'vbfVariables("(userCand(\'jesBBEC1+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetBBEC1Down = 'vbfVariables("(userCand(\'jesBBEC1-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetBBEC1Up = 'vetoJets(0.5, "(userCand(\'jesBBEC1+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetBBEC1Down = 'vetoJets(0.5, "(userCand(\'jesBBEC1-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetBBEC1yearUp = 'vbfVariables("(userCand(\'jesBBEC1year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1year+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetBBEC1yearDown = 'vbfVariables("(userCand(\'jesBBEC1year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1year-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetBBEC1yearUp = 'vetoJets(0.5, "(userCand(\'jesBBEC1year+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1year+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1year+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetBBEC1yearDown = 'vetoJets(0.5, "(userCand(\'jesBBEC1year-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesBBEC1year-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesBBEC1year-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetEC2Up = 'vbfVariables("(userCand(\'jesEC2+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetEC2Down = 'vbfVariables("(userCand(\'jesEC2-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetEC2Up = 'vetoJets(0.5, "(userCand(\'jesEC2+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetEC2Down = 'vetoJets(0.5, "(userCand(\'jesEC2-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetEC2yearUp = 'vbfVariables("(userCand(\'jesEC2year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2year+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetEC2yearDown = 'vbfVariables("(userCand(\'jesEC2year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2year-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetEC2yearUp = 'vetoJets(0.5, "(userCand(\'jesEC2year+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2year+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2year+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetEC2yearDown = 'vetoJets(0.5, "(userCand(\'jesEC2year-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesEC2year-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesEC2year-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetFlavorQCDUp = 'vbfVariables("(userCand(\'jesFlavorQCD+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesFlavorQCD+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesFlavorQCD+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetFlavorQCDDown = 'vbfVariables("(userCand(\'jesFlavorQCD-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesFlavorQCD-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesFlavorQCD-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetFlavorQCDUp = 'vetoJets(0.5, "(userCand(\'jesFlavorQCD+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesFlavorQCD+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesFlavorQCD+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetFlavorQCDDown = 'vetoJets(0.5, "(userCand(\'jesFlavorQCD-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesFlavorQCD-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesFlavorQCD-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetHFUp = 'vbfVariables("(userCand(\'jesHF+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHF+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHF+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetHFDown = 'vbfVariables("(userCand(\'jesHF-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHF-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHF-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetHFUp = 'vetoJets(0.5, "(userCand(\'jesHF+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHF+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHF+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetHFDown = 'vetoJets(0.5, "(userCand(\'jesHF-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHF-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHF-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetHFyearUp = 'vbfVariables("(userCand(\'jesHFyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHFyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHFyear+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetHFyearDown = 'vbfVariables("(userCand(\'jesHFyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHFyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHFyear-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetHFyearUp = 'vetoJets(0.5, "(userCand(\'jesHFyear+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHFyear+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHFyear+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetHFyearDown = 'vetoJets(0.5, "(userCand(\'jesHFyear-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesHFyear-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesHFyear-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetRelativeBalUp = 'vbfVariables("(userCand(\'jesRelativeBal+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetRelativeBalDown = 'vbfVariables("(userCand(\'jesRelativeBal-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetRelativeBalUpWoNoisyJets = 'vetoJets(0.5, "(userCand(\'jesRelativeBal+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetRelativeBalDownWoNoisyJets = 'vetoJets(0.5, "(userCand(\'jesRelativeBal-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal-\').pt > 50)").size()',
    vbfMassWoNoisyJets_JetRelativeSampleUp = 'vbfVariables("(userCand(\'jesRelativeSample+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample+\').pt() > 50)", 0.5).mass',
    vbfMassWoNoisyJets_JetRelativeSampleDown = 'vbfVariables("(userCand(\'jesRelativeSample-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample-\').pt() > 50)", 0.5).mass',
    jetVeto30WoNoisyJets_JetRelativeSampleUp = 'vetoJets(0.5, "(userCand(\'jesRelativeSample+\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample+\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample+\').pt > 50)").size()',
    jetVeto30WoNoisyJets_JetRelativeSampleDown = 'vetoJets(0.5, "(userCand(\'jesRelativeSample-\').pt > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample-\').pt > 30 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample-\').pt > 50)").size()',

    j1ptWoNoisyJets_JERUp = 'jetVariables("(userCand(\'jer+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JERDown = 'jetVariables("(userCand(\'jer-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt() > 50)", 0.5).at(0)',

    j1ptWoNoisyJets_JetAbsoluteUp = 'jetVariables("(userCand(\'jesJetAbsolute+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsolute+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsolute+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetAbsoluteDown = 'jetVariables("(userCand(\'jesJetAbsolute-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsolute-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsolute-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetAbsoluteyearUp = 'jetVariables("(userCand(\'jesJetAbsoluteyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsoluteyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsoluteyear+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetAbsoluteyearDown = 'jetVariables("(userCand(\'jesJetAbsoluteyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsoluteyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsoluteyear-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetBBEC1Up = 'jetVariables("(userCand(\'jesJetBBEC1+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetBBEC1Down = 'jetVariables("(userCand(\'jesJetBBEC1-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetBBEC1yearUp = 'jetVariables("(userCand(\'jesJetBBEC1year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1year+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetBBEC1yearDown = 'jetVariables("(userCand(\'jesJetBBEC1year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1year-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetEC2Up = 'jetVariables("(userCand(\'jesJetEC2+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetEC2Down = 'jetVariables("(userCand(\'jesJetEC2-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetEC2yearUp = 'jetVariables("(userCand(\'jesJetEC2year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2year+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetEC2yearDown = 'jetVariables("(userCand(\'jesJetEC2year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2year-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetFlavorQCDDown = 'jetVariables("(userCand(\'jesJetFlavorQCD-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetFlavorQCD-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetFlavorQCD-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetFlavorQCDUp = 'jetVariables("(userCand(\'jesJetFlavorQCD+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetFlavorQCD+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetFlavorQCD+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetHFUp = 'jetVariables("(userCand(\'jesJetHF+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHF+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHF+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetHFDown = 'jetVariables("(userCand(\'jesJetHF-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHF-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHF-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetHFyearUp = 'jetVariables("(userCand(\'jesJetHFyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHFyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHFyear+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetHFyearDown = 'jetVariables("(userCand(\'jesJetHFyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHFyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHFyear-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetRelativeBalUp = 'jetVariables("(userCand(\'jesRelativeBal+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetRelativeBalDown = 'jetVariables("(userCand(\'jesRelativeBal-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal-\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetRelativeSampleUp = 'jetVariables("(userCand(\'jesRelativeSample+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample+\').pt() > 50)", 0.5).at(0)',
    j1ptWoNoisyJets_JetRelativeSampleDown = 'jetVariables("(userCand(\'jesRelativeSample-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample-\').pt() > 50)", 0.5).at(0)',

    j2ptWoNoisyJets_JERUp = 'jetVariables("(userCand(\'jer+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JERDown = 'jetVariables("(userCand(\'jer-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jer-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jer-\').pt() > 50)", 0.5).at(10)',

    j2ptWoNoisyJets_JetAbsoluteUp = 'jetVariables("(userCand(\'jesJetAbsolute+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsolute+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsolute+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetAbsoluteDown = 'jetVariables("(userCand(\'jesJetAbsolute-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsolute-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsolute-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetAbsoluteyearUp = 'jetVariables("(userCand(\'jesJetAbsoluteyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsoluteyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsoluteyear+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetAbsoluteyearDown = 'jetVariables("(userCand(\'jesJetAbsoluteyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetAbsoluteyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetAbsoluteyear-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetBBEC1Up = 'jetVariables("(userCand(\'jesJetBBEC1+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetBBEC1Down = 'jetVariables("(userCand(\'jesJetBBEC1-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetBBEC1yearUp = 'jetVariables("(userCand(\'jesJetBBEC1year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1year+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetBBEC1yearDown = 'jetVariables("(userCand(\'jesJetBBEC1year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetBBEC1year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetBBEC1year-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetEC2Up = 'jetVariables("(userCand(\'jesJetEC2+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetEC2Down = 'jetVariables("(userCand(\'jesJetEC2-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetEC2yearUp = 'jetVariables("(userCand(\'jesJetEC2year+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2year+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2year+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetEC2yearDown = 'jetVariables("(userCand(\'jesJetEC2year-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetEC2year-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetEC2year-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetFlavorQCDUp = 'jetVariables("(userCand(\'jesJetFlavorQCD+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetFlavorQCD+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetFlavorQCD+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetFlavorQCDDown = 'jetVariables("(userCand(\'jesJetFlavorQCD-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetFlavorQCD-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetFlavorQCD-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetHFUp = 'jetVariables("(userCand(\'jesJetHF+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHF+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHF+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetHFDown = 'jetVariables("(userCand(\'jesJetHF-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHF-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHF-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetHFyearUp = 'jetVariables("(userCand(\'jesJetHFyear+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHFyear+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHFyear+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetHFyearDown = 'jetVariables("(userCand(\'jesJetHFyear-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesJetHFyear-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesJetHFyear-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetRelativeBalUp = 'jetVariables("(userCand(\'jesRelativeBal+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetRelativeBalDown = 'jetVariables("(userCand(\'jesRelativeBal-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeBal-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeBal-\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetRelativeSampleUp = 'jetVariables("(userCand(\'jesRelativeSample+\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample+\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample+\').pt() > 50)", 0.5).at(10)',
    j2ptWoNoisyJets_JetRelativeSampleDown = 'jetVariables("(userCand(\'jesRelativeSample-\').pt() > 50 | (abs(eta) < 2.65 | abs(eta) > 3.139)) & userCand(\'jesRelativeSample-\').pt() > 20 & abs(eta) < 4.7 & userFloat(\'idTight\') > 0.5 & (userInt(\'pileupJetId:fullId\')>3 | userCand(\'jesRelativeSample-\').pt() > 50)", 0.5).at(10)',

)


