'''

Ntuple branch template sets for bjet objects.

Each string is transformed into an expression on a FinalStateEvent object.

{object} should be replaced by an expression which evaluates to a pat::Muon
i.e. daughter(1) or somesuch.


'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

btagging = PSet(
	#Flavour
	objectJetFlavour ='{object}.hadronFlavour()',
)

pujets = PSet(
        objectIDTight='{object}.userFloat("idTight")',
        objectIDTightLepVeto='{object}.userFloat("idTightLepVeto")',
        objectIDLoose='{object}.userFloat("idLoose")',
	objectPUIDFullDiscriminant='{object}.userFloat("pileupJetId:fullDiscriminant")',
)












