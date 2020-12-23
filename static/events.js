class Event {
    static all = [];
    constructor(time/*String*/, type/*Number*/, short_topic/*String*/, topic/*String*/, cost/*Number*/, description/*String*/, imageURL/*String*/) {
        this.time = time;
        this.type = type;
        this.short_topic = short_topic;
        this.topic = topic;
        this.cost = cost;
        this.description = description;
        this.imageURL = imageURL;
        Event.all.push(this);
    }
    getTime() {
        let time = this.time.split(" ")[0].match(/(\d{2})-(\d{2})-(\d{4})/);
        return new Date(time[3], time[2] - 1, time[1]);
    }
    getStrTime() {
        return this.time.split(" ")[1];
    }
    getDay() {
        return (new Date(this.getTime())).getDay();
    }
}

new Event("01-12-2020 16:00-17:30", "Лекція", "Laravel Back-End", "Laravel Back-End Free Course", 0,
`Якщо вам цікава веб-розробка і ви бажаєте дізнатися щось нове для себе, запрошуємо на ввідну лекцію БЕЗКОШТОВНОГО бекенд-куру із вивчення фреймворку Laravel мовою програмування PHP 👩‍💻👨🏻‍💻
Курс вестиме професіонал-практик Senior Laravel Engineer, засновник веб-студії NickStudio, Микола Якубина.
Місце проведення #iHub_khm та online
❗️Увага❗️ Курс розрахований для тих, хто вже має навики веб-розробки (не для новачків)
🤓 Що потрібно вже вміти/знати:
- основи веб-розробки(html, css, js, jQuery, Ajax, Bootstrap);
- вміти працювати з IDE PHP Storm (чи іншим);
- знати, що таке локальний сервер;
- основи ООП та MVC архітектури;
- бажано ознайомитись наперед із статтями про Laravel та сферами його застосування.

Студенти, які успішно завершать курс, будуть стовідсотково запрошені на практику на реальний проект, а потім і на роботу над проектом.
#laravel #Web-dev #back-end #course`,
"IMG_5453");

new Event("03-12-2020 15:00-18:00", "Воркшоп-майстер-клас", "Website Layout from scratch", "Front-End. Website Layout from Scratch using Preprocessors", 0,
`В цей четвер пропонуємо вам цікавий івент, пов’язаний із веб-розробкою. Запрошений гість - професіонал-практик, фронтенд-розробник із 7-річним досвідом веб-розробки, СЕО ІТ Aкадемії @hashtag.khm Дмитро Пиріжок.

З собою потрібно мати гарний настрій та ноутбуки, будемо в режимі реального часу розробляти фронт-енд сайту на препроцесорах🤤

❗️Вопкшоп відбудеться лише в режимі оФлаЙн в @iHub.khm
Нетворкінг та coffee-break зі смаколиками ☕️🍪🥨 включено 😋
Чекаємо на вас, буде мегацікаво і суперкорисно 😉
#hashtag_khm  #workshop  #front-end_development`,
"IMG_5510");

new Event("04-12-2020 15.00-18.00", "Воркшоп-майстер-клас", "Photo Retouch", "Photo Retouch & Colour Correction", 0,
`В один із перших зимових днів хочемо запросити вас в теплу атмосферу воркшопу на тему "Ретуш і світлокорекція фото" 📸 в програмах Adobe Lightroom та Photoshop 🖼️

Спікер - студентка IT-спеціальності, фотограф-фрілансер, відео та контент мейкер - Софія Кравчук (@k.soni_)
Якщо вам цікава фотографія, її обробка, гармонія світла та тіні, атмосферність, а можливо, ви ще й нічого про це не знаєте, але бажаєте 😱
Тоді ми чекаємо на вас в iHub 😉
Якщо бажаєте, на воркшопі можемо розібрати і ваше фото🔥 деталі ПЕРЕД заходом
Обіцяємо багато натхнення🌸 та дружню теплу атмосферу 😍

Із собою рекомендовано мати ноутбук 💻(не обов'язково) та  бажання отримати корисну інформацію та хороший настрій😇
#workshop #photo #Photoshop #Lightroom #photocorrection`,
"IMG_5514");

new Event("07-12-2020 14:00-17:00", "Кіноперегляд", "Social Network", "Social Network", 0,
`Потрібно не тільки працювати та навчатись, але й знаходити час для розваг 😉
І вже в понеділок, 07.12 о 14:00 відбудеться перегляд культового фільму "Соціальна мережа"🎞🤩
Будемо разом дивитись про створення та розвиток найбільшої світової соцмережі Facebook, про реалізацію мрій її засновника - Марка Цукерберга, і про відданість своїй справі.🔥 🤓
Можна приходити із смаколиками, і зробити атмосферу кінозалу 🍪☕

#movie  #networking  #SocialNetwork #Facebook`,
"IMG_5515");

new Event("08-12-2020 15:00-18:00", "Воркшоп-майстер-клас", "Website Layout from scratch 2.0", "Front-End. Website Layout from Scratch using Preprocessors 2.0", 0,
`В цей четвер пропонуємо вам цікавий івент, пов’язаний із веб-розробкою. Запрошений гість - професіонал-практик, фронтенд-розробник із 7-річним досвідом веб-розробки, СЕО ІТ Aкадемії @hashtag.khm Дмитро Пиріжок.

З собою потрібно мати гарний настрій та ноутбуки, будемо в режимі реального часу розробляти фронт-енд сайту на препроцесорах🤤

❗️Вопкшоп відбудеться лише в режимі оФлаЙн в @iHub.khm
Нетворкінг та coffee-break зі смаколиками ☕️🍪🥨 включено 😋
Чекаємо на вас, буде мегацікаво і суперкорисно 😉
#hashtag_khm  #workshop  #front-end_development`,
"IMG_5551");

new Event("09-12-2020 16:00", "Зустріч", "Геопортал", "«Геопортал Хмельницької міської ради - нові можливості для розвитку громади»", 0,
`В рамках Меморандуму про співпрацю між Хмельницькою міською радою та Хмельницьким національним університетом 9.12.2020 о 16:00 в @iHub.khm відбудеться круглий стіл «Геопортал Хмельницької міської ради - нові можливості для розвитку громади» між представниками Міської ради та студентами @kisp_khnu
Запрошуються всі активні та ініціативні студенти, яким не байдужий розвиток рідного міста і які мають ідеї для покращення його благоустрою.
Посилання на онлайн-трансляцію:
Id: 733 761 1456
password: 123456
#meetup #OpenData #development`,
"c");

new Event("11-12-2020 16:30", "Воркшоп-майстер-клас", "Introduction to GIT", "Introduction to GIT", 0,
`Як і обіцяли - ще один івент від @massmediagroup, а саме від їх технічного директора, full stack розробника та випускника @kisp_khnu Романа Слободзяна @romaslobodzyan, у якому ми познайомимось із системами контролю версій та репозитарієм GIThub, що є просто must know у сфері розробки програмного забезпечення 🤓🧑‍💻
Чекаємо на вас в #ihub_khm та online 11 грудня о 16:30😉
За посиланням звертатися до організаторів.
#MassMediaGroup #kisp_khnu #workshop #GIT`,
"IMG_5621");

new Event("18-12-2020 15:00-17:00", "meetup, networking", "IT English Meetup", "IT English Meetup", 0,
`Would you like to step out of the comfort zone and dip into English for one  afternoon?😏
We invite you for IT English Meetup lead by Computer Engineering & Business Management Students of @khnu_khm
Bright Mapangera @vital_g25 and Marshia Mhazo this Friday, December 18th 3pm-5 pm
You will find out that conversational English is top 1 in IT soft skills list and have a great opportunity to improve your communication skills with our speakers 🙌
Great mood and networking is guaranteed 😃👌
#IT_English #meetup #networking #softskills`);