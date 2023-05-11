import FWCore.ParameterSet.Config as cms

process = cms.Process("PPSTiming2")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('RecoPPS.Local.totemTimingLocalReconstruction_cff')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.a1 = cms.EDAnalyzer("StreamThingAnalyzer",
    product_to_get = cms.string('m1')
)

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_Candidate_2023_04_07_14_18_21', '')

process.load("EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff")
process.load("RecoPPS.Configuration.recoCTPPS_cff")
#process.ctppsDiamondRecHits.timingCalibrationTag=cms.string("GlobalTag:PPSTestCalibration")
#process.ctppsDiamondRecHits.applyCalibration = False
#process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigiAlCaRecoProducer", "TimingDiamond")
process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigi", "TimingDiamond")

#process.load('CondCore.CondDB.CondDB_cfi')
#process.CondDB.connect = 'sqlite_file:ppsDiamondTiming_calibration.sqlite' # SQLite input
#process.PoolDBESSource = cms.ESSource('PoolDBESSource',
#        process.CondDB,
#        DumpStats = cms.untracked.bool(True),
#        toGet = cms.VPSet(
#            cms.PSet(
#                record = cms.string('PPSTimingCalibrationRcd'),
#                tag = cms.string('DiamondTimingCalibration')
#        )
#    )
#)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
                                  'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBiasXXX/EphemeralZeroBiasXXX/220906_YYY/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_ZZZ.root',
),
)

#process.load("ALCARECOPPSCalTrackBasedSel_cff")

process.load("CalibPPS.TimingCalibration.ppsTimingCalibrationPCLWorker_cfi")
process.DQMStore = cms.Service("DQMStore")

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("testoutput.root")
)

process.load("CalibPPS.TimingCalibration.ALCARECOPromptCalibProdPPSTimingCalib_cff")

process.ctppsPixelDigis.inputLabel = "hltPPSCalibrationRaw"
process.ctppsDiamondRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemRPRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemTimingRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
#process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigiAlCaRecoProducer", "worker")

# define the HLT base path                                                                                                                                                                                 
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel as _hlt
process.ALCARECOPPSCalTrackBasedSelHLT = _hlt.clone(
    andOr = True,
    HLTPaths = ['HLT_EphemeralZeroBias_v*'],
    #eventSetupPathKey = 'SiStripCalZeroBias', # in case we have a proper base key                                                                                                                         
    throw = False
)

# select events passing the filter on pixel tracks                                                                                                                                                         
from HLTrigger.special.hltPPSPerPotTrackFilter_cfi import hltPPSPerPotTrackFilter as _filter
process.hltPPSPerPotTrackFilter_45 = _filter.clone(
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
process.hltPPSPerPotTrackFilter_56 = _filter.clone(
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



#process.ppsTimingCalibrationPCLWorker.diamondRecHitTags = cms.InputTag("ctppsDiamondRecHits","","PPSTiming2")
process.ppsTimingCalibrationPCLWorker.diamondRecHitTags=cms.VInputTag(cms.InputTag("ctppsDiamondRecHits","","PPSTiming2"))




process.path = cms.Path(
    #process.a1* 
    #process.ctppsRawToDigi *
    process.ctppsDiamondRecHits *
    process.recoCTPPS *
    process.ALCARECOPPSCalTrackBasedSelHLT *
    (process.hltPPSPerPotTrackFilter_45 + process.hltPPSPerPotTrackFilter_56)*
    #process.seqALCARECOPPSCalTrackBasedSel*
    process.ppsTimingCalibrationPCLWorker
    )

process.end_path = cms.EndPath(
    process.dqmOutput
)

process.schedule = cms.Schedule(
    process.path,
    process.end_path
)
