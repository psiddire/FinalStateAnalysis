'''

Base class which makes nice plots.

Author: Evan K. Friis, UW

'''

import fnmatch
import re
import os
import rootpy.plotting.views as views
import rootpy.plotting as plotting
from FinalStateAnalysis.MetaData.data_views import data_views
from FinalStateAnalysis.PlotTools.RebinView import RebinView
from FinalStateAnalysis.PlotTools.SystematicsView     import SystematicsView
from FinalStateAnalysis.Utilities.struct import struct
import FinalStateAnalysis.Utilities.prettyjson as prettyjson
import ROOT
from ROOT import gStyle

#gStyle.SetOptTitle(0)
#gStyle.SetTitleFontSize(0.08)

_original_draw = plotting.Legend.Draw

def _monkey_patch_legend_draw(self, *args, **kwargs):
    ''' Make a plotting.legend look nice '''
    self.SetBorderSize(0)
    _original_draw(self, *args, **kwargs)
plotting.Legend.Draw = _monkey_patch_legend_draw

class Plotter(object):
    def __init__(self, files, lumifiles, outputdir, blinder=None, forceLumi=-1):
        ''' Initialize the Plotter object

        Files should be a list of SAMPLE_NAME.root files.
        Lumifiles should contain floats giving the effective luminosity of
        each of the files.

        If [blinder] is not None, it will be applied to the data view.
        '''
        self.outputdir = outputdir
        self.views = data_views(files, lumifiles, forceLumi)
        self.canvas = plotting.Canvas(name='Canvas', title='Canvas')
        self.canvas.SetLogy(True)
        self.canvas.cd()
        self.pad = plotting.Pad(0., 0., 1., 1.)
        self.pad.Draw()
        self.pad.cd()
        self.lower_pad = None
        if blinder:
            self.views['data']['unblinded_view'] = self.views['data']['view']
            self.views['data']['view'] = blinder(self.views['data']['view'])
        self.data = self.views['data']['view']
        self.keep = []
        self.mc_samples = [
            'Zjets_M50',
            'WplusJets_madgraph',
            'TTplusJets_madgraph',
            'WZ*',
            'ZZ*',
            'WW*',
        ]
        file_to_map = filter(lambda x: 'data_' in x, self.views.keys())[0]
        if not file_to_map: #no data here!
            file_to_map = self.views.keys()[0]
        #else:
        #    file_to_map = file_to_map[0]
        #from pdb import set_trace; set_trace()
        #self.file_dir_structure = Plotter.map_dir_structure( self.views[file_to_map]['file'] )

    @staticmethod
    def map_dir_structure(directory, dirName=''):
        objects = [(i.GetName(), i.GetClassName()) for i in directory.GetListOfKeys()]
        ret     = []
        for keyname, keyclass in objects:
            if keyclass.startswith('TDirectory'):
                subdirName = os.path.join(dirName,keyname)
                ret.append(subdirName)
                ret.extend(Plotter.map_dir_structure(directory.Get(keyname), subdirName))
        return ret

    @staticmethod
    def rebin_view(x, rebin):
        ''' Make a view which rebins histograms '''
        output = RebinView(x, rebin)
        return output

    @staticmethod
    def parse_formula(fcn_string, pars_string):
        pars       = []
        formula    = fcn_string
        for par_num, match in enumerate(re.finditer("(?P<name>\w+)(?P<boundaries>\[[^\]]+\]),? ?", pars_string)):
            par        = struct()
            par.num    = par_num
            par.name   = match.group('name')
            par.bounds = eval( match.group('boundaries') )
            formula    = formula.replace(par.name, '[%i]' % par.num)
            pars.append(par)

        ret = ROOT.TF1('ret', formula, 0, 200)
        for par in pars:
            ret.SetParName(par.num, par.name)
            if len(par.bounds) == 1:
                ret.FixParameter(par.num, par.bounds[0])
            else:
                ret.SetParameter(par.num, par.bounds[0])
                ret.SetParLimits(par.num, par.bounds[1], par.bounds[2])
        return ret


    def get_view(self, sample_pattern, key_name='view'):
        ''' Get a view which matches a pattern like "Zjets*"

        Generally key_name does not need to be modified, unless getting
        unblinded data via "unblinded_view"

        '''
        for sample, sample_info in self.views.iteritems():
            if fnmatch.fnmatch(sample, sample_pattern):
                try: 
                    return sample_info[key_name]
                except KeyError:
                    raise KeyError("you asked for %s in sample %s, but it was not found, I only have: %s" % (key_name, sample, ','.join(sample_info.keys())))
        raise KeyError("I can't find a view that matches %s, I have: %s" % (
            sample_pattern, " ".join(self.views.keys())))

    def make_stack(self, rebin=1, preprocess=None, folder='', sort=False):
        ''' Make a stack of the MC histograms '''
        
        mc_views = []
        for x in self.mc_samples:
            mc_view = self.get_view(x)
            if preprocess:
                mc_view = preprocess(mc_view)
            if folder:
                mc_view = self.get_wild_dir(mc_view, folder)
            mc_views.append(
                self.rebin_view(mc_view, rebin)
                )
            
        return views.StackView(*mc_views, sorted=sort)

    def make_sum(self, rebin=1, preprocess=None, folder=''):
        ''' Make a sum of the MC histograms '''

        mc_views = []
        for x in self.mc_samples:
            mc_view = self.get_view(x)
            if preprocess:
                mc_view = preprocess(mc_view)
            if folder:
                mc_view = self.get_wild_dir(mc_view, folder)
            mc_views.append(
                self.rebin_view(mc_view, rebin)
                )

        return views.SumView(*mc_views)

    def add_legend(self, samples, leftside=True, entries=None):
        ''' Build a legend using samples.

        If entries is None it will be taken from len(samples)

        '''
        nentries = entries if entries is not None else len(samples)
        legend = None
        if leftside:
            legend = plotting.Legend(nentries, leftmargin=0.03, topmargin=0.05, rightmargin=0.65)
        else:
            legend = plotting.Legend(nentries, rightmargin=0.01, topmargin=0.01, leftmargin=0.6, entryheight=0.04)
        for sample in samples:
            legend.AddEntry(sample)
        legend.SetEntrySeparation(0.02)
        legend.SetMargin(0.35)
        legend.Draw()
        self.keep.append(legend)
        return legend

    def add_cms_blurb(self, sqrts, jets, channel, preliminary=True, lumiformat='%0.1f'):
        ''' Add the CMS blurb '''
        latex = ROOT.TLatex()
        latex.SetNDC();
        latex.SetTextSize(0.04);
        latex.SetTextAlign(31);
        latex.SetTextAlign(11);
        label_text = "CMS"
        if preliminary:
            label_text += " Preliminary"
        data_text = "(2017, %i TeV) " % sqrts
        data_text += (lumiformat + " fb^{-1}") % (41.8)
            #self.views['data']['intlumi']/1000.)
        if channel=='h':
            jets_text = "#mu#tau_{h}, "
        else:
            jets_text = "#mu#tau_{e}, "
        if jets=='0Jet':
            jets_text += "0 Jet"
        elif jets=='1Jet':
            jets_text += "1 Jet"
        elif jets=='2Jet':
            jets_text += "2 Jet GG-enriched"
        elif jets=='2JetVBF':
            jets_text += "2 Jet VBF-enriched"
        self.keep.append(latex.DrawLatex(0.14, 0.84, label_text))
        self.keep.append(latex.DrawLatex(0.68, 0.94, data_text))
        self.keep.append(latex.DrawLatex(0.14, 0.80, jets_text))

    def add_ratio_plot_old(self, data_hist, mc_stack, x_range=None, ratio_range=0.5):
        #resize the canvas and the pad to fit the second pad
        self.canvas.SetCanvasSize( self.canvas.GetWw(), int(self.canvas.GetWh()*1.3) )
        self.canvas.cd()
        self.pad.SetPad(0, 0.33, 1., 1.)
        self.pad.Draw()
        self.canvas.cd()
        #create lower pad
        self.lower_pad = plotting.Pad( 0, 0., 1., 0.33)
        self.lower_pad.Draw()
        self.lower_pad.cd()
        
        mc_hist    = None
        if isinstance(mc_stack, plotting.HistStack):
            mc_hist = sum(mc_stack.GetHists())
        else:
            mc_hist = mc_stack
        data_clone = data_hist.Clone()
        data_clone.Divide(mc_hist)
        if not x_range:
            nbins = data_clone.GetNbinsX()
            x_range = (data_clone.GetBinLowEdge(1), 
                       data_clone.GetBinLowEdge(nbins)+data_clone.GetBinWidth(nbins))
        else:
            data_clone.GetXaxis().SetRangeUser(*x_range)
        ref_function = ROOT.TF1('f', "1.", *x_range)
        ref_function.SetLineWidth(3)
        ref_function.SetLineStyle(2)
        
        data_clone.Draw('ep')
        if ratio_range:
            data_clone.GetYaxis().SetRangeUser(1-ratio_range, 1+ratio_range)
        ref_function.Draw('same')
        self.keep.append(data_clone)
        self.keep.append(ref_function)
        self.pad.cd()
        return data_clone

    def add_ratio_plot(self, data_hist, mc_stack, err_hist, x_range=None, ratio_range=0.5):
        self.canvas.SetCanvasSize( self.canvas.GetWw(), int(self.canvas.GetWh()*1.3) )
        self.canvas.cd()
        self.pad.SetPad(0, 0.33, 1., 1.)
        self.pad.Draw()
        self.canvas.cd()
        self.lower_pad = plotting.Pad( 0, 0., 1., 0.33)
        self.lower_pad.SetGridx(True)
        self.lower_pad.SetGridy(True)
        self.lower_pad.Draw()
        self.lower_pad.cd()
        
        mc_hist    = None
        if isinstance(mc_stack, plotting.HistStack):
            mc_hist = sum(mc_stack.GetHists())
        else:
            mc_hist = mc_stack
        data_hist.Sumw2()
        mc_hist.Sumw2()
        data_clone = data_hist.Clone()
        data_clone.Sumw2()
        data_clone.Divide(mc_hist)

        for ibin in range(0,data_clone.GetXaxis().GetNbins()+1):
            if mc_hist.GetBinContent(ibin)<> 0:
                data_clone.SetBinError(ibin,data_hist.GetBinError(ibin)/mc_hist.GetBinContent(ibin))
        band = err_hist.Clone()
        band.SetName("bandplot")
        err = []
        ibin = 1 
        while ibin < band.GetXaxis().GetNbins()+1:
            if mc_hist.GetBinContent(ibin) <> 0 : 
                err.append((ibin, band.GetBinError(ibin)/band.GetBinContent(ibin)))
            ibin+=1
        band.Sumw2()
        band.Divide(mc_hist.Clone())
        band.SetFillStyle(0)
        for ibin in err:
            band.SetBinError(ibin[0], ibin[1])

        if not x_range:
            nbins = data_clone.GetNbinsX()
            x_range = (data_clone.GetBinLowEdge(1), 
                       data_clone.GetBinLowEdge(nbins)+data_clone.GetBinWidth(nbins))
        else:
            data_clone.GetXaxis().SetRangeUser(*x_range)
        ref_function = ROOT.TF1('f', "1.", *x_range)
        ref_function.SetLineWidth(2)
        ref_function.SetLineStyle(2)
        data_clone.SetTitle("")
        data_clone.GetYaxis().SetTitle("Obs./Exp.")
        data_clone.GetYaxis().SetTitleSize(0.04)
        data_clone.GetYaxis().SetLabelSize(0.04)
        data_clone.GetXaxis().SetLabelSize(0.04)
        data_clone.Draw()
        if ratio_range:
            data_clone.GetYaxis().SetRangeUser(1-ratio_range, 1+ratio_range)
        ref_function.Draw('same')

        band.SetMarkerStyle(0)
        band.SetLineColor(1)
        band.SetFillStyle('3002')
        band.SetFillColor(1)
        band.Draw('psamee2')

        self.keep.append(data_clone)
        self.keep.append(band)
        self.keep.append(ref_function)
        self.pad.cd()
        return data_clone

    def fit_shape(self, histo, model, x_range, fitopt='IRMENS'):
        tf1 = self.parse_formula(*model) 
        tf1.SetRange(*x_range)
        tf1.SetLineColor(ROOT.EColor.kAzure)
        tf1.SetLineWidth(3)
        result = histo.Fit(tf1, fitopt) #WL
        # "WL" Use Loglikelihood method and bin contents are not integer,
        #               i.e. histogram is weighted (must have Sumw2() set)
        # "Q"  Quiet mode (minimum printing)
        # "E"  Perform better Errors estimation using Minos technique
        # "M"  More. Improve fit results.
        #      It uses the IMPROVE command of TMinuit (see TMinuit::mnimpr).
        #      This algorithm attempts to improve the found local minimum by searching for a
        #      better one.
        # "R"  Use the Range specified in the function range
        # "N"  Do not store the graphics function, do not draw
        # "S"  The result of the fit is returned in the TFitResultPtr
        numpoints = tf1.GetNpx() #number of points in which the func is evaluated
        func_hist = plotting.Hist(numpoints, *x_range)
        (ROOT.TVirtualFitter.GetFitter()).GetConfidenceIntervals(func_hist)
        func_hist.linewidth = 0
        func_hist.fillcolor = ROOT.EColor.kAzure - 9
        func_hist.fillstyle = 3013
        func_hist.markersize = 0
        func_hist.Draw('same e3')
        tf1.Draw('same')
        self.keep.extend([
            tf1,
            func_hist
        ])
        return tf1

    def make_text_box(self, text, position='top-right'):
        look_up_positions = {
            'top-right'    : (0.73, 0.67, 0.96, 0.92),
            'top-left'     : (0.16, 0.67, 0.39, 0.92),
            'bottom-right' : (0.73, 0.15, 0.96, 0.4),
            'bottom-left'  : (0.16, 0.15, 0.39, 0.4),
            }
        p = look_up_positions[position] if isinstance(position, str) \
                         else position
        stat_box = ROOT.TPaveText(p[0], p[1], p[2], p[3], 'NDC')
        for line in text.split('\n'):
            print line
            stat_box.AddText(line)
        
        stat_box.SetFillColor(0)
        stat_box.SetBorderSize(1)
        return stat_box

    def reset(self):
        '''hard graphic reset'''
        del self.canvas
        del self.pad
        del self.lower_pad
        self.keep = []
        self.canvas = plotting.Canvas(name='Canvas', title='Canvas')
        self.canvas.cd()
        self.pad = plotting.Pad( 0., 0., 1., 1.)
        self.pad.Draw()
        self.pad.cd()
        self.lower_pad = None

    def save(self, filename, dotc=False, dotroot=False, json=False, verbose=False):
        ''' Save the current canvas contents to [filename] '''
        self.pad.Draw()
        self.canvas.Update()
        if not os.path.exists(self.outputdir):
            os.makedirs(self.outputdir)
        if verbose:
            print 'saving '+os.path.join(self.outputdir, filename) + '.png'
        self.canvas.SaveAs(os.path.join(self.outputdir, filename) + '.png')
        if dotc:
            self.canvas.SaveAs(os.path.join(self.outputdir, filename) + '.C')
        if json:
            jdict = {}
            for obj in self.keep:
                if isinstance(obj, ROOT.TH1):
                    jdict[obj.GetTitle()] = [obj.GetBinContent(1), obj.GetBinError(1)] 
                if isinstance(obj, ROOT.THStack):
                    jdict['hist_stack'] = {}
                    for i in obj.GetHists():
                        jdict['hist_stack'][i.GetTitle()] = [i.GetBinContent(1), i.GetBinError(1)]
            with open(os.path.join(self.outputdir, filename) + '.json', 'w') as jout:
                jout.write(prettyjson.dumps(jdict))
        if dotroot:
            outfile = ROOT.TFile.Open(os.path.join(self.outputdir, filename) + '.root')#, 'recreate')
            outfile.cd()
            self.canvas.Write()
            for obj in self.keep:
                obj.Write()
            self.reset()
            outfile.Close()
            #self.canvas = plotting.Canvas(name='adsf', title='asdf')
            #self.canvas.cd()
            #self.pad    = plotting.Pad(0., 0., 1., 1.) #ful-size pad
            #self.pad.cd()

        if self.keep and self.lower_pad:
            self.reset()
        else:
            self.keep = []
        self.canvas.SetLogx(False)
        self.canvas.SetLogy(True)
        
    def plot(self, sample, path, drawopt='', rebin=None, styler=None, xaxis='', xrange=None):
        ''' Plot a single histogram from a single sample.

        Returns a reference to the histogram.

        '''
        view = self.views[sample]['view']
        if rebin:
            view = self.rebin_view(view, rebin)
        histo = view.Get(path)
        if xrange:
            histo.GetXaxis().SetRange(xrange[0], xrange[1])
        if styler:
            styler(histo)
        histo.Draw(drawopt)
        histo.GetXaxis().SetTitle(xaxis)
        self.keep.append(histo)
        return histo

    def compare_shapes(self, sample1, sample2, path, rebin=None):
        ''' Compare the spectra from two different samples '''
        view1 = views.NormalizeView(self.views[sample1]['view'])
        if rebin:
            view1 = self.rebin_view(view1, rebin)
        histo1 = view1.Get(path)
        view2 = views.NormalizeView(self.views[sample2]['view'])
        if rebin:
            view2 = self.rebin_view(view2, rebin)
        histo2 = view2.Get(path)
        histo1.Draw('pe')
        histo2.SetMarkerColor(ROOT.EColor.kRed)
        histo2.Draw('pe,same')
        histo1.SetMaximum(
            1.2*max(histo1.GetMaximum(), histo2.GetMaximum()))
        self.keep.append( (histo1, histo2) )

    def expand_path(self, pattern):
        if any((i in pattern) for i in ['*', '?']):
            repattern = re.compile('^'+pattern.replace('*','[^/]*').replace('?','[^/]')+'$')
            return [i for i in self.file_dir_structure if repattern.match(i)]
        else:
            return [pattern]

    def get_wild_dir(self, view, path):
        'equivalent of SubdirectoryView, but with unix-style wildcards'
        paths = self.expand_path(path)
        return views.SumView(
            *[ views.SubdirectoryView(view, i) for i in paths]
            )

    def get_wild_path(self, view, path):
        'gets a FULL path with wildcards in it. By full it is intended till the histogram to be picked'
        base_name = os.path.baseODname(path)
        dir_name  = os.path.dirname(path)
        return self.get_wild_dir(view, dir_name).Get(base_name)

    def plot_mc_vs_data(self, folder, signal, variable, rebin=1, xaxis='',
                        leftside=True, xrange=None, preprocess=None,
                        show_ratio=False, ratio_range=0.5, sort=False, blind_region=False, control='', jets='', channel=''):
        ''' Compare Monte Carlo to data '''
        mc_stack_view = self.make_stack(rebin, preprocess, folder, sort)
        mc_stack = mc_stack_view.Get(variable)
        mc_stack.SetTitle("")
        mc_stack.Draw()
        mc_stack.GetHistogram().GetXaxis().SetTitle(xaxis)
        mc_stack.GetHistogram().GetYaxis().SetTitle("Events/bin")
        mc_stack.GetHistogram().GetYaxis().SetTitleOffset(1.4)
        if xrange:
            mc_stack.GetXaxis().SetRangeUser(xrange[0], xrange[1])
            mc_stack.Draw()
        self.keep.append(mc_stack)
        #####
        mc_sum_view = self.make_sum(rebin, preprocess, folder)
        mc_err = mc_sum_view.Get(variable)
        mc_err.Sumw2()
        #mc_err = SystematicsView.add_error(mc_err,  0.3)
        mc_err.SetMarkerStyle(0)
        mc_err.SetLineColor(1)
        mc_err.SetFillStyle('x')
        mc_err.SetFillColor(1)
        #mc_err.Draw('pe2 same')
        #mc_err.SetName('error')
        #####

        signalview=[]
        mymax=0
        for sig in signal:
            signal_view=self.get_view(sig)
            if preprocess:
                signal_view=preprocess(signal_view)
            signal_view = views.SubdirectoryView(signal_view, control)
            signal_view=self.get_wild_dir(
                self.rebin_view(signal_view,rebin),folder)
            signal=signal_view.Get(variable)
            signalview.append(signal)
            signalnew = signal.Clone()
            signalnew.Scale(50)
            signalnew.Draw("SAME")
            if signal.GetBinContent(signal.GetMaximumBin()) > mymax:
                mymax = signal.GetBinContent(signal.GetMaximumBin())
            self.keep.append(signal)

        data_view = views.SubdirectoryView(self.get_view('data'), control)
        if preprocess:
            data_view = preprocess( data_view )
        data_view = self.get_wild_dir(
            self.rebin_view(data_view, rebin),
            folder
            )
        data = data_view.Get(variable)

        if blind_region:
            for bin in range(data.GetNbinsX()+1):
                bg_count=mc_stack.GetStack().Last().GetBinContent(bin)
                if bg_count<=0 : bg_count=0
                sig_count=0
                for histo in signalview:
                    sig_count=histo.GetBinContent(bin)
                    if sig_count<=0: continue
                    if bool(bg_count<0.1 and sig_count>0) or ((float(sig_count)/float(sig_count+bg_count))>0.01):#0.01
                        data.SetBinContent(bin,0.)
                        data.SetBinError(bin,0.)

        data.Draw("SAME")
        self.keep.append(data)

        if data.GetMaximum() > mc_stack.GetMaximum():
            mc_stack.SetMaximum(1.2*data.GetMaximum())

        self.add_legend([data, mc_stack, signalview[0], signalview[1]], leftside, entries=len(mc_stack.GetHists())+len(signalview)+1)
        #self.add_legend([data, mc_stack], leftside, entries=len(mc_stack.GetHists())+1)
        #self.add_legend([data, mc_stack], leftside, entries=len(mc_stack.GetHists())+len(signalview)+1)
        self.add_cms_blurb(13, jets, channel)
        if show_ratio:
            self.add_ratio_plot(data, mc_stack, mc_err, xrange, ratio_range=0.5)


    def plot_mc_and_data(self, folder, variable, rebin=1, xaxis='',
                        leftside=True, xrange=None, preprocess=None,
                        show_ratio=False, ratio_range=0.2, sort=False):
        ''' Compare Monte Carlo to data '''
        #path = os.path.join(folder, variable)
        mc_stack_view = self.make_stack(rebin, preprocess, folder, sort)
        mc_stack = mc_stack_view.Get(variable)
        mc_stack.Draw()
        mc_stack.GetHistogram().GetXaxis().SetTitle(xaxis)
        if xrange:
            mc_stack.GetXaxis().SetRangeUser(xrange[0], xrange[1])
            mc_stack.Draw()
        self.keep.append(mc_stack)
        # Draw data
        data_view = self.get_view('data')
        if preprocess:
            data_view = preprocess( data_view )
        data_view = self.get_wild_dir(
            self.rebin_view(data_view, rebin),
            folder
            )
        data = data_view.Get(variable)
        data.Draw('same')
        self.keep.append(data)
        # Make sure we can see everything
        if data.GetMaximum() > mc_stack.GetMaximum():
            mc_stack.SetMaximum(1.2*data.GetMaximum())
        # Add legend
        self.add_legend([data, mc_stack], leftside, entries=len(mc_stack.GetHists())+1)
        if show_ratio:
            self.add_ratio_plot_old(data, mc_stack, xrange, ratio_range=0.2)
