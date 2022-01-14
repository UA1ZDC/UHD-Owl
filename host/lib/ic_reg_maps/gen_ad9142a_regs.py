#!/usr/bin/env python
#
# Copyright 2010 Ettus Research LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

########################################################################
# Template for raw text data describing registers
# name addr[bit range inclusive] default optional enums
########################################################################
REGS_TMPL="""\
########################################################################
## Common
########################################################################
SPI_LSB_FIRST           0x00[6]     0
DEVICE_RESET            0x00[5]     0
########################################################################
## PD_CONTROL 
########################################################################
PD_IDAC             0x01[7]     1
PD_QDAC             0x01[6]     1
PD_DATARCV          0x01[5]     0
PD_DEVICE           0x01[2]     0
PD_DACCLK           0x01[1]     0
PD_FRAME            0x01[0]     0
########################################################################
## INTERRUPT_ENABLE0
########################################################################
ENABLE_SYNC_LOST        0x03[6]     0
ENABLE_SYNC_LOCKED      0x03[5]     0
ENABLE_SYNC_DONE        0x03[4]     0
ENABLE_PLL_LOST         0x03[3]     0
ENABLE_PLL_LOCKED       0x03[2]     0
ENABLE_OVER_THRESHOLD   0x03[1]     0
ENABLE_DACOUT_MUTED     0x03[0]     0
########################################################################
## INTERRUPT_ENABLE1
########################################################################
ENABLE_PARITY_FAIL      0x04[7]     0
ENABLE_SED_FAIL         0x04[6]     0
ENABLE_DLL_WARNING      0x04[5]     0
ENABLE_DLL_LOCKED       0x04[4]     0
ENABLE_FIFO_UNDERFLOW   0x04[2]     0
ENABLE_FIFO_OVERFLOW    0x04[1]     0
ENABLE_FIFO_WARNING     0x04[0]     0
########################################################################
## INTERRUPT_FLAG0
########################################################################
INTERRUPT_SYNC_LOST           0x05[6]     0
INTERRUPT_SYNC_LOCKED         0x05[5]     0
INTERRUPT_SYNC_DONE           0x05[4]     0
INTERRUPT_PLL_LOST            0x05[3]     0
INTERRUPT_PLL_LOCKED          0x05[2]     0
INTERRUPT_OVER_THRESHOLD      0x05[1]     0
INTERRUPT_DACOUT_MUTED        0x05[0]     0
########################################################################
## INTERRUPT_FLAG1
########################################################################
INTERRUPT_PARITY_FAIL         0x06[7]     0
INTERRUPT_SED_FAIL            0x06[6]     0
INTERRUPT_DLL_WARNING         0x06[5]     0
INTERRUPT_DLL_LOCKED          0x06[4]     0
INTERRUPT_FIFO_UNDERFLOW      0x06[2]     0
INTERRUPT_FIFO_OVERFLOW       0x06[1]     0
INTERRUPT_FIFO_WARNING        0x06[0]     0
########################################################################
## RQ_SEL0
########################################################################
SEL_SYNC_LOST       0x07[6]     0
SEL_SYNC_LOCKED     0x07[5]     0
SEL_SYNC_DONE       0x07[4]     0
SEL_PLL_LOST        0x07[3]     0
SEL_PLL_LOCKED      0x07[2]     0
SEL_OVER_THRESHOLD  0x07[1]     0
SEL_DACOUT_MUTED    0x07[0]     0
########################################################################
## RQ_SEL1
#######################################################################
SEL_PARITY_FAIL         0x08[7]     0
SEL_SED_FAIL            0x08[6]     0
SEL_DLL_WARNING         0x08[5]     0
SEL_DLL_LOCKED          0x08[4]     0
SEL_FIFO_UNDERFLOW      0x08[2]     0
SEL_FIFO_OVERFLOW       0x08[1]     0
SEL_FIFO_WARNING        0x08[0]     0
########################################################################
## FRAME_MODE
########################################################################
PARUSAGE                0x09[5]     0
FRMUSAGE                0x09[4]     0
FRAME_PIN_USAGE         0x09[0:1]   0
########################################################################
## DATA_CNTR_0
########################################################################
DLL_ENABLE              0x0A[7]     0
DUTY_CORRECTION_ENABLE  0x0A[6]     1
DLL_PHASE_OFFSET        0x0A[0:3]   0
########################################################################
## DATA_CNTR_1
########################################################################
CLEAR_WARN          0x0B[7]     0
DATA_CNTR_1_Reserved  0x0B[0:6] 0x39  
########################################################################
## DATA_CNTR_2
########################################################################
DATA_CNTR_2_Reserved  0x0C[0:7] 0x64  
########################################################################
## DATA_CNTR_3
########################################################################
LOW_DCI_EN            0x0D[7]     0
DC_COUPLE_LOW_EN      0x0D[4]     0
DATA_CNTR_3_Reserved  0x0D[0:3] 0x6 
########################################################################
## DATA_STAT_0
########################################################################
DLL_LOCK            0x0E[7]     0
DLL_WARN            0x0E[6]     0
DLL_START_WARNING   0x0E[5]     0
DLL_END_WARNING     0x0E[4]     0
DCI_ON              0x0E[2]     0
DLL_RUNNING         0x0E[0]     0
########################################################################
## DACCLK_RECEIVER_CTRL
########################################################################
DACCLK_DUTYCYCLE_CORRECTION         0x10[7]       1
DACCLK_RECEIVER_CTRL_Reserved       0x10[6]       1
DACCLK_CROSSPOINT_CTRL_ENABLE       0x10[5]       1
DACCLK_CROSSPOINT_LEVEL             0x10[0:4]     0x1F
########################################################################
## REFCLK_RECEIVER_CTRL
########################################################################
DUTYCYCLE_CORRECTION                0x11[7]     0  
REFCLK_RECEIVER_CTRL_Reserved       0x11[6]     1    
REFCLK_CROSSPOINT_CTRL_ENABLE       0x11[5]     0  
REFCLK_CROSSPOINT_LEVEL             0x11[0:4]   0x1F  
########################################################################
## PLL_CTRL0
########################################################################
PLL_ENABLE          0x12[7]     0
AUTO_MANUAL_SEL     0x12[6]     0
PLL_MANUAL_BAND     0x12[0:5]   0
########################################################################
## PLL_CTRL2
########################################################################
PLL_LOOP_BW         0x14[5:7]   0x7
PLL_CP_CURRENT      0x14[0:4]   0x7
########################################################################
## PLL_CTRL3
########################################################################
DIGLOGIC_DIVIDER        0x15[6:7]   0x3
CROSSPOINT_CTRL_EN      0x15[4]     0
VCO_DIVIDER             0x15[2:3]   0x2
LOOP_DIVIDER            0x15[0:1]   0x1
########################################################################
## PLL_STATUS0
########################################################################
PLL_LOCK                    0x16[7]     0
VCO_CTRL_VOLTAGE_READBACK   0x16[0:3]   0
########################################################################
## PLL_STATUS1
########################################################################
PLL_BAND_READBACK           0x17[0:5]   0
########################################################################
## IDAC_FS_ADJ0
########################################################################
IDAC_FULLSCALE_ADJUST_LSB   0x18[0:7]   0xF9
########################################################################
## IDAC_FS_ADJ1
########################################################################
IDAC_FS_ADJ1_Reserved       0x19[5:7]   0x7
IDAC_FULLSCALE_ADJUST_MSB   0x19[0:1]   1
########################################################################
## QDAC_FS_ADJ0
########################################################################
QDAC_FULLSCALE_ADJUST_LSB   0x1A[0:7]   0xF9
########################################################################
## QDAC_FS_ADJ1
########################################################################
QDAC_FULLSCALE_ADJUST_MSB   0x1B[0:1]   1
########################################################################
## DIE_TEMP_SENSOR_CTRL
########################################################################
FS_CURRENT              0x1C[4:6]   0
REF_CURRENT             0x1C[1:3]   1
DIE_TEMP_SENSOR_EN      0x1C[0]     0
########################################################################
## DIE_TEMP_SENSOR_LSB
########################################################################
DIE_TEMP_LSB            0x1D[0:7]   0
########################################################################
## DIE_TEMP_SENSOR_MSB
########################################################################
DIE_TEMP_MSB            0x1E[0:7]   0
########################################################################
## CHIP_ID 
########################################################################
CHIP_ID                 0x1F[0:7]   0xA
########################################################################
## INTERRUPT_CONFIG 
########################################################################
INTERRUPT_CONFIGURATION     0x20[0:7]   0
########################################################################
## SYNC_CTRL
########################################################################
SYNC_CLK_EDGE_SEL       0x21[1]    0
SYNC_ENABLE             0x21[0]    0
########################################################################
## FRAME_RST_CTRL
########################################################################
ARM_FRAME               0x22[3]    0
EN_CON_FRAME_RESET      0x22[2]    0
FRAME_RESET_MODE        0x22[0:1]  2
########################################################################
## FIFO_LEVEL_CONFIG
########################################################################
INTEGER_FIFO_LEVEL_REQUEST      0x23[4:6]    4
FRACTIONAL_FIFO_LEVEL_REQUEST   0x23[0:2]    0
########################################################################
## FIFO_LEVEL_READBACK
########################################################################
INTEGER_FIFO_LEVEL_READBACK     0x24[4:6]    0
FRACTIONAL_FIFO_LEVEL_READBACK  0x24[0:2]    0
########################################################################
## FIFO_CTRL
########################################################################
FIFO_SPI_RESET_ACK          0x25[1]    0
FIFO_SPI_RESET_REQUEST      0x25[0]    0
########################################################################
## DATA_FORMAT
########################################################################
DATA_FORMAT         0x26[7]    0
DATA_PAIRING        0x26[6]    0
DATA_BUS_INVERT     0x26[5]    0
DATA_BUS_WIDTH      0x26[0]    0
########################################################################
## DATAPATH_CTRL
########################################################################
INVSINC_ENABLE                  0x27[7]    0
NCO_ENABLE                      0x27[6]    0
IQ_GAIN_ADJ_DCOFFSET_ENABLE     0x27[5]    0
IQ_PHASE_ADJ_ENABLE             0x27[4]    0
FS4_MODULATION_ENABLE           0x27[2]    0
NCO_SIDEBAND_SEL                0x27[1]    0
SEND_IDATA_TO_QDAC              0x27[0]    0
########################################################################
## INTERPOLATION_CTRL
########################################################################
INTERPOLATION_MODE          0x28[0:1]    0
########################################################################
## OVER_THRESHOLD_CTRL0
########################################################################
THRESHOLD_LEVEL_REQUEST_LSB     0x29[0:7]    0
########################################################################
## OVER_THRESHOLD_CTRL1
########################################################################
THRESHOLD_LEVEL_REQUEST_MSB     0x2A[0:4]    0
########################################################################
## OVER_THRESHOLD_CTRL2
########################################################################
ENABLE_PROTECTION               0x2B[7]     0
IQ_DATA_SWAP                    0x2B[6]     0
SAMPLE_WINDOW_LENGTH            0x2B[0:3]   0
########################################################################
## INPUT_POWER_READBACK_LSB
########################################################################
INPUT_POWER_READBACK_LSB  0x2C[0:7]    0
########################################################################
## INPUT_POWER_READBACK_MSB
########################################################################
INPUT_POWER_READBACK_MSB  0x2D[0:4]    0
########################################################################
## NCO_CTRL
########################################################################
NCO_FRAME_UPDATE_ACK        0x30[6]     0
SPI_NCO_PHASE_RST_ACK       0x30[5]     0
SPI_NCO_PHASE_RST_REQ       0x30[4]     0
NCO_SPI_UPDATE_ACK          0x30[1]     0
NCO_SPI_UPDATE_REQ          0x30[0]     0
########################################################################
## NCO_FREQ_TUNING_WORD0
########################################################################
NCO_FTW0            0x31[0:7]    0
########################################################################
## NCO_FREQ_TUNING_WORD1
########################################################################
NCO_FTW1            0x32[0:7]    0
########################################################################
## NCO_FREQ_TUNING_WORD2
########################################################################
NCO_FTW2            0x33[0:7]    0
########################################################################
## NCO_FREQ_TUNING_WORD3
########################################################################
NCO_FTW3            0x34[0:7]    0x10
########################################################################
## NCO_PHASE_OFFSET0
#######################################################################
NCO_PHASE_OFFSET_LSB        0x35[0:7]    0
########################################################################
## NCO_PHASE_OFFSET1
########################################################################
NCO_PHASE_OFFSET_MSB        0x36[0:7]    0
########################################################################
## IQ_PHASE_ADJ0
########################################################################
IQ_PHASE_ADJ_LSB            0x37[0:7]    0
########################################################################
## IQ_PHASE_ADJ1
########################################################################
IQ_PHASE_ADJ_MSB            0x38[0:4]    0
########################################################################
## LVDS_IN_PWR_DOWN_0
########################################################################
PWR_DOWN_DATA_INPUT_BITS    0x39[0:3]    0
########################################################################
## IDAC_DC_OFFSET0
########################################################################
IDAC_DC_OFFSET_LSB          0x3B[0:7]    0
########################################################################
## IDAC_DC_OFFSET1
########################################################################
IDAC_DC_OFFSET_MSB          0x3C[0:7]    0
########################################################################
## QDAC_DC_OFFSET0
########################################################################
QDAC_DC_OFFSET_LSB          0x3D[0:7]    0
########################################################################
## QDAC_DC_OFFSET1
########################################################################
QDAC_DC_OFFSET_MSB          0x3E[0:7]    0
########################################################################
## IDAC_GAIN_ADJ
########################################################################
IDAC_GAIN_ADJ               0x3F[0:5]    0x20
########################################################################
## QDAC_GAIN_ADJ
########################################################################
QDAC_GAIN_ADJ           0x40[0:5]    0x20
########################################################################
## GAIN_STEP_CTRL0
########################################################################
RAMP_UP_STEP            0x41[0:5]    0x01
########################################################################
## GAIN_STEP_CTRL1
########################################################################
DAC_OUTPUT_OFF          0x42[7]      0
DAC_OUTPUT_STATUS       0x42[6]      1
RAMP_DOWN_STEP          0x42[0:5]    1
########################################################################
## TX_ENABLE_CTRL
########################################################################
TXENABLE_GAINSTEP_EN        0x43[2]      1
TXENABLE_SLEEP_EN           0x43[1]      1
TXENABLE_POWER_DOWN_EN      0x43[0]      1
########################################################################
## DAC_OUTPUT_CTRL
########################################################################
DAC_OUTPUT_CTRL_EN              0x44[7]      1
FIFO_WARNING_SHUTDOWN_EN        0x44[3]      1
OVERTHRESHOLD_SHUTDOWN_EN       0x44[2]      1
FIFO_ERROR_SHUTDOWN_EN          0x44[0]      1
########################################################################
## ENABLE_DLL_DELAY_CELL0
########################################################################
DELAY_CELL0_ENABLE           0x5E[0:7]    0xFF
########################################################################
## ENABLE_DLL_DELAY_CELL1
#######################################################################
ENABLE_DLL_DELAY_CELL1_Reserved     0x5F[3:7]    0x0C
DELAY_CELL1_ENABLE                   0x5F[0:2]    0x7
########################################################################
## SED_CTRL
########################################################################
SED_ENABLE              0x60[7]      0
SED_ERR_CLEAR           0x60[6]      0
AED_ENABLE              0x60[5]      0
SED_DEPTH               0x60[4]      0
AED_PASS                0x60[2]      0
AED_FAIL                0x60[1]      0
SED_FAIL                0x60[0]      0
########################################################################
## SED_PATT_L_I0
########################################################################
SED_PATT_L_I0           0x61[0:7]    0
########################################################################
## SED_PATT_H_I0
########################################################################
SED_PATT_H_I0           0x62[0:7]    0
########################################################################
## SED_PATT_L_Q0
########################################################################
SED_PATT_L_Q0           0x63[0:7]    0
########################################################################
## SED_PATT_H_Q0
########################################################################
SED_PATT_H_Q0           0x64[0:7]    0
########################################################################
## SED_PATT_L_I1
########################################################################
SED_PATT_L_I1           0x61[0:7]    0
########################################################################
## SED_PATT_H_I1
########################################################################
SED_PATT_H_I1           0x66[0:2]    0
########################################################################
## SED_PATT_L_Q1
########################################################################
SED_PATT_L_Q1           0x67[0:7]    0
########################################################################
## SED_PATT_H_Q1
########################################################################
SED_PATT_H_Q1           0x68[0:2]    0
########################################################################
## PARITY_CTRL
########################################################################
PARITY_ENABLE           0x6A[7]     0  
PARITY_EVEN             0x6A[6]     0 
PARITY_ERR              0x6A[5]     0 
CLEAR                   0x6A[2:4]   0 
PARERRFAL               0x6A[1]     0 
PARERRIS                0x6A[0]     0 
"""

########################################################################
# Template for methods in the body of the struct
########################################################################
BODY_TMPL="""\
boost::uint8_t get_reg(boost::uint16_t addr){
    boost::uint8_t reg = 0;
    switch(addr){
    % for addr in sorted(set(map(lambda r: r.get_addr(), regs))):
    case ${addr}:
        % for reg in filter(lambda r: r.get_addr() == addr, regs):
        reg |= (boost::uint8_t(${reg.get_name()}) & ${reg.get_mask()}) << ${reg.get_shift()};
        % endfor
        break;
    % endfor
    }
    return reg;
}

boost::uint32_t get_write_reg(boost::uint16_t addr){
    return (boost::uint16_t(addr) << 8) | get_reg(addr);
}

boost::uint32_t get_read_reg(boost::uint16_t addr){
    return (boost::uint16_t(addr) << 8) | (1 << 23);
}
"""

if __name__ == '__main__':
    import common; common.generate(
        name='ad9142a_regs',
        regs_tmpl=REGS_TMPL,
        body_tmpl=BODY_TMPL,
        file=__file__,
    )