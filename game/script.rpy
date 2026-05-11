# 6th Grade English Learning Simulator
# "I'm {color=#00ccff}going to{/color} ~" Unit — The Jungle Book Story

# 기존 튜토리얼 에러 방지
define e = Character("Eileen")

# ── 이미지 선언 ──────────────────────────────────
image bg01   = "images/BG-01.png"
image bg02   = "images/BG-02.png"
image bg03   = "images/BG-03.png"
image bg04   = "images/BG-04.png"
image bg05   = "images/BG-05.png"
image bg06   = "images/BG-06.png"
image bg07   = "images/BG-07.png"

image cg01   = "images/CG-01.png"
image cg02   = "images/CG-02.png"
image cg03   = "images/CG-03.png"
image cg04   = "images/CG-04.png"

image mow01  = "images/CH-MOW-01.png"
image mow02  = "images/CH-MOW-02.png"
image mow03  = "images/CH-MOW-03.png"
image mow04  = "images/CH-MOW-04.png"
image mow05  = "images/CH-MOW-05.png"
image mow06  = "images/CH-MOW-06.png"

image bal01  = "images/CH-BAL-01.png"
image bal02  = "images/CH-BAL-02.png"
image bal03  = "images/CH-BAL-03.png"

image bag01  = "images/CH-BAG-01.png"
image bag02  = "images/CH-BAG-02.png"
image bag03  = "images/CH-BAG-03.png"

image riy01  = "images/CH-RIY-01.png"
image riy02  = "images/CH-RIY-02.png"
image riy03  = "images/CH-RIY-03.png"

image pat01  = "images/CH-PAT-01.png"
image pat02  = "images/CH-PAT-02.png"

image shk01  = "images/CH-SHK-01.png"
image shk02  = "images/CH-SHK-02.png"
image shk03  = "images/CH-SHK-03.png"

image gry01  = "images/CH-GRY-01.png"
image gry02  = "images/CH-GRY-02.png"

# ── 화면 맞춤 트랜스폼 ─────────────────────────
transform fit_bg:
    fit "cover"
    align (0.5, 0.5)

# 인간 캐릭터용: 캔버스 전체 높이 기준으로 세로 꽉 채움, 하단 정렬
# 이미지가 2400x1309 가로형이라 height 기준으로 scale해야 전신이 잘 보임
transform fit_ch:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.5, 1.0)

# 왼쪽에 배치 (2캐릭터 씬에서 왼쪽 캐릭터)
transform fit_ch_left:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.28, 1.0)

# 아주 왼쪽에 배치 (3캐릭터 씬에서 왼쪽)
transform fit_ch_far_left:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.15, 1.0)

# 가까이 속삭일 때 왼쪽
transform fit_ch_close_left:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.35, 1.0)

# 가까이 속삭일 때 오른쪽
transform fit_ch_close_right:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.65, 1.0)

# 아주 오른쪽에 배치 (3캐릭터 씬에서 오른쪽)
transform fit_ch_far_right:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.85, 1.0)

# 오른쪽에 배치 (2캐릭터 씬에서 오른쪽 캐릭터)
transform fit_ch_right:
    ysize 650
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.72, 1.0)

# 동물(4족 보행, 가로형 이미지에 몸이 꽉 차있음): 화면 너비 기준으로 배치
transform fit_animal:
    xsize 750
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.5, 1.0)

# 동물 왼쪽
transform fit_animal_left:
    xsize 600
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.25, 1.0)

# 동물 오른쪽
transform fit_animal_right:
    xsize 600
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.75, 1.0)

# 발루용: 상체가 위쪽으로 나오는 통통한 형태 — 약간 크게
transform fit_baloo:
    ysize 580
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.5, 1.0)

transform fit_baloo_left:
    ysize 580
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.3, 1.0)

transform fit_baloo_right:
    ysize 580
    fit "contain"
    anchor (0.5, 1.0)
    pos (0.7, 1.0)

# ── 캐릭터 정의 ───────────────────────────────
define Mowgli   = Character("Mowgli",   color="#f5c842")
define Baloo    = Character("Baloo",    color="#e8a04a")
define Bagheera = Character("Bagheera", color="#8888ff")
define Riya     = Character("Riya",     color="#ff88aa")
define Patel    = Character("Mr. Patel",color="#66ccaa")
define Shere    = Character("Shere Khan",color="#ff4444")
define Gray     = Character("Gray",     color="#aaaaff")
define Narrator = Character(None,       what_color="#dddddd")

# ════════════════════════════════════════════
# START
# ════════════════════════════════════════════
label start:
    scene cg01 at fit_bg
    Narrator "Mowgli, the jungle boy.\nToday, he has to leave for the human village."
    Narrator "(정글의 소년 모글리. 그는 오늘, 인간 마을로 떠나야 한다.)"
    jump scene_0

# ════════════════════════════════════════════
# SCENE 0 — 오프닝 : 정글의 경계
# ════════════════════════════════════════════
label scene_0:
    scene bg01 at fit_bg
    show bal02 at fit_baloo_left
    show bag01 at fit_animal_right

    Bagheera "Mowgli, it is time now."

    Bagheera "(모글리, 이제 때가 됐어.)"
    Bagheera "You {color=#00ccff}are going to{/color} live in the human village now."
    Bagheera "(너는 이제 인간 마을에서 살게 될 거야.)"

    hide bal02
    hide bag01
    show mow02 at fit_ch

    Mowgli "But Baloo... Bagheera... I don't want to go."

    Mowgli "(하지만 발루… 바기라… 난 가기 싫어.)"

    show bal02 at fit_baloo_right

    Baloo "Hey, little friend."

    Baloo "(이봐, 꼬마 친구.)"
    Baloo "You {color=#00ccff}are going to{/color} be great out there. I know it."
    Baloo "(넌 그곳에서 아주 잘 지낼 거야. 난 알아.)"

    Mowgli "Are you {color=#00ccff}going to{/color} visit me someday?"

    Mowgli "(언젠가 날 보러 올 거야?)"

    show bag01 at fit_animal_right

    Bagheera "We {color=#00ccff}are going to{/color} always watch over you."

    Bagheera "(우린 항상 널 지켜볼 거야.)"
    Bagheera "Right here in the jungle."
    Bagheera "(여기 정글에서 말이야.)"

    hide bal02
    hide bag01
    hide mow02
    show mow03 at fit_ch

    Mowgli "(혼잣말) What am I {color=#00ccff}going to{/color} do there… all alone?"

    Mowgli "(거기서 난 무얼 하게 될까… 혼자서 말이야.)"

    jump scene_1

# ════════════════════════════════════════════
# SCENE 1 — 마을 입구 : 첫 만남
# ════════════════════════════════════════════
label scene_1:
    hide mow03
    scene bg02 at fit_bg
    show mow01 at fit_ch_left
    show riy01 at fit_ch_right

    Riya "Hello! Is this your first time here?"

    Riya "(안녕! 여긴 처음이야?)"
    Riya "Are you {color=#00ccff}going to{/color} stay in our village?"
    Riya "(우리 마을에 머물 거야?)"

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} say? (모글리는 뭐라고 대답할까?)"

    menu:
        "A) \"Yes! I {b}{color=#ffff00}am going to{/color}{/b} stay and learn everything!\"":
            Mowgli "Yes! I {color=#00ccff}am going to{/color} stay and learn everything!"
            Mowgli "(응! 난 여기에 머물며 모든 걸 배울 거야!)"
            jump route_a

        "B) \"I {b}{color=#ffff00}am not going to{/color}{/b} stay long. I {b}{color=#ffff00}am going to{/color}{/b} go back to the jungle.\"":
            Mowgli "I {color=#00ccff}am not going to{/color} stay long. I {color=#00ccff}am going to{/color} go back to the jungle."
            Mowgli "(난 오래 머물지 않을 거야. 정글로 돌아갈 거거든.)"
            jump route_b

# ════════════════════════════════════════════
# ROUTE A — 마을에 남기로 한 모글리
# ════════════════════════════════════════════
label route_a:
    jump scene_a1

# ── SCENE A-1 — 마을 학교 : 첫날 ────────────
label scene_a1:
    hide mow01
    hide riy01
    scene bg03 at fit_bg
    show mow03 at fit_ch
    show riy01 at fit_ch_far_right
    show pat01 at fit_ch_far_left

    Riya "Welcome, Mowgli! This is our school."

    Riya "(환영해, 모글리! 여긴 우리 학교야.)"
    Riya "What are you {color=#00ccff}going to{/color} study first?"
    Riya "(넌 먼저 뭘 공부할 거야?)"

    Mowgli "I {color=#00ccff}am going to{/color} learn how to read."

    Mowgli "(난 읽는 법을 배울 거야.)"
    Mowgli "Bagheera said that is very important."
    Mowgli "(바기라가 그게 아주 중요하다고 했거든.)"

    Patel "Hello, Mowgli. I am Mr. Patel."

    Patel "(안녕, 모글리. 나는 파텔 선생님이란다.)"
    Patel "Are you {color=#00ccff}going to{/color} try your best today?"
    Patel "(오늘 최선을 다해 볼 거니?)"

    hide riy01
    hide pat01

    show mow03 at fit_ch_close_right

    Mowgli "Yes! I {color=#00ccff}am going to{/color} try really hard!"

    Mowgli "(네! 정말 열심히 해볼 거예요!)"

    show riy03 at fit_ch_close_left

    Riya "(속삭이며) I {color=#00ccff}am going to{/color} help you, Mowgli."

    Riya "(내가 널 도와줄게, 모글리.)"
    Riya "We {color=#00ccff}are going to{/color} be best friends!"
    Riya "(우린 최고의 친구가 될 거야!)"

    jump qa_1a

# ── Q&A 1A — 선생님의 질문 ──────────────────
label qa_1a:
    hide mow03
    hide riy03
    scene bg03 at fit_bg
    show pat02 at fit_ch

    Patel "Mowgli, tomorrow is your first test."

    Patel "(모글리, 내일은 너의 첫 시험이란다.)"
    Patel "What are you {color=#00ccff}going to{/color} do to prepare?"
    Patel "(준비하기 위해 넌 무얼 할 거니?)"

    Narrator "💬 Choose Mowgli's answer! (모글리의 대답을 고르세요!)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} read my book tonight.\"":
            Mowgli "I {color=#00ccff}am going to{/color} read my book tonight."
            Mowgli "(오늘 밤에 책을 읽을 거예요.)"
            Patel "Great! Reading {color=#00ccff}is going to{/color} help you so much. Well done!"
            Patel "(훌륭해! 독서가 너에게 큰 도움이 될 거야. 잘했어!)"

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} practice writing with Riya.\"":
            Mowgli "I {color=#00ccff}am going to{/color} practice writing with Riya."
            Mowgli "(리야와 함께 쓰기 연습을 할 거예요.)"
            Patel "Wonderful! Riya {color=#00ccff}is going to{/color} be a great study partner!"
            Patel "(멋지구나! 리야가 좋은 공부 짝꿍이 될 거야!)"

        "C) \"I {b}{color=#ffff00}am going to{/color}{/b} ask Bagheera for advice.\"":
            Mowgli "I {color=#00ccff}am going to{/color} ask Bagheera for advice."
            Mowgli "(바기라에게 조언을 구할 거예요.)"
            Patel "That is sweet, Mowgli. Your jungle friends {color=#00ccff}are going to{/color} be proud of you!"
            Patel "(상냥하구나, 모글리. 정글 친구들도 널 자랑스러워할 거야!)"

    jump scene_a2

# ── SCENE A-2 — 마을 광장 : 불안한 소문 ──
label scene_a2:
    hide pat02
    scene bg04 at fit_bg
    show mow01 at fit_ch_left
    show riy02 at fit_ch_right

    Riya "Mowgli! I heard something scary!"

    Riya "(모글리! 무서운 소식을 들었어!)"
    Riya "People are saying a huge beast {color=#00ccff}is going to{/color} come to our village!"
    Riya "(마을 사람들이 거대한 맹수가 마을로 올 거라고 하더라!)"

    hide mow01
    show mow04 at fit_ch_left

    Mowgli "...Shere Khan."

    Mowgli "(...시어칸.)"
    Mowgli "He {color=#00ccff}is going to{/color} try to scare everyone here."
    Mowgli "(그는 여기 있는 모두를 겁주려 할 거야.)"

    Riya "Are you {color=#00ccff}going to{/color} do something about it?!"

    Riya "(뭔가 할 거야?!)"

    hide mow04
    show mow01 at fit_ch_left

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} do? (모글리는 어떻게 할까?)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} warn everyone in the village!\"":
            Mowgli "I {color=#00ccff}am going to{/color} warn everyone in the village!"
            Mowgli "(마을 사람들에게 모두 경고할 거야!)"
            Riya "Then I {color=#00ccff}am going to{/color} help you!"
            Riya "(그럼 나도 도와줄게!)"
            $ riya_joins = True

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} go find him myself.\"":
            Mowgli "I {color=#00ccff}am going to{/color} go find him myself."
            Mowgli "(직접 그를 찾아갈 거야.)"
            Riya "By yourself?! Be careful, Mowgli!"
            Riya "(혼자서?! 조심해, 모글리!)"
            $ riya_joins = False

    jump qa_2a

# ── QA-2A — 정글 경계 : 발루의 긴급 경고 ──────────────
label qa_2a:
    hide mow01
    hide riy02
    scene bg06 at fit_bg
    show mow04 at fit_ch_left
    show bal03 at fit_baloo_right

    Baloo "Mowgli! I {color=#00ccff}am going to{/color} tell you something very important!"

    Baloo "(모글리! 매우 중요한 사실을 말해줄게!)"
    Baloo "Shere Khan {color=#00ccff}is going to{/color} attack the village at sunset!"
    Baloo "(시어칸이 해질 무렵 마을을 공격할 거야!)"

    hide mow04
    show mow03 at fit_ch_left

    Mowgli "BALOO! I already know. We {color=#00ccff}are going to{/color} need a plan."

    Mowgli "(발루! 나도 알아. 우린 계획이 필요해.)"

    hide bal03
    show bag03 at fit_animal_right

    Bagheera "Mowgli, only you can stop him."

    Bagheera "(모글리, 오직 네가 그를 막을 수 있어.)"
    Bagheera "You know both the jungle and the village. We {color=#00ccff}are going to{/color} need that."
    Bagheera "(넌 정글과 마을 양쪽을 알잖아. 그게 필요해.)"

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} do to protect both worlds? (모글리는 두 세계를 지키기 위해 무얼 할까?)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} stand between them and protect both sides!\"":
            Mowgli "I {color=#00ccff}am going to{/color} stand between them and protect both sides!"
            Mowgli "(양쪽 사이에 서서 둘 다 지킬 거야!)"
            jump ending_1

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} call the villagers. We {b}{color=#ffff00}are going to{/color}{/b} face him together!\"":
            Mowgli "I {color=#00ccff}am going to{/color} call the villagers. We {color=#00ccff}are going to{/color} face him together!"
            Mowgli "(마을 사람들을 부를게. 다 같이 맞서는 거야!)"
            Bagheera "Together… that is the way."
            Bagheera "(함께라면… 그게 맞는 방법이야.)"
            Narrator "Mowgli ran back to the village as fast as he could..."
            Narrator "(모글리는 전력을 다해 마을로 달려갔다…)"
            jump ending_1

# ── ENDING 1 — 두 세계의 다리 ───────────────
label ending_1:
    hide mow03
    hide bag03
    scene cg02 at fit_bg

    Mowgli "Everyone! This is my family from the jungle."

    Mowgli "(여러분! 이쪽은 정글에서 온 제 가족이에요.)"
    Mowgli "We {color=#00ccff}are going to{/color} be friends — all of us, together!"
    Mowgli "(우린 모두 친구가 될 거예요, 다 함께요!)"

    show riy01 at fit_ch

    Riya "Are you {color=#00ccff}going to{/color} teach us about the jungle?"

    Riya "(정글에 대해 우리에게 가르쳐 줄 거니?)"

    show bal03 at fit_ch

    Baloo "We {color=#00ccff}are going to{/color} have SO much fun!"

    Baloo "(우린 정말 즐거운 시간을 보낼 거야!)"

    hide riy01
    hide bal03
    show bag03 at fit_ch

    Bagheera "(조용히) Mowgli… you {color=#00ccff}are going to{/color} change this world."

    Bagheera "(모글리... 넌 이 세상을 바꿀 거란다.)"

    hide bag03
    show mow06 at fit_ch

    Mowgli "I {color=#00ccff}am going to{/color} love both worlds. Forever."

    Mowgli "(저는 두 세계 모두를 사랑할 거예요. 영원히요.)"

    hide mow06
    Narrator "⭐ THE END ⭐"
    Narrator "Mowgli became a bridge between two worlds."
    Narrator "(모글리는 두 세계를 잇는 다리가 되었습니다.)"
    Narrator "Keeping both the jungle and the village in his heart forever."
    Narrator "(정글과 마을 모두를 영원히 마음속에 간직한 채로요.)"

    return

# ════════════════════════════════════════════
# ROUTE B — 정글로 돌아가기로 한 모글리
# ════════════════════════════════════════════
label route_b:
    jump scene_b1

# ── SCENE B-1 — 정글 입구 : 돌아온 모글리 ───
label scene_b1:
    hide mow01
    hide riy01
    scene bg05 at fit_bg
    show mow05 at fit_ch

    Mowgli "(혼잣말) I {color=#00ccff}am going to{/color} find Baloo and Bagheera."

    Mowgli "(발루와 바기라를 찾을 거야.)"
    Mowgli "I {color=#00ccff}am going to{/color} go back where I belong."
    Mowgli "(내가 있던 곳으로 돌아갈 거야.)"

    hide mow05
    show shk01 at fit_animal

    Narrator "The bushes shake, and Shere Khan appears..."

    Narrator "(수풀이 흔들리며 Shere Khan이 나타난다…)"

    Shere "Man-cub."

    Shere "(인간의 아이야.)"
    Shere "You {color=#00ccff}are going to{/color} be sorry you came back."
    Shere "(이곳에 돌아온 걸 후회하게 될 거다.)"

    hide shk01
    show mow05 at fit_ch_left

    Mowgli "I {color=#00ccff}am not going to{/color} run. Not anymore."

    Mowgli "(도망치지 않을 거야. 더 이상은.)"

    show shk01 at fit_animal_right

    Shere "Then what are you {color=#00ccff}going to{/color} do, little man-cub?"

    Shere "(그럼 어쩔 셈이야, 꼬마 인간?)"

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} say to Shere Khan? (모글리는 시어칸에게 뭐라고 말할까?)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} protect the jungle. Are you {b}{color=#ffff00}going to{/color}{/b} help me or hurt me?\"":
            Mowgli "I {color=#00ccff}am going to{/color} protect the jungle. Are you {color=#00ccff}going to{/color} help me or hurt me?"
            Mowgli "(난 정글을 지킬 거야. 날 도울 거야, 아니면 해칠 거야?)"
            jump route_bl

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} leave. I {b}{color=#ffff00}am not going to{/color}{/b} fight you.\"":
            Mowgli "I {color=#00ccff}am going to{/color} leave. I {color=#00ccff}am not going to{/color} fight you."
            Mowgli "(난 떠날 거야. 너와 싸우지 않을 거야.)"
            jump route_br

# ════════════════════════════════════════════
# ROUTE B-L — 대결과 화해
# ════════════════════════════════════════════
label route_bl:
    hide mow05
    hide shk01
    scene bg06 at fit_bg
    show mow03 at fit_ch_left
    show shk02 at fit_animal_right

    Shere "(Long silence) ...Protect the jungle? From what?"

    Shere "((긴 침묵) ...정글을 지킨다고? 무엇으로부터?)"
    Mowgli "Humans. They {color=#00ccff}are going to{/color} cut down the trees."
    Mowgli "(인간들. 그들은 나무를 베어낼 거야.)"
    Mowgli "I {color=#00ccff}am going to{/color} stop them."
    Mowgli "(내가 그들을 막을 거야.)"
    Mowgli "But I {color=#00ccff}am going to{/color} need your help."
    Mowgli "(하지만 네 도움이 필요해.)"
    Shere "You {color=#00ccff}are going to{/color} ask ME for help?"
    Shere "(나한테 도움을 청하겠다고?)"

    hide shk02
    show mow03 at fit_ch_left

    Mowgli "Yes. Because we {color=#00ccff}are going to{/color} lose everything if we don't work together."

    Mowgli "(응. 함께하지 않으면 우린 모든 걸 잃게 될 거니까.)"
    Mowgli "Are you {color=#00ccff}going to{/color} let that happen?"
    Mowgli "(그렇게 되도록 내버려 둘 거야?)"

    hide mow03
    show shk02 at fit_animal_right

    Shere "…What exactly are you {color=#00ccff}going to{/color} do, man-cub?"

    Shere "(…정확히 뭘 할 셈이야, 꼬마 인간?)"

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} do to save the jungle? (모글리는 정글을 구하기 위해 무얼 할까?)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} talk to the humans peacefully.\"":
            Mowgli "I {color=#00ccff}am going to{/color} talk to the humans peacefully."
            Mowgli "(인간들과 평화롭게 대화할 거야.)"
            Shere "You {color=#00ccff}are going to{/color} talk? Words {color=#00ccff}are going to{/color} stop them?"
            Shere "(대화를 한다고? 말로 그들을 막을 수 있을 것 같아?)"
            Mowgli "Yes. I {color=#00ccff}am going to{/color} speak for both humans and the jungle."
            Mowgli "(응. 난 인간과 정글 모두를 위해 말할 거야.)"

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} use human tools to protect us.\"":
            Mowgli "I {color=#00ccff}am going to{/color} use human tools to protect us."
            Mowgli "(우리를 보호하기 위해 인간의 도구들을 쓸 거야.)"
            Shere "…You {color=#00ccff}are going to{/color} use human tools against them."
            Shere "(…인간의 도구를 이용해 그들에게 맞서겠다는 거군.)"
            Mowgli "I {color=#00ccff}am going to{/color} use everything I have learned. For us."
            Mowgli "(우리를 위해 내가 배운 모든 걸 쓸 거야.)"

        "C) \"I {b}{color=#ffff00}am going to{/color}{/b} make a plan with all the animals together.\"":
            Mowgli "I {color=#00ccff}am going to{/color} make a plan with all the animals together."
            Mowgli "(모든 동물들과 함께 계획을 세울 거야.)"
            Shere "You {color=#00ccff}are going to{/color} gather the animals? Even me?"
            Shere "(동물들을 모으겠다고? 나까지도?)"
            Mowgli "Especially you. Everyone {color=#00ccff}is going to{/color} listen if you stand with me."
            Mowgli "(특히 너. 네가 나와 함께한다면 모두가 귀를 기울일 거야.)"

    jump ending_2

# ── ENDING 2 — 정글의 수호자 ─────────────────
label ending_2:
    hide mow03
    hide shk02
    scene cg03 at fit_bg

    show shk03 at fit_animal

    Shere "(처음으로 고개를 숙이며) Then… I {color=#00ccff}am going to{/color} follow you. Just this once."

    Shere "(그렇다면... 널 따를게. 이번 한 번만.)"

    hide shk03
    show bal03 at fit_baloo_left
    show bag03 at fit_animal_right

    Baloo "Mowgli!! We {color=#00ccff}are going to{/color} help too!"

    Baloo "(모글리!! 우리도 도울게!)"
    Bagheera "All of us. We {color=#00ccff}are going to{/color} protect this jungle together."
    Bagheera "(우리 모두. 다 함께 이 정글을 지키는 거야.)"

    hide bal03
    hide bag03
    show mow03 at fit_ch

    Mowgli "We {color=#00ccff}are going to{/color} save our home."

    Mowgli "(우리의 집을 구할 거야.)"

    hide mow03
    show mow06 at fit_ch

    Mowgli "(정글을 바라보며) This is where I {color=#00ccff}am going to{/color} stand. Right here. Forever."

    Mowgli "(여기가 내가 설 곳이야. 바로 여기. 영원히.)"

    hide mow06
    Narrator "⭐ THE END ⭐"
    Narrator "Mowgli became the protector of the jungle."
    Narrator "(모글리는 정글의 수호자가 되었습니다.)"
    Narrator "All animals will follow this boy from two worlds."
    Narrator "(두 세계에 속한 이 소년을 모든 동물들이 따르게 될 것입니다.)"

    return

# ════════════════════════════════════════════
# ROUTE B-R — 나만의 길
# ════════════════════════════════════════════
label route_br:
    hide mow05
    hide shk01
    scene bg07 at fit_bg
    show mow05 at fit_ch_right
    show gry01 at fit_animal_left

    Gray "Mowgli! You are back!"

    Gray "(모글리! 돌아왔구나!)"
    Gray "Are you {color=#00ccff}going to{/color} stay with us? Are you {color=#00ccff}going to{/color} stay forever?!"
    Gray "(우리랑 같이 있을 거야? 영원히 있을 거야?!)"

    hide mow05
    show mow02 at fit_ch_right

    Mowgli "I... I am not sure, Gray."

    Mowgli "(나… 나도 잘 모르겠어, 그레이.)"
    Mowgli "I {color=#00ccff}am not going to{/color} fit in the village."
    Mowgli "(난 마을에 어울리지 않아.)"
    Mowgli "But… am I {color=#00ccff}going to{/color} fit here anymore either?"
    Mowgli "(하지만... 이젠 여기에도 어울릴 수 있을까?)"

    hide gry01
    show gry02 at fit_animal_left

    Gray "What are you {color=#00ccff}going to{/color} do then, Mowgli?"

    Gray "(그럼 어떻게 할 거야, 모글리?)"

    hide gry02
    hide mow02
    show mow02 at fit_ch

    Mowgli "…I {color=#00ccff}am going to{/color} find my own path."

    Mowgli "(…내 길을 찾을 거야.)"

    hide mow02
    show bal01 at fit_baloo_left
    show bag01 at fit_animal_right

    Baloo "(나타나며) Little cub. I {color=#00ccff}am going to{/color} ask you something important."

    Baloo "(꼬마야. 중요한 걸 하나 물어볼게.)"
    Baloo "What are you {color=#00ccff}going to{/color} be — a jungle creature, or a human?"
    Baloo "(넌 무엇이 될 거야? 정글의 동물, 아니면 인간?)"

    Narrator "💬 What is Mowgli {color=#00ccff}going to{/color} answer? (모글리는 뭐라고 대답할까?)"

    menu:
        "A) \"I {b}{color=#ffff00}am going to{/color}{/b} be both.\"":
            Mowgli "I {color=#00ccff}am going to{/color} be both."
            Mowgli "(둘 다 될 거야.)"
            Baloo "Ha! Are you {color=#00ccff}going to{/color} live in both places?"
            Baloo "(하! 두 곳 모두에서 살겠다고?)"
            Mowgli "Yes. I {color=#00ccff}am going to{/color} try."
            Mowgli "(응. 해볼 거야.)"

        "B) \"I {b}{color=#ffff00}am going to{/color}{/b} choose the jungle.\"":
            Mowgli "I {color=#00ccff}am going to{/color} choose the jungle."
            Mowgli "(정글을 선택할 거야.)"
            Bagheera "Are you sure, Mowgli? The village {color=#00ccff}is going to{/color} need you too."
            Bagheera "(정말이야, 모글리? 마을도 널 필요로 할 거야.)"
            Mowgli "I know. But the jungle {color=#00ccff}is going to{/color} need me more right now."
            Mowgli "(알아. 하지만 지금은 정글이 날 더 필요로 할 거야.)"

        "C) \"I {b}{color=#ffff00}am going to{/color}{/b} find a new place — just for me.\"":
            Mowgli "I {color=#00ccff}am going to{/color} find a new place — just for me."
            Mowgli "(새로운 곳을 찾을 거야. 나만을 위한 곳을.)"
            Baloo "A new place? Are you {color=#00ccff}going to{/color} build it yourself?"
            Baloo "(새로운 곳? 네가 직접 만들 거야?)"
            Mowgli "I {color=#00ccff}am going to{/color} try. Will you help me?"
            Mowgli "(해볼 거야. 도와줄래?)"
            Baloo "We {color=#00ccff}are going to{/color} help you every single step!"
            Baloo "(매 순간 널 도울게!)"

    jump ending_3

# ── ENDING 3 — 나만의 길 ─────────────────────
label ending_3:
    hide bal01
    hide bag01
    scene cg04 at fit_bg

    show bal02 at fit_baloo

    Baloo "Are you {color=#00ccff}going to{/color} be okay… alone out there?"

    Baloo "(밖에서 혼자서도... 괜찮겠어?)"

    hide bal02
    show mow06 at fit_ch

    Mowgli "I {color=#00ccff}am not going to{/color} be alone, Baloo."

    Mowgli "(난 혼자가 아닐 거야, 발루.)"
    Mowgli "I {color=#00ccff}am going to{/color} carry all of you with me."
    Mowgli "(너희 모두를 내 안에 간직할 테니까.)"
    Mowgli "Right here."
    Mowgli "(바로 여기에.)"

    hide mow06
    show bag02 at fit_animal

    Bagheera "Then we {color=#00ccff}are going to{/color} be with you. Always."

    Bagheera "(그렇다면 우린 너와 함께할 거야. 영원히.)"

    hide bag02
    show mow06 at fit_ch

    Mowgli "I {color=#00ccff}am going to{/color} walk my own road."

    Mowgli "(난 나만의 길을 갈 거야.)"
    Mowgli "And that {color=#00ccff}is going to{/color} change my life."
    Mowgli "(그리고 그것이 내 삶을 바꿔놓겠지.)"

    hide mow06
    Narrator "⭐ THE END ⭐"
    Narrator "Mowgli did not choose the jungle or the village."
    Narrator "(모글리는 정글도, 마을도 선택하지 않았습니다.)"
    Narrator "He decided to walk his own path, and that will change everything."
    Narrator "(자신만의 길을 걷기로 했고, 그것이 모든 것을 바꿔놓게 될 것입니다.)"

    return
