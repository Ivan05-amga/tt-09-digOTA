# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.binary import BinaryValue



@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test digOta")

    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out[0].value == BinaryValue('Z')

    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out[0].value == 0
    
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out[0].value == 0

    dut.Vip.value = 1
    dut.Vin.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.Out.value == BinaryValue('Z')
