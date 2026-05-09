# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SSD Controller Performance Calculator - Streamlit web application for calculating SSD performance metrics (sequential read/write, random read). Migrated from VBA Excel.

Author: Suke (747982670@163.com)

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

Default password: `ssd2024` (configured in `.streamlit/secrets.toml`)

## Architecture

Single-file Streamlit app (`app.py`) with three main sections:

1. **Data Definitions** (lines 1-618)
   - `FLASH_PARAMS`: NAND Flash parameters for X2/X3/X4/X5 series
   - `CONTROLLERS`: Controller configs (9205, 9503, 8803)
   - `IO_SPEED_OPTIONS`: Available IO speeds

2. **Calculation Functions** (lines 620-1280)
   - `calc_globals()`: Initialize calculation parameters
   - `calc_seq_rd_performance()`: Sequential read performance
   - `calc_rnd_rd_performance()`: Random read performance
   - `calc_seq_wr_performance()`: Sequential write performance (SLC mode)
   - `calc_xlc_seq_wr_performance()`: XLC direct write mode
   - SCA mode functions: `sca_calc_seq_rd/wr/rnd_rd_performance()`

3. **UI Section** (lines 1282+)
   - Password authentication via `check_access()`
   - Sidebar configuration inputs
   - Yeestor brand styling (deep blue #1a365d, green #38a169)

## Key Parameters

- **Controller types**: 9205 (4 channels), 9503 (4 channels), 8803 (1 channel)
- **Flash types**: X2/X3/X4/X5 series with varying pagesize, pagecnt, Plane Num
- **Modes**: Conv (conventional) vs SCA (specialized access)
- **Features**: Dummy Mode, Cache Programming, Seq 4K Read (9205 only)

## Adding New Flash Parameters

1. Update `FLASH_PARAMS` dictionary in `app.py`
2. Include all timing parameters (tR_t, tPROG_t, tBERS_t, etc.)
3. Set `tDummyMode` and `tDirectWrite` to `'yes'` or `'no'` if supported

## Styling Notes

Yeestor brand colors applied via CSS:
- Sidebar: deep blue gradient (#1a365d to #2d5a87)
- Buttons/accents: green (#38a169)
- Selectbox text: black on white/light background