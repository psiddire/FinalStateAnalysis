'''

Ntuple branch template sets for generic candidate objects.

Author: Evan K. Friis

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

kinematics = PSet(
    objectPt = '{object}.pt',
    objectEta = '{object}.eta',
    objectPhi = '{object}.phi',
    objectCharge = '{object}.charge',
    objectMass = '{object}.mass',
)

vertex_info = PSet(
    objectVZ = '{object}.vz',
    objectIP3D = 'getIP3D({object_idx})',
    objectIP3DErr = 'getIP3DErr({object_idx})', # uncertainty of IP3D
    objectSIP3D = 'getIP3D({object_idx}) / getIP3DErr({object_idx})',
    objectPVDZ = 'getPVDZ({object_idx})',
    objectPVDXY = 'getPVDXY({object_idx})',
    objectSIP2D = 'getIP2D({object_idx}) / getIP2DErr({object_idx})',
)

# The info about the associated pat::Jet
base_jet = PSet(
    objectJetPt = '{object}.userFloat("jetPt")',
    objectJetDR = '{object}.userFloat("jetDR")',
    objectJetBtag = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").bDiscriminator("") : -5',
    objectJetPFCISVBtag = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") : -5',
    objectJetEtaPhiSpread = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").constituentEtaPhiSpread() : -5',
    objectJetEtaEtaMoment = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").etaetaMoment() : -5',
    objectJetEtaPhiMoment = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").etaphiMoment() : -5',
    objectJetPhiPhiMoment = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").phiphiMoment() : -5',
    objectJetArea = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").jetArea() : -5',
    objectJetPartonFlavour = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").partonFlavour : -100',
    objectJetHadronFlavour = '? {object}.userCand("patJet").isNonnull ? '
        '{object}.userCand("patJet").hadronFlavour : -100',
)

