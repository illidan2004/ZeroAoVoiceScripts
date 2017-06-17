﻿from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c030b.bin",                # FileName
        "c030b",                    # MapName
        "c030b",                    # Location
        0x002A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 0, 0, 1],
    )

    BuildStringList((
        "c030b",                  # 0
        "中央广场",               # 1
        "西街",                   # 2
        "行政区",                 # 3
        "住宅街",                 # 4
        "欢乐街",                 # 5
        "东街",                   # 6
        "旧城区",                 # 7
        "港湾区",                 # 8
        "ＩＢＣ",                 # 9
        "站前街道",               # 10
        "后巷",                   # 11
        "乌尔斯拉间道",           # 12
        "东克洛斯贝尔街道",       # 13
        "西克洛斯贝尔街道",       # 14
        "玛因兹山道",             # 15
    ))

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央广场")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西街")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "欢乐街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "东街")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧城区")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "站前街道")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "后巷")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_2E0",          # 00, 0
        "Function_1_2E1",          # 01, 1
    ))


    def Function_0_2E0(): pass

    label("Function_0_2E0")

    Return()

    # Function_0_2E0 end

    def Function_1_2E1(): pass

    label("Function_1_2E1")

    Return()

    # Function_1_2E1 end

    SaveToFile()

Try(main)
