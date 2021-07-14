import os

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

import amino


import base64


import random


import wikipedia


from gtts import gTTS


import urllib.request


from pytube import YouTube


from moviepy.editor import *


from BotHelpers import Helper


from collections import Counter

from keep_alive import keep_alive
keep_alive()

# login


Email = "rovawe9572@dghetian.com"


Password = "ooo456ooo"


# comId


comId = '162126963'


# orginal White list urls


vip = "http://aminoapps.com/p/evs4nu4"


vip2 = "http://aminoapps.com/p/y137fk"


vip3 = "http://aminoapps.com/p/white"


vip4 = "http://aminoapps.com/p/white"


vip5 = "http://aminoapps.com/p/white"


# DeviceIds


dv = '01a2314def86e0f1acf1f154fd8e2b65fd2a0dfc43a682806368a715840f9e5a94f96b1a7a2fccba31'


dv1 = '01b473c479a665bf7753255243f06e8b8caad45ead985dc1d6ec389b8ba7fd690ecc722f4acf2a17c1'


dv2 = '01b126e5544eb07cb2fbe12bc0f9b1ddcefe702088026a20892c78af39e74c97d0a1f3765825391bdd'


dv3 = '014b0c4e03c7df4e8b585eff8a5af3ed0732d9ebf4472e758a35332bb1ea3478f864bb02cc1fe0ffe4'


dv4 = '019fdeb4a923217e25a18049eb7f71bc9300f6d699bbfbeba624e657bc5600902a49454164e7703536'


dv5 = '0149F0FDB25250030785A42198B38088CC0ABF4DBCE4378545EA18D48D524A85D971D0E382CBE8857A'


dv6 = '0126869AF8DCCB676C171F6278E199F3B8A335266BFD5A480F770D871E70793755CA3089AA00E0DE80'


dv7 = '019B6133991CBC2428F822E55AEF0499B3E674928B3268072CC9381881024F07047DCB9A82899C91B8'


dv8 = '019294F2DFBD6298723C4AF70A979D8C4C2DE7035BD014FCE004F94D0D18BADBB15AB93A7A8B8B3D29'





msg = f"""





[C] مرحباً بك أنرت الدردشة!





[C]نرجوا منك قراءة القوانين لتجنب المخالفة





"""





client = amino.Client()


client.login(Email, Password)


aaa = Helper(headers=client.headers, client=client, amino=amino)


aaa.setCom(comId)


wikipedia.set_lang('ar')


vipId = client.get_from_code(vip).objectId


vipId2 = client.get_from_code(vip2).objectId


vipId3 = client.get_from_code(vip3).objectId


vipId4 = client.get_from_code(vip4).objectId


vipId5 = client.get_from_code(vip5).objectId


whiteList = [vipId, vipId2, vipId3, vipId4, vipId5]


blackList = []


sub = aaa.sub


print('Done')








@client.event('on_group_member_leave')


def on_group_member_leave(data: amino.objects.Event):


    author = data.message.author


    chatId = data.message.chatId


    msgG = f"""





[C] وداعاً {author.nickname}





[C] نتمنى لك أوقات سعيدة!





"""


    sub.send_message(chatId=chatId, message=msgG)








@client.event('on_group_member_join')


def on_group_member_join(data: amino.objects.Event):


    author = data.message.author


    chatId = data.message.chatId


    url = author.userId


    url = client.get_from_id(url, 0, comId).shortUrl


    icon = urllib.request.urlopen(author.icon)


    sub.send_message(chatId=chatId, message=msg, embedTitle=author.nickname, embedLink=url, embedContent=author.content, embedImage=icon)








@client.event('on_chat_tip')


def on_chat_tip(data: amino.objects.Event):


    msg = data.message


    coins = msg.extensions['tippingCoins']


    chatId = data.message.chatId


    author = data.message.author


    sub.send_message(chatId=chatId, message='[C]شكرا لك على ' + str(coins) + ' قرش' + '\n\n[C]' + author.nickname)








@client.event('on_text_message')


def on_text_message(data: amino.objects.Event):


    mention = data.message.mentionUserIds


    content = data.message.content


    msgId = data.message.messageId


    chatId = data.message.chatId


    author = data.message.author


    if author.userId in blackList: pass


    else:


        if 'ههه' in content:


            sub.send_message(chatId=chatId, message='دوم الضحكة', replyTo=msgId)





        if content.startswith('!تابعيني'):


            if 'تابعيني' in content[8:11]: sub.follow(author.userId)


            else:


                ID = content[8:]


                ID = client.get_from_code(ID).objectId


                sub.follow(userId=ID)


            sub.send_message(chatId=chatId, message='تم متابعة العضو', replyTo=msgId)





        if content.startswith('!unfollow'):


            if 'me' in content[10:13]: sub.unfollow(author.userId)


            else:


                ID = content[10:]


                ID = client.get_from_code(ID).objectId


                sub.unfollow(userId=ID)


            sub.send_message(chatId=chatId, message='تم الغاء متابعة العضو', replyTo=msgId)





        if content.startswith('!tr'):


            MsgContent = sub.get_message_info(chatId=chatId, messageId=msgId).extensions['replyMessage']['content']


            t = trans()


            tr = t.translate(MsgContent, lang_tgt='en')


            sub.send_message(chatId=chatId, message='[CI]' + tr, replyTo=msgId)





        if content.startswith('!say'):


            if len(content) > 70: pass


            else:


                sayed = gTTS(content[5:], slow=False, lang='ar')


                sayed.save('sayed.mp3')


                with open('sayed.mp3', 'rb') as fp:


                    sub.send_message(chatId=chatId, file=fp, fileType='audio')


                os.remove('sayed.mp3')





        if content.startswith('!msg'):


            lst = content.split()


            s = Counter(lst)


            if s['!msg'] != 1:


                blackList.append(author.userId)


                sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لبدأ سبام!!!',


                                 replyTo=msgId)


            else: sub.send_message(chatId=chatId, message=content[5:])





        if content.startswith('!get'):


            if 'me' in content[5:9]: GID = author.userId; com = comId


            else:


                GID = client.get_from_code(content[5:])


                com = GID.path[1:GID.path.index('/')]


            sub.send_message(chatId=chatId, message=f'''


        


[C]comId = {com}





[C]objectId = {GID.objectId}





''', replyTo=msgId)





        if content.startswith('!base64'):


            try:


                en = base64.b64decode(content[8:])


            except:


                en = base64.b64encode(content[8:].encode())


            sub.send_message(chatId=chatId, message=f'[CI]{en.decode()}', replyTo=msgId)





        if '!help' in content:


            sub.send_message(chatId=chatId, message="""[BIC]بدائية الأوامر (!)





[C]- help : إرسال جميع الأوامر


[C]- base64 [النص] : فك وتشفير


[C]- follow [رابط بروفايل] : متابعة


[C]- unfollow [رابط بروفايل] : إلغاء المتابعة


[C]- comment [me - رابط بروفايل - منشن] : ترك بصمة على الحائط





[C]- tr [يجب الرد على الرسالة التي تريد ترجمتها]





[C]- msg [الرسالة] : إرسالة رسالة


[C]- get [رابط] : id إستخراج ال


[C]- say [الرسالة] : إرسالة رسالة صوتية


[C]- search [النص] : البحث في قوقل


[C]- ex [رابط مقطع يوتيوب] : أستخراج الصوت من مقطع


[C]- longEx [رابط مقطع يوتيوب] : أستخراج الصوت من مقطع طويل


[C]- res [None - رابط دردشة] : إستخراج صور الدردشة وإرسالها





[BIC]القائمة البيضاء





[C]- prank [عدد القروش] : إرسال قروش وهمية


[C]- black [منشن - رابط بروفايل] : إضافة عضو إلى القائمة السوداء


[C]- white [منشن - رابط بروفايل] : إضافة عضو إلى القائمة البيضاء


[C]- unblack [منشن - رابط بروفايل] : إزالة عضو من القائمة السوداء


[C]- unwhite [منشن - رابط بروفايل] : إزالة عضو من القائمة البيضاء


[C]- view [True - False] : وضع الأطلاع


[C]- join [رابط دردشة] : دخول دردشة


[C]- chat [منشن - me - رابط عضو] : بدأ دردشة


[C]- vc : دخول الدردشة المباشرة كمشاهدة


[C]- deviceId : إعطائك ديفايس اي دي


[C]- kick [منشن] : طرد عضو


[C]- ban [منشن] : طرد عضو نهائي


[C]- post [t=عنوان & c=محتوى] : إنشاء مدونة


[C]- start : بدأ غرفة صوتية


[C]- end : أنهاء الغرفة الصوتية


[C]- set com [comId] : تعيين منتدى جديد


[C]- set welcome [رسالة الترحيب] : تعيين رسالة ترحيب جديدة





[BC]أوامر سبيشيال-تشان


[C]- نداء سبيشيال : Bella


[C]- Bella give me [أي شيء] : إعطائك شيء


[C]- Bella kiss me : تقبيلك


[C]- Bella sit on my lap : تجلس فحضنك


[C]- Bella join the chat : دعوتها للدردشة ومن ثم وضع هذا الأمر لكي تنضم





""", replyTo=msgId)





        if content.startswith('!search'):


            st = wikipedia.search(content[8:])


            s = wikipedia.summary(st[0])


            sub.send_message(chatId=chatId, message=f"""


[CBI]{st[0]}  


  


[CI]{s[0:1990]}""", replyTo=msgId)





        if content.startswith('!res'):


            if 'http' in content:


                obj = client.get_from_code(content[5:])


                COM = obj.path


                COM = COM[1:COM.index('/')]


                subO = amino.SubClient(COM, profile=client.profile)


                info = subO.get_chat_thread(obj.objectId)


                icons = [info.icon, info.backgroundImage]


            else:


                info = sub.get_chat_thread(chatId)


                icons = [info.icon, info.backgroundImage]


            for icon in icons:


                ic = urllib.request.urlopen(icon)


                sub.send_message(chatId, fileType='image', file=ic)





        if content.startswith('!longEx'):


            Video = YouTube(content[8:])


            Video.streams.first().download(filename='video')


            vc = VideoFileClip('video.mp4')


            trim = vc.subclip(0, 180)


            ac = trim.audio


            ac.write_audiofile('audio.mp3')


            with open('audio.mp3', 'rb') as fp:


                sub.send_message(chatId=chatId, fileType='audio', file=fp)


            vc.close()


            ac.close()


            os.remove('video.mp4')


            os.remove('audio.mp3')





        if content.startswith('!ex'):


            Video = YouTube(content[4:])


            Video.streams.first().download(filename='video')


            vc = VideoFileClip('video.mp4')


            ac = vc.audio


            ac.write_audiofile('audio.mp3')


            with open('audio.mp3', 'rb') as fp:


                sub.send_message(chatId=chatId, fileType='audio', file=fp)


            vc.close()


            ac.close()


            os.remove('video.mp4')


            os.remove('audio.mp3')





        if content.startswith('!comment'):


            if mention is None:


                if 'me' in content[9:12]:


                    sub.comment('[CB]👉👈💗', userId=author.userId)


                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=author.userId)


                else:


                    obj = client.get_from_code(content[9:]).objectId


                    sub.comment('[CB]👉👈💗', userId=obj)


                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=obj)


            else:


                for user in mention:


                    sub.comment('👉👈💗', userId=user)


                    sub.send_message(chatId, "تم ترك تعليق في حائط <$العضو$>", replyTo=msgId, mentionUserIds=user)





        if content.startswith('!Bella join the chat'):


            sub.join_chat(chatId)





        if content.startswith('!Bella sit on my lap'):


            sub.send_message(chatId=chatId, message="I will sit 👉👈💞", replyTo=msgId)





        if content.startswith('!Bella'):


            sub.send_message(chatId=chatId, message="عيونها 👈👉💗", replyTo=msgId)





        if content.startswith('!Bella kiss me'):


            sub.send_message(chatId=chatId, message="Take a kiss 👉👈💞", replyTo=msgId)





        if content.startswith('!Bella give me'):


            sub.send_message(chatId=chatId, message="This is a " + content[14:] + f" for {author.nickname} 👉👈💞",replyTo=msgId)





        if author.userId in whiteList:


            if content.startswith('!ban'):


                for user in mention:


                    if user == client.userId:


                        blackList.append(author.userId)


                        sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لطرد البوت!!!', replyTo=msgId)


                    else:


                        sub.kick(user, chatId, False)


                        sub.send_message(chatId, message=f'[C] تم حظر هذا <$العضو$> لمخالفته القواعد! ',mentionUserIds=[user])





            if content.startswith('!kick'):


                for user in mention:


                    if user == client.userId:


                        blackList.append(author.userId)


                        sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لطرد البوت!!!', replyTo=msgId)


                    else:


                        sub.kick(user, chatId, True)


                        sub.send_message(chatId, message=f'[C] تم طرد هذا <$العضو$> لمخالفته القواعد! ', mentionUserIds=[user])





            if content.startswith('!deviceId'):


                r = random.choice([dv, dv1, dv2, dv3, dv4, dv5, dv6, dv7, dv8])


                sub.start_chat(userId=author.userId, message=r)


                sub.send_message(chatId, message=f'[C]<$@{author.nickname}$> أنظر إلى رسائلك الخاصة ', mentionUserIds=[author.userId])





            if content.startswith('!chat'):


                if mention is None:


                    if 'me' in content[6:9]:


                        sub.start_chat(userId=author.userId, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')


                    else:


                        obj = client.get_from_code(content[6:]).objectId


                        sub.start_chat(userId=obj, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')


                    sub.send_message(chatId, message='[C] تم بدأ دردشة مع العضو!', replyTo=msgId)


                else:


                    for user in mention:


                        sub.start_chat(userId=user, message='[C] تم بدأ دردشة معك بسبب أمر من أعضاء القائمة البيضاء')


                        sub.send_message(chatId, message='[C] <$تم بدأ دردشة مع هذا <$العضو!', mentionUserIds=user, replyTo=msgId)





            if content.startswith('!join'):


                obj = client.get_from_code(content[6:]).objectId


                info = sub.get_chat_thread(obj)


                sub.join_chat(obj)


                sub.send_message(chatId, message=f'تم دخول {info.title}', replyTo=msgId)





            if content.startswith('!view'):


                if 'False' in content:


                    sub.edit_chat(chatId, viewOnly=False)


                    sub.send_message(chatId=chatId, message="تم ألغاء تفعيل وضع الأطلاع", replyTo=msgId)


                else:


                    sub.edit_chat(chatId, viewOnly=True)


                    sub.send_message(chatId=chatId, message="تم تفعيل وضع الأطلاع", replyTo=msgId)





            if content.startswith('!unwhite'):


                if mention is None:


                    obj = client.get_from_code(content[9:]).objectId


                    if obj == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)


                    else: whiteList.remove(obj); sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة البيضاء!', replyTo=msgId)


                else:


                    for user in mention:


                        if user == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)


                        else: whiteList.remove(user); sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة البيضاء!', replyTo=msgId)





            if content.startswith('!unblack'):


                if mention is None: blackList.remove(client.get_from_code(content[9:]).objectId)


                else:


                    for user in mention:


                        blackList.remove(user)


                sub.send_message(chatId=chatId, message='[C] تم إزالة العضو من القائمة السوداء!', replyTo=msgId)





            if content.startswith('!vc'):


                client.join_video_chat_as_viewer(comId=comId, chatId=chatId)


                sub.send_message(chatId=chatId, message='[C] تم الدخول كمشاهدة!', replyTo=msgId)





            if content.startswith('!white'):


                if mention is None: whiteList.append(client.get_from_code(content[7:]).objectId)


                else:


                    for user in mention:


                        whiteList.append(user)


                sub.send_message(chatId=chatId, message='[C] تم إضافة العضو إلى القائمة البيضاء!', replyTo=msgId)





            if content.startswith('!black'):


                if mention is None:


                    obj = client.get_from_code(content[8:]).objectId


                    if obj == vipId:


                        pass


                    else:


                        blackList.append(obj)


                else:


                    for user in mention:


                        if user == vipId: blackList.append(author.userId); sub.send_message(chatId=chatId, message='[C] تم إضافتك إلى القائمة السوداء بسبب محاولتك لأزالة قائد القائمة البيضاء!!!', replyTo=msgId)





                sub.send_message(chatId=chatId, message='[C] تم إضافة العضو إلى القائمة السوداء!', replyTo=msgId)





            if '!start' in content:


                aaa.start_vc(comId, chatId, 1)


                sub.send_message(chatId, message='[C] تم بدأ غرفة المشاهدة')





            if '!end' in content:


                aaa.end_vc(comId, chatId)


                sub.send_message(chatId, message='[C] تم إيقاف غرفة المشاهدة')





            if content.startswith('!prank'):


                coins = content[7:]


                sub.send_coins(chatId=chatId, coins=coins, transactionId='2516934b-5e08-4ec7-8fea-6169b7f8862f')





            if content.startswith('!post'):


                content = str(content)


                print(content)


                tit = content[content.index('t='):content.index('&')]


                tit = tit.replace('t=', '')


                con = content[content.index('c='):]


                con = con.replace('t=', '')


                con = con.replace('c=', '')


                sub.post_blog(title=tit, content=con)


                sub.send_message(chatId=chatId, message=f"""[C] تم إنشاء المدونة


[C] العنوان : {tit}


[C] المحتوى : {con}""", replyTo=msgId)





            if content.startswith('!set welcome'):


                con = content[13:]


                global msg


                msg = con


                sub.send_message(chatId, f"""[C] تم إعادة تعيين رسالة الترحيب


{con}""")


