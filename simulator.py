import random

# weights
# STR, DEX, INT, LUK, MHP, MMP, LVD, DEF, ATK, MAT, MOV, JUM, ALL

opDict = dict()

opDict["STR"] = 1
opDict["DEX"] = 2
opDict["INT"] = 3
opDict["LUK"] = 4
opDict["DSD"] = 5
opDict["DSI"] = 6
opDict["DSL"] = 7
opDict["DDI"] = 8
opDict["DDL"] = 9
opDict["DIL"] = 10
opDict["MHP"] = 11
opDict["MMP"] = 12
opDict["LVD"] = 13
opDict["DEF"] = 14
opDict["ATK"] = 15
opDict["MAT"] = 16
opDict["MOV"] = 17
opDict["JUM"] = 18
opDict["ALL"] = 19

keys = list(opDict.keys())
for key in keys:
    opDict[opDict[key]] = key


weightDict = dict()
weightDict["STR"] = weightDict["DEX"] = weightDict["INT"] = weightDict["LUK"] = 5
weightDict["DSD"] = weightDict["DSI"] = weightDict["DSL"] = weightDict["DDI"] = weightDict["DDL"] = weightDict["DIL"] = 7
weightDict["MHP"] = weightDict["MMP"] = 8
weightDict["LVD"] = 4
weightDict["DEF"] = 9
weightDict["ATK"] = weightDict["MAT"] = 8
weightDict["MOV"] = weightDict["JUM"] = 10
weightDict["ALL"] = 1


def update(currStatus: dict, selected: str, value: int = None):
    """
    currStatus dict에 selected 된 스탯을 추가한다.

    Args:
        currStatus: dict
        selected: 선택된 스탯의 이름 (opStr)

    Returns:
        updated currStatus
    """

    # TODO: 옵션별 값 추가 (value)
    if selected in ["DSD", "DSI", "DSL", "DDI", "DDL", "DIL"]:
        # 이중 스탯
        statStr = selected[1:]
        if "S" in statStr:
            currStatus = update(currStatus, "STR", value)
        if "D" in statStr:
            currStatus = update(currStatus, "DEX", value)
        if "I" in statStr:
            currStatus = update(currStatus, "INT", value)
        if "L" in statStr:
            currStatus = update(currStatus, "LUK", value)
    else:
        currStatus[selected] += value
    return currStatus


def select(start, end):
    """[start, end)"""
    assert start < end
    currStatus = dict()
    weightSum = 0
    for i in range(start, end):
        weightSum += weightDict[opDict[i]]

    n = random.randint(1, weightSum)
    cumulativeSum = 0
    for i in range(start, end):
        opStr = opDict[i]
        currRange = (cumulativeSum + 1, cumulativeSum + weightDict[opStr])
        if currRange[0] <= n <= currRange[1]:
            update(currStatus, opStr)


# 1. 정해진 순서에 따라 배열된 추가옵션들 중 가중치에 따라 첫번째 옵션을 선택
