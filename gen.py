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
def _geo(en_c,ar_c,price_en,price_ar,tz_en,tz_ar,extra_en,extra_ar):
    return (f"Online Music Lessons in {en_c}",f"دروس موسيقى أونلاين في {ar_c}",f"Online singing and music lessons for students in {en_c}",f"دروس غناء وموسيقى أونلاين للطلاب في {ar_c}",
     f"Online singing, piano, oud and guitar lessons for students in {en_c}. {price_en}",f"دروس غناء وبيانو وعود وجيتار أونلاين للطلاب في {ar_c}. {price_ar}",
     [f"Students in {en_c} can take one-to-one music lessons with Mohamed Nasser over video call. Lessons are online only: there is no studio or branch in {en_c}.",
      price_en, tz_en, extra_en,
      "Subjects: vocal coaching and singing, piano, oud, guitar, drums and music theory, for children and adults, beginner to advanced. To book, email "+EMAIL+" with the subject, your level and your country."],
     [f"يمكن للطلاب في {ar_c} أخذ دروس موسيقى فردية مع محمد ناصر عبر مكالمة فيديو. الدروس أونلاين فقط، ولا يوجد استوديو أو فرع في {ar_c}.",
      price_ar, tz_ar, extra_ar,
      "المواد: تدريب صوتي وغناء وبيانو وعود وجيتار ودرامز ونظرية موسيقية، للأطفال والكبار من المبتدئ إلى المتقدم. للحجز راسل "+EMAIL+" واذكر المادة ومستواك وبلدك."])
GEO={
"online-music-lessons-egypt":_geo("Egypt","مصر","The lesson rate for students in Egypt is 600 EGP per hour.","سعر الدرس للطلاب في مصر 600 جنيه للساعة.",
  "Time zone: lessons are scheduled in Cairo time, and lessons are available every day.","التوقيت: تُحدد المواعيد بتوقيت القاهرة والدروس متاحة كل يوم.",
  "Students in Egypt can learn Arabic and international songs, oud and maqam basics, and music theory in Arabic or English.","يمكن للطلاب في مصر تعلم الأغاني العربية والعالمية وأساسيات العود والمقامات والنظرية الموسيقية بالعربية أو الإنجليزية."),
"online-music-lessons-saudi-arabia":_geo("Saudi Arabia","السعودية","The Gulf lesson rate is 50 SAR per hour for students in Saudi Arabia.","سعر الدرس في الخليج 50 ريالاً للساعة للطلاب في السعودية.",
  "Time zone: Saudi Arabia is on UTC+3 all year. Lessons are available every day, so you can choose a time that suits your schedule.","التوقيت: السعودية على توقيت UTC+3 طوال العام. الدروس متاحة كل يوم لتختار الوقت المناسب لك.",
  "Students in Saudi Arabia can take lessons in Arabic or English, including Arabic singing, oud and piano.","يمكن للطلاب في السعودية أخذ الدروس بالعربية أو الإنجليزية، ومنها الغناء العربي والعود والبيانو."),
"online-music-lessons-uae":_geo("the UAE","الإمارات","The Gulf lesson rate is 50 AED per hour for students in the UAE.","سعر الدرس في الخليج 50 درهماً للساعة للطلاب في الإمارات.",
  "Time zone: the UAE is on UTC+4 all year. Lessons are available every day, so you can choose a time that suits your schedule.","التوقيت: الإمارات على توقيت UTC+4 طوال العام. الدروس متاحة كل يوم لتختار الوقت المناسب لك.",
  "Students in the UAE can take lessons in Arabic or English. Mohamed has also taught in international schools, so he is used to working with students from different backgrounds.","يمكن للطلاب في الإمارات أخذ الدروس بالعربية أو الإنجليزية. درّس محمد أيضاً في مدارس دولية فهو معتاد على العمل مع طلاب من خلفيات مختلفة."),
"online-music-lessons-worldwide":("Online Music Lessons Worldwide","دروس موسيقى أونلاين حول العالم","Online music lessons for students worldwide","دروس موسيقى أونلاين للطلاب حول العالم",
  "Online singing, piano, oud and guitar lessons for students in Kuwait, Qatar, the UK, the USA and anywhere else. International rate: $20 per hour.","دروس غناء وبيانو وعود وجيتار أونلاين للطلاب في الكويت وقطر وبريطانيا وأمريكا وأي مكان آخر. السعر الدولي 20 دولاراً للساعة.",
  ["Mohamed Nasser teaches one-to-one music lessons over video call to students in any country. There is no studio or branch: all lessons are online.","International rate: $20 per hour. Gulf rate: 50 AED or 50 SAR per hour. Egypt rate: 600 EGP per hour. If you live in Kuwait, Qatar, Bahrain or Oman, email to confirm the rate in your currency.","Students in Kuwait, Qatar, Bahrain, Oman, the UK, the USA, Canada, Australia and Europe can choose a lesson time that fits their time zone, since lessons are available every day.","Subjects: vocal coaching and singing, piano, oud, guitar, drums and music theory, for children and adults, beginner to advanced. To book, email "+EMAIL+" with the subject, your level and your country."],
  ["يدرّس محمد ناصر دروس موسيقى فردية عبر مكالمة فيديو لطلاب في أي دولة. لا يوجد استوديو أو فرع: كل الدروس أونلاين.","السعر الدولي: 20 دولاراً للساعة. سعر الخليج: 50 درهماً أو 50 ريالاً للساعة. سعر مصر: 600 جنيه للساعة. إذا كنت في الكويت أو قطر أو البحرين أو عُمان راسلنا لتأكيد السعر بعملتك.","يمكن للطلاب في الكويت وقطر والبحرين وعُمان وبريطانيا وأمريكا وكندا وأستراليا وأوروبا اختيار وقت الدرس المناسب لتوقيتهم لأن الدروس متاحة كل يوم.","المواد: تدريب صوتي وغناء وبيانو وعود وجيتار ودرامز ونظرية موسيقية، للأطفال والكبار من المبتدئ إلى المتقدم. للحجز راسل "+EMAIL+" واذكر المادة ومستواك وبلدك."]),
}
REDIR={"online-music-lessons-kuwait":"online-music-lessons-worldwide","online-music-lessons-qatar":"online-music-lessons-worldwide","online-music-lessons-uk":"online-music-lessons-worldwide","online-music-lessons-usa":"online-music-lessons-worldwide"}
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
ART.update({
"guitar-for-beginners":("Guitar for Beginners: Your First Weeks","الجيتار للمبتدئين: أول أسابيعك","Guitar for beginners: your first weeks","الجيتار للمبتدئين: أول أسابيعك",
 "How to start guitar: tuning, first chords, finger pain and a simple practice plan for beginners.","كيف تبدأ الجيتار: الدوزان وأول الأكوردات وألم الأصابع وخطة تمرين بسيطة للمبتدئين.",
 ["Start by tuning your guitar every time you play. A tuner app on your phone is enough.","Learn two or three easy open chords first, such as Em, Am and C, and change between them slowly.","Your fingertips may hurt for the first weeks. Short sessions of 10 to 15 minutes each day are better than one long session.","In an online lesson the teacher can see your hand position on camera and fix it early."],
 ["ابدأ بدوزنة الجيتار في كل مرة تعزف فيها. يكفي تطبيق دوزان على الهاتف.","تعلّم أولاً أكوردين أو ثلاثة سهلة مثل Em وAm وC وبدّل بينها ببطء.","قد تؤلمك أطراف الأصابع في الأسابيع الأولى. جلسات قصيرة من 10 إلى 15 دقيقة يومياً أفضل من جلسة طويلة واحدة.","في الدرس أونلاين يرى المدرس وضع يدك بالكاميرا ويصححه مبكراً."]),
"music-theory-basics":("Music Theory Basics for Beginners","أساسيات النظرية الموسيقية للمبتدئين","Music theory basics for beginners","أساسيات النظرية الموسيقية للمبتدئين",
 "Music theory basics: notes, rhythm, scales and key signatures explained simply.","أساسيات النظرية الموسيقية: النغمات والإيقاع والسلالم والعلامات الثابتة بشرح مبسط.",
 ["Music theory is the language of music. You do not need it to start playing, but it makes learning faster.","Begin with the notes and the staff, then note lengths and rhythm, then the major scale.","Practice by playing what you learn on your instrument or singing it, not only reading it.","A teacher can connect theory to the songs you want to play."],
 ["النظرية الموسيقية هي لغة الموسيقى. لا تحتاجها لتبدأ العزف لكنها تجعل التعلم أسرع.","ابدأ بالنغمات والمدرج الموسيقي ثم أطوال النغمات والإيقاع ثم السلم الكبير.","تدرّب بعزف أو غناء ما تتعلمه على آلتك وليس بالقراءة فقط.","يستطيع المدرس ربط النظرية بالأغاني التي تريد عزفها."]),
"music-lessons-for-kids-how-to-start":("Music Lessons for Kids: How to Start","دروس الموسيقى للأطفال: كيف تبدأ","Music lessons for kids: how to start","دروس الموسيقى للأطفال: كيف تبدأ",
 "Tips for parents: choosing an instrument, lesson length and keeping children motivated in online music lessons.","نصائح لأولياء الأمور: اختيار الآلة ومدة الدرس وتحفيز الطفل في دروس الموسيقى أونلاين.",
 ["Let your child try a few instruments or singing before choosing. Interest matters more than the instrument.","Younger children do best with shorter lessons and short daily practice, with a parent nearby for the first sessions online.","Choose songs the child likes. Small wins keep children motivated.","Mohamed Nasser has taught children and adults and has taught in international schools. Email "+EMAIL+" to ask about a first lesson."],
 ["دع طفلك يجرب عدة آلات أو الغناء قبل الاختيار. اهتمام الطفل أهم من نوع الآلة.","الأطفال الأصغر يستفيدون من دروس أقصر وتمرين يومي قصير، مع وجود أحد الوالدين بالقرب في الجلسات الأولى أونلاين.","اختر أغاني يحبها الطفل. الإنجازات الصغيرة تبقي الطفل متحمساً.","درّس محمد ناصر الأطفال والكبار ودرّس في مدارس دولية. راسل "+EMAIL+" للسؤال عن الدرس الأول."]),
})
ART.update({
"breathing-techniques-for-singers":("Breathing Techniques for Singers","تقنيات التنفس للمغنين","Breathing techniques for singers","تقنيات التنفس للمغنين",
 "Simple breathing exercises for singers: low breathing, steady exhale and relaxed posture.","تمارين تنفس بسيطة للمغنين: التنفس العميق والزفير الثابت والوضعية المسترخية.",
 ["Good breath support makes singing easier and protects your voice. Start by standing or sitting tall with relaxed shoulders.","Place a hand on your belly and breathe in slowly through the nose so the belly and lower ribs expand. Do not lift the shoulders.","Exhale on a steady 'sss' for as long as is comfortable, then try it on a hum. Aim for an even flow, not a push.","Practice for a few minutes a day. A teacher can check your posture and breathing on camera."],
 ["دعم التنفس الجيد يجعل الغناء أسهل ويحمي صوتك. ابدأ بالوقوف أو الجلوس بظهر مستقيم وكتفين مسترخيتين.","ضع يدك على بطنك وخذ شهيقاً بطيئاً من الأنف ليتمدد البطن والأضلاع السفلية. لا ترفع الكتفين.","ازفر على صوت 'سسس' ثابت بقدر ما يريحك ثم جرّب على همهمة. الهدف تدفق متساوٍ وليس دفعاً.","تمرّن بضع دقائق يومياً. يستطيع المدرس مراجعة وضعيتك وتنفسك بالكاميرا."]),
"how-to-practice-singing-every-day":("How to Practice Singing Every Day","كيف تتدرب على الغناء يومياً","How to practice singing every day","كيف تتدرب على الغناء يومياً",
 "A simple daily singing practice plan: warm-up, technique, a song and a short review.","خطة يومية بسيطة لتدريب الغناء: تسخين وتقنية وأغنية ومراجعة قصيرة.",
 ["A short daily routine works better than one long weekly session. Fifteen to thirty minutes is a good start.","Begin with a warm-up of breathing and humming for five minutes. Then spend ten minutes on one technique, such as pitch accuracy or breath control.","Sing one song you like and record yourself. Listen back and note one thing to improve next time.","Rest your voice if it feels tired or sore. A teacher can set a plan that fits your level."],
 ["روتين يومي قصير أفضل من جلسة طويلة أسبوعية. من 15 إلى 30 دقيقة بداية جيدة.","ابدأ بتسخين بالتنفس والهمهمة لخمس دقائق. ثم خصص عشر دقائق لتقنية واحدة مثل دقة النغمة أو التحكم في التنفس.","غنِّ أغنية تحبها وسجّل نفسك. استمع وحدد شيئاً واحداً تحسّنه في المرة القادمة.","أرح صوتك إذا شعرت بتعب أو ألم. يستطيع المدرس وضع خطة تناسب مستواك."]),
"online-vs-private-singing-lessons":("Online vs In-Person Singing Lessons","دروس الغناء أونلاين أم حضورياً","Online vs in-person singing lessons","دروس الغناء أونلاين أم حضورياً",
 "Online or in-person singing lessons? What changes, what stays the same and how to decide.","دروس الغناء أونلاين أم حضورياً؟ ما الذي يتغير وما الذي يبقى وكيف تقرر.",
 ["Online lessons save travel time and let you learn with a teacher in another city or country. You need a quiet room, a stable connection and a phone or laptop.","In-person lessons give the teacher more direct sound in the room. Online lessons still cover technique, breathing, repertoire and feedback in real time.","Wired headphones and a good internet connection help the sound quality. Many students find online lessons easier to fit into a busy week.","All of Mohamed Nasser's lessons are one-to-one and online. Email "+EMAIL+" to ask about a first lesson."],
 ["الدروس أونلاين توفر وقت المواصلات وتتيح لك التعلم مع مدرس في مدينة أو دولة أخرى. تحتاج غرفة هادئة واتصالاً ثابتاً وهاتفاً أو لابتوب.","الدروس الحضورية تعطي المدرس صوتاً مباشراً أكثر في الغرفة. الدروس أونلاين تغطي أيضاً التقنية والتنفس والأغاني والملاحظات لحظياً.","السماعات السلكية واتصال إنترنت جيد يحسّنان جودة الصوت. يجد كثير من الطلاب أن الدروس أونلاين أسهل في أسبوع مزدحم.","كل دروس محمد ناصر فردية وأونلاين. راسل "+EMAIL+" للسؤال عن الدرس الأول."]),
})
P["online-singing-lessons"]=("Online Singing Lessons","دروس غناء أونلاين","Online singing lessons with a professional vocal coach","دروس غناء أونلاين مع مدرب صوت محترف",
 "Private online singing lessons with a vocal coach of 10 years: technique, songs and stage confidence, for kids and adults.","دروس غناء خاصة أونلاين مع مدرب صوت بخبرة 10 سنوات: تقنية وأغانٍ وثقة على المسرح للأطفال والكبار.",
 ["Online singing lessons with Mohamed Nasser are one-to-one video lessons built around your voice. In each lesson you warm up, work on one technical goal and sing a song with live feedback.","Typical goals: better pitch, wider range, breath control, singing without strain, learning Arabic or international songs, or preparing for an audition or performance.","Lessons suit children and adults, from complete beginners to working singers. You need a phone or laptop, a quiet room and a stable internet connection.","Mohamed has 10 years of teaching experience and worked as an opera voice coach with singers and artists in Egypt and the Arab world."],
 ["دروس الغناء أونلاين مع محمد ناصر هي دروس فيديو فردية مبنية على صوتك. في كل درس تسخّن وتعمل على هدف تقني واحد وتغني أغنية مع ملاحظات مباشرة.","أهداف شائعة: تحسين دقة النغمة وتوسيع المدى والتحكم في التنفس والغناء بدون إجهاد وتعلم أغانٍ عربية أو عالمية أو التحضير لاختبار أو حفلة.","الدروس مناسبة للأطفال والكبار من المبتدئين تماماً إلى المغنين المحترفين. تحتاج هاتفاً أو لابتوب وغرفة هادئة واتصال إنترنت ثابتاً.","لدى محمد 10 سنوات من خبرة التدريس وعمل كمدرب صوت أوبرالي مع مغنين وفنانين في مصر والعالم العربي."])
P["blog"]=("Guides and Articles","مقالات وأدلة","Music learning guides","أدلة تعلم الموسيقى",
 "Practical guides on singing, piano, guitar and oud from a vocal coach and music teacher with 10 years of experience.","أدلة عملية عن الغناء والبيانو والجيتار والعود من مدرب صوت ومدرس موسيقى بخبرة 10 سنوات.",
 ["Short, practical guides for students and parents, written by Mohamed Nasser."],["أدلة قصيرة وعملية للطلاب وأولياء الأمور بقلم محمد ناصر."])
P.update(GEO); P.update(ART)
SERVICES=[s for s in P if s not in("about","contact","blog") and s not in GEO and s not in ART]
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
    WA=""  # WhatsApp number (digits) - left empty until the user approves publishing it
    is_art=slug in ART; is_geo=slug in GEO
    FAQ_EN=[("What lessons do you teach?","Vocal coaching and singing, piano, oud, guitar, drums and music theory."),
     ("Are the lessons online?","Yes. All lessons are one-to-one over video call. There is no studio or branch."),
     ("Who are the lessons for?","Children and adults, from complete beginners to advanced students and working singers."),
     ("How much do lessons cost?","From $20 per hour internationally, 600 EGP per hour in Egypt and 50 AED or SAR per hour in the Gulf."),
     ("How do I book a lesson?","Email "+EMAIL+" with the subject you want, your level and your country."),
     ("What is your experience?","10 years of teaching singing and instruments, teaching in international schools and working as an opera voice coach with singers and artists in Egypt and the Arab world.")]
    FAQ_AR=[("ما الدروس التي تقدمها؟","تدريب صوتي وغناء وبيانو وعود وجيتار ودرامز ونظرية موسيقية."),
     ("هل الدروس أونلاين؟","نعم. كل الدروس فردية عبر مكالمة فيديو. لا يوجد استوديو أو فرع."),
     ("لمن الدروس؟","للأطفال والكبار من المبتدئين تماماً إلى المتقدمين والمغنين المحترفين."),
     ("كم سعر الدرس؟","من 20 دولاراً للساعة دولياً، و600 جنيه للساعة في مصر، و50 درهماً أو ريالاً للساعة في الخليج."),
     ("كيف أحجز درساً؟","راسل "+EMAIL+" واذكر المادة ومستواك وبلدك."),
     ("ما خبرتك؟","10 سنوات في تدريس الغناء والآلات، مع التدريس في مدارس دولية والعمل كمدرب صوت أوبرالي مع مغنين وفنانين في مصر والعالم العربي.")]
    FAQ=FAQ_AR if ar else FAQ_EN
    RF={"online-music-lessons-egypt":("Do you teach in Arabic?","Yes. Lessons can be in Arabic or English.","هل الدروس بالعربية؟","نعم. يمكن أن تكون الدروس بالعربية أو الإنجليزية."),
        "online-music-lessons-saudi-arabia":("What currency is the rate in?","The Gulf rate is 50 SAR per hour for students in Saudi Arabia.","بأي عملة السعر؟","سعر الخليج 50 ريالاً للساعة للطلاب في السعودية."),
        "online-music-lessons-uae":("What currency is the rate in?","The Gulf rate is 50 AED per hour for students in the UAE.","بأي عملة السعر؟","سعر الخليج 50 درهماً للساعة للطلاب في الإمارات."),
        "online-music-lessons-worldwide":("What if I live in Kuwait, Qatar, the UK or the USA?","Lessons are online, so you can book from anywhere. The international rate is $20 per hour. Email to confirm the rate in your currency.","ماذا لو كنت في الكويت أو قطر أو بريطانيا أو أمريكا؟","الدروس أونلاين فيمكنك الحجز من أي مكان. السعر الدولي 20 دولاراً للساعة. راسلنا لتأكيد السعر بعملتك.")}
    if slug in RF: FAQ=FAQ+[(RF[slug][2],RF[slug][3])] if ar else FAQ+[(RF[slug][0],RF[slug][1])]
    show_faq = not is_art and slug not in ("blog","contact")
    LBL=dict(book="احجز درساً" if ar else "Book a lesson", wa="واتساب" if ar else "WhatsApp", home="الرئيسية" if ar else "Home",
             lessons="الدروس" if ar else "Lessons", blog="المقالات" if ar else "Guides", about="عن محمد" if ar else "About", contact="التواصل" if ar else "Contact",
             faq="أسئلة شائعة" if ar else "Frequently asked questions", method="منهج التدريس" if ar else "Teaching approach",
             cred="الخبرة والمؤهلات" if ar else "Experience and background", country="دروس حسب البلد (أونلاين)" if ar else "Lessons by country (online)",
             more="اقرأ أيضاً" if ar else "Related guides", skip="تخطَّ إلى المحتوى" if ar else "Skip to content")
    # structured data
    schema["@graph"].append({"@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":BRAND,"inLanguage":["en","ar"],"publisher":{"@id":BASE+"/#person"}})
    crumbs=[(LBL["home"],url("index",l))]
    if slug!="index":
        if is_art: crumbs.append((LBL["blog"],url("blog",l)))
        crumbs.append((h,url(slug,l)))
    if len(crumbs)>1:
        schema["@graph"].append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":n+1,"name":c[0],"item":c[1]} for n,c in enumerate(crumbs)]})
    if is_art:
        schema["@graph"].append({"@type":"Article","headline":h,"description":d,"inLanguage":l,"author":{"@id":BASE+"/#person"},"mainEntityOfPage":url(slug,l)})
    if show_faq:
        schema["@graph"].append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]})
    ps="".join(f"<p>{html.escape(x)}</p>" for x in body)
    cta=f'<p class="cta"><a class="btn" href="{url("contact",l)}">{LBL["book"]}</a> <a class="btn alt" href="mailto:{EMAIL}">{EMAIL}</a>'+(f' <a class="btn alt" href="https://wa.me/{WA}">{LBL["wa"]}</a>' if WA else "")+'</p>'
    def lst_(keys): return "<ul>"+"".join(f'<li><a href="{url(k,l)}">{P[k][1 if ar else 0]}</a></li>' for k in keys)+"</ul>"
    extra_html=""
    if slug in("index","online-lessons"):
        extra_html+=f'<h2>{LBL["lessons"]}</h2>'+lst_(SERVICES)
        extra_html+=f'<h2>{LBL["country"]}</h2>'+lst_(GEO)
        extra_html+=f'<h2>{LBL["blog"]}</h2>'+lst_(ART)
    if slug=="blog": extra_html+=lst_(ART)
    if slug in SERVICES and slug not in("index",):
        rel=[k for k in ART][:3]; extra_html+=f'<h2>{LBL["more"]}</h2>'+lst_(rel)
    if is_art:
        extra_html+=f'<h2>{LBL["more"]}</h2>'+lst_([k for k in ART if k!=slug][:3])
    if slug in("index","about"):
        meth=(["كل درس فردي ومبني على صوتك أو آلتك وأهدافك.","نبدأ بتسخين وهدف تقني واحد ثم نطبقه على قطعة أو أغنية تحبها.","تحصل على ملاحظات واضحة وتمرين قصير للأسبوع."] if ar else
              ["Every lesson is one-to-one and built around your voice or instrument and your goals.","Each lesson starts with a warm-up and one technical goal, then applies it to a piece or song you like.","You leave with clear feedback and a short practice plan for the week."])
        extra_html+=f'<h2>{LBL["method"]}</h2><ul>'+"".join(f"<li>{x}</li>" for x in meth)+'</ul>'
    if slug=="index":
        cred=(["10 سنوات من خبرة التدريس","بكالوريوس التربية الموسيقية (كلية التربية الموسيقية، 2020)","دراسة العلاج بالموسيقى في كونسرفتوار القاهرة (2017)","التدريس في مدارس دولية","العمل كمدرب صوت أوبرالي مع مغنين وفنانين في مصر والعالم العربي"] if ar else
              ["10 years of teaching experience","Bachelor of Music Education (Faculty of Music Education, 2020)","Music therapy studies at the Cairo Conservatory (2017)","Taught in international schools","Worked as an opera voice coach with singers and artists in Egypt and the Arab world"])
        extra_html+=f'<h2>{LBL["cred"]}</h2><ul>'+"".join(f"<li>{x}</li>" for x in cred)+'</ul>'
    faq_html=(f'<section><h2>{LBL["faq"]}</h2>'+"".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q,a in FAQ)+'</section>') if show_faq else ""
    bc="".join((f'<a href="{c[1]}">{html.escape(c[0])}</a> &rsaquo; ' if n<len(crumbs)-1 else f'<span>{html.escape(c[0])}</span>') for n,c in enumerate(crumbs)) if len(crumbs)>1 else ""
    bc_html=f'<nav class="bc" aria-label="Breadcrumb">{bc}</nav>' if bc else ""
    nav="".join(f'<a href="{u}">{n}</a>' for n,u in [(LBL["lessons"],url("online-lessons",l)),(LBL["blog"],url("blog",l)),(LBL["about"],url("about",l)),(LBL["contact"],url("contact",l))])+f'<a href="{other}" hreflang="{"en" if ar else "ar"}" lang="{"en" if ar else "ar"}">{"English" if ar else "العربية"}</a>'
    css="*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,'Segoe UI',Tahoma,sans-serif;line-height:1.7;color:#1b1f2a;background:#fbf9f4}a{color:#8a6d1f}header{background:#12182b;padding:.9rem 1rem}.w{max-width:48rem;margin:auto;padding:0 1rem}header .w{display:flex;flex-wrap:wrap;gap:.6rem 1.2rem;align-items:center;justify-content:space-between}header a{color:#f3e6bf;text-decoration:none}.brand{font-family:Georgia,serif;font-size:1.25rem;font-weight:700}nav a{margin-inline-end:1rem;font-size:.95rem}.hero{background:linear-gradient(135deg,#12182b,#2a2340);color:#fff;padding:2.5rem 0}.hero h1{font-family:Georgia,serif;font-size:clamp(1.8rem,5vw,2.8rem);margin:.2rem 0 .8rem;line-height:1.2;color:#fff}main{padding:1.2rem 0 2rem}h1,h2{font-family:Georgia,serif;line-height:1.25}h2{margin-top:2rem;color:#12182b}.bc{font-size:.85rem;margin:.8rem 0}.bc a{color:#8a6d1f}.cta{margin:1.4rem 0}.btn{display:inline-block;background:#c9a227;color:#12182b;padding:.7rem 1.2rem;border-radius:.4rem;text-decoration:none;font-weight:700;margin:.2rem .4rem .2rem 0}.btn.alt{background:transparent;color:inherit;border:1px solid #c9a227}.hero .btn.alt{color:#f3e6bf}details{border:1px solid #e3dcc7;border-radius:.4rem;padding:.6rem .9rem;margin:.5rem 0;background:#fff}summary{cursor:pointer;font-weight:600}footer{background:#12182b;color:#f3e6bf;padding:1.5rem 0;margin-top:2rem}footer a{color:#f3e6bf}.skip{position:absolute;left:-999px}.skip:focus{left:.5rem;top:.5rem;background:#fff;padding:.4rem;z-index:9}"
    head=f'<!DOCTYPE html><html lang="{l}" dir="{"rtl" if ar else "ltr"}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t)}</title><meta name="description" content="{html.escape(d)}"><link rel="canonical" href="{url(slug,l)}"><link rel="alternate" hreflang="en" href="{url(slug,"en")}"><link rel="alternate" hreflang="ar" href="{url(slug,"ar")}"><link rel="alternate" hreflang="x-default" href="{url(slug,"en")}"><meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#12182b"><meta property="og:title" content="{html.escape(t)}"><meta property="og:description" content="{html.escape(d)}"><meta property="og:type" content="{"article" if is_art else "website"}"><meta property="og:url" content="{url(slug,l)}"><meta property="og:site_name" content="{BRAND}"><meta property="og:locale" content="{"ar_AR" if ar else "en_US"}"><meta property="og:image" content="{BASE}/og-card.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(t)}"><meta name="twitter:description" content="{html.escape(d)}"><meta name="twitter:image" content="{BASE}/og-card.png"><meta name="google-site-verification" content="sDAZ7iyrpQMqOidXQUyYy06PUCxTk1MjHHnBAAGbfaQ" /><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><style>{css}</style></head>'
    brand="موها فوكال كوتش" if ar else BRAND
    hdr=f'<body><a class="skip" href="#main">{LBL["skip"]}</a><header><div class="w"><a class="brand" href="{url("index",l)}">{brand}</a><nav aria-label="Main">{nav}</nav></div></header>'
    if slug=="index":
        top=f'<section class="hero"><div class="w"><h1>{html.escape(h)}</h1>{ps}{cta}</div></section><main id="main" class="w">{extra_html}{faq_html}</main>'
    else:
        top=f'<main id="main" class="w">{bc_html}<h1>{html.escape(h)}</h1>{ps}{cta}{extra_html}{faq_html}</main>'
    foot=f'<footer><div class="w"><p>{brand} | <a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="{SAME[0]}" rel="me">Instagram</a> | <a href="{SAME[1]}" rel="me">TikTok</a> | <a href="{SAME[2]}" rel="me">Facebook</a></p></div></footer></body></html>'
    return head+hdr+top+foot
def stub(slug,l):
    tgt=url(REDIR[slug],l); me=url(slug,l)
    return f'<!DOCTYPE html><html lang="{l}"><head><meta charset="utf-8"><title>Redirecting</title><link rel="canonical" href="{tgt}"><meta http-equiv="refresh" content="0; url={tgt}"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body><p><a href="{tgt}">{tgt}</a></p></body></html>'
for l in("en","ar"):
    for r in REDIR:
        d="."+("/ar" if l=="ar" else "")+"/"+r
        os.makedirs(d,exist_ok=True); open(d+"/index.html","w",encoding="utf-8").write(stub(r,l))
slugs=["index"]+list(P)
urls=[]
for l in("en","ar"):
    for s in slugs:
        d="."+("/ar" if l=="ar" else "")+("" if s=="index" else "/"+s)
        os.makedirs(d,exist_ok=True); open(d+"/index.html","w",encoding="utf-8").write(page(s,l)); urls.append(url(s,l))
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc></url>" for u in urls)+"</urlset>")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print(len(urls),"urls")
try:
    from PIL import Image, ImageDraw, ImageFont
    im=Image.new("RGB",(1200,630),(18,24,43)); dr=ImageDraw.Draw(im)
    def F(sz,b=True):
        for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
            try: return ImageFont.truetype(p,sz)
            except Exception: pass
        return ImageFont.load_default()
    dr.rectangle([60,60,1140,570],outline=(201,162,39),width=4)
    dr.text((100,170),"Moha Vocal Coach",font=F(86),fill=(243,230,191))
    dr.text((100,300),"Mohamed Nasser",font=F(48),fill=(255,255,255))
    dr.text((100,380),"Online singing, piano, oud and guitar lessons",font=F(36),fill=(201,162,39))
    dr.text((100,470),"mohavocalcoach.github.io",font=F(30),fill=(243,230,191))
    im.save("og-card.png",optimize=True); print("og-card ok")
except Exception as e: print("og-card skipped",e)
