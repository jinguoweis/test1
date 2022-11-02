# FILENAME:scaleDegree.py


# 他评焦虑
def otherSASFunc(sc):
    osaDegree = ''
    if sc <= 7:
        osaDegree = 'Negative'  # 无焦虑
    elif sc > 7 and sc <= 14:
        osaDegree = 'probable'  # 可能焦虑
    elif sc > 14 and sc <= 21:
        osaDegree = 'certian'  # 肯定焦虑
    elif sc >21 and sc <= 29:
        osaDegree = 'obviously'  # 明显焦虑
    elif sc > 29:
        osaDegree = 'serious'  # 严重焦虑

    return osaDegree


# 他评抑郁
def otherSDSFunc(sc):
    osdDegree = ''
    if sc < 8:
        osdDegree = 'Negative'  # 无抑郁
    elif sc >= 8 and sc <= 20:
        osdDegree = 'Depressed State'  # 抑郁状态，并不构成抑郁症
    elif sc > 20 and sc <= 35:
        osdDegree = 'Mild/Moderate'  # 轻度、中度抑郁
    elif sc > 35:
        osdDegree = 'serious'  # 严重抑郁

    return osdDegree

# 自评焦虑
def selfSASFunc(sc):
    ssaDegree = ''
    if sc < 50:
        ssaDegree = 'Not In Range'
    elif sc >= 50 and sc <= 59:
        ssaDegree = 'Mild'  # 轻度
    elif sc >= 60 and sc <= 69:
        ssaDegree = 'Moderate'  # 中度
    elif sc >= 70:
        ssaDegree = 'Severe'   # 重度

    return ssaDegree

# 自评抑郁
def selfSDSFunc(sc):
    ssdDegree = ''
    if sc < 53:
        ssdDegree = 'Not In Range'
    elif sc >= 53 and sc <= 62:
        ssdDegree = 'Mild'  # 轻度
    elif sc >= 63 and sc <= 72:
        ssdDegree = 'Moderate'  # 中度
    elif sc >= 73:
        ssdDegree = 'Severe'  # 重度

    return ssdDegree