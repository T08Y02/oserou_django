import os
import time
import random
import math


def ban_place(ban, gyou, retsu, color):
    ban[gyou][retsu] = color
    return ban

def ban_reverse(ban, gyou, retsu):
    if ban[gyou][retsu] == 1:
        ban[gyou][retsu] = 2
    elif ban[gyou][retsu] == 2:
        ban[gyou][retsu] = 1
    else:
        print("error")
    return ban

def ban_reverse_onestone(ban, gyou, retsu, color):
    before_c = 0
    after_c = 0
    if color == 2:
        before_c = 1
        after_c = 2
    else:
        before_c = 2
        after_c = 1
    ue = 0
    migiue = 0
    migi = 0
    migisita = 0
    sita = 0
    hidarisita = 0
    hidari = 0
    hidariue = 0

    for i in range(gyou+1):
        if i == 0:
            if gyou-i == 0:
                break
            else:
                continue
        else:
            if gyou - i == 0:
                if ban[gyou-i][retsu] == after_c:
                    break
                else:
                    ue = 0
                    break
            else:
                if ban[gyou-i][retsu] == before_c:
                    ue += 1
                elif ban[gyou-i][retsu] == after_c:
                #print(gyou-i)
                    break
                else:
                    ue = 0
                    break
    for i in range(ue):
        ban = ban_reverse(ban, gyou - i - 1, retsu)

    for i in range(7 - retsu + 1):
        if i==0:
            if retsu + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
            else:
                if ban[gyou][retsu + i] == before_c:
                    migi += 1
                elif ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
    for i in range(migi):
        ban = ban_reverse(ban, gyou, retsu + i + 1)

    for i in range(7 - gyou + 1):
        if i==0:
            if gyou + i == 7:
                break
            else:
                continue
        else:
            if gyou + i == 7:
                if ban[gyou+i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
            else:
                if ban[gyou+i][retsu] == before_c:
                    sita += 1
                elif ban[gyou + i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
    for i in range(sita):
        ban = ban_reverse(ban, gyou + i + 1, retsu)


    for i in range(retsu+1):
        if i == 0:
            if retsu - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou][retsu - i] == after_c:
                    break
                else:
                    hidari = 0
                    break
            else:
                if ban[gyou][retsu-i] == before_c:
                    hidari += 1
                elif ban[gyou][retsu-i] == after_c:
                    #print(gyou-i)
                    break
                else:
                    hidari = 0
                    break

    for i in range(hidari):
        ban = ban_reverse(ban, gyou, retsu - i - 1)

    for i in range(gyou+1):
        if i==0:
            if retsu + i == 7 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            else:
                if ban[gyou - i][retsu + i] == before_c:
                    migiue += 1
                elif ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
    for i in range(migiue):
        ban = ban_reverse(ban, gyou - i - 1, retsu + i + 1)


    for i in range(7- gyou +1):
        if i==0:
            if retsu + i == 7 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            else:
                if ban[gyou + i][retsu + i] == before_c:
                    migisita += 1
                elif ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
    for i in range(migisita):
        ban = ban_reverse(ban, gyou + i + 1, retsu + i + 1)


    for i in range(7- gyou +1):
        if i==0:
            if retsu - i == 0 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            else:
                if ban[gyou + i][retsu - i] == before_c:
                    hidarisita += 1
                elif ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
    for i in range(hidarisita):
        ban = ban_reverse(ban, gyou + i + 1, retsu - i - 1)


    for i in range(gyou+1):
        if i==0:
            if retsu - i == 0 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            else:
                if ban[gyou - i][retsu - i] == before_c:
                    hidariue += 1
                elif ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
    for i in range(hidariue):
        ban = ban_reverse(ban, gyou - i - 1, retsu - i - 1)
    return ban

def board_placestone(ban, gyou, retsu, color):
    ban = ban_place(ban, gyou, retsu, color)
    ban = ban_reverse_onestone(ban, gyou, retsu, color)
    return ban
