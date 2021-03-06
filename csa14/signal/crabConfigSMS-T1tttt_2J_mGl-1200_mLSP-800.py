from WMCore.Configuration import Configuration 
config = Configuration() 
config.section_("General") 
config.General.requestName = 'SMS-T1tttt_2J_mGl-1200_mLSP-800'
config.General.workArea = 'crab_projects'

config.section_("JobType") 
config.JobType.pluginName = 'Analysis' 
config.JobType.psetName = 'miniAOD-prod_PAT.py' 
#config.JobType.allowNonProductionCMSSW = False
config.JobType.allowNonProductionCMSSW = True

config.section_("Data") 
#config.Data.inputDataset = '/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM' 
#config.Data.inputDataset = '/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'
#config.Data.inputDataset = '/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'
#config.Data.inputDataset = '/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'
config.Data.inputDataset = '/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'
#config.Data.inputDataset = '/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'
#/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/duanders-Spring14dr-PU_S14_POSTLS170_V6AN1-miniAOD706p1-814812ec83fce2f620905d2bb30e9100/USER
#config.Data.inputDataset = '/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Spring14dr-PU_S14_POSTLS170_V6-v1/AODSIM'

config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/' 
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 3 
config.Data.publication = True 
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
#config.Data.publishDbsUrl = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' 
config.Data.publishDataName = 'Spring14dr-PU_S14_POSTLS170_V6AN1-miniAOD706p1' 
config.Data.outLFN = '/store/user/adraeger/'
config.Data.ignoreLocality = True

config.section_("Site") 
config.Site.storageSite = 'T2_DE_DESY' 
#config.Site.whitelist = ['T2_DE_DESY']

