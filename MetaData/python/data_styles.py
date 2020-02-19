'''

Define styles for the different data samples.

The keys correspond to "logical" samples, defined in data_name_map of
datadefs.py

The values are dictionaries, which can be passed as kwargs to objects which
inherit from rootpy Plottable


http://ndawe.github.com/rootpy/reference/rootpy.plotting.html#rootpy.plotting.core.Plottable

'''

from FinalStateAnalysis.Utilities.solarized import colors

data_styles = {
    'GluGlu_LFV*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : 0,
        'fillstyle'   : 0,
        'linestyle'   : 1,
        'linewidth'   : 4,
        'linecolor'   : '#E42732',
        'name'        : "GG (B=20%)",
    },
    'VBF_LFV*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : 0,
        'fillstyle'   : 0,
        'linestyle'   : 1,
        'linewidth'   : 4,
        'linecolor'   : '#104E9B',
        'name'        : "VBF (B=20%)",
    },
    '*HToTauTau*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#c243cd',
        'fillstyle'   : 'solid',
        'linecolor'   : '#c243cd',
        'name'        : "HTT",
    },
    'DY*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#4496c8',
        'linecolor'   : '#4496c8',
        'name'        : "Zll",
        'fillstyle'   : 'solid',
    },
    'DYTT*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#ffcc66',
        'linecolor'   : '#ffcc66',
        'name'        : "Ztt",
        'fillstyle'   : 'solid',
    },
    'W*Jets*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#32CD32',
        'linecolor'   : '#32CD32',
        'name'        : "W + jets",
        'fillstyle'   : 'solid',
    },
    'WG*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : colors['blue'],
        'linecolor'   : colors['blue'],
        'name'        : "WGamma",
        'fillstyle'   : 'solid',
    },
    'EWK*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : colors['orange'],
        'linecolor'   : colors['orange'],
        'name'        : "EWK",
        'fillstyle'   : 'solid',
    },
    'QCD*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#ffccff',
        'linecolor'   : '#ffccff',
        'name'        : "Fakes",
        'fillstyle'   : 'solid',
    },
    'TT*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#9999cc',
        'linecolor'   : '#9999cc',
        'name'        : "ttbar",
        'fillstyle'   : 'solid',
    },
    'ST*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#999900',
        'linecolor'   : '#999900',
        'name'        : "singlet",
        'fillstyle'   : 'solid',
    },
    'VH*' : {
        'legendstyle' : 'l',
        'drawstyle'   : 'hist',
        'fillcolor'   : 0,
        'fillstyle'   : 0,
        'linestyle'   : 2,
        'linewidth'   : 4,
        'linecolor'   : '#1C1C76',
        'name'        : "VH",
    },
    'WZ*' : {
        'legendstyle' : 'f',
        'drawstyle'   : 'hist',
        'fillcolor'   : '#12cadd',
        'linecolor'   : '#12cadd',
        'name'        : "Diboson",
        'fillstyle'   : 'solid',
    },
    'data*' : {
        'legendstyle' : 'pe',
        'drawstyle'   : 'pe',
        'markerstyle' : 20,
        'name'        : "Observed",
    },
}

#makes life easier when converting shape files
data_styles['fakes'] = data_styles['DY*']
data_styles['wz'] = data_styles['WZ*']
data_styles['charge_fakes'] = data_styles['TT*']
