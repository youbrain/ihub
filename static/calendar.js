const time = location.search.match(/\?t\=(\d{0,2})(\d{4})/);
let date = new Date();
if (time) {
    date.setMonth(+time[1]);
    date.setFullYear(+time[2]);
} else history.pushState(null, null, "?t=" + date.getMonth() + [] + date.getFullYear());

const months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
const day = ["Недiля", "Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота"];

function resetTime(d) {
    d.setHours(0); d.setMinutes(0); d.setSeconds(0); d.setMilliseconds(0);
}

function setSelection() {
    let month = months[date.getMonth()];
    let year  = date.getFullYear();
    document.getElementById("date").innerHTML = `${month} ${year}`;


    let a = document.querySelectorAll("div.month_nav a");
    let d = new Date(date.getTime());
    d.setMonth(d.getMonth() - 1);
    a[0].setAttribute("href", `?t=${d.getMonth()}${d.getFullYear()}`);
    d.setMonth(d.getMonth() + 2);
    a[1].setAttribute("href", `?t=${d.getMonth()}${d.getFullYear()}`);

    if (date.getMonth() != (new Date).getMonth() || date.getFullYear() != (new Date).getFullYear()) {
        let today = document.createElement("a");
        today.innerHTML = `<br>
            <a href="?t=${(new Date).getMonth()}${(new Date).getFullYear()}" class="today_btn">
                <button type="button" class="btn btn-danger btn-sm">Сьогодні</button>
            </a>`;
        document.querySelector("div.month_nav>div").append(today);
    }
}
setSelection();

function fill() {
    let d = new Date(date.getTime()); d.setDate(1);
    while (d.getDay() != 1) { d.setDate(d.getDate() - 1); }

    let elems = document.querySelectorAll("#calendar td");
    resetTime(d);
    for (let elem of elems) {
        elem.classList.add("t" + d.getTime());
        let thisMonth = true;
        if (d.getMonth()!=date.getMonth()) {
            elem.classList.add("other");
            thisMonth = false;
        }
        if (d.getDay() == 1 && !thisMonth && elem != elems[0]) {
            elem.remove();
            continue;
        }
        elem.innerHTML = `<span>${d.getDate()}</span>`;
        
        if (d.getMonth() == (new Date()).getMonth() && d.getDate() == (new Date()).getDate() && d.getFullYear() == (new Date()).getFullYear()) elem.setAttribute("id", "today");
        d.setDate(d.getDate() + 1);
    }
}
fill();  

function addEvents(events) {
    function showEvent(i) {
        let event = Event.all[i];
        if (!location.search.match(/\?e=(\d+)/)) history.pushState(null, null, `${location.search}?e=${i}`);
        document.querySelector("#alert").classList.add("show");
        document.body.classList.add("not-scroll");
        window.scrollTo(0, 0);
        document.querySelector("#alert").scrollTo(0, 0);

        document.querySelector("#alert").onclick = function (e) {
            if (e.target == this) {
                history.pushState(null, null, location.search.replace(/\?e=(\d+)/, ""));
                document.querySelector("#alert").classList.remove("show");
                document.body.classList.remove("not-scroll");
            }
        }

        let $ = se => document.querySelector(`#alert > .block ${se}`);
        $(".type").innerHTML = event.type;
        $(".topic").innerHTML = event.topic;
        if (event.imageURL) $("img").setAttribute("src", `${event.imageURL}`);
        else $("img").setAttribute("src", "#");
        $(".description p").innerHTML = event.description;
        $(".description").classList.remove("show");
        
        // $(".cost").innerHTML = `<span>${event.cost || "$ ВАРТІСТЬ:"}</span>: Безкоштовно`;
        
        $(".when h5").innerHTML = `${day[event.getDay()]} ${event.getStrTime()}`
    }
    function addEvent(elem, event, i) {
        if (!elem) return;
        elem.innerHTML += `
        <div class="event">
            <div class="topic">${event.short_topic}</div>
            <div class="time">${event.time.split(" ")[1]}</div>
        </div>`
        elem.classList.add(`e${i}`);
        elem.childNodes[2].onclick = () => showEvent(i);
    }
    
    for (let event of events) {
        let time = event.getTime();
        resetTime(time);
        addEvent(document.querySelector(`td.t${time.getTime()}`), event, events.indexOf(event));
    }
}
addEvents(Event.all);

let _event = location.search.match(/\?e=(\d+)/);
if (_event) {
    let elem = document.querySelector(`td.e${_event[1]} .event`)
    if (elem) elem.onclick();
}

function copy(text) {
    let link = document.getElementById("link");
    link.setAttribute("value", text);
    link.select();
    document.execCommand("copy");
}