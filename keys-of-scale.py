print('升降符號標示如下:')
print('C,A#,Eb\n')

for a in range(1,100):
    a=1
    key1 = str(input('輸入原調:'))
    key2 = str(input('輸入欲轉調:'))

    keylist1 = [0, 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    keylist2 = [0, 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


    for keynum in range(1, 13):
        if key1 == keylist1[keynum] :
            keynum1 = keynum
            break

        elif key1 == keylist2[keynum] :
            keynum1 = keynum
            break

    for keynum in range(1, 13):
        if key2 == keylist1[keynum] :
            keynum2 = keynum
            break

        elif key2 == keylist2[keynum] :
            keynum2 = keynum
            break


    scale = keynum2-keynum1
    if scale>6:
        print(scale-12)
    elif scale<0:
        if scale<-6:
            print('半音=',scale+12)
        else:
            print('半音=',scale)
    else:
        print('半音=',scale)