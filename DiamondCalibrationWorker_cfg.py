import FWCore.ParameterSet.Config as cms

process = cms.Process("PPSTiming2")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('RecoPPS.Local.totemTimingLocalReconstruction_cff')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

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
#'/store/data/Run2022C/AlCaPPSPrompt/ALCARECO/PPSCalMaxTracks-PromptReco-v1/000/357/479/00000/24a1d212-d92e-446d-85c7-7867596992aa.root'
#'/store/data/Run2022C/AlCaPPSPrompt/ALCARECO/PPSCalMaxTracks-PromptReco-v1/000/357/479/00000/246293f9-b84e-41cc-a992-880dd4d99222.root'
#'/store/data/Run2022C/AlCaPPSPrompt/ALCARECO/PPSCalMaxTracks-PromptReco-v1/000/357/329/00000/34f014fe-db35-4c71-aba5-a76206ded90a.root'
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_11.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_12.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_13.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_14.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_16.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_17.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_18.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_19.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_1.root',      # 
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_2.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_21.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_22.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_23.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_25.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_26.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_27.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_28.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_29.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_3.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_30.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_32.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_33.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_34.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_35.root',
#                                 'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias4/EphemeralZeroBias4/220906_135951/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_36.root'
                                  'file:/eos/cms/store/group/phys_pps/AOD_EphemeralZeroBias_Run2022C/EphemeralZeroBias7/EphemeralZeroBias7/220906_102839/0000/RECO_RAW2DIGI_L1Reco_RECO_PAT_47.root',
),
)

process.load("ALCARECOPPSCalTrackBasedSel_cff")

process.load("CalibPPS.TimingCalibration.ppsTimingCalibrationPCLWorker_cfi")
process.DQMStore = cms.Service("DQMStore")

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("worker_output.root")
)

process.load("CalibPPS.TimingCalibration.ALCARECOPromptCalibProdPPSTimingCalib_cff")

process.ctppsPixelDigis.inputLabel = "hltPPSCalibrationRaw"
process.ctppsDiamondRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemRPRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemTimingRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
#process.ctppsDiamondRecHits.digiTag = cms.InputTag("ctppsDiamondRawToDigiAlCaRecoProducer", "worker")

#process.ppsTimingCalibrationPCLWorker.diamondRecHitTags = cms.InputTag("ctppsDiamondRecHits","","PPSTiming2")
process.ppsTimingCalibrationPCLWorker.diamondRecHitTags=cms.VInputTag(cms.InputTag("ctppsDiamondRecHits","","PPSTiming2"))

process.path = cms.Path(
    #process.a1* 
    #process.ctppsRawToDigi *
    #process.ctppsDiamondRecHits *
    process.recoCTPPS *
    process.seqALCARECOPPSCalTrackBasedSel*
    process.ppsTimingCalibrationPCLWorker
    )

process.end_path = cms.EndPath(
    process.dqmOutput
)

process.schedule = cms.Schedule(
    process.path,
    process.end_path
)
