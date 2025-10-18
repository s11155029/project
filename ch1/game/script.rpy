define a = Character('官員', color="#A9CCE3")
define b = Character('新兵', color="#C8E6C9")
define c = Character('哥哥', color="#FFB3B3")
define d = Character('中尉', color="#FFD27F")
define e = Character('亞伯特_柯勒', color="#D4C99E")

image bg ch1 train = "images/bg/ch.1/bg_ch1_train.png" #蒸汽火車上
image bg ch1 office = "images/bg/ch.1/bg_ch1_conscription_office.png" #報名辦公室
image bg ch1 home = "images/bg/ch.1/bg_ch1_home.png" # 亞伯特回憶家鄉
image bg ch1 assembly = "images/bg/ch.1/bg_ch1_assembly_point.png" #前線集結地
image bg ch1 camp_site = "images/bg/ch.1/bg_ch1_camp_site.png" #營地
image bg ch1 camp = "images/bg/ch.1/bg_ch1_camp.png" #帳篷內
image bg ch1 fire = "images/bg/ch.1/bg_ch1_fire_forest.png" #夢中森林大火


# 亞伯特 柯勒
image albert_kohler_hat = im.Flip("images/ch/albert_kohler/albert_kohler_hat.png", horizontal=True)
image albert_kohler_signup = im.Flip("images/ch/albert_kohler/albert_kohler_singup.png", horizontal=True)
image albert_kohler_note = im.Flip("images/ch/albert_kohler/albert_kohler_note.png", horizontal=True)
image albert_kohler_upset = im.Flip("images/ch/albert_kohler/albert_kohler_upset.png", horizontal=True)

# 官員
image official_indifferent = im.Flip("images/ch/official/official_indifferent.png", horizontal=True)
image official_focus = im.Flip("images/ch/official/offical_focus.png", horizontal=True)

# 新兵
image new_soilder_whisper = im.Flip("images/ch/new_soldier/new_soilder_whisper.png", horizontal=True)

# 中尉
image Lieutenant_yelling = im.Flip("images/ch/Lieutenant/Lieutenant_yelling", horizontal=True)


# 哥哥
image brother_wet = im.Flip("images/ch/brother/brother_wet.png", horizontal=True)


#物品
image boots = "images/it/boots.png" # 軍靴
image helmet = "images/it/helmet.png" # 鋼盔
image note = "images/it/note.png" # 筆記本
image flour = "images/it/flour.png" # 麵粉袋

# 半身角色，左側站位
transform stand_left_half:
    zoom 0.6       # 半身建議 0.85~1.0
    xalign 0.0     # 靠畫面最左邊
    yalign 1.0     # 腳/底部貼地

# 物品統一顯示設定：畫面中央，縮放 0.6
transform item_center:
    zoom 0.6
    xalign 0.5
    yalign 0.5

# 半透明黑幕
image dim_overlay = Solid("#00000080")  # 80 是透明度，可改 00-FF

# === 歷史重點：光點＋彈窗 ===

screen history_focus(title, content):
    modal True
    zorder 200
    add Solid("#000000A0")
    frame:
        align (0.5, 0.5)
        xsize 900
        ysize 600
        padding (20, 20)
        background "#FFFFFF"
        vbox:
            text title size 40 color "#000"
            null height 12         # ← 取代 separator
            viewport:
                draggable True
                mousewheel True
                vbox:
                    spacing 8
                    for line in content:
                        text line size 28 color "#000"
            null height 16
            textbutton "關閉" action Hide("history_focus") xalign 0.5

transform pulse_glow:
    alpha 0.25
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.25
    repeat

# 光點按鈕樣式
style glow_pin_button is default:
    background None
    padding (0, 0)

style glow_pin_button_text is default:
    size 60
    color "#FFD54A"
    outlines [(2, "#0008")]

screen glow_points(scene_id, points):
    zorder 190
    for p in points:
        if p["scene"] == scene_id:
            textbutton "●" style "glow_pin_button" at pulse_glow:
                xpos p["xpos"]
                ypos p["ypos"]
                xanchor 0.5
                yanchor 0.5
                action Show("history_focus", title=p["title"], content=p["content"])

default ch1_points = [
    { "scene": "world_war_1",
      "title": "第一次世界大戰",
      "content": [
          "1916正值第一次世界大戰期間，2月在法國東北部德國發動凡爾賽戰役，是第一次世界大戰中為期最長，傷亡慘重的一場戰役，死傷人數高達七十萬，德軍在初始占上風，但在法軍頑強抵抗下最終沒有拿下法國。",
          "5月底時，德國與英國在北海發生日德蘭海戰",
          "7月開始，持續至11月，英法聯軍發動索姆和戰役，目的是為了緩解凡爾賽戰役所帶來的壓力，這場戰爭重重打擊了德國，此戰役首日也是英軍死傷最多的一天，值得關注的是，索姆和戰爭是坦克首次被使用於戰場上"
      ],
      "xpos": 0.50, "ypos": 0.60 },

    { "scene": "battle_of_the_marne",
      "title": "馬恩和戰役",
      "content": [
          "馬恩和戰役分別發生在第一次世界大戰初期1914與末期1918共兩次",
          "第一次的馬恩和戰役被視為是第一次世界大戰的轉折點，主要阻止了德國對法國發離的攻陷，並從機動站轉為長期的壕溝戰，德軍不得已撤退至艾納河，進入消耗的西線戰士。"
          "第二次馬恩和戰役則是德國最後一次的大型全面進攻，結局卻大敗協約國(法、美、英)爭趨於結束，最終在同年(1918)11月簽屬停戰協議，德國只能轉為全面防守。"
      ],
      "xpos": 0.50, "ypos": 0.60 }
]
# === end ===

# 小框：顯示英文單字與中文解釋
screen vocab_gloss(term, defi):
    modal False            # 不鎖畫面，對話框不會消失
    zorder 350
    frame:
        align (0.5, 0.5)   # 螢幕正中
        padding (16, 14)
        background "#FFFFFF"
        vbox:
            text term size 34 color "#004D99"
            null height 6
            text defi size 28 color "#111"
            null height 8
            textbutton "關閉" action Hide("vocab_gloss") xalign 0.5
    # 允許用滑鼠左鍵/空白鍵關閉，不會推進文字
    key "dismiss" action Hide("vocab_gloss")

# 超連結回呼（改成直接 show_screen，不切換 context）
init python:
    def _gloss_handler(link):
        # link: "term|defi"
        try:
            term, defi = link.split("|", 1)
        except ValueError:
            term, defi = link, ""
        # 立刻顯示小框
        renpy.show_screen("vocab_gloss", term=term, defi=defi)
        # 立刻刷新互動，避免這次點擊把對話往下推
        renpy.restart_interaction()

    # 註冊 handler
    config.hyperlink_handlers["gl"] = _gloss_handler

    # 外觀
    style.hyperlink_text.color = "#4EA3FF"
    style.hyperlink_text.hover_color = "#7FC3FF"
    style.hyperlink_text.underline = True



label start:
    jump chapter1

label chapter1:

    scene bg ch1 train with fade
    "德國，1916年春末。亞伯特·柯勒坐在{a=gl:steam train|蒸汽火車}蒸汽火車{/a}的木製{a=gl:bench|長椅}長椅{/a}上，窗外是逐漸遠去的巴伐利亞山丘。"
    "綠意在鐵軌的顛簸中模糊成了抹茶色的霧，他的指尖緊握著{a=gl:military cap|軍帽}軍帽{/a}。"
    "那是他昨天從徵兵辦公室領到的，一頂過大的灰綠色制帽，還有發霉的味道。"
    "火車終於到了前線集結地。下車時，風裡混著焦油與汗水的味道。"

    scene bg ch1 train with dissolve
    show screen glow_points("world_war_1", ch1_points)
    hide screen glow_points
    show helmet
    hide helmet with dissolve

    show bg ch1 office with fade
    "他才十七歲，實際上連這頂帽子都戴不穩。但當他在{a=gl:sign up|報名}報名{/a}時昂首挺胸，說出十八歲時，那名官員連眉毛都沒抬一下，只問了一句"

    show official_indifferent at stand_left_half
    a "你還能跑嗎？"
    hide official_indifferent

    show bg ch1 home with fade
    show screen glow_points("battle_of_the_marne", ch1_points)
    "亞伯特能跑。他能跑，能打靶，能提起家裡的{a=gl:flour|麵粉}麵粉袋{/a}，更重要的是，他能逃。"
    "逃離那個被沉默壓得快要崩潰的家，自從哥哥在馬恩河戰役中陣亡後，父親就像牆上褪色的軍功勳章一樣，失去了光澤。"
    "母親日日點著{a=gl:candle|蠟燭}蠟燭{/a}祈禱，眼神裡沒有{a=gl:future|未來}未來{/a}，只有等待。"
     hide screen glow_points


    scene bg ch1 assembly with fade
    "亞伯特不想等。他要去前線，去證明他不是次等的柯勒，不是那個在家裡背影永遠比哥哥小一號的弟弟。他要成為男人，在{a=gl:battlefield|戰場}戰場{/a}上掙來屬於自己的名字。"
    show new_soilder_whisper at stand_left_half
    b "索姆河。"
    "旁邊的新兵低聲說，像是在{a=gl:chew|咀嚼}咀嚼{/a}一個陌生的地名，聽說那裡像沼澤一樣，泥濘能把人吸進去。"
    hide new_soilder_whisper
    "亞伯特沒答話。他從背包裡抽出哥哥留下的筆記本，裡頭只有幾頁潦草的{a=gl:handwriting|筆跡}筆跡{/a}，從他嘴裡默默地唸出..."
    show albert_kohler_note at stand_left_half
    e "戰場很吵，但真正的恐懼是{a=gl:silence|安靜}安靜{/a}的時候。你會聽見自己的心跳，還有死人的呼吸。"
    hide albert_kohler_note


    show dim_overlay
    show note at item_center with dissolve
    $ renpy.pause()
    hide note with dissolve
    hide dim_overlay with dissolve

    scene bg ch1 assembly with fade
    "火車終於到了前線集結地。下車時，風裡混著{a=gl:tar|焦油}焦油{/a}與汗水的味道。"

    scene bg ch1 camp_site with fade
    show Lieutenant_yelling at stand_left_half
    "一位{a=gl:lieutenant|中尉}中尉{/a}大聲點名，命令一批新兵跟著他走進帳篷登記。亞伯特走進帳篷時，腳踩在濕軟的{a=gl:mud|泥地}泥地{/a}裡，發出窸窣聲，像是腐爛的蘋果被擠壓"
    hide Lieutenant_yelling
    "營地裡沒有想像中的激昂軍歌，也沒有榮耀的旗幟。只有一排排低矮的帳篷、一臉疲憊的老兵、還有空中盤旋不去的寒鴉，彷彿在替這片土地做記錄。"
    show albert_kohler_signup at stand_left_half
    e "亞伯特·柯勒，二等兵。"
    hide albert_kohler_signup
    show official_focus at stand_left_half
    "他對一名{a=gl:register|登記}登記{/a}軍官報上名字。那人頭也不抬地寫下，然後給了他一個破舊的{a=gl:helmet|鋼盔}鋼盔{/a}和一雙沾血的{a=gl:boots|靴子}靴子{/a}。”
    a "這雙還能穿。"
    hide official_focus

    show boots
    show albert_kohler_upset at item_center with dissolve
    $ renpy.pause()
    hide albert_kohler_upset with dissolve
    hide boots with dissolve

    show albert_kohler_upset at stand_left_half
    "亞伯特想起哥哥在家中留下的最後一句話：別讓別人的腳印決定你的人生"
    "現在，他正穿上不屬於他的靴子，走進一條不知盡頭的路。"
    hide albert_kohler_upset

    scene bg ch1 camp with fade
    "當夜，他被分派到第72步兵團，一支剛從前線撤下補給的部隊。士兵們大多不說話，只是在吃罐頭肉時偶爾咒罵天氣和{a=gl:commander|指揮官}指揮官{/a}。亞伯特躺在潮濕的鋪草上，聽著外面零星的槍聲與遠方大砲的回音。
    "這聲音很遠，卻像是從心裡傳來。他不再是亞伯特·柯勒，學生，弟弟，村裡的{a=gl:postman|郵差}郵差{/a}小幫手。"
    "他現在是士兵，是一枚將被投入{a=gl:flame|火焰}火焰{/a}的彈殼，是一塊還沒被填入戰壕的泥土"

    scene bg ch1 fire with fade
    "當夜幕低垂，寒鴉落在營地的旗杆上，啼聲似哭。亞伯特第一次夢見哥哥，夢中他穿著濕透的軍服，站在燃燒的樹林中，回頭望著亞伯特，眼神既陌生又哀傷。"
    show brother_wet at stand_left_half
    c "你還想來?"
    "亞伯特沒有回答"
    hide brother_wet

    return


