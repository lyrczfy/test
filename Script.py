class script(object):
    START_TXT = """<b>𝖧𝖾𝗒 {},𝖭𝗂𝖼𝖾 𝖳𝗈 𝖬𝖾𝖾𝗍 𝖸𝗈𝗎

𝖧𝖾𝗋𝖾 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖦𝖾𝗍 𝖥𝗂𝗅𝖾𝗌 𝖨𝗇𝗌𝗂𝖽𝖾 𝖳𝗁𝖾 𝖡𝗈𝗍,
𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖭𝖺𝗆𝖾 𝖶𝗂𝗍𝗁 𝖯𝗋𝗈𝗉𝖾𝗋 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀..!!

𝖧𝗂𝗍 /cmds 𝖥𝗈𝗋 𝖬𝗈𝗋𝖾.</b>"""

    SPELL_TEXT = """<b>🔖 𝖸𝗈 {} ,
𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽 𝖬𝖾𝖽𝗂𝖺 𝖥𝗂𝗅𝖾𝗌 𝖠𝗋𝖾 𝖭𝗈𝗍 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾.😶</b>
"""
    
    
    HELP_TXT = """<b>𝖧𝖾𝗒 {}

<u>How to Search Movies ‼️</u>
Just Send Name Correctly.
 
<u>Examples:</u>

Oppam 2016
Baahubali 2015

Oppam 2016 1080p
Baahubali 2015 1080p
<blockquote>(For Getting only 1080p Quality Files)</blockquote>
 
Baahubali 2015 Malayalam 
Baahubali 2015 Tamil
<blockquote>(For Dubbed Movie Files)</blockquote>

<u>How to Search Series/Anime/KDrama ‼️</u>
Just Send Name Correctly.
 
<u>Examples:</u>

Dark S02
<blockquote>(S02 for Season 2)</blockquote>

House of the dragon S02E02
<blockquote>(E02 for Episode 2)</blockquote>
 
Brinda S01 Combined
Brinda S01 Merged
<blockquote>(Combined/Merged File)</blockquote>

Berserk S01E07 720p
<blockquote>(720p Quality Files)</blockquote>

𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝗪𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻/𝗘𝗽𝗶𝘀𝗼𝗱𝗲/𝗦𝗲𝗿𝗶𝗲𝘀/𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗 , . : -</b>"""

    CMDS_TXT = """<b>𝖧𝖾𝗒 {} 🫵,
    
/alive - 𝖢𝗁𝖾𝖼𝗄 𝖠𝗅𝗂𝗏𝖾

/help - 𝖦𝗎𝗂𝖽𝖺𝗇𝖼𝖾 𝖥𝗈𝗋 𝖴𝗌𝖺𝗀𝖾

/about - 𝖪𝗇𝗈𝗐 𝖠𝖻𝗈𝗎𝗍 𝖳𝗁𝖾 𝖡𝗈𝗍</b>"""

    SURPRISE_TXT = """<b>𝖰𝗎𝗂𝖼𝗄𝗅𝗒 𝖩𝗈𝗂𝗇 𝖮𝗎𝗋 𝖦𝗋𝗈𝗎𝗉𝗌 & 𝖢𝗁𝖺𝗇𝗇𝖾𝗅,
𝖫𝖾𝗍 𝖳𝗁𝖾 𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖥𝗎𝗇 𝖡𝖾𝗀𝗂𝗇.!</b>"""

    DMCA_TXT = """<b>📯𝗗𝗜𝗦𝗖𝗟𝗔𝗜𝗠𝗘𝗥 :
<blockquote>𝖠𝗅𝗅 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗍𝗁𝗂𝗌 𝖻𝗈𝗍 𝖺𝗋𝖾 𝖿𝗋𝖾𝖾𝗅𝗒 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗈𝗇 𝗍𝗁𝖾 𝗂𝗇𝗍𝖾𝗋𝗇𝖾𝗍 𝗈𝗋 𝗉𝗈𝗌𝗍𝖾𝖽 𝖻𝗒 𝗌𝗈𝗆𝖾𝖻𝗈𝖽𝗒 𝖾𝗅𝗌𝖾.
𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗂𝗌 𝗂𝗇𝖽𝖾𝗑𝗂𝗇𝗀 𝖿𝗂𝗅𝖾𝗌 𝗐𝗁𝗂𝖼𝗁 𝖺𝗋𝖾 𝖺𝗅𝗋𝖾𝖺𝖽𝗒 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗈𝗇 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖿𝗈𝗋 𝖾𝖺𝗌𝖾 𝗈𝖿 𝗌𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀,
𝖶𝖾 𝗋𝖾𝗌𝗉𝖾𝖼𝗍 𝖺𝗅𝗅 𝗍𝗁𝖾 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝗅𝖺𝗐𝗌 𝖺𝗇𝖽 𝗐𝗈𝗋𝗄𝗌 𝗂𝗇 𝖼𝗈𝗆𝗉𝗅𝗂𝖺𝗇𝖼𝖾 𝗐𝗂𝗍𝗁 𝖣𝖬𝖢𝖠 𝖺𝗇𝖽 𝖤𝖴𝖢𝖣.</blockquote>

𝖨𝖿 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗂𝗌 𝖺𝗀𝖺𝗂𝗇𝗌𝗍 𝗅𝖺𝗐 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗎𝗌 𝗌𝗈 𝗍𝗁𝖺𝗍 𝗂𝗍 𝖼𝖺𝗇 𝖻𝖾 𝗋𝖾𝗆𝗈𝗏𝖾𝖽 𝖺𝗌𝖺𝗉.</b>"""

    DELETE_TXT = """‼️ 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧 ‼️

<blockquote>⚠️ 𝗙𝗶𝗹𝗲 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗶𝗻 𝟱 𝗠𝗶𝗻𝘂𝘁𝗲𝘀.</blockquote>

𝗜𝗳 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘁𝗵𝗶𝘀 𝗳𝗶𝗹𝗲, 𝗞𝗶𝗻𝗱𝗹𝘆 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗶𝘀 𝗳𝗶𝗹𝗲 𝘁𝗼 𝗮𝗻𝘆 𝗰𝗵𝗮𝘁 (𝘀𝗮𝘃𝗲𝗱) 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱..."""

    DELETED_TXT = """𝗬𝗼𝘂𝗿 𝗙𝗶𝗹𝗲 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗧𝗼 𝗔𝘃𝗼𝗶𝗱 𝗕𝗢𝗧 𝗕𝗮𝗻.

𝗬𝗼𝘂 𝗖𝗮𝗻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗔𝗴𝗮𝗶𝗻 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁! 🫵"""

    ABOUT_TXT = """<b>○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='telegram.me/rzxbots'>RZ</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <a href='https://www.python.org/download/releases/3.0/'>𝖯𝗒𝗍𝗁𝗈𝗇 𝟥</a>
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com/'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖥𝗋𝖾𝖾 𝖳𝗂𝖾𝗋</a>
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : <a href='https://t.me/source_Codez/3/'>VPS</a></b>"""
    
    STATUS_TXT = """<b>𝖥𝗂𝗅𝖾𝗌 : <code>{}</code>
𝖴𝗌𝖾𝗋𝗌 : <code>{}</code>
𝖢𝗁𝖺𝗍𝗌 : <code>{}</code>
𝖴𝗌𝖾𝖽 : <code>{}</code>
𝖥𝗋𝖾𝖾 : <code>{}</code></b>

𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 <b>[𝖱𝖹𝖷𝖡𝖮𝖳𝖲](telegram.me/rzxbots/11)</b>"""

    INFO = """
𝖳𝗁𝗂𝗌 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖠𝖿𝗍𝖾𝗋 5 𝖬𝗂𝗇𝗎𝗍𝖾𝗌 𝗍𝗈 𝖯𝗋𝖾𝗏𝖾𝗇𝗍 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 !

𝖨𝖿 𝖸𝗈𝗎 𝖣𝗈 𝖭𝗈𝗍 𝖲𝖾𝖾 𝖳𝗁𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝖾𝖽 𝖲𝖾𝗋𝗂𝖾𝗌 𝖥𝗂𝗅𝖾 , 𝖫𝗈𝗈𝗄 𝖠𝗍 𝗍𝗁𝖾 𝖭𝖾𝗑𝗍 𝖯𝖺𝗀𝖾"""

    TIPS = """
 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗙𝗼𝗿𝗺𝗮𝘁𝘀

• 𝖡𝗅𝖺𝖼𝗄 𝖠𝖽𝖺𝗆 
• 𝖣𝗁𝗈𝗈𝗆 3 𝖧𝗂𝗇𝖽𝗂
• 𝖦𝗈𝗅𝖽 2022
• 𝖣𝗈𝗇 2
• 𝖶𝖾𝖽𝗇𝖾𝗌𝖽𝖺𝗒 𝖲01
• 𝖶𝖾𝖽𝗇𝖾𝗌𝖽𝖺𝗒 𝖲01𝖤01

‼️𝗗𝗼𝗻𝘁 𝗮𝗱𝗱 𝘄𝗼𝗿𝗱𝘀 & 𝘀𝘆𝗺𝗯𝗼𝗹𝘀  , . - 𝗹𝗶𝗸𝗲 send link movie series 𝗲𝘁𝗰‼️"""

    SINFO = """
𝖧𝖾𝗒 𝖡𝗋𝗈 😍

🎯 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖡𝗎𝗍𝗍𝗈𝗇 𝖻𝖾𝗅𝗈𝗐 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖠𝗇𝖽 𝖲𝗍𝖺𝗋𝗍 𝖳𝗁𝖾 𝖡𝗈𝗍 ⬇️"""

    CAPTION = """
<code>{file_name}</code>

𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 <b>[𝖱𝖹𝖷𝖡𝖮𝖳𝖲](telegram.me/rzxbots)</b>"""

    IMDB_TEMPLATE_TXT = """
🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> 
🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  
🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} 

🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [𝖱𝖹𝖷𝖡𝖮𝖳𝖲](telegram.me/rzxbots)"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""
    
    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏2.7.3 [ 𝖲𝗍𝖺𝖻𝗅𝖾 ]</code></b>"""

    LOGO = """RZXBOTS"""
