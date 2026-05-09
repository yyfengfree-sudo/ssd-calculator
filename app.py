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
        st.title("SSD 控制器性能计算器")
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader("访问验证")
            password = st.text_input("请输入访问密码", type="password")
            if st.button("进入系统", use_container_width=True):
                # 默认密码: ssd2024
                if password == st.secrets.get("password", "ssd2024"):
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("密码错误")
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

    # 得一微电子 Yeestor 风格配色 - 科技蓝绿色调
    st.markdown("""
    <style>
        /* 主背景色 - 科技感浅蓝 */
        .stApp {
            background: linear-gradient(135deg, #f0f7ff 0%, #e8f5f0 100%);
        }
        /* 侧边栏样式 - 深蓝渐变 */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a365d 0%, #2d5a87 100%);
        }
        /* 侧边栏内所有元素样式优化 */
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] .stHeader {
            color: #ffffff;
        }
        /* 侧边栏标签样式 - 增强清晰度 */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stCheckbox label {
            color: #ffffff !important;
            font-weight: 600 !important;
            font-size: 15px !important;
            letter-spacing: 0.5px;
        }
        /* 侧边栏选择框容器 */
        section[data-testid="stSidebar"] .stSelectbox,
        section[data-testid="stSidebar"] .stCheckbox {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 5px;
        }
        /* 侧边栏下拉选择框 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
            background-color: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 6px;
        }
        /* 侧边栏选择框选中值 - 多种选择器覆盖 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] .css-1poimk {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] .css-1poimk p {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] .css-1poimk span {
            color: #ffffff !important;
        }
        /* 侧边栏选择框value容器 */
        section[data-testid="stSidebar"] .stSelectbox [data-testid="stMarkdownContainer"] {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] .stSelectbox [data-testid="stMarkdownContainer"] p {
            color: #ffffff !important;
        }
        /* 侧边栏选择框所有嵌套div */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div > div {
            color: #ffffff !important;
        }
        /* 侧边栏选择框button内的值 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] button {
            color: #ffffff !important;
        }
        /* 侧边栏选择框input */
        section[data-testid="stSidebar"] .stSelectbox input {
            color: #ffffff !important;
            background-color: transparent !important;
        }
        /* 侧边栏选择框placeholder */
        section[data-testid="stSidebar"] .stSelectbox input::placeholder {
            color: rgba(255, 255, 255, 0.6) !important;
        }
        /* 侧边栏选择框svg图标 */
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] svg {
            fill: #ffffff !important;
        }
        /* 侧边栏下拉选项列表 */
        section[data-testid="stSidebar"] ul[role="listbox"] {
            background-color: #2d5a87 !important;
        }
        section[data-testid="stSidebar"] ul[role="listbox"] li {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] ul[role="listbox"] li:hover,
        section[data-testid="stSidebar"] ul[role="listbox"] li[aria-selected="true"] {
            background-color: rgba(56, 161, 105, 0.3) !important;
        }
        /* 侧边栏复选框 */
        section[data-testid="stSidebar"] .stCheckbox input[type="checkbox"] {
            accent-color: #38a169;
        }
        /* 侧边栏分隔线 */
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.3);
        }
        /* 侧边栏信息提示 */
        section[data-testid="stSidebar"] .stAlert {
            background-color: rgba(56, 161, 105, 0.2);
            border: 1px solid #38a169;
            color: #ffffff;
        }
        /* 标题样式 - 主品牌蓝 */
        h1 {
            color: #1a365d;
            font-weight: 600;
            border-bottom: 3px solid #38a169;
            padding-bottom: 10px;
        }
        h2, h3 {
            color: #2d5a87;
        }
        /* 主按钮样式 - 得一绿 */
        .stButton > button[kind="primary"] {
            background-color: #38a169;
            color: white;
            border: none;
            font-weight: 500;
        }
        .stButton > button[kind="primary"]:hover {
            background-color: #2f855a;
        }
        /* 主内容区选择框样式 */
        .stSelectbox label, .stCheckbox label {
            color: #1a365d !important;
            font-weight: 500;
        }
        /* 分隔线 */
        hr {
            border-color: #38a169;
            opacity: 0.5;
        }
        /* Metric 卡片 - 蓝绿渐变 */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, #ffffff 0%, #f0f7ff 100%);
            border: 2px solid #38a169;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(26, 54, 93, 0.1);
        }
        [data-testid="stMetric"] label {
            color: #2d5a87;
        }
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #1a365d;
            font-weight: 700;
        }
        /* 信息提示框 */
        .stAlert {
            border-radius: 8px;
        }
        /* 品牌宣传区域 */
        .brand-banner {
            background: linear-gradient(90deg, #1a365d 0%, #38a169 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .brand-banner h2 {
            color: white;
            margin: 0;
        }
        .brand-banner p {
            margin: 5px 0 0 0;
            opacity: 0.9;
        }
        /* 页脚 */
        .footer-info {
            text-align: center;
            padding: 20px;
            color: #4a5568;
            font-size: 14px;
        }
        .footer-info a {
            color: #38a169;
        }
    </style>
    """, unsafe_allow_html=True)

    # 品牌宣传 Banner
    st.markdown("""
    <div class="brand-banner">
        <h2>得一微电子 Yeestor</h2>
        <p>专业 SSD 控制器解决方案 | 高性能存储技术</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("SSD 控制器性能计算器")
    st.markdown("---")

    with st.sidebar:
        # 侧边栏品牌宣传
        st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h2 style="color: #38a169; margin: 0;">Yeestor</h2>
            <p style="color: #ffffff; opacity: 0.8; font-size: 12px;">得一微电子</p>
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

        # 侧边栏页脚
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; opacity: 0.8;">
            <p style="color: #ffffff; font-size: 11px;">作者: Suke</p>
            <p style="color: #38a169; font-size: 11px;">747982670@163.com</p>
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
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("控制器")
        st.write(f"类型: {ctrl_type}")
        st.write(f"通道: {ch_num}")
        st.write(f"IO速度: {io_speed} MT/s")
        st.write(f"CE: {ce_num}")
    with col2:
        st.subheader("Flash")
        st.write(f"类型: {flash_type}")
        st.write(f"Plane: {plane_num}")
        st.write(f"Cache编程: {'启用' if is_cache_prog else '禁用'}")
    with col3:
        st.subheader("模式")
        st.write(f"接口: {if_type}")
        st.write(f"Dummy: {'启用' if is_dummy_mode_en else '禁用'}")
        st.write(f"计算: {calc_type}")

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
                st.subheader("计算结果 (XLC Direct Write)")
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

            st.subheader("计算结果")
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Seq Rd (GB/s)", f"{g.get('SeqRdSpeed', 0):.3f}")
                st.metric("Real Seq Wr (GB/s)", f"{g.get('RealSeqWrSpeed', 0):.3f}")
                st.metric("Seq Wr (GB/s)", f"{g.get('SeqWrSpeed', 0):.3f}")
                st.metric("Rnd Rd (K IOPS)", f"{g.get('RndRdIops', 0):.3f}")
                st.metric("Real Seq Wr Tabupdate (GB/s)", f"{g.get('RealSeqWrSpeedTabupdate', 0):.3f}")
            with c2:
                st.metric("Seq Rd 1024base (GB/s)", f"{g.get('SeqRdSpeed1024base', 0):.3f}")
                st.metric("Real Seq Wr 1024base (GB/s)", f"{g.get('RealSeqWrSpeed1024base', 0):.3f}")
                st.metric("Seq Wr 1024base (GB/s)", f"{g.get('SeqWrSpeed1024base', 0):.3f}")
                st.metric("-", "-")
                st.metric("Real Seq Wr Tabupdate 1024base (GB/s)", f"{g.get('RealSeqWrSpeed1024baseTabupdate', 0):.3f}")

        # 重置计算标志，但保留结果
        # st.session_state.calculate = False

    # 页脚 - 作者信息
    st.markdown("---")
    st.markdown("""
    <div class="footer-info">
        <p><strong>作者：Suke</strong> | 联系邮箱：<a href="mailto:747982670@163.com">747982670@163.com</a></p>
        <p>基于得一微电子 Yeestor SSD 控制器技术 | 性能计算工具 v1.0</p>
        <p style="opacity: 0.7; font-size: 12px;">© 2024 Yeestor SSD Performance Calculator</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
