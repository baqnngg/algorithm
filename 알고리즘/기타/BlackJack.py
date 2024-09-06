import random
import copy
import time
card = [["ace-clover",11],["ace-spade",11],["ace-heart",11],["ace-Diamond",11],["2-clover",2],["2-spade",2],["2-heart",2],["2-Diamond",2],
        ["3-clover",3],["3-spade",3],["3-heart",3],["3-Diamond",3],["4-clover",4],["4-spade",4],["4-heart",4],["4-Diamond",4],
        ["5-clover",5],["5-spade",5],["5-heart",5],["5-Diamond",5],["6-clover",6],["6-spade",6],["6-heart",6],["6-Diamond",6],
        ["7-clover",7],["7-spade",7],["7-heart",7],["7-Diamond",7],["8-clover",8],["8-spade",8],["8-heart",8],["8-Diamond",8],
        ["9-clover",9],["9-spade",9],["9-heart",9],["9-Diamond",9],["10-clover",10],["10-spade",10],["10-heart",10],["10-Diamond",10],
        ["queen-clover",10],["queen-spade",10],["queen-heart",10],["queen-Diamond",10],["king-clover",10],["king-spade",10],["king-heart",10],["king-Diamond",10],
        ["jack-clover",10],["jack-spade",10],["jack-heart",10],["jack-Diamond",10],["joke1",10],["joker2",10]]

cheap = {1:100,2:500,3:1000,4:2000,5:5000,6:10000}
money = []  #player의 돈

start = input("\033[37m게임을 시작하시겠습니까? (y,n) : \033[0m")

if start == "y":

    playercnt = int(input("\033[37m몇명의 player로 하시겠습니까? : \033[0m"))

    #기본 돈 지급
    for i in range(playercnt):
            line = [] 
            money.append(line)
            l = str(i+1)
            pname = input("\033[37m이름을 정하시오 : \033[0m")
            money[i].append(pname)
            money[i].append(1000)
            money[i].append(1)
            print("\033[37m이름 : "+money[i][0],", 돈 : ",str(money[i][1])+" $\033[0m")

    while 1:
        player = [] 
        bat = []    #player가 얼마 걸었는지

        total = [] #합계

        #방문처리 초기화
        for i in range(playercnt):
             money[i][2] = 1

        #카드복사
        playcard = copy.deepcopy(card)

        #배팅
        for i in range(playercnt):
            while 1:
                time.sleep(0.3)
                bating = int(input("\n\033[37m"+str(money[i][0])+"의 "+"\033[33m배팅 \033[37m: 1/100, 2/500, 3/1000, 4/2000, 5/5000, 6/10000, 7/올인 : \033[0m"))
                if bating == 7:
                     break
                elif bating < 0 or bating > 7:
                    print("잘못입력함")
                    continue
                elif money[i][1] < cheap[bating]:
                    print("소지한 금액이 적습니다.")
                    continue
                else:
                    break

            l = str(i+1)
            if bating == 7:
                bat.append(money[i][1])
                time.sleep(0.2)
                print("\n\033[31m"+l+"번째 player가 올인하셨습니다.\033[0m")
            else:
                f = str(cheap[bating])
                bat.append(cheap[bating])
                time.sleep(0.3)
                print('\033[31m'+l+"\033[0m\033[37m번째 player가 \033[31m"+f+"\033[0m\033[37m을 거셨습니다.\033[0m")

        #시작부분
        #player
        for i in range(playercnt):  #빈 리스트 생성
            line = [] 
            player.append(line)

        for i in range(playercnt):
            one = random.choice(playcard)   #카드두개 랜덤하게 선택하는 부분
            player[i].append(one)   #?번째 player가 뽑은 카드추가
            playcard.remove(one)    #player가 뽑은 카드 삭제
            total.append(one)
            two = random.choice(playcard)
            if two[1] == 11 and total[i][1] > 10:    #ace가 1로 변하는 조건
                    two[1] = 1
            total.remove(one)
            t = one[1]+two[1]
            total.append(t)
            player[i].append(two)  
            time.sleep(0.3)
            print('\n\033[36m'+money[i][0]+" :", player[i][0][0], ",", player[i][1][0], "총점수 : " , total[i],"\033[0m\n")           
            playcard.remove(two)

        #dealer
        dealer = []
        one = random.choice(playcard) #카드두개 랜덤하게 선택하는 부분
        total.append(one)
        dealer.append(one)  #딜러가 뽑은 카드 추가
        two = random.choice(playcard)
        if two[1] == 11 and total[playercnt][1] > 10:    #ace가 1로 변하는 조건
                playcard.remove(one) #딜러가 뽑은 카드 삭제
                playcard.remove(two)
                two[1] = 1
                total.remove(one)
                dealer.append(two)
                time.sleep(0.3)
                print("\033[32m딜러의 첫 번째 카드입니다 : ",one[0],"\033[0m\n")
        else:
            playcard.remove(one) #딜러가 뽑은 카드 삭제
            playcard.remove(two)
            total.remove(one)
            dealer.append(two)
            total.append(one[1]+two[1])
            time.sleep(0.3)
            print("\033[32m딜러의 첫 번째 카드입니다 : ",one[0],"\033[0m\n")

        #player들 게임 본격 
        i = 0
        u = 0
        p = 0
        while 1:
            select = 0
            p = str(i+1)

            if u == playercnt:
                time.sleep(0.3)
                print("\033[31m게임오버!\033[0m")
                escape = int(input("\033[37m그만하고 싶으시면 0, 계속하고 싶으시면 1 : \033[0m"))
                if escape == 0:
                    break
                else:
                    continue

            #player중에 이미 끝난 player들 건너뛰는작업
            if money[i][2] == 0:
                i += 1
                continue

            select = int(input("\033[37m"+money[i][0]+"의 선택(hit : 0, stand : 1) : \033[0m"))
            if select == 0: 
                three = random.choice(playcard)
                player[i].append(three)
                playcard.remove(three)
                if three[1] == 11 and total[i] > 10:    #ace가 1로 변하는 조건
                    three[1] = 1                       #1로 변환
                total[i] = int(total[i]) + three[1]
                time.sleep(0.3)
                print("\n\033[37m"+money[i][0]+"의 카드 : ",player[i], "총점수 : " , total[i],"\n\033[0m")

                if total[i] > 21:
                    time.sleep(0.3)
                    print("\033[31m"+money[i][0]+"가 패배하셨습니다.\n\033[0m")
                    money[i][2] = 0
                    money[i][1] = money[i][1] - bat[i]
                    time.sleep(0.3)
                    print("\033[31m"+p+"번째 player의 남은돈 :",money[i][1],"\033[0m")
                    if money[i][2] == 0:
                        u += 1
                    i += 1

            if select == 1:
                print("\n\033[37m"+money[i][0]+"의 카드 : ",player[i], "총점수 : " , total[i],"\n\033[0m")
                i += 1

            if i >= playercnt:
                break      

        if u == playercnt:
            escape = int(input("\033[37m그만하고 싶으시면 0, 계속하고 싶으시면 1 : \033[0m"))
            if escape == 0:
                break
            else:
                continue

        
        #게임 갈리는 구간
        for i in range(playercnt):
            #player중에 이미 끝난 player들 건너뛰는작업
            if money[i][2] == 0:
                continue 
            #딜러의 점수가 16점이하면 실행
            if total[playercnt] <= 16:   #딜러가 카드뽑는구간
                three = random.choice(playcard)
                dealer.append(three)
                playcard.remove(three)
                total[playercnt] = int(three[1]) + int(total[playercnt])    
                #딜러가 22이상이면은 딜러의 패배 
                if total[playercnt] >= 22:
                    time.sleep(0.3)
                    print("\033[37m딜러의 카드를 오픈합니다 : ", dealer, "총점수 : ",total[playercnt],"\033[0m")
                    if total[i] == 21 and len(player[i]) == 2:  #블랙잭일때
                            money[i][1] = (bat[i] * 2.5) + money[i][1] - bat[i]
                            print("\033[33m블랙잭! \033[37m"+money[i][0]+"의 승리입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                            continue
                    
                    money[i][1] = (bat[i] * 2) + money[i][1] - bat[i]
                    time.sleep(0.3)
                    print("\033[37m"+money[i][0]+"의 승리입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                    continue
            
            #딜러의 점수가 17점이상이면 실행
            if total[playercnt] >= 17:
                    if total[playercnt] > 21: #딜러가 21을 초과 했을때
                        time.sleep(0.3)
                        print("\033[37m딜러의 카드를 오픈합니다 : ", dealer, "총점수 : ",total[playercnt],"\033[0m")
                        money[i][1] = (bat[i] * 2) + money[i][1] - bat[i]
                        time.sleep(0.3)
                        print("\033[37m"+money[i][0]+"의 승리입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                        continue

                    #무승부
                    if total[playercnt] == total[i]: #딜러의 점수와 player의 점수가 같을때
                        time.sleep(0.3)
                        print("\033[37m딜러의 카드를 오픈합니다 : ", dealer, "총점수 : ",total[playercnt],"\033[0m")
                        time.sleep(0.3)
                        print(str(money[i][0])+"의 \033[33m무승부\033[0m\n")
                        continue

                    #player 승리
                    if total[playercnt] < total[i]: #딜러의 점수보다 player의 점수가 높을때
                        time.sleep(0.3)
                        print("\033[37m딜러의 카드를 오픈합니다 : ", dealer, "총점수 : ",total[playercnt],"\033[0m")

                        if total[i] == 21 and len(player[i]) == 2:  #블랙잭일때
                            money[i][1] = (bat[i] * 2.5) + money[i][1] - bat[i]
                            print("\033[33m블랙잭! \033[37m"+money[i][0]+"의 승리입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                            continue

                        money[i][1] = (bat[i] * 2) + money[i][1] - bat[i]
                        time.sleep(0.3)
                        print("\033[37m"+money[i][0]+"의 승리입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                        continue
                    #패배
                    if total[playercnt] > total[i]: #딜러의 점수보다 player의 점수가 낮을때
                        time.sleep(0.3)
                        print("\033[37m딜러의 카드를 오픈합니다 : ", dealer, "총점수 : ",total[playercnt],"\033[0m")
                        money[i][1] = money[i][1] - bat[i]
                        time.sleep(0.3)
                        print("\033[37m"+money[i][0]+"의 패배입니다. 남은돈 : "+str(money[i][1])+"\033[0m\n")
                        continue            
        
        escape = int(input("\033[37m그만하고 싶으시면 0, 계속하고 싶으시면 1 : \033[0m"))
        if escape == 0:
            print("\n게임이 끝났습니다.\n")
            money.sort(key=lambda x: (x[2], -x[1]))
            for i in range(playercnt):
                print("\033[33m"+str(i+1)+"위 :",money[i][0],"돈 :",money[i][1],"\n\033[0m")
            break

else:
    print("\033[31m게임을 종료합니다.\033[0m")   