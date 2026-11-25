import os, json, html
BASE="https://mohavocalcoach.github.io"  # set at publish time
EMAIL="mmohanaser@gmail.com"
NAME="Mohamed Nasser"; BRAND="Moha Vocal Coach"
# slug: (en title, ar title, en h1, ar h1, en desc, ar desc, en body[], ar body[])
P={
"vocal-coaching":("Professional Vocal Coaching Online","تدريب صوتي احترافي أونلاين","Professional vocal coaching online","تدريب صوتي احترافي أونلاين",
 "Online vocal coaching with a voice coach who has worked at the Opera and with singers and artists in Egypt and the Arab world.","تدريب صوتي أونلاين مع مدرب عمل في الأوبرا ومع مغنين وفنانين في مصر والعالم العربي.",
 ["Vocal coaching with Mohamed Nasser covers breathing, posture, pitch control, tone and stage confidence. Lessons are one-to-one and online, for beginners and for working singers.","He has 10 years of teaching experience and worked as an opera voice coach, training singers and artists in Egypt and the Arab world."],
 ["يشمل التدريب الصوتي مع محمد ناصر التنفس ووضعية الجسم والتحكم في النغمة وجودة الصوت والثقة على المسرح. الدروس فردية وأونلاين للمبتدئين والمغنين المحترفين.","لديه 10 سنوات من خبرة التدريس وعمل كمدرب صوت أوبرالي لتدريب مغنين وفنانين في مصر والعالم العربي."]),
"singing-lessons":("Private Singing Lessons","دروس غناء خاصة","Private singing lessons, online","دروس غناء خاصة أونلاين",
 "One-to-one online singing lessons for kids and adults, beginner to advanced.","دروس غناء فردية أونلاين للأطفال والكبار من المبتدئ إلى المتقدم.",
 ["Private singing lessons are built around your voice and your goals: learning songs, improving range, or preparing to perform.","Lessons run online, every day of the week, for children and adults."],
 ["دروس الغناء الخاصة مبنية على صوتك وأهدافك: تعلم الأغاني أو توسيع المدى الصوتي أو التحضير للأداء.","الدروس أونلاين طوال أيام الأسبوع للأطفال والكبار."]),
"voice-training":("Professional Voice Training","تدريب الصوت الاحترافي","Professional voice training","تدريب الصوت الاحترافي",
 "Voice training for singers, artists and speakers: technique, breath support and healthy vocal habits.","تدريب صوت للمغنين والفنانين: التقنية ودعم التنفس وعادات صوتية صحية.",
 ["Voice training focuses on technique you can repeat: breath support, resonance, warm-ups and vocal habits that protect your voice.","It suits singers, artists and anyone who wants a stronger, more reliable voice."],
 ["يركز تدريب الصوت على تقنيات يمكن تكرارها: دعم التنفس والرنين والإحماء وعادات تحمي صوتك.","مناسب للمغنين والفنانين وكل من يريد صوتاً أقوى وأكثر ثباتاً."]),
"piano-lessons":("Piano Lessons Online","دروس بيانو أونلاين","Piano lessons online","دروس بيانو أونلاين",
 "Online piano lessons for children and adults, from first notes to advanced playing.","دروس بيانو أونلاين للأطفال والكبار من أول نغمة إلى العزف المتقدم.",
 ["Piano lessons start where you are: reading notes, hand position, scales, and pieces you want to play.","Lessons are private and online."],
 ["تبدأ دروس البيانو من مستواك: قراءة النوتة ووضعية اليد والسلالم والمقطوعات التي تريد عزفها.","الدروس فردية وأونلاين."]),
"oud-lessons":("Oud Lessons Online","دروس عود أونلاين","Oud lessons online","دروس عود أونلاين",
 "Learn oud online: technique, maqam basics and Arabic repertoire, for beginners to advanced players.","تعلم العود أونلاين: التقنية وأساسيات المقام والريبرتوار العربي.",
 ["Oud lessons cover holding and picking technique, tuning, maqam basics and Arabic pieces.","Lessons are private and online, for kids and adults."],
 ["تشمل دروس العود تقنية المسك والريشة والدوزنة وأساسيات المقام والمقطوعات العربية.","الدروس فردية وأونلاين للأطفال والكبار."]),
"guitar-lessons":("Guitar Lessons Online","دروس جيتار أونلاين","Guitar lessons online","دروس جيتار أونلاين",
 "Private online guitar lessons: chords, rhythm, songs and technique for beginners and up.","دروس جيتار خاصة أونلاين: الكوردات والإيقاع والأغاني والتقنية.",
 ["Guitar lessons begin with chords, rhythm and simple songs, then move to technique and the style you want to play.","Lessons are private and online."],
 ["تبدأ دروس الجيتار بالكوردات والإيقاع وأغاني بسيطة ثم التقنية والأسلوب الذي تريده.","الدروس فردية وأونلاين."]),
"drums-lessons":("Drum Lessons Online","دروس درامز أونلاين","Drum lessons online","دروس درامز أونلاين",
 "Online drum lessons: grip, rhythm reading and grooves for beginners and up.","دروس درامز أونلاين: المسك وقراءة الإيقاع والجروفات.",
 ["Drum lessons cover grip, timing, rudiments, reading rhythms and playing along with songs.","Lessons are private and online."],
 ["تشمل دروس الدرامز المسك والتوقيت والأساسيات وقراءة الإيقاعات والعزف مع الأغاني.","الدروس فردية وأونلاين."]),
"music-theory":("Music Theory Lessons","دروس نظرية موسيقية","Music theory lessons online","دروس نظرية موسيقية أونلاين",
 "Music theory lessons: notation, scales, intervals and ear training, taught online.","دروس نظرية موسيقية: النوتة والسلالم والمسافات وتدريب الأذن.",
 ["Music theory lessons cover reading notation, scales, intervals, chords and ear training, linked to your instrument or voice.","Lessons are private and online."],
 ["تشمل دروس النظرية قراءة النوتة والسلالم والمسافات والكوردات وتدريب الأذن مرتبطة بآلتك أو صوتك.","الدروس فردية وأونلاين."]),
"music-education":("Music Education","التعليم الموسيقي","Music education","التعليم الموسيقي",
 "Music education from a teacher with a Bachelor of Music Education and 10 years of teaching.","تعليم موسيقي من مدرس حاصل على بكالوريوس التربية الموسيقية و10 سنوات خبرة.",
 ["Mohamed Nasser holds a Bachelor of Music Education (Faculty of Music Education, 2020) and has 10 years of teaching experience.","Music education here means structured lessons in voice and instruments, adapted to age and level."],
 ["محمد ناصر حاصل على بكالوريوس التربية الموسيقية (كلية التربية الموسيقية 2020) ولديه 10 سنوات خبرة في التدريس.","التعليم الموسيقي هنا يعني دروساً منظمة في الصوت والآلات حسب العمر والمستوى."]),
"international-school-music-teacher":("International School Music Teacher","مدرس موسيقى للمدارس الدولية","Music teacher with international school experience","مدرس موسيقى بخبرة في المدارس الدولية",
 "Music teacher who has taught in international schools, available for private and online lessons.","مدرس موسيقى درّس في مدارس دولية، متاح لدروس خاصة وأونلاين.",
 ["Mohamed Nasser has taught music in international schools and brings classroom experience to private lessons.","Schools or parents can get in touch by email to discuss needs."],
 ["درّس محمد ناصر الموسيقى في مدارس دولية ويقدم خبرة الفصل الدراسي في الدروس الخاصة.","يمكن للمدارس أو أولياء الأمور التواصل بالبريد الإلكتروني لمناقشة الاحتياجات."]),
"music-lessons-for-children":("Music Lessons for Children","دروس موسيقى للأطفال","Music lessons for children, online","دروس موسيقى للأطفال أونلاين",
 "Online music lessons for children: singing, piano, guitar, drums and oud.","دروس موسيقى أونلاين للأطفال: غناء وبيانو وجيتار ودرامز وعود.",
 ["Children's lessons are paced for age and attention span, with songs and games alongside technique.","Singing, piano, guitar, drums and oud are available online."],
 ["دروس الأطفال مناسبة للعمر ومدة التركيز مع أغاني وألعاب بجانب التقنية.","الغناء والبيانو والجيتار والدرامز والعود متاحة أونلاين."]),
"music-lessons-for-adults":("Music Lessons for Adults","دروس موسيقى للكبار","Music lessons for adults, online","دروس موسيقى للكبار أونلاين",
 "Online music lessons for adult beginners and returning players.","دروس موسيقى أونلاين للكبار المبتدئين والعائدين للعزف.",
 ["Adult lessons fit your schedule and goals, whether you are starting from zero or returning after a break.","Lessons are online, every day."],
 ["دروس الكبار تناسب جدولك وأهدافك سواء بدأت من الصفر أو عدت بعد انقطاع.","الدروس أونلاين طوال أيام الأسبوع."]),
"online-lessons":("Online Music Lessons","دروس موسيقى أونلاين","Online music lessons worldwide","دروس موسيقى أونلاين لكل العالم",
 "All lessons are online, one-to-one, for students in Egypt, the Gulf, Europe and beyond. No in-person studio.","كل الدروس أونلاين وفردية لطلاب في مصر والخليج وأوروبا وغيرها. لا يوجد استوديو حضوري.",
 ["All lessons are held online by video call. There is no physical studio or branch, so lessons are not offered in person.","Students join from Egypt, the Gulf, Europe and elsewhere. Prices: from $20/hour (international), 600 EGP/hour (Egypt), 50 AED/SAR per hour (Gulf)."],
 ["كل الدروس تتم أونلاين بمكالمة فيديو. لا يوجد استوديو أو فرع فعلي، لذلك لا تتوفر دروس حضورية.","ينضم الطلاب من مصر والخليج وأوروبا وغيرها. الأسعار: من 20 دولار للساعة (دولي)، 600 جنيه للساعة (مصر)، 50 درهم/ريال للساعة (الخليج)."]),
"about":("About Mohamed Nasser","عن محمد ناصر","About Mohamed Nasser","عن محمد ناصر",
 "Mohamed Nasser: vocal coach and music teacher with 10 years of experience.","محمد ناصر: مدرب صوت ومدرس موسيقى بخبرة 10 سنوات.",
 ["Mohamed Nasser is a vocal coach and music teacher with 10 years of teaching experience. He has a Bachelor of Music Education (Faculty of Music Education, 2020) and studied music therapy at the Cairo Conservatory (2017).","He has taught in international schools and worked as an opera voice coach, training singers and artists in Egypt and the Arab world."],
 ["محمد ناصر مدرب صوت ومدرس موسيقى بخبرة 10 سنوات. حاصل على بكالوريوس التربية الموسيقية (كلية التربية الموسيقية 2020) ودرس العلاج بالموسيقى في كونسرفتوار القاهرة (2017).","درّس في مدارس دولية وعمل كمدرب صوت أوبرالي لتدريب مغنين وفنانين في مصر والعالم العربي."]),
"contact":("Contact and Booking","التواصل والحجز","Contact and booking","التواصل والحجز",
 "Book an online lesson with Moha Vocal Coach by email.","احجز درساً أونلاين مع موها فوكال كوتش عبر البريد الإلكتروني.",
 ["To book a lesson, email "+EMAIL+" with the subject you want (singing, piano, oud, guitar, drums or theory), your level and your country.","Lessons are available every day, online."],
 ["لحجز درس راسل "+EMAIL+" واذكر المادة (غناء أو بيانو أو عود أو جيتار أو درامز أو نظرية) ومستواك وبلدك.","الدروس متاحة كل يوم أونلاين."]),
}
def _geo(slug,en_c,ar_c,price_en,price_ar):
    return (f"Online Music Lessons in {en_c}",f"دروس موسيقى أونلاين في {ar_c}",f"Online singing and music lessons for students in {en_c}",f"دروس غناء وموسيقى أونلاين للطلاب في {ar_c}",
     f"Online singing, piano, oud and guitar lessons for students in {en_c}, with a teacher who has 10 years of experience.",f"دروس غناء وبيانو وعود وجيتار أونلاين للطلاب في {ar_c} مع مدرس بخبرة 10 سنوات.",
     [f"Students in {en_c} can take one-to-one music lessons with Mohamed Nasser over video call. Lessons are online only: there is no studio or branch in {en_c}.",
      "Subjects: vocal coaching and singing, piano, oud, guitar, drums and music theory, for children and adults, beginner to advanced.",
      price_en,"To book, email "+EMAIL+" with the subject, your level and your country."],
     [f"يمكن للطلاب في {ar_c} أخذ دروس موسيقى فردية مع محمد ناصر عبر مكالمة فيديو. الدروس أونلاين فقط، ولا يوجد استوديو أو فرع في {ar_c}.",
      "المواد: تدريب صوتي وغناء وبيانو وعود وجيتار ودرامز ونظرية موسيقية، للأطفال والكبار من المبتدئ إلى المتقدم.",
      price_ar,"للحجز راسل "+EMAIL+" واذكر المادة ومستواك وبلدك."])
_pe="Price: 600 EGP per hour."; _pa="السعر: 600 جنيه للساعة."
_ge="Gulf price: from 50 AED or SAR per hour."; _ga="سعر الخليج: من 50 درهماً أو ريالاً للساعة."
_ie="International price: from $20 per hour."; _ia="السعر الدولي: من 20 دولاراً للساعة."
GEO={
"online-music-lessons-egypt":_geo("","Egypt","مصر",_pe,_pa),
"online-music-lessons-saudi-arabia":_geo("","Saudi Arabia","السعودية",_ge,_ga),
"online-music-lessons-uae":_geo("","the UAE","الإمارات",_ge,_ga),
"online-music-lessons-kuwait":_geo("","Kuwait","الكويت",_ge,_ga),
"online-music-lessons-qatar":_geo("","Qatar","قطر",_ge,_ga),
"online-music-lessons-uk":_geo("","the UK","بريطانيا",_ie,_ia),
"online-music-lessons-usa":_geo("","the USA","أمريكا",_ie,_ia),
}
ART={
"how-to-warm-up-your-voice":("How to Warm Up Your Voice Before Singing","كيف تسخّن صوتك قبل الغناء","How to warm up your voice before singing","كيف تسخّن صوتك قبل الغناء",
 "A simple vocal warm-up routine: breathing, lip trills, humming and gentle scales before you sing.","روتين بسيط لتسخين الصوت: التنفس وتمرين الشفاه والهمهمة والسلالم الخفيفة قبل الغناء.",
 ["A warm-up prepares your voice the way stretching prepares a body. Five to ten minutes is enough for most singers.","Start with slow breathing: breathe in through the nose for four counts and out on a soft hiss for eight. Then hum gently on a comfortable pitch and slide up and down.","Add lip trills or a relaxed 'brrr' on easy scales, then sing a few simple vowels (ah, eh, oh). Stop if you feel pain or strain.","A teacher can check your breathing and posture and adapt the routine to your voice. Book a lesson by email."],
 ["التسخين يجهّز صوتك كما يجهّز التمدد الجسم. خمس إلى عشر دقائق تكفي لمعظم المغنين.","ابدأ بتنفس بطيء: شهيق من الأنف لأربع عدّات وزفير بصوت هسهسة هادئ لثماني عدّات. ثم همهم بهدوء على نغمة مريحة واصعد وانزل بالصوت.","أضف تمرين الشفاه أو 'برر' مسترخية على سلالم سهلة، ثم غنِّ حروف علة بسيطة (آ، إي، أو). توقف إذا شعرت بألم أو شد.","يستطيع المدرس مراجعة تنفسك ووضعية جسمك وتعديل الروتين حسب صوتك. احجز درساً عبر البريد."]),
"how-to-choose-an-online-singing-teacher":("How to Choose an Online Singing Teacher","كيف تختار مدرس غناء أونلاين","How to choose an online singing teacher","كيف تختار مدرس غناء أونلاين",
 "What to look for in an online singing teacher: experience, lesson format, goals and a clear first lesson.","ما الذي تبحث عنه في مدرس الغناء أونلاين: الخبرة وشكل الدرس والأهداف وبداية واضحة.",
 ["Look for real teaching experience and clear information about who the teacher is and what they have done.","Check that lessons are one-to-one, that the teacher listens to your goals, and that you get specific feedback after each exercise.","Ask what equipment you need. A phone or laptop, a quiet room and a stable internet connection are enough to start.","Mohamed Nasser has 10 years of teaching experience and has worked as an opera voice coach. Email "+EMAIL+" to ask about a first lesson."],
 ["ابحث عن خبرة تدريس حقيقية ومعلومات واضحة عن المدرس وما عمله.","تأكد أن الدروس فردية وأن المدرس يستمع لأهدافك وأنك تحصل على ملاحظات محددة بعد كل تمرين.","اسأل عن الأدوات المطلوبة. يكفي هاتف أو لابتوب وغرفة هادئة واتصال إنترنت ثابت للبدء.","لدى محمد ناصر 10 سنوات من خبرة التدريس وعمل كمدرب صوت أوبرالي. راسل "+EMAIL+" للسؤال عن الدرس الأول."]),
"learn-piano-online-for-beginners":("Learn Piano Online: A Beginner's Guide","تعلم البيانو أونلاين: دليل للمبتدئين","Learn piano online: a beginner's guide","تعلم البيانو أونلاين: دليل للمبتدئين",
 "How to start learning piano online: posture, finger numbers, reading notes and short daily practice.","كيف تبدأ تعلم البيانو أونلاين: وضعية الجلوس وأرقام الأصابع وقراءة النوتة وتمرين يومي قصير.",
 ["You can start piano with a keyboard at home. A keyboard with full-size keys is better than a toy one, but any keyboard works for the first weeks.","Learn the basics first: sit with a straight back, keep wrists relaxed, number your fingers 1 to 5, and find middle C.","Practice 15 to 20 minutes a day instead of one long session a week. Short, regular practice builds skill faster.","A teacher watching over video can correct hand position early, before bad habits form."],
 ["يمكنك بدء البيانو بكيبورد في البيت. الكيبورد بمفاتيح كاملة أفضل من الألعاب، لكن أي كيبورد يصلح للأسابيع الأولى.","تعلّم الأساسيات أولاً: اجلس بظهر مستقيم وأرخِ المعصمين ورقّم الأصابع من 1 إلى 5 وجد نغمة دو الوسطى.","تمرّن 15 إلى 20 دقيقة يومياً بدل جلسة طويلة واحدة أسبوعياً. التمرين القصير المنتظم يبني المهارة أسرع.","مدرس يراقبك بالفيديو يصحح وضعية اليد مبكراً قبل أن تتكوّن عادات خاطئة."]),
"oud-for-beginners":("Oud for Beginners: Getting Started","العود للمبتدئين: كيف تبدأ","Oud for beginners: getting started","العود للمبتدئين: كيف تبدأ",
 "Starting the oud: holding the instrument, using the right hand, tuning basics and first maqam practice.","بداية العزف على العود: مسكة الآلة وحركة اليد اليمنى وأساسيات الدوزان وأول تمارين المقامات.",
 ["The oud is a fretless string instrument, so ear training matters from the first lesson.","Learn how to hold the oud comfortably, how to use the plectrum (risha) with a relaxed right hand, and how to tune the strings.","Begin with simple exercises on one string, then move to short phrases in common maqams such as Rast and Hijaz.","Online lessons work well for oud: the teacher can see your hand position on camera and play the example for you to repeat."],
 ["العود آلة وترية بلا دسانين، لذلك تدريب الأذن مهم من أول درس.","تعلّم كيف تمسك العود بارتياح وكيف تستخدم الريشة بيد يمنى مسترخية وكيف تدوزن الأوتار.","ابدأ بتمارين بسيطة على وتر واحد ثم انتقل لجمل قصيرة في مقامات شائعة مثل الراست والحجاز.","الدروس أونلاين مناسبة للعود: يرى المدرس وضع يدك بالكاميرا ويعزف المثال لتكرره."]),
}
P.update(GEO); P.update(ART)
SERVICES=[s for s in P if s not in("about","contact") and s not in GEO and s not in ART]
SAME=["https://www.instagram.com/moha_vocal_coach","https://www.tiktok.com/@moha_vocal_coach","https://www.facebook.com/share/1FFcQWyfV2/","https://mohavocalcoach.carrd.co"]
def url(slug,l): 
    p=("" if slug=="index" else slug+"/"); return f"{BASE}/{'ar/' if l=='ar' else ''}{p}"
def page(slug,l):
    if slug=="index":
        t,h,d="Moha Vocal Coach | Online Singing, Piano, Oud, Guitar","Moha Vocal Coach",P["vocal-coaching"][4]
        d="Online vocal coach and music teacher: singing, piano, oud, guitar, drums and music theory, with 10 years of teaching experience."
        body=["Mohamed Nasser has 10 years of teaching singing and instruments, has taught in international schools, and worked as an opera voice coach training singers and artists in Egypt and the Arab world.","All lessons are online and one-to-one, for children and adults, beginner to advanced.","Mohamed Nasser is also known by his teaching name, Moha Vocal Coach: vocal coach, oud teacher and piano teacher online."]
        if l=="ar":
            t,h="موها فوكال كوتش | دروس غناء وبيانو وعود وجيتار أونلاين","موها فوكال كوتش"
            d="مدرب صوت ومدرس موسيقى أونلاين: غناء وبيانو وعود وجيتار ودرامز ونظرية موسيقية بخبرة 10 سنوات."
            body=["لدى محمد ناصر 10 سنوات في تدريس الغناء والآلات، ودرّس في مدارس دولية، وعمل كمدرب صوت أوبرالي لتدريب مغنين وفنانين في مصر والعالم العربي.","كل الدروس أونلاين وفردية للأطفال والكبار من المبتدئ إلى المتقدم.","محمد ناصر معروف أيضاً باسمه التدريسي موها فوكال كوتش: مدرب صوت ومدرس عود وبيانو أونلاين."]
    else:
        e=P[slug]; i=1 if l=="ar" else 0
        t=e[i]+(" | "+("موها فوكال كوتش" if l=="ar" else BRAND)); h=e[2+i]; d=e[4+i]; body=e[6+i]
    ar=l=="ar"
    nav="".join(f'<a href="{url(s,l)}">{P[s][1 if ar else 0]}</a> ' for s in ["about","online-lessons","contact"])
    svc="".join(f'<li><a href="{url(s,l)}">{P[s][1 if ar else 0]}</a></li>' for s in SERVICES)
    other=url(slug,"ar" if l=="en" else "en")
    schema={"@context":"https://schema.org","@graph":[
     {"@type":"Person","@id":BASE+"/#person","name":NAME,"alternateName":["Moha Vocal Coach","محمد ناصر","موها فوكال كوتش"],"jobTitle":"Vocal Coach and Music Teacher","url":BASE+"/","sameAs":SAME,"email":EMAIL,"alumniOf":{"@type":"CollegeOrUniversity","name":"Faculty of Music Education"}},
     {"@type":"WebPage","@id":url(slug,l),"name":t,"description":d,"inLanguage":l,"about":{"@id":BASE+"/#person"}}]}
    if slug in SERVICES:
        schema["@graph"].append({"@type":"Service","name":h,"description":d,"provider":{"@id":BASE+"/#person"},"serviceType":h,"areaServed":"Worldwide (online)","availableChannel":{"@type":"ServiceChannel","serviceUrl":url("contact",l)}})
    ps="".join(f"<p>{html.escape(x)}</p>" for x in body)
    home_link=f'<p><a href="{url("contact",l)}">{"احجز درساً" if ar else "Book a lesson"}</a></p>'
    lst=f'<h2>{"الخدمات" if ar else "Lessons"}</h2><ul>{svc}</ul>' if slug in("index","online-lessons") else ""
    if slug in("index","online-lessons"):
        lst+=f'<h2>{"دروس حسب البلد" if ar else "Lessons by country (online)"}</h2><ul>'+"".join(f'<li><a href="{url(s,l)}">{P[s][1 if ar else 0]}</a></li>' for s in GEO)+f'</ul><h2>{"مقالات" if ar else "Guides"}</h2><ul>'+"".join(f'<li><a href="{url(s,l)}">{P[s][1 if ar else 0]}</a></li>' for s in ART)+'</ul>'

    return f'''<!DOCTYPE html><html lang="{l}" dir="{'rtl' if ar else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t)}</title><meta name="description" content="{html.escape(d)}"><link rel="canonical" href="{url(slug,l)}"><link rel="alternate" hreflang="en" href="{url(slug,'en')}"><link rel="alternate" hreflang="ar" href="{url(slug,'ar')}"><link rel="alternate" hreflang="x-default" href="{url(slug,'en')}"><meta property="og:title" content="{html.escape(t)}"><meta property="og:description" content="{html.escape(d)}"><meta property="og:type" content="website"><meta property="og:url" content="{url(slug,l)}"><meta name="google-site-verification" content="sDAZ7iyrpQMqOidXQUyYy06PUCxTk1MjHHnBAAGbfaQ" /><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><style>body{{font-family:system-ui,sans-serif;max-width:46rem;margin:auto;padding:1rem;line-height:1.6}}nav a{{margin-inline-end:1rem}}</style></head><body><header><a href="{url('index',l)}"><strong>{"موها فوكال كوتش" if ar else BRAND}</strong></a> <nav>{nav}<a href="{other}">{"English" if ar else "العربية"}</a></nav></header><main><h1>{html.escape(h)}</h1>{ps}{home_link}{lst}</main><footer><p>{EMAIL} | <a href="{SAME[0]}">Instagram</a> | <a href="{SAME[1]}">TikTok</a> | <a href="{SAME[2]}">Facebook</a></p></footer></body></html>'''
slugs=["index"]+list(P)
urls=[]
for l in("en","ar"):
    for s in slugs:
        d="."+("/ar" if l=="ar" else "")+("" if s=="index" else "/"+s)
        os.makedirs(d,exist_ok=True); open(d+"/index.html","w",encoding="utf-8").write(page(s,l)); urls.append(url(s,l))
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc></url>" for u in urls)+"</urlset>")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print(len(urls),"urls")
