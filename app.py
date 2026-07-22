import streamlit as st
import json

FLASH_PARAMS = {
    "X2 9060": {
        "pagesize": 18432,
        "pagecnt": 2304,
        "Plane Num": 4,
        "tDummyMode": None,
        "tDirectWrite": None,
        "tPageOfWl": 3,
        "tR_t": 26000,
        "tPROG_t": 180000,
        "tBERS_t": 4000000,
        "tXLCPROG_t": 620000,
        "tXLCBERS_t": 9000000,
        "tPLRBSY_t": 180,
        "tPLPBSY_t": 180,
        "tMPP_t": None,
        "tPCBSY_t": 4300,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": 180,
        "tRCBSY_t": 3800,
        "FlashIOSpeed": 1600,
        "tWB_t": 100,
        "tWPRE_t": 25,
        "tRPRE_t": 25,
        "tDQSRE_t": 24,
        "tRPST_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_t": 15,
        "tCHZ_t": 30,
        "tCS_t": 20,
        "tCALS_t": 15,
        "tCALH_t": 5,
        "tWP_t": 11,
        "tWC_t": 25,
        "tRR_t": 20,
        "tCCS_t": 400,
        "tADL_t": 400,
        "tWPST_t": 6.5,
        "tWHR_t": 80,
        "tWHR2_t": None,
        "tCDQSH_t": 100,
        "tDBS_t": 5,
        "tRHW_t": 100,
        "tCSD_t": 10,
        "tCACI_t": None,
        "tCELCLK_t": None,
        "tCLKLCE_t": None,
        "tSCR_t": None,
        "tRPRE2_t": None,
        "tRPST_CA_t": None,
        "tRPSTH_CA_t": None,
        "tWPST_CA_t": None,
        "tWPSTH_CA_t": None,
        "tW2R_CA_t": None,
        "tR2W_CA_t": None,
        "tCACOPST_t": None,
        "tCLKCA_t": None,
        "tCEH2_t": None,
        "tCACO_t": None,
        "tSCRES_t": None,
        "tPLRBSY": 1800,
        "tRCBSY": 4300,
        "tR": 5000,
        "tPLPBSY": 1280,
        "tPROG": 180000,
        "tPCBSY": 12380,
        "tCS": 110,
        "tWB": 103,
        "tRR": 20,
        "tCCS": 403,
        "tRPRE": 28,
        "tDQSRE": 5,
        "tRPST": None,
        "tCHZ": 33,
        "tCEH2L": 112,
        "tADL": 400,
        "tWPRE": 29,
        "tWPST": 11,
    },
    "X2 6070": {
        "pagesize": 18432,
        "pagecnt": 3048,
        "Plane Num": 6,
        "tDummyMode": None,
        "tDirectWrite": None,
        "tPageOfWl": 4,
        "tR_t": 50000,
        "tPROG_t": 244000,
        "tBERS_t": 5000000,
        "tXLCPROG_t": 3276000,
        "tXLCBERS_t": 9000000,
        "tPLRBSY_t": None,
        "tPLPBSY_t": None,
        "tMPP_t": None,
        "tPCBSY_t": None,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": None,
        "tRCBSY_t": None,
        "FlashIOSpeed": 1200,
        "tWB_t": None,
        "tWPRE_t": None,
        "tRPRE_t": None,
        "tDQSRE_t": None,
        "tRPST_t": None,
        "tRPSTH_t": None,
        "tCHZ_t": None,
        "tCS_t": None,
        "tCALS_t": None,
        "tCALH_t": None,
        "tWP_t": None,
        "tWC_t": None,
        "tRR_t": None,
        "tCCS_t": None,
        "tADL_t": None,
        "tWPST_t": None,
        "tWHR_t": None,
        "tWHR2_t": None,
        "tCDQSH_t": None,
        "tDBS_t": None,
        "tRHW_t": None,
        "tCSD_t": None,
        "tCACI_t": None,
        "tCELCLK_t": None,
        "tCLKLCE_t": None,
        "tSCR_t": None,
        "tRPRE2_t": None,
        "tRPST_CA_t": None,
        "tRPSTH_CA_t": None,
        "tWPST_CA_t": None,
        "tWPSTH_CA_t": None,
        "tW2R_CA_t": None,
        "tR2W_CA_t": None,
        "tCACOPST_t": None,
        "tCLKCA_t": None,
        "tCEH2_t": None,
        "tCACO_t": None,
        "tSCRES_t": None,
        "tPLRBSY": None,
        "tRCBSY": None,
        "tR": None,
        "tPLPBSY": None,
        "tPROG": None,
        "tPCBSY": None,
        "tCS": None,
        "tWB": None,
        "tRR": None,
        "tCCS": None,
        "tRPRE": None,
        "tDQSRE": None,
        "tRPST": None,
        "tCHZ": None,
        "tCEH2L": None,
        "tADL": None,
        "tWPRE": None,
        "tWPST": None,
    },
    "X3 9060": {
        "pagesize": 18368,
        "pagecnt": 4176,
        "Plane Num": 6,
        "tDummyMode": None,
        "tDirectWrite": None,
        "tPageOfWl": 3,
        "tR_t": 22000,
        "tPROG_t": 81000,
        "tBERS_t": 4000000,
        "tXLCPROG_t": 385000,
        "tXLCBERS_t": 5000000,
        "tPLRBSY_t": None,
        "tPLPBSY_t": None,
        "tMPP_t": None,
        "tPCBSY_t": None,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": None,
        "tRCBSY_t": None,
        "FlashIOSpeed": 2400,
        "tWB_t": None,
        "tWPRE_t": None,
        "tRPRE_t": None,
        "tDQSRE_t": None,
        "tRPST_t": None,
        "tRPSTH_t": None,
        "tCHZ_t": None,
        "tCS_t": None,
        "tCALS_t": None,
        "tCALH_t": None,
        "tWP_t": None,
        "tWC_t": None,
        "tRR_t": None,
        "tCCS_t": None,
        "tADL_t": None,
        "tWPST_t": None,
        "tWHR_t": None,
        "tWHR2_t": None,
        "tCDQSH_t": None,
        "tDBS_t": None,
        "tRHW_t": None,
        "tCSD_t": None,
        "tCACI_t": None,
        "tCELCLK_t": None,
        "tCLKLCE_t": None,
        "tSCR_t": None,
        "tRPRE2_t": None,
        "tRPST_CA_t": None,
        "tRPSTH_CA_t": None,
        "tWPST_CA_t": None,
        "tWPSTH_CA_t": None,
        "tW2R_CA_t": None,
        "tR2W_CA_t": None,
        "tCACOPST_t": None,
        "tCLKCA_t": None,
        "tCEH2_t": None,
        "tCACO_t": None,
        "tSCRES_t": None,
        "tPLRBSY": None,
        "tRCBSY": None,
        "tR": None,
        "tPLPBSY": None,
        "tPROG": None,
        "tPCBSY": None,
        "tCS": None,
        "tWB": None,
        "tRR": None,
        "tCCS": None,
        "tRPRE": None,
        "tDQSRE": None,
        "tRPST": None,
        "tCHZ": None,
        "tCEH2L": None,
        "tADL": None,
        "tWPRE": None,
        "tWPST": None,
    },
    "X4 9060": {
        "pagesize": 18432,
        "pagecnt": 4800,
        "Plane Num": 4,
        "tDummyMode": 'yes',
        "tDirectWrite": 'yes',
        "tPageOfWl": 3,
        "tR_t": 19000,
        "tPROG_t": 80000,
        "tBERS_t": 3800000,
        "tXLCPROG_t": 1020000,
        "tXLCBERS_t": 4000000,
        "tPLRBSY_t": 0,
        "tPLPBSY_t": 50,
        "tMPP_t": 100,
        "tPCBSY_t": 4000,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": 0,
        "tRCBSY_t": 2500,
        "FlashIOSpeed": 3600,
        "tWB_t": 100,
        "tWPRE_t": 25,
        "tRPRE_t": 25,
        "tDQSRE_t": 1.5,
        "tRPST_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_t": 15,
        "tCHZ_t": 30,
        "tCS_t": 20,
        "tCALS_t": 5,
        "tCALH_t": 5,
        "tWP_t": 4.5,
        "tWC_t": 10,
        "tRR_t": 20,
        "tCCS_t": 300,
        "tADL_t": 300,
        "tWPST_t": 6.5,
        "tWHR_t": 80,
        "tWHR2_t": None,
        "tCDQSH_t": 100,
        "tDBS_t": 5,
        "tRHW_t": 100,
        "tCSD_t": 10,
        "tCACI_t": 8,
        "tCELCLK_t": 20,
        "tCLKLCE_t": 20,
        "tSCR_t": 50,
        "tRPRE2_t": 30,
        "tRPST_CA_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_CA_t": 50,
        "tWPST_CA_t": 6.5,
        "tWPSTH_CA_t": 50,
        "tW2R_CA_t": 20,
        "tR2W_CA_t": 'tCACOPST + tCEH2 + tCELCLK',
        "tCACOPST_t": 'tCLKCA+0.5*tCACO',
        "tCLKCA_t": 30,
        "tCEH2_t": 30,
        "tCACO_t": 8,
        "tSCRES_t": 10,
        "tPLRBSY": 0,
        "tRCBSY": 2500,
        "tR": 19000,
        "tPLPBSY": 100,
        "tPROG": 80000,
        "tPCBSY": 4000,
        "tCS": 20,
        "tWB": 100,
        "tRR": 20,
        "tCCS": 300,
        "tRPRE": 25,
        "tDQSRE": 1.5,
        "tRPST": None,
        "tCHZ": 30,
        "tCEH2L": 112,
        "tADL": 300,
        "tWPRE": 25,
        "tWPST": 6.5,
    },
    "X4 9070": {
        "pagesize": 18432,
        "pagecnt": 6408,
        "Plane Num": 6,
        "tDummyMode": 'yes',
        "tDirectWrite": 'yes',
        "tPageOfWl": 3,
        "tR_t": 22000,
        "tPROG_t": 77000,
        "tBERS_t": 5000000,
        "tXLCPROG_t": 1200000,
        "tXLCBERS_t": 7000000,
        "tPLRBSY_t": 50,
        "tPLPBSY_t": 50,
        "tMPP_t": 100,
        "tPCBSY_t": 3100,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": 50,
        "tRCBSY_t": 2500,
        "FlashIOSpeed": 3600,
        "tWB_t": 100,
        "tWPRE_t": 25,
        "tRPRE_t": 25,
        "tDQSRE_t": 1.5,
        "tRPST_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_t": 15,
        "tCHZ_t": 30,
        "tCS_t": 20,
        "tCALS_t": 3,
        "tCALH_t": 3,
        "tWP_t": 4.5,
        "tWC_t": 10,
        "tRR_t": 20,
        "tCCS_t": 300,
        "tADL_t": 300,
        "tWPST_t": 6.5,
        "tWHR_t": 80,
        "tWHR2_t": None,
        "tCDQSH_t": 100,
        "tDBS_t": 5,
        "tRHW_t": 100,
        "tCSD_t": 10,
        "tCACI_t": 8,
        "tCELCLK_t": 20,
        "tCLKLCE_t": 20,
        "tSCR_t": 50,
        "tRPRE2_t": 30,
        "tRPST_CA_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_CA_t": 50,
        "tWPST_CA_t": 6.5,
        "tWPSTH_CA_t": 50,
        "tW2R_CA_t": 20,
        "tR2W_CA_t": 'tCACOPST + tCEH2 + tCELCLK',
        "tCACOPST_t": 'tCLKCA+0.5*tCACO',
        "tCLKCA_t": 30,
        "tCEH2_t": 30,
        "tCACO_t": 8,
        "tSCRES_t": 10,
        "tPLRBSY": None,
        "tRCBSY": None,
        "tR": None,
        "tPLPBSY": None,
        "tPROG": None,
        "tPCBSY": 4300,
        "tCS": 25,
        "tWB": None,
        "tRR": None,
        "tCCS": None,
        "tRPRE": None,
        "tDQSRE": None,
        "tRPST": None,
        "tCHZ": None,
        "tCEH2L": None,
        "tADL": None,
        "tWPRE": None,
        "tWPST": None,
    },
    "X4 6080": {
        "pagesize": 19136,
        "pagecnt": 8480,
        "Plane Num": 8,
        "tDummyMode": 'yes',
        "tDirectWrite": 'no',
        "tPageOfWl": 4,
        "tR_t": 22000,
        "tPROG_t": 80000,
        "tBERS_t": 5000000,
        "tXLCPROG_t": 1550000,
        "tXLCBERS_t": 10000000,
        "tPLRBSY_t": 50,
        "tPLPBSY_t": 50,
        "tMPP_t": 100,
        "tPCBSY_t": 4000,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": 0,
        "tRCBSY_t": 2500,
        "FlashIOSpeed": 3600,
        "tWB_t": 100,
        "tWPRE_t": 25,
        "tRPRE_t": 25,
        "tDQSRE_t": 1.5,
        "tRPST_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_t": 15,
        "tCHZ_t": 30,
        "tCS_t": 20,
        "tCALS_t": 3,
        "tCALH_t": 3,
        "tWP_t": 4.5,
        "tWC_t": 10,
        "tRR_t": 20,
        "tCCS_t": 300,
        "tADL_t": 300,
        "tWPST_t": 6.5,
        "tWHR_t": 80,
        "tWHR2_t": None,
        "tCDQSH_t": 100,
        "tDBS_t": 5,
        "tRHW_t": 100,
        "tCSD_t": 10,
        "tCACI_t": 8,
        "tCELCLK_t": 20,
        "tCLKLCE_t": 20,
        "tSCR_t": 50,
        "tRPRE2_t": 30,
        "tRPST_CA_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_CA_t": 50,
        "tWPST_CA_t": 6.5,
        "tWPSTH_CA_t": 50,
        "tW2R_CA_t": 20,
        "tR2W_CA_t": 'tCACOPST + tCEH2 + tCELCLK',
        "tCACOPST_t": 'tCLKCA+0.5*tCACO',
        "tCLKCA_t": 30,
        "tCEH2_t": 30,
        "tCACO_t": 8,
        "tSCRES_t": 10,
        "tPLRBSY": None,
        "tRCBSY": None,
        "tR": None,
        "tPLPBSY": None,
        "tPROG": None,
        "tPCBSY": None,
        "tCS": None,
        "tWB": None,
        "tRR": None,
        "tCCS": None,
        "tRPRE": None,
        "tDQSRE": None,
        "tRPST": None,
        "tCHZ": None,
        "tCEH2L": None,
        "tADL": None,
        "tWPRE": None,
        "tWPST": None,
    },
    "X5 6080": {
        "pagesize": 19456,
        "pagecnt": 8480,
        "Plane Num": 8,
        "tDummyMode": 'yes',
        "tDirectWrite": 'no',
        "tPageOfWl": 4,
        "tR_t": 22000,
        "tPROG_t": 70000,
        "tBERS_t": 5000000,
        "tXLCPROG_t": 1550000,
        "tXLCBERS_t": 10000000,
        "tPLRBSY_t": 50,
        "tPLPBSY_t": 50,
        "tMPP_t": 100,
        "tPCBSY_t": 4000,
        "tPCBSY2_t": 6000,
        "tPLEBSY_t": 0,
        "tRCBSY_t": 2500,
        "FlashIOSpeed": 3600,
        "tWB_t": 100,
        "tWPRE_t": 25,
        "tRPRE_t": 25,
        "tDQSRE_t": 1.5,
        "tRPST_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_t": 15,
        "tCHZ_t": 30,
        "tCS_t": 20,
        "tCALS_t": 3,
        "tCALH_t": 3,
        "tWP_t": 4.5,
        "tWC_t": 10,
        "tRR_t": 20,
        "tCCS_t": 300,
        "tADL_t": 300,
        "tWPST_t": 6.5,
        "tWHR_t": 80,
        "tWHR2_t": None,
        "tCDQSH_t": 100,
        "tDBS_t": 5,
        "tRHW_t": 100,
        "tCSD_t": 10,
        "tCACI_t": 8,
        "tCELCLK_t": 20,
        "tCLKLCE_t": 20,
        "tSCR_t": 50,
        "tRPRE2_t": 30,
        "tRPST_CA_t": 'tDQSRE + 0.5*tRC',
        "tRPSTH_CA_t": 50,
        "tWPST_CA_t": 6.5,
        "tWPSTH_CA_t": 50,
        "tW2R_CA_t": 20,
        "tR2W_CA_t": 'tCACOPST + tCEH2 + tCELCLK',
        "tCACOPST_t": 'tCLKCA+0.5*tCACO',
        "tCLKCA_t": 30,
        "tCEH2_t": 30,
        "tCACO_t": 8,
        "tSCRES_t": 10,
        "tPLRBSY": None,
        "tRCBSY": None,
        "tR": None,
        "tPLPBSY": None,
        "tPROG": None,
        "tPCBSY": None,
        "tCS": None,
        "tWB": None,
        "tRR": None,
        "tCCS": None,
        "tRPRE": None,
        "tDQSRE": None,
        "tRPST": None,
        "tCHZ": None,
        "tCEH2L": None,
        "tADL": None,
        "tWPRE": None,
        "tWPST": None,
    },
}

CONTROLLERS = {
    "9205": {
        "ChNum": 4,
        "IoSpeed": 1600,
        "RdCwMode": "Yes",
        "tabupdateloss": 0.02,
        "MrdSeqRd": 3600,
        "MrdSeqWr": 3200,
        "MrdRndRdIops": 500,
        "MrdRndWrIops": 500,
        "tSlcCmd": 33,
        "t00Addr32": 280,
        "t00Addr30": 415,
        "t31Cmd": 33,
        "t05AddrE0": 280,
        "t80Addr": 247,
        "tWPSH": 28,
        "tWP": 10,
        "tCDQSH": 103,
        "tDBS": 5,
        "t11Cmd": 146,
        "t81Addr": 247,
        "t10Cmd": 146
    },
    "9503": {
        "ChNum": 4,
        "IoSpeed": 4800,
        "RdCwMode": "No",
        "tabupdateloss": 0.02,
        "MrdSeqRd": 14500,
        "MrdSeqWr": 14000,
        "MrdRndRdIops": 3000,
        "MrdRndWrIops": 3000,
        "tSlcCmd": 56,
        "t00Addr32": 280,
        "t00Addr30": 465,
        "t31Cmd": 33,
        "t05AddrE0": 280,
        "t80Addr": 247,
        "tWPSH": 28,
        "tWP": 10,
        "tCDQSH": 103,
        "tDBS": 5,
        "t11Cmd": 146,
        "t81Addr": 247,
        "t10Cmd": 146
    },
    "8803": {
        "ChNum": 1,
        "IoSpeed": 3200,
        "RdCwMode": "No",
        "tabupdateloss": 0.02,
        "MrdSeqRd": 4300,
        "MrdSeqWr": 4000,
        "MrdRndRdIops": 650,
        "MrdRndWrIops": 650,
        "tSlcCmd": 33,
        "t00Addr32": 280,
        "t00Addr30": 415,
        "t31Cmd": 33,
        "t05AddrE0": 180,
        "t80Addr": 247,
        "tWPSH": None,
        "tWP": None,
        "tCDQSH": None,
        "tDBS": None,
        "t11Cmd": 0,
        "t81Addr": 247,
        "t10Cmd": 0
    }
}

IO_SPEED_OPTIONS = [4800, 3600, 3200, 2800, 2400, 1600, 1200, 1000, 800, 400]


# ======================== 访问控制 ========================
def check_access():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # 登录页面精密科技风格
        st.markdown("""
        <style>
            .login-container {
                max-width: 500px;
                margin: 80px auto;
                padding: 40px;
                background: var(--metric-bg);
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(15,43,77,0.25);
                border: 2px solid #38a169;
            }
            .login-title {
                text-align: center;
                color: #0f2b4d;
                font-family: 'Noto Sans SC', sans-serif;
                font-weight: 800;
                font-size: 28px;
                margin-bottom: 10px;
            }
            .login-subtitle {
                text-align: center;
                color: #2d5a87;
                font-family: 'Noto Sans SC', sans-serif;
                font-size: 14px;
                margin-bottom: 30px;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="login-container">
            <h1 class="login-title">SSD 控制器性能计算器</h1>
            <p class="login-subtitle">得一微电子 Yeestor · Precision Calculator</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader("访问验证")
            st.markdown("<p style='color: #718096; font-size: 12px; margin-bottom: 15px; font-family: \"Noto Sans SC\", sans-serif;'>请输入访问密码以继续</p>", unsafe_allow_html=True)
            password = st.text_input("密码", type="password", placeholder="输入密码...")
            if st.button("进入系统", use_container_width=True):
                # 默认密码: ssd2024
                if password == st.secrets.get("password", "ssd2024"):
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("密码错误，请重新输入")
        return False
    return True

# ======================== 参数获取函数 ========================
def param_in_flash(flash_type, search_string):
    params = FLASH_PARAMS.get(flash_type, {})
    val = params.get(search_string, params.get("Plane Num", 0))
    if search_string in ("tDummyMode", "tDirectWrite"):
        return 1 if val == "yes" else 0
    if val is None:
        return 0
    return val


def param_in_control(ctrl_type, search_string):
    ctrl = CONTROLLERS.get(ctrl_type, {})
    val = ctrl.get(search_string, 0)
    if val is None:
        return 0
    return val


# ======================== 计算函数 ========================
def calc_globals(cfg):
    g = {}
    g["IoSpeed"] = cfg["IoSpeed"]
    g["ChNum"] = cfg["ChNum"]
    g["CeNum"] = cfg["CeNum"]
    g["PlaneNum"] = cfg["PlaneNum"]
    g["CtrlType"] = cfg["CtrlType"]
    g["WarmUpCycle"] = cfg["WarmUpCycle"]
    g["FlashType"] = cfg["FlashType"]
    g["isSeq4kRd"] = cfg["isSeq4kRd"]
    g["isCacheProg"] = cfg["isCacheProg"]
    g["CalcTypeIdx"] = cfg["CalcTypeIdx"]
    g["isDummyModeEn"] = cfg["isDummyModeEn"]
    g["isScaMode"] = cfg["isScaMode"]
    g["isToFinalEdge"] = cfg["isToFinalEdge"]
    g["isToEnableNTO"] = cfg["isToEnableNTO"]

    g["pageofWl"] = param_in_flash(g["FlashType"], "tPageOfWl")
    g["PageCnt"] = param_in_flash(g["FlashType"], "pagecnt") / g["pageofWl"]
    g["PageSize"] = param_in_flash(g["FlashType"], "pagesize")
    g["4kSize"] = g["PageSize"] / 4
    g["unit"] = 1.0 / g["IoSpeed"] * 1000.0
    g["dfi"] = (g["IoSpeed"] / 2) / 4
    g["dfiCycle"] = 1.0 / g["dfi"] * 1000.0

    g["MrdSeqRdSpeed"] = param_in_control(g["CtrlType"], "MrdSeqRd")
    g["MrdSeqWrSpeed"] = param_in_control(g["CtrlType"], "MrdSeqWr")
    g["MrdRndRdIops"] = param_in_control(g["CtrlType"], "MrdRndRdIops")
    g["MrdRndWrIops"] = param_in_control(g["CtrlType"], "MrdRndWrIops")
    g["TabUpdateLoss"] = param_in_control(g["CtrlType"], "tabupdateloss")
    return g


def calc_seq_rd_performance(g):
    tSlcCmd = param_in_flash(g["FlashType"], "tCS_t")
    tCALS = param_in_flash(g["FlashType"], "tCALS_t")
    tWC = param_in_flash(g["FlashType"], "tWC_t")
    tCALH = param_in_flash(g["FlashType"], "tCALH_t")
    tcmd = tCALS + tCALH
    t6addr = tCALS + tWC * 6 + tCALH
    t6addrcmd = tcmd + t6addr + tcmd
    tDa31Cmd = tcmd + tWC
    t00Addr30 = t6addrcmd

    tWB = param_in_flash(g["FlashType"], "tWB_t")
    tRR = param_in_flash(g["FlashType"], "tRR_t")
    tPLRBSY = param_in_flash(g["FlashType"], "tPLRBSY_t")
    tR = param_in_flash(g["FlashType"], "tR_t")

    if g["isDummyModeEn"]:
        tSlcMultiPlaneRd = tSlcCmd + t6addrcmd * (g["PlaneNum"] - 1) + t00Addr30 + tWB + tR
    else:
        tSlcMultiPlaneRd = tSlcCmd + (t6addrcmd + tWB + tPLRBSY) * (g["PlaneNum"] - 1) + t00Addr30 + tWB + tR

    tRCBSY = param_in_flash(g["FlashType"], "tRCBSY_t")
    tCSD = param_in_flash(g["FlashType"], "tCSD_t")
    tCHZ = param_in_flash(g["FlashType"], "tCHZ_t")
    tCacheRd = tDa31Cmd + tCSD

    t05AddrE0 = tcmd + t6addr + tcmd
    tCCS = param_in_flash(g["FlashType"], "tCCS_t")
    tRPRE = param_in_flash(g["FlashType"], "tRPRE_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tRPST = tDQSRE + tRC
    tRPSTH = param_in_flash(g["FlashType"], "tRPSTH_t")
    tCS = param_in_flash(g["FlashType"], "tCS_t")
    tRHW = param_in_flash(g["FlashType"], "tRHW_t")
    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tCheckSts = tCS + tcmd + tWHR + tRPRE + tDQSRE + g["unit"] + tRPST + tRPSTH + tRHW

    t4kTransfer = t05AddrE0 + tCCS + tRPRE + tDQSRE + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST + tRPSTH + tRHW

    if g["isSeq4kRd"]:
        tPageTransfer = t4kTransfer * 4
    else:
        tRawPageTransfer = (g["PageSize"] + g["WarmUpCycle"]) * g["unit"]
        tPageTransfer = t05AddrE0 + tCCS + tRPRE + tDQSRE + tRawPageTransfer + tRPST + tRPSTH + tRHW

    tMultiPlaneTransfer = tCheckSts + tPageTransfer * g["PlaneNum"] + tCacheRd

    Tmp1 = g["PlaneNum"] * g["CeNum"] * g["PageCnt"] * 16384
    if tRCBSY > (tMultiPlaneTransfer * (g["CeNum"] - 1)):
        Tmp2 = (tMultiPlaneTransfer + tRCBSY) * g["PageCnt"] + tSlcMultiPlaneRd
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tMultiPlaneTransfer * g["CeNum"] * g["PageCnt"] + tSlcMultiPlaneRd
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)

    g["SeqRdSpeed"] = speed * g["ChNum"]
    g["SeqRdSpeed1024base"] = speed2 * g["ChNum"]


def calc_rnd_rd_performance(g):
    tSlcCmd = param_in_flash(g["FlashType"], "tCS_t")
    tCALS = param_in_flash(g["FlashType"], "tCALS_t")
    tWC = param_in_flash(g["FlashType"], "tWC_t")
    tCALH = param_in_flash(g["FlashType"], "tCALH_t")
    tcmd = tCALS + tCALH
    t6addr = tCALS + tWC * 6 + tCALH
    t4addr = tCALS + tWC * 4 + tCALH
    t6addrcmd = tcmd + t6addr + tcmd

    tWB = param_in_flash(g["FlashType"], "tWB_t")
    tR = param_in_flash(g["FlashType"], "tR_t")
    tSlc4KRd = tSlcCmd + t6addrcmd

    t05AddrE0 = tcmd + t6addr + tcmd
    tCCS = param_in_flash(g["FlashType"], "tCCS_t")
    tRPRE = param_in_flash(g["FlashType"], "tRPRE_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tRPST = tDQSRE + tRC
    tCS = param_in_flash(g["FlashType"], "tCS_t")
    tRHW = param_in_flash(g["FlashType"], "tRHW_t")
    tRPSTH = param_in_flash(g["FlashType"], "tRPSTH_t")
    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tCheckSts = tcmd + t4addr + tWHR + tRPRE + g["unit"] + tRPST + tRPSTH + tRHW

    t4kTransfer = t05AddrE0 + tCCS + tRPRE + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST + tRPSTH + tRHW
    tAipr4kTransfer = tCheckSts + t4kTransfer + tSlc4KRd

    if g["CtrlType"] == "8803":
        tAipr4kTransfer = tAipr4kTransfer + tCheckSts

    Tmp1 = g["PlaneNum"] * g["CeNum"] * 4096
    if tR > (tAipr4kTransfer * (g["CeNum"] * g["PlaneNum"] - 1)):
        Tmp2 = tAipr4kTransfer + tR
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tAipr4kTransfer * g["CeNum"] * g["PlaneNum"]
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)

    g["RandRdSpeed"] = speed * g["ChNum"]
    g["RandRdSpeed1024base"] = speed2 * g["ChNum"]
    IOPS = g["PlaneNum"] * g["CeNum"] * 1000 * 1000 / Tmp2
    g["RndRdIops"] = IOPS * g["ChNum"]


def calc_seq_wr_performance(g):
    tCALS = param_in_flash(g["FlashType"], "tCALS_t")
    tCALH = param_in_flash(g["FlashType"], "tCALH_t")
    tWC = param_in_flash(g["FlashType"], "tWC_t")
    tcmd = tCALS + tCALH
    t6addr = tCALS + tWC * 6 + tCALH
    t6addrcmd = tcmd + t6addr + tcmd

    tDa = tWC
    t80Addr = tcmd + t6addr
    t11Cmd = tcmd
    t81Addr = tcmd + t6addr
    t15Cmd = tcmd

    tPLPBSY = param_in_flash(g["FlashType"], "tPLPBSY_t")
    tPROG = param_in_flash(g["FlashType"], "tPROG_t")
    tPCBSY = param_in_flash(g["FlashType"], "tPCBSY2_t")
    tBERS_t = param_in_flash(g["FlashType"], "tBERS_t")

    tADL = param_in_flash(g["FlashType"], "tADL_t")
    tWPRE = param_in_flash(g["FlashType"], "tWPRE_t")
    tWPST = param_in_flash(g["FlashType"], "tWPST_t")
    tCHZ = param_in_flash(g["FlashType"], "tCHZ_t")
    tCS = param_in_flash(g["FlashType"], "tCS_t")
    tMPP = param_in_flash(g["FlashType"], "tMPP_t")
    tWB = param_in_flash(g["FlashType"], "tWB_t")

    tRPRE = param_in_flash(g["FlashType"], "tRPRE_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tRPST = tDQSRE + tRC
    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tRHW = param_in_flash(g["FlashType"], "tRHW_t")
    tCheckSts = tcmd + tWHR + tRPRE + g["unit"] + tRPST + tRHW

    tCDQSH = param_in_flash(g["FlashType"], "tCDQSH_t")
    tDBS = param_in_flash(g["FlashType"], "tDBS_t")

    if tWB > (tCDQSH + tDBS):
        tmp3 = tWB
    else:
        tmp3 = tCDQSH + tDBS

    tRawPageTransfer = (g["PageSize"] + g["WarmUpCycle"]) * g["unit"]

    if g["isDummyModeEn"]:
        t8011PageTransfer = t80Addr + tADL + tRawPageTransfer + tWPST + tCALS + tCDQSH + tDBS + tMPP + tCHZ + tCS
    else:
        t8011PageTransfer = t80Addr + tADL + tRawPageTransfer + tWPST + tCALS + tmp3 + tCheckSts

    t8115PageTransfer = t81Addr + tADL + tRawPageTransfer + tWPST + tCALS + tCDQSH + tDBS
    t80118115MultiPlaneTransfer = tDa + t8011PageTransfer * (g["PlaneNum"] - 1) + t8115PageTransfer
    tCkSts80118115MultiPlaneTransfer = t80118115MultiPlaneTransfer + tCheckSts

    if g["isCacheProg"]:
        TimeTmp = tPROG - t80118115MultiPlaneTransfer
    else:
        TimeTmp = tPROG

    Tmp1 = g["PlaneNum"] * g["CeNum"] * g["PageCnt"] * 16384

    if TimeTmp > (t80118115MultiPlaneTransfer * (g["CeNum"] - 1)):
        if g["isCacheProg"]:
            Tmp2 = (tCkSts80118115MultiPlaneTransfer + (tPROG - t80118115MultiPlaneTransfer)) * (g["PageCnt"] - 1) + (tCkSts80118115MultiPlaneTransfer + tPROG)
        else:
            Tmp2 = (tCkSts80118115MultiPlaneTransfer + tPROG) * g["PageCnt"]
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tBERS_t)
        RealSpeed2 = Tmp1 / ((Tmp2 + tBERS_t) * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tCkSts80118115MultiPlaneTransfer * g["CeNum"] * g["PageCnt"] + tPROG
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tBERS_t)
        RealSpeed2 = Tmp1 / ((Tmp2 + tBERS_t) * 1.024 * 1.024 * 1.024)

    g["SeqWrSpeed"] = speed * g["ChNum"]
    g["SeqWrSpeed1024base"] = speed2 * g["ChNum"]
    g["RealSeqWrSpeed"] = RealSpeed * g["ChNum"]
    g["RealSeqWrSpeedTabupdate"] = (1 - g["TabUpdateLoss"]) * g["RealSeqWrSpeed"]
    g["RealSeqWrSpeed1024base"] = RealSpeed2 * g["ChNum"]
    g["RealSeqWrSpeed1024baseTabupdate"] = (1 - g["TabUpdateLoss"]) * g["RealSeqWrSpeed1024base"]


def calc_xlc_seq_wr_performance(g):
    tCALS = param_in_flash(g["FlashType"], "tCALS_t")
    tCALH = param_in_flash(g["FlashType"], "tCALH_t")
    tWC = param_in_flash(g["FlashType"], "tWC_t")
    tcmd = tCALS + tCALH
    t6addr = tCALS + tWC * 6 + tCALH
    t6addrcmd = tcmd + t6addr + tcmd

    tDa = tWC
    t80Addr = tcmd + t6addr
    t11Cmd = tcmd
    t81Addr = tcmd + t6addr
    t15Cmd = tcmd

    tPLPBSY = param_in_flash(g["FlashType"], "tPLPBSY_t")
    tPROG = param_in_flash(g["FlashType"], "tPROG_t")
    tPCBSY = param_in_flash(g["FlashType"], "tPCBSY2_t")
    tBERS_t = param_in_flash(g["FlashType"], "tBERS_t")
    tXLCBERS = param_in_flash(g["FlashType"], "tXLCBERS_t")

    tADL = param_in_flash(g["FlashType"], "tADL_t")
    tWPRE = param_in_flash(g["FlashType"], "tWPRE_t")
    tWPST = param_in_flash(g["FlashType"], "tWPST_t")
    tCHZ = param_in_flash(g["FlashType"], "tCHZ_t")
    tCS = param_in_flash(g["FlashType"], "tCS_t")
    tMPP = param_in_flash(g["FlashType"], "tMPP_t")
    tWB = param_in_flash(g["FlashType"], "tWB_t")

    tRPRE = param_in_flash(g["FlashType"], "tRPRE_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tRPST = tDQSRE + tRC
    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tRHW = param_in_flash(g["FlashType"], "tRHW_t")
    tCheckSts = tcmd + tWHR + tRPRE + g["unit"] + tRPST + tRHW

    tCDQSH = param_in_flash(g["FlashType"], "tCDQSH_t")
    tDBS = param_in_flash(g["FlashType"], "tDBS_t")

    if tWB > (tCDQSH + tDBS):
        tmp3 = tWB
    else:
        tmp3 = tCDQSH + tDBS

    tRawPageTransfer = (g["PageSize"] + g["WarmUpCycle"]) * g["unit"]

    if g["isDummyModeEn"]:
        t8011PageTransfer = t80Addr + tADL + tRawPageTransfer + tWPST + tCALS + tCDQSH + tDBS + tMPP + tCHZ + tCS
    else:
        t8011PageTransfer = t80Addr + tADL + tRawPageTransfer + tWPST + tCALS + tmp3 + tCheckSts

    t8115PageTransfer = t81Addr + tADL + tRawPageTransfer + tWPST + tCALS + tCDQSH + tDBS
    t80118115MultiPlaneTransfer = tDa + t8011PageTransfer * (g["PlaneNum"] - 1) + t8115PageTransfer
    tCkSts80118115MultiPlaneAndWL = g["pageofWl"] * (tCheckSts + t80118115MultiPlaneTransfer) + (g["pageofWl"] - 1) * tPCBSY

    tXLCPROG = param_in_flash(g["FlashType"], "tXLCPROG_t")
    TimeTmp = tXLCPROG

    Tmp1 = g["PlaneNum"] * g["pageofWl"] * g["CeNum"] * g["PageCnt"] * 16384

    if TimeTmp > (tCkSts80118115MultiPlaneAndWL * (g["CeNum"] - 1)):
        Tmp2 = (tCkSts80118115MultiPlaneAndWL + tXLCPROG) * g["PageCnt"]
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tXLCBERS)
        RealSpeed2 = Tmp1 / ((Tmp2 + tXLCBERS) * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tCkSts80118115MultiPlaneAndWL * g["CeNum"] * g["PageCnt"] + tXLCPROG
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tXLCBERS)
        RealSpeed2 = Tmp1 / ((Tmp2 + tXLCBERS) * 1.024 * 1.024 * 1.024)

    g["SeqWrSpeed"] = speed * g["ChNum"]
    g["SeqWrSpeed1024base"] = speed2 * g["ChNum"]
    g["RealSeqWrSpeed"] = RealSpeed * g["ChNum"]
    g["RealSeqWrSpeed1024base"] = RealSpeed2 * g["ChNum"]


def sca_calc_seq_rd_performance(g):
    tCELCLK = param_in_flash(g["FlashType"], "tCELCLK_t")
    tCACI = param_in_flash(g["FlashType"], "tCACI_t")

    tmpCACI = 0
    while tmpCACI <= tCACI:
        tmpCACI = tmpCACI + g["dfiCycle"]
    tCACI = tmpCACI

    tcmd = 3 * tCACI
    tDACmd = tcmd
    taddr = tcmd
    t00Addr32 = tcmd + 6 * taddr + tcmd
    t00Addr30 = t00Addr32
    tSCE = tcmd
    tSCT = tcmd

    tWB = param_in_flash(g["FlashType"], "tWB_t")
    tRR = param_in_flash(g["FlashType"], "tRR_t")
    tPLRBSY = param_in_flash(g["FlashType"], "tPLRBSY_t")
    tR = param_in_flash(g["FlashType"], "tR_t")

    if g["isDummyModeEn"]:
        tSlcMultiPlaneRd = tCELCLK + tDACmd + t00Addr32 * (g["PlaneNum"] - 1) + t00Addr30 + tWB + tR
    else:
        tSlcMultiPlaneRd = tCELCLK + tDACmd + (t00Addr32 + tWB + tPLRBSY) * (g["PlaneNum"] - 1) + t00Addr30 + tWB + tR

    tRCBSY = param_in_flash(g["FlashType"], "tRCBSY_t")
    t31Cmd = tcmd
    tCLKLCE = param_in_flash(g["FlashType"], "tCLKLCE_t")
    tCacheRd = tCELCLK + tDACmd + t31Cmd + tCLKLCE

    if g["isToEnableNTO"]:
        tNTOon = tCELCLK + tcmd + tCLKLCE
    else:
        tNTOon = 0
    tNTOoff = tNTOon

    t05AddrE0 = tcmd + 6 * taddr + tcmd
    tRPRE2 = param_in_flash(g["FlashType"], "tRPRE2_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tSCR = param_in_flash(g["FlashType"], "tSCR_t")
    tRPST_CA = tDQSRE + 0.5 * tRC
    tRPSTH_CA = param_in_flash(g["FlashType"], "tRPSTH_CA_t")

    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tCACO = param_in_flash(g["FlashType"], "tCACO_t")
    tmpCACO = 0
    while tmpCACO <= tCACO:
        tmpCACO = tmpCACO + g["dfiCycle"]
    tCACO = tmpCACO

    tCEH2 = param_in_flash(g["FlashType"], "tCEH2_t")
    tCLKCA = param_in_flash(g["FlashType"], "tCLKCA_t")
    tW2R_CA = param_in_flash(g["FlashType"], "tW2R_CA_t")
    tCACOPST = tCLKCA + 0.5 * tCACO
    tR2W_CA = tCACOPST + tCEH2 + tCELCLK
    tCheckSts = tCELCLK + tcmd + tWHR + tCACI + tW2R_CA + tCACO * 4 + tR2W_CA

    if g["isToFinalEdge"]:
        tSCT = 0

    tSCRES = param_in_flash(g["FlashType"], "tSCRES_t")
    tCCS = param_in_flash(g["FlashType"], "tCCS_t")

    if tSCE > tSCRES:
        tmp3 = tSCE
    else:
        tmp3 = tSCRES

    if (tNTOon + tmp3 + tSCR) > tCCS:
        tmp4 = tNTOon + tmp3 + tSCR
    else:
        tmp4 = tCCS

    if tRPSTH_CA > (tNTOoff + tCLKLCE + tCELCLK + t05AddrE0):
        CalcMode = False
    else:
        CalcMode = True

    if CalcMode:
        t4kTransfer = tCELCLK + t05AddrE0 + tmp4 + tRPRE2 + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST_CA + tSCT + tNTOoff + tCLKLCE
    else:
        t4kTransfer = tmp4 + tRPRE2 + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST_CA + tSCT + tRPSTH_CA

    if g["isSeq4kRd"]:
        tPageTransfer = t4kTransfer * 4
    else:
        tRawPageTransfer = (g["PageSize"] + g["WarmUpCycle"]) * g["unit"]
        if CalcMode:
            tPageTransfer = tCELCLK + tSCE + tRPRE2 + tRawPageTransfer + tRPST_CA + tSCT + tNTOoff + tCLKLCE
        else:
            tPageTransfer = tmp4 + tRPRE2 + tRawPageTransfer + tRPST_CA + tSCT + tRPSTH_CA

    tMultiPlaneTransfer = tCacheRd + tPageTransfer * g["PlaneNum"]
    tMultiPlaneTransfer = tMultiPlaneTransfer - (t05AddrE0 + tmp4 - tmp3 - tSCR)

    Tmp1 = g["PlaneNum"] * g["CeNum"] * g["PageCnt"] * 16384
    if tRCBSY > (tMultiPlaneTransfer * (g["CeNum"] - 1)):
        Tmp2 = (tMultiPlaneTransfer + tRCBSY) * g["PageCnt"] + tSlcMultiPlaneRd
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tMultiPlaneTransfer * g["CeNum"] * g["PageCnt"] + tSlcMultiPlaneRd
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)

    g["SeqRdSpeed"] = speed * g["ChNum"]
    g["SeqRdSpeed1024base"] = speed2 * g["ChNum"]


def sca_calc_rand_rd_performance(g):
    tCELCLK = param_in_flash(g["FlashType"], "tCELCLK_t")
    tCACI = param_in_flash(g["FlashType"], "tCACI_t")

    tmpCACI = 0
    while tmpCACI <= tCACI:
        tmpCACI = tmpCACI + g["dfiCycle"]
    tCACI = tmpCACI

    tcmd = 3 * tCACI
    tDACmd = tcmd
    taddr = tcmd
    t00Addr32 = tcmd + 6 * taddr + tcmd
    t00Addr30 = t00Addr32
    t77cmd4addr = tcmd + 4 * taddr

    tSCE = tcmd
    tSCT = tcmd

    tWB = param_in_flash(g["FlashType"], "tWB_t")
    tRR = param_in_flash(g["FlashType"], "tRR_t")
    tPLRBSY = param_in_flash(g["FlashType"], "tPLRBSY_t")
    tR = param_in_flash(g["FlashType"], "tR_t")

    tCLKLCE = param_in_flash(g["FlashType"], "tCLKLCE_t")

    if g["isToEnableNTO"]:
        tNTOon = tCELCLK + tcmd + tCLKLCE
    else:
        tNTOon = 0
    tNTOoff = tNTOon

    t05AddrE0 = tcmd + 6 * taddr + tcmd
    tRPRE2 = param_in_flash(g["FlashType"], "tRPRE2_t")
    tDQSRE = param_in_flash(g["FlashType"], "tDQSRE_t")
    tRC = g["unit"] * 2
    tSCR = param_in_flash(g["FlashType"], "tSCR_t")
    tRPST_CA = tDQSRE + 0.5 * tRC
    tRPSTH_CA = param_in_flash(g["FlashType"], "tRPSTH_CA_t")

    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tCACO = param_in_flash(g["FlashType"], "tCACO_t")
    tmpCACO = 0
    while tmpCACO <= tCACO:
        tmpCACO = tmpCACO + g["dfiCycle"]
    tCACO = tmpCACO

    tCEH2 = param_in_flash(g["FlashType"], "tCEH2_t")
    tCLKCA = param_in_flash(g["FlashType"], "tCLKCA_t")
    tW2R_CA = param_in_flash(g["FlashType"], "tW2R_CA_t")
    tCACOPST = tCLKCA + 0.5 * tCACO
    tR2W_CA = tCACOPST + tCEH2 + tCELCLK
    tCheckSts = tCELCLK + t77cmd4addr + tWHR + tCACI + tW2R_CA + tCACO * 4 + tR2W_CA

    if g["isToFinalEdge"]:
        tSCT = 0

    tSCRES = param_in_flash(g["FlashType"], "tSCRES_t")
    tCCS = param_in_flash(g["FlashType"], "tCCS_t")

    if tSCE > tSCRES:
        tmp3 = tSCE
    else:
        tmp3 = tSCRES

    if (tNTOon + tmp3 + tSCR) > tCCS:
        tmp4 = tNTOon + tmp3 + tSCR
    else:
        tmp4 = tCCS

    if tRPSTH_CA > (tNTOoff + tCLKLCE + tCELCLK + t05AddrE0):
        CalcMode = False
    else:
        CalcMode = True

    if CalcMode:
        tAipr4kTransfer = tCELCLK + t05AddrE0 + tmp4 + tRPRE2 + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST_CA + tSCT + tNTOoff + tCLKLCE
    else:
        tAipr4kTransfer = tmp4 + tRPRE2 + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST_CA + tSCT + tRPSTH_CA

    tAipr4kTransfer = tCELCLK + tSCE + tSCR + tRPRE2 + (g["4kSize"] + g["WarmUpCycle"]) * g["unit"] + tRPST_CA + tSCT + tNTOoff + tCLKLCE

    tMultiPlane4KApirTransfer = tAipr4kTransfer * g["PlaneNum"]

    Tmp1 = g["PlaneNum"] * g["CeNum"] * 4096
    if tR > (tAipr4kTransfer * (g["CeNum"] * g["PlaneNum"] - 1)):
        Tmp2 = tAipr4kTransfer + tR
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tMultiPlane4KApirTransfer * g["CeNum"]
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)

    g["RandRdSpeed"] = speed * g["ChNum"]
    g["RandRdSpeed1024base"] = speed2 * g["ChNum"]
    IOPS = g["PlaneNum"] * g["CeNum"] * 1000 * 1000 / Tmp2
    g["RndRdIops"] = IOPS * g["ChNum"]


def sca_calc_seq_wr_performance(g):
    tCELCLK = param_in_flash(g["FlashType"], "tCELCLK_t")
    tCLKLCE = param_in_flash(g["FlashType"], "tCLKLCE_t")
    tCACI = param_in_flash(g["FlashType"], "tCACI_t")

    tmpCACI = 0
    while tmpCACI <= tCACI:
        tmpCACI = tmpCACI + g["dfiCycle"]
    tCACI = tmpCACI

    tcmd = 3 * tCACI
    t10Cmd = tcmd
    t11Cmd = tcmd
    t15Cmd = tcmd
    taddr = tcmd
    tDa = tcmd
    t80Addr12 = tcmd + 6 * taddr
    t81Addr12 = tcmd + 6 * taddr
    tSCE = tcmd
    tSCT = tcmd

    tPLPBSY = param_in_flash(g["FlashType"], "tPLPBSY_t")
    tPROG = param_in_flash(g["FlashType"], "tPROG_t")
    tPCBSY = param_in_flash(g["FlashType"], "tPCBSY2_t")
    tBERS_t = param_in_flash(g["FlashType"], "tBERS_t")

    tADL = param_in_flash(g["FlashType"], "tADL_t")
    tWPST_CA = param_in_flash(g["FlashType"], "tWPST_CA_t")
    tWPSTH_CA = param_in_flash(g["FlashType"], "tWPSTH_CA_t")
    tMPP = param_in_flash(g["FlashType"], "tMPP_t")
    tWB = param_in_flash(g["FlashType"], "tWB_t")

    tWHR = param_in_flash(g["FlashType"], "tWHR_t")
    tCACO = param_in_flash(g["FlashType"], "tCACO_t")
    tmpCACO = 0
    while tmpCACO <= tCACO:
        tmpCACO = tmpCACO + g["dfiCycle"]
    tCACO = tmpCACO
    tCEH2 = param_in_flash(g["FlashType"], "tCEH2_t")
    tCLKCA = param_in_flash(g["FlashType"], "tCLKCA_t")
    tW2R_CA = param_in_flash(g["FlashType"], "tW2R_CA_t")
    tCACOPST = tCLKCA + 0.5 * tCACO
    tR2W_CA = tCACOPST + tCEH2 + tCELCLK
    tCheckSts = tCELCLK + tcmd + tWHR + tCACI + tW2R_CA + tCACO * 4 + tR2W_CA

    if g["isToEnableNTO"]:
        tNTOon = tCELCLK + tcmd + tCLKLCE
    else:
        tNTOon = 0
    tNTOoff = tNTOon

    if g["isToFinalEdge"]:
        tSCT = 0

    if g["isDummyModeEn"]:
        if tWPSTH_CA < tMPP:
            tmp3 = tMPP
        else:
            tmp3 = tWPSTH_CA
    else:
        if tWPSTH_CA < (tWB + tCheckSts):
            tmp3 = tWB + tCheckSts
        else:
            tmp3 = tWPSTH_CA

    tRawPageTransfer = (g["PageSize"] + g["WarmUpCycle"]) * g["unit"]

    t8011PageTransfer = tCELCLK + tDa + t80Addr12 + tADL + tRawPageTransfer + tWPST_CA + tSCT + tNTOoff + t11Cmd + tmp3
    t8115PageTransfer = tCELCLK + tDa + t81Addr12 + tADL + tRawPageTransfer + tWPST_CA + tSCT + tNTOoff + t15Cmd + tCLKLCE
    t80118115MultiPlaneTransfer = t8011PageTransfer * (g["PlaneNum"] - 1) + t8115PageTransfer
    tCkSts80118115MultiPlaneTransfer = t80118115MultiPlaneTransfer

    if g["isCacheProg"]:
        TimeTmp = tPROG - t80118115MultiPlaneTransfer
    else:
        TimeTmp = tPROG

    Tmp1 = g["PlaneNum"] * g["CeNum"] * g["PageCnt"] * 16384
    if TimeTmp > (t80118115MultiPlaneTransfer * (g["CeNum"] - 1)):
        if g["isCacheProg"]:
            Tmp2 = (tCkSts80118115MultiPlaneTransfer + (tPROG - t80118115MultiPlaneTransfer)) * (g["PageCnt"] - 1) + (tCkSts80118115MultiPlaneTransfer + tPROG)
        else:
            Tmp2 = (tCkSts80118115MultiPlaneTransfer + tPROG) * g["PageCnt"]
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tBERS_t)
        RealSpeed2 = Tmp1 / ((Tmp2 + tBERS_t) * 1.024 * 1.024 * 1.024)
    else:
        Tmp2 = tCkSts80118115MultiPlaneTransfer * g["CeNum"] * g["PageCnt"] + tPROG
        speed = Tmp1 / Tmp2
        speed2 = Tmp1 / (Tmp2 * 1.024 * 1.024 * 1.024)
        RealSpeed = Tmp1 / (Tmp2 + tBERS_t)
        RealSpeed2 = Tmp1 / ((Tmp2 + tBERS_t) * 1.024 * 1.024 * 1.024)

    g["SeqWrSpeed"] = speed * g["ChNum"]
    g["SeqWrSpeed1024base"] = speed2 * g["ChNum"]
    g["RealSeqWrSpeed"] = RealSpeed * g["ChNum"]
    g["RealSeqWrSpeed1024base"] = RealSpeed2 * g["ChNum"]


# ======================== Streamlit UI ========================
def main():
    if not check_access():
        return

    st.set_page_config(page_title="SSD 控制器性能计算器", layout="wide")

    # 得一微电子 Yeestor - 科技精密风格界面
    st.markdown("""
    <style>
        /* 导入独特字体 */
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700;900&display=swap');

        /* CSS变量定义 - 精密配色系统 */
        :root {
            --yeestor-deep: #0f2b4d;
            --yeestor-primary: #1a365d;
            --yeestor-accent: #2d5a87;
            --yeestor-glow: #38a169;
            --yeestor-glow-bright: #48c774;
            --yeestor-surface: #f7fafc;
            --yeestor-text: #1a1a1a;
            --yeestor-muted: #718096;
            --metric-bg: linear-gradient(145deg, rgba(255,255,255,0.98) 0%, rgba(247,250,252,0.95) 100%);
            --card-shine: linear-gradient(135deg, rgba(56,161,105,0.1) 0%, transparent 50%);
        }

        /* 主背景 - 科技网格纹理 */
        .stApp {
            background:
                radial-gradient(circle at 20% 80%, rgba(56,161,105,0.08) 0%, transparent 40%),
                radial-gradient(circle at 80% 20%, rgba(26,54,93,0.08) 0%, transparent 40%),
                linear-gradient(135deg, #f0f7ff 0%, #e8f5f0 50%, #f7fafc 100%);
            background-attachment: fixed;
        }

        /* 科技网格背景纹理 */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image:
                radial-gradient(circle at 1px 1px, rgba(26,54,93,0.03) 1px, transparent 0);
            background-size: 32px 32px;
            pointer-events: none;
            z-index: 0;
        }
        /* 侧边栏 - 深邃精密风格 */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f2b4d 0%, #1a365d 40%, #2d5a87 100%);
            box-shadow: inset -1px 0 8px rgba(0,0,0,0.1);
            position: relative;
        }
        /* 侧边栏微妙光效 */
        section[data-testid="stSidebar"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(ellipse at 50% 0%, rgba(56,161,105,0.15) 0%, transparent 60%);
            pointer-events: none;
        }
        /* 侧边栏内所有元素 */
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] .stHeader {
            color: #ffffff;
        }
        /* 侧边栏标签 - 精密字体 */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stCheckbox label {
            color: #ffffff !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            letter-spacing: 0.3px;
            font-family: 'Noto Sans SC', 'JetBrains Mono', sans-serif;
        }
        /* 侧边栏选择框容器 - 悬浮效果 */
        section[data-testid="stSidebar"] .stSelectbox,
        section[data-testid="stSidebar"] .stCheckbox {
            background-color: rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 10px 14px;
            margin-bottom: 8px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.25s ease;
        }
        section[data-testid="stSidebar"] .stSelectbox:hover,
        section[data-testid="stSidebar"] .stCheckbox:hover {
            background-color: rgba(255, 255, 255, 0.12);
            border-color: rgba(56,161,105,0.3);
        }
        /* 侧边栏下拉选择框 - 精密输入框 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
            background-color: rgba(247,250,252,0.95);
            border: 2px solid rgba(56,161,105,0.4);
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            transition: all 0.2s ease;
        }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"]:hover {
            border-color: #38a169;
            box-shadow: 0 0 12px rgba(56,161,105,0.3);
        }
        /* 侧边栏选择框所有文字 - 精密黑色 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"],
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] * {
            color: #0f2b4d !important;
            fill: #0f2b4d !important;
            font-family: 'JetBrains Mono', 'Noto Sans SC', monospace;
        }
        /* 侧边栏下拉选项列表 - 精密白色 */
        section[data-testid="stSidebar"] [data-baseweb="listbox"] {
            background-color: #ffffff !important;
            border: 2px solid #38a169;
            border-radius: 10px;
            box-shadow: 0 8px 24px rgba(15,43,77,0.2);
        }
        section[data-testid="stSidebar"] [data-baseweb="listbox"] li {
            color: #0f2b4d !important;
            background-color: #ffffff !important;
            font-family: 'JetBrains Mono', monospace;
            padding: 12px 16px;
            transition: all 0.15s ease;
        }
        section[data-testid="stSidebar"] [data-baseweb="listbox"] li:hover {
            background-color: #f0f7ff !important;
            color: #1a365d !important;
            border-left: 3px solid #38a169;
        }
        section[data-testid="stSidebar"] [data-baseweb="listbox"] li[aria-selected="true"] {
            background-color: linear-gradient(90deg, #d4edda 0%, #f0f7ff 100%) !important;
            color: #0f2b4d !important;
            font-weight: 600;
        }
        /* 针对全局下拉弹出层 */
        div[data-baseweb="listbox"] {
            background-color: #ffffff !important;
            border: 2px solid #38a169;
            border-radius: 10px;
            box-shadow: 0 8px 24px rgba(15,43,77,0.25);
        }
        div[data-baseweb="listbox"] li {
            color: #0f2b4d !important;
            background-color: #ffffff !important;
            font-family: 'JetBrains Mono', monospace;
            padding: 12px 16px;
        }
        div[data-baseweb="listbox"] li:hover {
            background-color: #f0f7ff !important;
            border-left: 3px solid #38a169;
        }
        /* 侧边栏复选框 - 精密风格 */
        section[data-testid="stSidebar"] .stCheckbox input[type="checkbox"] {
            accent-color: #38a169;
            width: 18px;
            height: 18px;
            border-radius: 4px;
        }
        /* 侧边栏分隔线 - 精密线条 */
        section[data-testid="stSidebar"] hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, rgba(56,161,105,0.5) 0%, rgba(255,255,255,0.2) 50%, rgba(56,161,105,0.5) 100%);
            margin: 15px 10px;
        }
        /* 侧边栏信息提示 */
        section[data-testid="stSidebar"] .stAlert {
            background-color: rgba(56,161,105,0.15);
            border: 1px solid rgba(56,161,105,0.4);
            color: #ffffff;
            border-radius: 8px;
        }
        /* 标题样式 - 精密主品牌蓝 */
        h1 {
            color: #0f2b4d;
            font-weight: 700;
            font-family: 'Noto Sans SC', sans-serif;
            font-size: 34px;
            text-align: center;
            margin-bottom: 20px;
            position: relative;
            letter-spacing: 1px;
        }
        h1::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 3px;
            background: linear-gradient(90deg, #38a169 0%, #2d5a87 50%, #38a169 100%);
            border-radius: 2px;
        }
        h2, h3 {
            color: #1a365d;
            font-family: 'Noto Sans SC', sans-serif;
            font-weight: 600;
        }
        /* 主按钮样式 - 精密得一绿 */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #38a169 0%, #2f855a 100%);
            color: white;
            border: none;
            font-weight: 600;
            font-family: 'Noto Sans SC', sans-serif;
            border-radius: 10px;
            padding: 14px 28px;
            box-shadow: 0 4px 12px rgba(56,161,105,0.35);
            transition: all 0.25s ease;
            letter-spacing: 0.5px;
        }
        .stButton > button[kind="primary"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(56,161,105,0.45);
            background: linear-gradient(135deg, #48c774 0%, #38a169 100%);
        }
        .stButton > button[kind="primary"]:active {
            transform: translateY(-1px);
        }
        /* 主内容区选择框样式 - 精密风格 */
        .stSelectbox label, .stCheckbox label {
            color: #0f2b4d !important;
            font-weight: 600;
            font-family: 'Noto Sans SC', sans-serif;
        }
        /* 分隔线 - 精密渐变 */
        hr {
            border: none;
            height: 2px;
            background: linear-gradient(90deg, #0f2b4d 0%, #38a169 25%, #2d5a87 50%, #38a169 75%, #0f2b4d 100%);
            margin: 25px 0;
            opacity: 0.8;
        }
        /* Metric 卡片 - 精密数据展示 */
        [data-testid="stMetric"] {
            background: var(--metric-bg);
            border: 2px solid #38a169;
            border-radius: 14px;
            padding: 18px 20px;
            box-shadow:
                0 3px 12px rgba(15,43,77,0.15),
                inset 0 1px 0 rgba(255,255,255,0.8);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        [data-testid="stMetric"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--card-shine);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow:
                0 8px 24px rgba(56,161,105,0.25),
                inset 0 1px 0 rgba(255,255,255,0.9);
            border-color: #48c774;
        }
        [data-testid="stMetric"]:hover::before {
            opacity: 1;
        }
        [data-testid="stMetric"] label {
            color: #2d5a87 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            font-family: 'Noto Sans SC', sans-serif;
            letter-spacing: 0.3px;
        }
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #0f2b4d !important;
            font-weight: 700 !important;
            font-size: 26px !important;
            font-family: 'JetBrains Mono', monospace;
        }
        /* 信息提示框 - 精密风格 */
        .stAlert {
            border-radius: 12px;
            border-left: 4px solid;
            font-family: 'Noto Sans SC', sans-serif;
        }
        .stAlert[data-baseweb="notification"] {
            background-color: rgba(247,250,252,0.9);
        }
        /* 品牌宣传区域 - 精密科技风格 */
        .brand-banner {
            background: linear-gradient(135deg, #0f2b4d 0%, #1a365d 25%, #2d5a87 50%, #38a169 80%, #48c774 100%);
            color: white;
            padding: 28px 40px;
            border-radius: 18px;
            margin: 25px 0;
            box-shadow:
                0 6px 20px rgba(15,43,77,0.35),
                inset 0 2px 0 rgba(255,255,255,0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
        }
        /* 品牌光效 */
        .brand-banner::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(56,161,105,0.2) 0%, transparent 50%);
            animation: brandGlow 8s ease-in-out infinite;
        }
        @keyframes brandGlow {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(20%, 20%); }
        }
        .brand-banner-left h1 {
            color: white;
            margin: 0;
            font-size: 30px;
            font-weight: 900;
            letter-spacing: 3px;
            font-family: 'Noto Sans SC', sans-serif;
            text-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        .brand-banner-left p {
            margin: 10px 0 0 0;
            opacity: 0.85;
            font-size: 15px;
            font-family: 'Noto Sans SC', sans-serif;
            letter-spacing: 1px;
        }
        .brand-banner-right {
            text-align: right;
            position: relative;
            z-index: 1;
        }
        .brand-banner-right .tagline {
            font-size: 14px;
            opacity: 0.75;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: 2px;
        }
        /* 配置卡片 - 精密数据展示 */
        .config-card {
            background: var(--metric-bg);
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 18px;
            margin: 12px 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            transition: all 0.25s ease;
            position: relative;
        }
        .config-card:hover {
            box-shadow: 0 6px 18px rgba(15,43,77,0.12);
            border-color: rgba(56,161,105,0.3);
        }
        .config-card-title {
            color: #0f2b4d;
            font-weight: 700;
            font-size: 17px;
            margin-bottom: 12px;
            border-bottom: 2px solid #38a169;
            padding-bottom: 8px;
            font-family: 'Noto Sans SC', sans-serif;
            letter-spacing: 1px;
        }
        .config-card p {
            margin: 8px 0;
            font-size: 14px;
            font-family: 'Noto Sans SC', sans-serif;
        }
        .config-card p strong {
            color: #2d5a87;
            font-weight: 600;
        }
        /* 结果展示卡片 - 精密数据面板 */
        .result-card {
            background: linear-gradient(135deg, #0f2b4d 0%, #1a365d 50%, #2d5a87 100%);
            color: white;
            border-radius: 18px;
            padding: 25px;
            margin: 15px 0;
            box-shadow:
                0 6px 20px rgba(15,43,77,0.35),
                inset 0 2px 0 rgba(255,255,255,0.1);
            position: relative;
            overflow: hidden;
        }
        /* 结果卡片光效 */
        .result-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 200%;
            height: 100%;
            background: linear-gradient(90deg, transparent 0%, rgba(56,161,105,0.15) 50%, transparent 100%);
            animation: resultShine 3s ease-in-out infinite;
        }
        @keyframes resultShine {
            0% { transform: translateX(-50%); }
            100% { transform: translateX(50%); }
        }
        .result-card-title {
            color: #38a169;
            font-weight: 800;
            font-size: 19px;
            margin-bottom: 18px;
            text-align: center;
            font-family: 'Noto Sans SC', sans-serif;
            letter-spacing: 2px;
            text-shadow: 0 1px 4px rgba(0,0,0,0.3);
            position: relative;
            z-index: 1;
        }
        /* Metric增强 */
        [data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid #38a169 !important;
            border-radius: 12px !important;
            padding: 20px !important;
            box-shadow: 0 3px 10px rgba(26, 54, 93, 0.15) !important;
            transition: transform 0.2s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(26, 54, 93, 0.25) !important;
        }
        [data-testid="stMetric"] label {
            color: #2d5a87 !important;
            font-size: 14px !important;
            font-weight: 500 !important;
        }
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #1a365d !important;
            font-weight: 700 !important;
            font-size: 24px !important;
        }
        /* Tabs样式 - 精密导航 */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(247,250,252,0.9);
            border-radius: 12px 12px 0 0;
            padding: 12px 24px;
            font-weight: 600;
            font-family: 'Noto Sans SC', sans-serif;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(240,247,255,1);
            border-color: rgba(56,161,105,0.3);
        }
        .stTabs [aria-selected="true"] {
            background-color: #0f2b4d !important;
            color: white !important;
            border-color: #38a169;
        }
        /* 页脚 - 精密信息区域 */
        .footer-info {
            text-align: center;
            padding: 30px;
            color: #4a5568;
            font-size: 14px;
            background: var(--metric-bg);
            border-radius: 14px;
            margin-top: 25px;
            border: 1px solid rgba(56,161,105,0.2);
            box-shadow: 0 3px 12px rgba(15,43,77,0.08);
            font-family: 'Noto Sans SC', sans-serif;
        }
        .footer-info a {
            color: #38a169;
            font-weight: 600;
            text-decoration: none;
            transition: color 0.2s ease;
        }
        .footer-info a:hover {
            color: #48c774;
        }
        .footer-info p {
            margin: 8px 0;
            letter-spacing: 0.3px;
        }
        /* 加载动画 */
        .stSpinner > div {
            border-color: #38a169 transparent transparent transparent;
        }
        /* 文字选中样式 */
        ::selection {
            background: rgba(56,161,105,0.25);
            color: #0f2b4d;
        }
    </style>
    """, unsafe_allow_html=True)

    # 品牌宣传 Banner
    st.markdown("""
    <div class="brand-banner">
        <div class="brand-banner-left">
            <h1>得一微电子 Yeestor</h1>
            <p>专业 SSD 控制器解决方案 | 高性能存储技术</p>
        </div>
        <div class="brand-banner-right">
            <p class="tagline">Innovation · Performance · Reliability</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.title("SSD 控制器性能计算器")
    st.markdown("---")

    with st.sidebar:
        # 侧边栏品牌宣传 - 精密科技风格
        st.markdown("""
        <div style="text-align: center; padding: 15px 0;">
            <h2 style="color: #38a169; margin: 0; font-size: 24px; font-weight: 800; letter-spacing: 2px; font-family: 'Noto Sans SC', sans-serif;">Yeestor</h2>
            <p style="color: #ffffff; opacity: 0.85; font-size: 13px; margin-top: 8px; letter-spacing: 1px; font-family: 'Noto Sans SC', sans-serif;">得一微电子</p>
            <p style="color: rgba(56,161,105,0.8); font-size: 11px; margin-top: 5px; font-family: 'JetBrains Mono', monospace;">Precision · Innovation</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.header("配置参数")

        ctrl_type = st.selectbox("控制器类型", list(CONTROLLERS.keys()))
        ctrl = CONTROLLERS[ctrl_type]
        max_ch = int(ctrl["ChNum"])
        ch_num = st.selectbox("通道数量(ChNum)", list(range(1, max_ch + 1))[::-1])

        max_io = ctrl["IoSpeed"]
        available_io = [s for s in IO_SPEED_OPTIONS if s <= max_io]
        io_speed = st.selectbox("IO 速度 (MT/s)", available_io)

        ce_num = st.selectbox("CE 数量", list(range(1, 9)))
        warm_up = st.selectbox("WarmUp 周期", [4, 2, 1, 0])

        flash_type = st.selectbox("Flash 类型", list(FLASH_PARAMS.keys()))
        flash = FLASH_PARAMS[flash_type]
        plane_num_max = int(flash.get("Plane Num") or 1)
        # 从原始Excel看，plane数量是从第8行读取的
        # 但我们的JSON里可能没有"Plane Num"，让我用tPageOfWl相关逻辑调整
        # 实际上原始数据里Plane Num是有的，让我检查一下
        plane_options = []
        for i in range(1, plane_num_max + 1):
            op = plane_num_max + 1 - i
            if op % 2 == 0:
                plane_options.append(op)
        plane_options.append(1)
        plane_options = sorted(list(set(plane_options)), reverse=True)
        if not plane_options:
            plane_options = [1]
        plane_num = st.selectbox("Plane 数量", plane_options)

        cache_prog = st.selectbox("Cache 编程", ["启用 (en cache prog)", "禁用 (dis cache prog)"])
        is_cache_prog = (cache_prog == "启用 (en cache prog)")

        calc_type = st.selectbox("计算模式", ["slc write", "tlc direct write"])
        calc_type_idx = 1 if calc_type == "tlc direct write" else 0

        if_type = st.selectbox("接口类型", ["Conv", "SCA"])
        is_sca = (if_type == "SCA")

        is_to_final_edge = False
        is_to_enable_nto = False
        if is_sca:
            edge_type = st.selectbox("CACLK Edge 模式", ["to first CACLK edge", "to final CACLK edge"])
            is_to_final_edge = (edge_type == "to final CACLK edge")
            nto = st.selectbox("NTO", ["Disable NTO", "Enable NTO"])
            is_to_enable_nto = (nto == "Enable NTO")

        dummy_mode = st.selectbox("Dummy Mode", ["Enable", "Disable"])
        is_dummy_mode_en = (dummy_mode == "Enable")

        # 检查flash是否支持dummy mode
        if is_dummy_mode_en and param_in_flash(flash_type, "tDummyMode") == 0:
            st.warning("This Flash Not Support DummyMode")
            is_dummy_mode_en = False

        # Seq 4K Read 选项 - 仅 9205 控制器可用
        is_seq4k_rd_enabled = (ctrl_type == "9205")
        if not is_seq4k_rd_enabled:
            st.info("Seq 4K Read 仅 9205 控制器支持")
        is_seq4k_rd = st.checkbox("Seq 4K Read", value=False, disabled=not is_seq4k_rd_enabled)

        st.markdown("---")
        if st.button("开始计算", type="primary", use_container_width=True):
            st.session_state.calculate = True

        # 侧边栏页脚 - 精密作者信息
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; opacity: 0.9;">
            <p style="color: #ffffff; font-size: 12px; margin: 5px 0; font-family: 'Noto Sans SC', sans-serif;">作者: Suke</p>
            <p style="color: #38a169; font-size: 11px; margin: 3px 0; font-family: 'JetBrains Mono', monospace; letter-spacing: 1px;">747982670@163.com</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 10px; margin-top: 8px; font-family: 'JetBrains Mono', monospace;">v1.0 · 2024</p>
        </div>
        """, unsafe_allow_html=True)

    # 构建配置
    cfg = {
        "IoSpeed": io_speed,
        "ChNum": ch_num,
        "CeNum": ce_num,
        "PlaneNum": plane_num,
        "CtrlType": ctrl_type,
        "WarmUpCycle": warm_up,
        "FlashType": flash_type,
        "isSeq4kRd": is_seq4k_rd,
        "isCacheProg": is_cache_prog,
        "CalcTypeIdx": calc_type_idx,
        "isDummyModeEn": is_dummy_mode_en,
        "isScaMode": is_sca,
        "isToFinalEdge": is_to_final_edge,
        "isToEnableNTO": is_to_enable_nto
    }

    # 显示当前配置
    st.markdown("### 当前配置概览")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="config-card">
            <div class="config-card-title">控制器配置</div>
            <p><strong>类型:</strong> {}</p>
            <p><strong>通道:</strong> {}</p>
            <p><strong>IO速度:</strong> {} MT/s</p>
            <p><strong>CE数量:</strong> {}</p>
        </div>
        """.format(ctrl_type, ch_num, io_speed, ce_num), unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="config-card">
            <div class="config-card-title">Flash配置</div>
            <p><strong>类型:</strong> {}</p>
            <p><strong>Plane:</strong> {}</p>
            <p><strong>Cache编程:</strong> {}</p>
        </div>
        """.format(flash_type, plane_num, '启用' if is_cache_prog else '禁用'), unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="config-card">
            <div class="config-card-title">模式设置</div>
            <p><strong>接口:</strong> {}</p>
            <p><strong>Dummy:</strong> {}</p>
            <p><strong>计算:</strong> {}</p>
        </div>
        """.format(if_type, '启用' if is_dummy_mode_en else '禁用', calc_type), unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.get("calculate", False):
        # 计算
        g = calc_globals(cfg)

        if calc_type_idx == 1:
            # tlc direct write
            if param_in_flash(flash_type, "tDirectWrite") == 0:
                st.error("This Flash Not Support XLC DirectWrite")
            else:
                calc_xlc_seq_wr_performance(g)
                st.markdown("""
                <div class="result-card">
                    <div class="result-card-title">计算结果 - XLC Direct Write</div>
                </div>
                """, unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                with c1:
                    st.metric("Real Seq Wr (GB/s)", f"{g.get('RealSeqWrSpeed', 0):.3f}")
                    st.metric("Seq Wr (GB/s)", f"{g.get('SeqWrSpeed', 0):.3f}")
                with c2:
                    st.metric("Real Seq Wr 1024base (GB/s)", f"{g.get('RealSeqWrSpeed1024base', 0):.3f}")
                    st.metric("Seq Wr 1024base (GB/s)", f"{g.get('SeqWrSpeed1024base', 0):.3f}")
        else:
            if is_sca:
                sca_calc_seq_rd_performance(g)
                sca_calc_seq_wr_performance(g)
                sca_calc_rand_rd_performance(g)
            else:
                calc_seq_rd_performance(g)
                calc_seq_wr_performance(g)
                calc_rnd_rd_performance(g)

            st.markdown("""
            <div class="result-card">
                <div class="result-card-title">计算结果 - SLC Mode</div>
            </div>
            """, unsafe_allow_html=True)

            # 创建两行展示结果
            row1_col1, row1_col2, row1_col3 = st.columns(3)
            with row1_col1:
                st.metric("Seq Rd (GB/s)", f"{g.get('SeqRdSpeed', 0):.3f}")
            with row1_col2:
                st.metric("Seq Wr (GB/s)", f"{g.get('SeqWrSpeed', 0):.3f}")
            with row1_col3:
                st.metric("Rnd Rd (K IOPS)", f"{g.get('RndRdIops', 0):.3f}")

            row2_col1, row2_col2, row2_col3 = st.columns(3)
            with row2_col1:
                st.metric("Real Seq Wr (GB/s)", f"{g.get('RealSeqWrSpeed', 0):.3f}")
            with row2_col2:
                st.metric("Real Seq Wr Tabupdate (GB/s)", f"{g.get('RealSeqWrSpeedTabupdate', 0):.3f}")
            with row2_col3:
                st.markdown("""
                <div style="background: rgba(255,255,255,0.9); border-radius: 16px; padding: 18px 16px; box-shadow: 0 4px 20px rgba(15,43,77,0.12); min-height: 120px;">
                    <div style="font-size: 14px; color: #4a5568; margin-bottom: 10px; font-weight: 600;">后端Rnd Wr（KIOPS）</div>
                    <div style="font-size: 28px; font-weight: 800; color: #0f2b4d; line-height: 1.2; margin-bottom: 8px;">暂时不提供参考</div>
                    <div style="font-size: 12px; color: #718096; line-height: 1.5;">因为随机写性能和表格更新流程强相关，也就是和FTL架构相关，所以不提供</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("**1024 Base 计算结果**")
            row3_col1, row3_col2, row3_col3 = st.columns(3)
            with row3_col1:
                st.metric("Seq Rd 1024base (GB/s)", f"{g.get('SeqRdSpeed1024base', 0):.3f}")
            with row3_col2:
                st.metric("Seq Wr 1024base (GB/s)", f"{g.get('SeqWrSpeed1024base', 0):.3f}")
            with row3_col3:
                st.metric("Real Seq Wr 1024base (GB/s)", f"{g.get('RealSeqWrSpeed1024base', 0):.3f}")

        # 重置计算标志，但保留结果
        # st.session_state.calculate = False

    # 页脚 - 精密信息展示
    st.markdown("---")
    st.markdown("""
    <div class="footer-info">
        <p><strong>作者：Suke</strong> | 联系邮箱：<a href="mailto:747982670@163.com">747982670@163.com</a></p>
        <p style="margin-top: 10px;">基于得一微电子 Yeestor SSD 控制器技术 · 精密性能计算工具</p>
        <p style="opacity: 0.6; font-size: 12px; margin-top: 8px;">© 2024 Yeestor SSD Performance Calculator · Precision · Innovation · Reliability</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
