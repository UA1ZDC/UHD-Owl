//
// Copyright 2021 Ettus Research, A National Instruments Company
//
// SPDX-License-Identifier: LGPL-3.0-or-later
//
// Module: power_regs_regmap_utils.vh
// Description:
// The constants in this file are autogenerated by XmlParse.

//===============================================================================
// A numerically ordered list of registers and their HDL source files
//===============================================================================

  // RF_POWER_CONTROL : 0x0 (power_regs.v)
  // RF_POWER_STATUS  : 0x4 (power_regs.v)
  // PRC_CONTROL      : 0x8 (power_regs.v)

//===============================================================================
// RegTypes
//===============================================================================

//===============================================================================
// Register Group POWER_REGS_REGISTERS
//===============================================================================

  // RF_POWER_CONTROL Register (from power_regs.v)
  localparam RF_POWER_CONTROL = 'h0; // Register Offset
  localparam RF_POWER_CONTROL_SIZE = 32;  // register width in bits
  localparam RF_POWER_CONTROL_MASK = 32'h7;
  localparam ENABLE_TX_7V0_SIZE = 1;  //RF_POWER_CONTROL:ENABLE_TX_7V0
  localparam ENABLE_TX_7V0_MSB  = 0;  //RF_POWER_CONTROL:ENABLE_TX_7V0
  localparam ENABLE_TX_7V0      = 0;  //RF_POWER_CONTROL:ENABLE_TX_7V0
  localparam ENABLE_RX_7V0_SIZE = 1;  //RF_POWER_CONTROL:ENABLE_RX_7V0
  localparam ENABLE_RX_7V0_MSB  = 1;  //RF_POWER_CONTROL:ENABLE_RX_7V0
  localparam ENABLE_RX_7V0      = 1;  //RF_POWER_CONTROL:ENABLE_RX_7V0
  localparam ENABLE_3V3_SIZE = 1;  //RF_POWER_CONTROL:ENABLE_3v3
  localparam ENABLE_3V3_MSB  = 2;  //RF_POWER_CONTROL:ENABLE_3v3
  localparam ENABLE_3V3      = 2;  //RF_POWER_CONTROL:ENABLE_3v3

  // RF_POWER_STATUS Register (from power_regs.v)
  localparam RF_POWER_STATUS = 'h4; // Register Offset
  localparam RF_POWER_STATUS_SIZE = 32;  // register width in bits
  localparam RF_POWER_STATUS_MASK = 32'h3;
  localparam P7V_A_STATUS_SIZE = 1;  //RF_POWER_STATUS:P7V_A_STATUS
  localparam P7V_A_STATUS_MSB  = 0;  //RF_POWER_STATUS:P7V_A_STATUS
  localparam P7V_A_STATUS      = 0;  //RF_POWER_STATUS:P7V_A_STATUS
  localparam P7V_B_STATUS_SIZE = 1;  //RF_POWER_STATUS:P7V_B_STATUS
  localparam P7V_B_STATUS_MSB  = 1;  //RF_POWER_STATUS:P7V_B_STATUS
  localparam P7V_B_STATUS      = 1;  //RF_POWER_STATUS:P7V_B_STATUS

  // PRC_CONTROL Register (from power_regs.v)
  localparam PRC_CONTROL = 'h8; // Register Offset
  localparam PRC_CONTROL_SIZE = 32;  // register width in bits
  localparam PRC_CONTROL_MASK = 32'h1;
  localparam PLL_REF_CLOCK_ENABLE_SIZE = 1;  //PRC_CONTROL:PLL_REF_CLOCK_ENABLE
  localparam PLL_REF_CLOCK_ENABLE_MSB  = 0;  //PRC_CONTROL:PLL_REF_CLOCK_ENABLE
  localparam PLL_REF_CLOCK_ENABLE      = 0;  //PRC_CONTROL:PLL_REF_CLOCK_ENABLE
