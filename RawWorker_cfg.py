import FWCore.ParameterSet.Config as cms

process = cms.Process("worker")

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
#process.GlobalTag = GlobalTag(process.GlobalTag, autoCond['run3_data_prompt'], '')
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_Candidate_2023_04_07_14_18_21', '')

#process.GlobalTag.toGet = cms.VPSet(
#  cms.PSet(record = cms.string("PPSTimingCalibrationLUTRcd"),
#           tag = cms.string("PPSDiamondTimingCalibrationLUT_null_payload"),
#           connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
#          )
#)

process.load("EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff")
process.load("RecoPPS.Configuration.recoCTPPS_cff")

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
#    '/store/data/Run2022B/AlCaPPS/RAW/v1/000/355/207/00000/c23440f4-49c0-44aa-b8f6-f40598fb4705.root',
#'file:/eos/cms/store/group/dpg_ctpps/comm_ctpps/ALCAPPS-RAW/000/355/988/00000/7728d214-b404-4578-b781-b0c207cfb875.root'
'file:/eos/cms/store/group/dpg_ctpps/comm_ctpps/ALCAPPS-RAW/000/355/998/00000/3565321b-e898-4bc8-b1af-3efda50465fb.root'
),
)

process.load("CalibPPS.TimingCalibration.ppsTimingCalibrationPCLWorker_cfi")
process.DQMStore = cms.Service("DQMStore")

#process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#    fileName = cms.untracked.string("DQMHistograms_worker_output.root")
#)

process.output = cms.OutputModule("PoolOutputModule",
                                  fileName = cms.untracked.string("worker_output.root"),
                                  outputCommands = cms.untracked.vstring('keep *')) 

process.load("CalibPPS.TimingCalibration.ALCARECOPromptCalibProdPPSTimingCalib_cff")

process.ctppsPixelDigis.inputLabel = "hltPPSCalibrationRaw"
process.ctppsDiamondRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemRPRawToDigi.rawDataTag = "hltPPSCalibrationRaw"
process.totemTimingRawToDigi.rawDataTag = "hltPPSCalibrationRaw"

process.path = cms.Path(
    #process.a1* 
    process.ctppsRawToDigi *
    process.recoCTPPS *
    process.ppsTimingCalibrationPCLWorker * 
    process.MEtoEDMConvertPPSTimingCalib
)

process.end_path = cms.EndPath(
    process.output
)

process.schedule = cms.Schedule(
    process.path,
    process.end_path
)
