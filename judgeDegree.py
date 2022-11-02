# FILENAME:judgeDegree.py

def judgeDeg(prob):
    prob = int(prob*100)
    degree = ''
    if prob <= 54:
        degree = 'Mild'  # 轻度
    elif prob >54 and prob <=78:
        degree = 'Moderate'  # 中度
    elif prob > 78:
        degree = 'Severe'  # 重度

    return degree
