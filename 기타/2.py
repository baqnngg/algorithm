import tkinter as tk
from PIL import Image, ImageTk

class MBTIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MBTI 검사")
        self.results = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
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

        self.name_label = tk.Label(root, text="이름을 입력하세요", font=("Arial", 14))
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        self.name_button = tk.Button(root, text="시작하기", font=("Arial", 12), command=self.start_test)
        self.name_button.pack(pady=10)
        
    def start_test(self):
        self.username = self.name_entry.get().strip()
        
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.name_button.pack_forget()

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

        # 결과 레이블 업데이트
        result_text = f"{self.username}님의 MBTI 유형은 {mbti}입니다!"
        self.result_label = tk.Label(self.root, text=result_text, font=("Arial", 15))
        self.result_label.pack(pady=20)
        
        self.close_button = tk.Button(self.root, text="닫기", font=("Arial", 12), command=self.root.quit)
        self.close_button.pack(pady=10)

        # 이미지 레이블 추가
        try:
            # 버튼 제거
            self.button_yes.pack_forget()
            self.button_no.pack_forget()

            # 이미지 로드
            if mbti == "INFP":
                self.show_image('everything.png')
                self.show_image('run.png')
            elif mbti == "ISFP":
                self.show_image('byebyemyblue.png')
                self.show_image('mindu.png')
            elif mbti == "ISFJ":
                self.show_image('foreveryoung.png')
                self.show_image('2soon.png')
            elif mbti == "ISTP":
                self.show_image('lovememore.png')
                self.show_image('soso.png')
            elif mbti == "ISTJ":
                self.show_image('누구나비밀은있다.png')
                self.show_image('callonme.png')
            elif mbti == "INTP":
                self.show_image('now.png')
                self.show_image('seoul.png')
            elif mbti == "INTJ":
                self.show_image('imyours.png')
                self.show_image('vavavis.png')
            elif mbti == "INFJ":
                self.show_image('blue.png')
                self.show_image('umi.png')
            elif mbti == "ENFP":
                self.show_image('callmemaybe.png')
                self.show_image('blankspace.png')
            elif mbti == "ENFJ":
                self.show_image('paris.png')
                self.show_image('secrets.png')
            elif mbti == "ENTJ":
                self.show_image('16shots.png')
                self.show_image('hypnotic.png')
            elif mbti == "ENTP":
                self.show_image('prettysavage.png')
                self.show_image('ghost.png')
            elif mbti == "ESFP":
                self.show_image('whatmakesyoubeautiful.png')
                self.show_image('아름다운밤이야.png')
            elif mbti == "ESFJ":
                self.show_image('nothing.png')
                self.show_image('07britney.png')
            elif mbti == "ESTJ":
                self.show_image('wealllie.png')
                self.show_image('champion.png')
            else:
                self.show_image('apt.png')
                self.show_image('homesweethome.png')
        except Exception as e:
            print(f"이미지 로드 중 오류 발생: {e}")
        
    def show_image(self, image_name):
        try:
            img_path = f'img\\{image_name}'  # 기존 경로에서 이미지를 로드합니다.
            img = Image.open(img_path)
            img = img.resize((200, 200))  # 창에 맞게 이미지 크기 조정
            img_tk = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.root, image=img_tk)
            image_label.image = img_tk  # 이미지를 유지하기 위한 참조
            image_label.pack(pady=10)
        except FileNotFoundError:
            print(f"이미지 파일을 찾을 수 없습니다: {image_name}")

# Tkinter 창 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = MBTIApp(root)
    root.mainloop()