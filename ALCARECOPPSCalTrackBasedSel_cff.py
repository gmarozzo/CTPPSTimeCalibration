import FWCore.ParameterSet.Config as cms

# define the HLT base path
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel as _hlt
ALCARECOPPSCalTrackBasedSelHLT = _hlt.clone(
    andOr = True,
    HLTPaths = ['HLT_EphemeralZeroBias_v*'],
    #eventSetupPathKey = 'SiStripCalZeroBias', # in case we have a proper base key
    throw = False
)

# perform basic PPS reconstruction
from EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff import *
from RecoPPS.Configuration.recoCTPPS_cff import *

# select events passing the filter on pixel tracks
from HLTrigger.special.hltPPSPerPotTrackFilter_cfi import hltPPSPerPotTrackFilter as _filter
hltPPSPerPotTrackFilter_45 = _filter.clone(
    pixelFilter = cms.VPSet(
        cms.PSet( # sector 45, near pot
            detid = cms.uint32(2022703104),
            minTracks = cms.int32(0),
            maxTracks = cms.int32(1000),
        ),
        cms.PSet( # sector 45, far pot
            detid = cms.uint32(2023227392),
            minTracks = cms.int32(1),
            maxTracks = cms.int32(4),
        ),
    )
)
hltPPSPerPotTrackFilter_56 = _filter.clone(
    pixelFilter = cms.VPSet(
        cms.PSet( # sector 56, near pot
            detid = cms.uint32(2039480320),
            minTracks = cms.int32(0),
            maxTracks = cms.int32(1000),
        ),
        cms.PSet( # sector 56, far pot
            detid = cms.uint32(2040004608),
            minTracks = cms.int32(1),
            maxTracks = cms.int32(4),
        ),
    )
)

seqALCARECOPPSCalTrackBasedSel = cms.Sequence(
    #ctppsRawToDigi *
    #recoCTPPS *
    ALCARECOPPSCalTrackBasedSelHLT *
    (hltPPSPerPotTrackFilter_45 + hltPPSPerPotTrackFilter_56)
)
