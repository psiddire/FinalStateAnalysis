
import array
from FinalStateAnalysis.Utilities.FileInPath import FileInPath
import ROOT
from rootpy.io import root_open
# MC distributions (built at bottom of file)
_MC_NVTX_DISTRIBUTIONS = {}

class NvtxWeight(object):
    def __init__(self, mctag):

        ROOT.TH1.AddDirectory(False)
        self.mc = None
        self.data = None
        
        file = ROOT.TFile.Open(_MC_NVTX_DISTRIBUTIONS['Data'])
        pu = file.Get('numOfVtx')
        self.data = pu.Clone()
        self.data.SetDirectory(0)
        file.Close()
        # Normalize
        self.data.Scale(1./self.data.Integral())
        #print 'scaling data'
        if not mctag in _MC_NVTX_DISTRIBUTIONS:
            raise KeyError("Unknown NVTX distribution %s, allowed: %s" %
                           (mctag, " ".join(_MC_NVTX_DISTRIBUTIONS.keys())))
        mc_file = ROOT.TFile.Open(_MC_NVTX_DISTRIBUTIONS[mctag])
        if not mc_file:
            raise IOError("Can't open %s MC file: %s" % (mctag, _MC_NVTX_DISTRIBUTIONS[mctag]))

        mc_base = mc_file.Get('numOfVtx')
        self.mc = mc_base.Clone()
        self.mc.SetName('numOfVtx_mc')
        
        # Make sure bins are consistent
        if not ROOT.TEfficiency.CheckBinning(self.mc, self.data):
            error = "Data and MC NVTX histograms do not have the same binning!\n"
            def print_bins(tag, x):
                return "%s: (%i, %0.1f, %0.1f)" % (
                    tag, x.GetNbinsX(), x.GetXaxis().GetXmin(),
                    x.GetXaxis().GetXmax())
            error += print_bins(mctag, self.mc)
            error += "\n"
            error += print_bins('data', self.data)
            raise ValueError(error)
       # Normalize MC
        self.mc.Scale(1./self.mc.Integral())
        ROOT.TH1.AddDirectory(True)
        
    def __call__(self, nvtx):
        '''
        Get the NVTX weight given the true number of interactions
        '''
        bin = self.data.FindBin(nvtx)
        data = self.data.GetBinContent(bin)
        mc = self.mc.GetBinContent(bin)
        if mc:
            return data/mc
        else:
            return 1.0

_MC_NVTX_DISTRIBUTIONS['Data'] = FileInPath("FinalStateAnalysis/TagAndProbe/data/nvtxData.root").full_path()
_MC_NVTX_DISTRIBUTIONS['GGHMT'] = FileInPath("FinalStateAnalysis/TagAndProbe/data/nvtxGG.root").full_path()
_MC_NVTX_DISTRIBUTIONS['VBFHMT'] = FileInPath("FinalStateAnalysis/TagAndProbe/data/nvtxVBF.root").full_path()
