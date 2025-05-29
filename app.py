from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "super-secret-key"

# Your pool of questions
QUESTION_POOL = [
  {
    "question": "🌍 ประเทศใดมีจำนวนประชากรมากที่สุดในโลก?",
    "options": ["🇮🇳 อินเดีย", "🇺🇸 สหรัฐอเมริกา", "🇨🇳 จีน", "🇮🇩 อินโดนีเซีย"],
    "correct": "🇨🇳 จีน"
  },
  {
    "question": "💡 ใครเป็นผู้ประดิษฐ์หลอดไฟฟ้า?",
    "options": ["⚡️ นิโคลา เทสลา", "🧠 อัลเบิร์ต ไอน์สไตน์", "🛠️ โธมัส เอดิสัน", "🍎 ไอแซก นิวตัน"],
    "correct": "🛠️ โธมัส เอดิสัน"
  },
  {
    "question": "🥚 สัตว์ชนิดใดที่เป็นเลี้ยงลูกด้วยนมแต่สามารถวางไข่ได้?",
    "options": ["🐬 ปลาโลมา", "🦆 ตัวตุ่นปากเป็ด","🌊🐎 ม้านํ้า", "😅 พี่", "❌ ไม่มีในตัวเลือก"],
    "correct": "🦆 ตัวตุ่นปากเป็ด"
  },
  {
    "question": "ท้ายชื่ออนิเมะจาก 🕶️🔵🤞🏻🔴🤌🏻🫴🏻🟣 ☝️👹 ?",
    "options": ["มหาเวทย์ผนึกมาร", "กินทามะ", "สมุดมรณะ", "คําอธิษฐานในวันที่จากลา"],
    "correct": "มหาเวทย์ผนึกมาร"
  },
  {
    "question": "🔬 ธาตุใดมีเลขอะตอมเท่ากับ 79?",
    "options": ["🥉 ทองแดง (Cu)", "🥈 เงิน (Ag)", "🪙 ทองคำ (Au)", "🧱 ธาตุดิน"],
    "correct": "🪙 ทองคำ (Au)"
  },
  {
    "question": "🌦️ อะไรคือสาเหตุหลักที่ทำให้เกิด “ฤดูต่าง ๆ” บนโลก?",
    "options": [
      "🌞 การเปลี่ยนระยะทางจากดวงอาทิตย์",
      "🌀 การเอียงของแกนโลกขณะโคจรรอบดวงอาทิตย์",
      "🔄 การหมุนรอบตัวเองของโลก",
      "💪 ท่านชัชชาติเดิน"
    ],
    "correct": "🌀 การเอียงของแกนโลกขณะโคจรรอบดวงอาทิตย์"
  },
  {
    "question": "🧠 ถ้า 0 = x² + 3x + 2 แล้วข้อใดเป็นคำตอบ?",
    "options": ["-1", "2", "1", "4", "🆘 ช่วยด้วยยย"],
    "correct": "-1"
  },
  {
    "question": "📍 พี่อยู่จังหวัดอะไร?",
    "options": ["🏔️ เชียงราย", "🏙️ เซี่ยงไฮ้", "🏞️ เชียงใหม่", "🌄 แม่สาย", "จังหวัดไรนิ"],
    "correct": "🏔️ เชียงราย"
  },
  {
    "question": "🍓 Which one isn't a fruit?",
    "options": ["Spinach", "Bilimbi", "Apple🍎📢🔥♪♫♪", "Banana🍌📢♪♪♫🔥"],
    "correct": "Spinach"
  },
  {
    "question": "😴 สภาพพี่จะหน้าตาเหมือนคนง่วงตลอดเวลาและชอบสิ่งมีชีวิตที่เรียกว่า...?",
    "options": ["🐱 แมว", "🐱 แมว", "🐱 แมว", "🐱 แมว", "🐱 แมว", "🐱 แมว"],
    "correct": "🐱 แมว"
  }
]
1
@app.route('/')
def index():
    session['score'] = 0
    session['q_index'] = 0
    session['questions'] = random.sample(QUESTION_POOL, 10)  # 10 random questions
    return redirect(url_for('chat'))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if session['q_index'] >= 10:

        if session['score'] > 5 :
            return redirect(url_for('suf'))
        else:
            return redirect(url_for('result'))

    if request.method == 'POST':
        user_answer = request.form['answer']
        current_q = session['questions'][session['q_index']]
        
        if user_answer == current_q['correct']:
            print(user_answer)
            print(current_q['correct'] )
            session['score'] += 1
        session['q_index'] += 1
        return redirect(url_for('chat'))

    current_q = session['questions'][session['q_index']]
    return render_template('chat.html', question=current_q, index=session['q_index'] + 1)

@app.route('/result')
def result():
    return render_template('result.html', score=session['score'])

@app.route('/suf')
def suf():
    return render_template('winner.html', score=session['score'])

if __name__ == '__main__':
    app.run(debug=True)
