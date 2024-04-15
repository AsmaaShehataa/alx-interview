#!/usr/bin/python3
'''LockBoxes Challenge of alx_interview dir to unlock boxes using Gen_keys'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    Gen_keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        Gen_keys.update(boxes[i])
        for key in Gen_keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in opened_boxes and i != 0:
            return False
    return True
