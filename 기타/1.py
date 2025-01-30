from PIL import Image
import tkinter as tk
from tkinter import messagebox

name=""

if name !="":
    print(f'{name}님 반갑습니다.')
else:
    name=input('안녕하세요. 당신의 이름은 무엇인가요? ')
    print(f'{name}님 반갑습니다.')

print(f'지금부터 {name}님의 mbti검사가 실행됩니다.')

class MBTIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MBTI 검사")

        # 결과를 저장할 변수
        self.results = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

        # 질문 리스트
        self.questions = [
            ("둘보다는 여럿이 훨씬 좋다. 다양하게 많이 모일 수록 더 신나며 재미있다.", "E", "I"),
            ("한곳에 얽매이기 싫으며 새 영역을 개척하고 미지의 세계를 탐험하고 싶다.", "P", "J"),
            ("혼자 있는 때가 별로 없다. 가능한 사람들과 어울려 시간을 많이 보낸다.", "E", "I"),
            ("나는 걱정이 많다. 남들은 잘 신경쓰지 않는 일도 미리 생각하고 염려한다.", "N", "S"),
            ("악밥감이 심한 환경에서도 평정심을 유지하는 편이다.", "T", "F"),
            ("단순하고 직관적인 아이디어보다는 복잡하고 참신한 아이디어에 흥미를 느낀다.", "N", "S"),
            ("마음이 여리다. 누군가 고통받는 이야기를 들으면 뭐라도 도와줘야 한다.", "F", "T"),
            ("일반적으로 사실에 기반한 주장보다 감정적으로 공감가는 내용이 더 설득력 있다고 느낀다.", "F", "T"),
            ("상상 속에서 산다. 혼자서 채과 영화, 비현실적인 가상 세계에 잘 빠져든다.", "N", "S"),
            ("변화보다 안정과 익숙함이 좋다.", "J", "P"),
            ("다른 사람에게 내가 어떤 사람으로 보일지 걱정하는 경우가 많다.", "E", "I"),
            ("생활 공간과 업무 공간이 깨끗하게 정돈되어 있다.", "J", "P"),
        ]

        self.question_index = 0

        # 질문 레이블
        self.question_label = tk.Label(root, text=self.questions[self.question_index][0], wraplength=500, font=("Arial", 15))
        self.question_label.pack(pady=20)


        # 버튼 생성
        self.button_yes = tk.Button(root, text="예", font=("Arial", 12), width=10, command=lambda: self.answer("yes"))
        self.button_yes.pack(pady=10)

        self.button_no = tk.Button(root, text="아니오", font=("Arial", 12), width=10, command=lambda: self.answer("no"))
        self.button_no.pack(pady=10)

    def answer(self, user_answer):
        current_question = self.questions[self.question_index]
        if user_answer == "yes":
            self.results[current_question[1]] += 1
        else:
            self.results[current_question[2]] += 1

        # 다음 질문으로 이동
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index][0])
        else:
            self.show_result()

    def show_result(self):
        # MBTI 결과 계산
        mbti = ""
        mbti += "E" if self.results["E"] > self.results["I"] else "I"
        mbti += "S" if self.results["S"] > self.results["N"] else "N"
        mbti += "T" if self.results["T"] > self.results["F"] else "F"
        mbti += "J" if self.results["J"] > self.results["P"] else "P"

        # 결과 메시지
        messagebox.showinfo("결과",f"{name}님의 MBTI 유형은 {mbti}입니다!")
        
        if mbti=="INFP":
            print(f"INFP인 {name}님에게 추천해드릴 음악은 검정치마 - EVERYTHING , 선우정아 – 도망가자 입니다.")
            img1=Image.open('everything.png')
            img1.show()
            img2=Image.open('run.png')
            img2.show()

        elif mbti=="ISFP":
            print(f"ISFP인 {name}님에게 추천해드릴 음악은 박예린 -  bye bye my blue , 마인드유 - 사랑해줘요 입니다.")
            img3=Image.open('byebyemyblue.png')
            img3.show()
            img4=Image.open('mindu.png')
            img4.show()
            
        elif mbti=="ISFJ":
            print(f"ISFJ인 {name}님에게 추천해드릴 음악은 블랙핑크 - forever young , Keshi - 2 soon 입니다.")
            img5=Image.open('foreveryoung.png')
            img5.show()
            img6=Image.open('2soon.png')
            img6.show()

        elif mbti=="ISTP":
            print(f"ISTP인 {name}님에게 추천해드릴 음악은 Dosii - love me more , 백아연 - 쏘쏘 입니다.")
            img7=Image.open('lovememore.png')
            img7.show()
            img8=Image.open('soso.png')
            img8.show()

         
        elif mbti=="ISTJ":
            print(f"ISTJ인 {name}님에게 추천해드릴 음악은 아이유 - 누구나 비밀은 있다 , Starley - Call on me 입니다.")
            img9=Image.open('누구나비밀은있다.png')
            img9.show()
            img10=Image.open('callonme.png')
            img10.show()

            
        elif mbti=="INTP":
            print(f"INTP인 {name}님에게 추천해드릴 음악은 기리보이 - 이때다 , 장재인-서울 느와르 입니다.")
            img11=Image.open('now.png')
            img11.show()
            img12=Image.open('seoul.png')
            img12.show()

        elif mbti=="INTJ":
            print(f"INTJ인 {name}님에게 추천해드릴 음악은 Jason Mraz - I'm yours , Florina - Va va vis 입니다.")
            img13=Image.open('imyours.png')
            img13.show()
            img14=Image.open('vavavis.png')
            img14.show()


        elif mbti=="INFJ":
            print(f"INFJ인 {name}님에게 추천해드릴 음악은 태연 – Blue , UMI - Midnight Blues 입니다.")
            img15=Image.open('blue.png')
            img15.show()
            img16=Image.open('umi.png')
            img16.show()

        elif mbti=="ENFP":
            print(f"ENFP인 {name}님에게 추천해드릴 음악은  Carly Rae Jepsen - call me maybe , Taylor Swift - Blank Space 입니다.")
            img17=Image.open('callmemaybe.png')
            img17.show()
            img18=Image.open('blankspace.png')
            img18.show()

        elif mbti=="ENFJ":
            print(f"ENFJ인 {name}님에게 추천해드릴 음악은 Lauv - Paris in the rain , Jvke - Secrets 입니다.")
            img19=Image.open('paris.png')
            img19.show()
            img20=Image.open('secrets.png')
            img20.show()


        elif mbti=="ENTJ":
            print(f"ENTJ인 {name}님에게 추천해드릴 음악은 Stefflon Don - 16 shots , Zella Day - Hypnotic 입니다.")
            img21=Image.open('16shots.png')
            img21.show()
            img22=Image.open('hypnotic.png')
            img22.show()


        elif mbti=="ENTP":
            print(f"ENTP인 {name}님에게 추천해드릴 음악은 블랙핑크 - pretty savage , Confetti - ghost 입니다.")
            img23=Image.open('prettysavage.png')
            img23.show()
            img24=Image.open('ghost.png')
            img24.show()

        elif mbti=="ESFP":
            print(f"ESFP인 {name}님에게 추천해드릴 음악은 One direction - what makes you beautiful , 비스트 – 아름다운 밤이야 입니다.")
            img25=Image.open('whatmakesyoubeautiful.png')
            img25.show()
            img26=Image.open('아름다운밤이야.png')
            img26.show()

        elif mbti=="ESFJ":
            print(f"ESFJ인 {name}님에게 추천해드릴 음악은 Burno Major – nothing , Chelsea Collins - 07 Britney 입니다.")
            img27=Image.open('nothing.png')
            img27.show()
            img28=Image.open('07britney.png')
            img28.show()


        elif mbti=="ESTJ":
            print(f"ESTJ인 {name}님에게 추천해드릴 음악은 하진 - we all lie , Bishop Briggs - Champion 입니다.")
            img29=Image.open('wealllie.png')
            img29.show()
            img30=Image.open('champion.png')
            img30.show()


        else:
            print(f"ESTP인 {name}님에게 추천해드릴 음악은 Rose - APT. , GDRAGON - HOME SWEET HOME 입니다.")
            img31=Image.open('img\apt.png')
            img31.show()
            img32=Image.open('homesweethome.png')
            img32.show()


        self.root.quit()


# Tkinter 창 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = MBTIApp(root)
    root.mainloop()