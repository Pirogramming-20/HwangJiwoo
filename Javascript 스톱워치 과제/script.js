const time = document.getElementById("time");
const start = document.getElementById("start");
const stop = document.getElementById("stop");
const reset = document.getElementById("reset");

const record = document.getElementById("record");
const deleteBtn = document.getElementById("delete__btn");
const checkAll = document.querySelector(".check__all");

let clock = 0;
let timerId;

start.addEventListener("click", activeWatch)

// start 버튼
function activeWatch() {
    printTime();
    timerId = setTimeout(activeWatch, 10);
}

// 시간계산
function printTime() {
    clock++;
    time.innerText = timeToString();
}

// 시간을 문자열로 변환
function timeToString() {
    sec = parseInt(clock / 100);
    mSec =  clock % 100;

    return String(sec).padStart(2, '0') + ":" + String(mSec).padStart(2, '0');
}

// stop 버튼
stop.addEventListener("click",stopWatch)

function stopWatch() {
    if (timerId !== null) {
        clearTimeout(timerId);
        timerId = null;
        const recordContent = document.createElement("div");
        recordContent.classList.add("record__content");

        const checkBtn = document.createElement("div");
        checkBtn.classList.add("check__btn");

        const recordTime = document.createElement("div");
        recordTime.classList.add("record__time");
        recordTime.innerText = time.innerText;

        recordContent.appendChild(checkBtn);
        recordContent.appendChild(recordTime);

        record.appendChild(recordContent);
    }
}

// reset 버튼
reset.addEventListener("click", () => {
    time.innerText = "00:00";
    clock = 0;
})

// 삭제할 기록 체크
record.addEventListener("click", (e) => {
    e.target.parentNode.classList.toggle("checked");

    let contentGroup = document.getElementsByClassName("record__content");
    let contentArray = Array.from(contentGroup);
    let len = contentArray.length;
    let cnt = 0;
    contentArray.forEach((element) => {
        if (element.classList.contains("checked")) {
            cnt++;
        }
    })

    if (len === cnt) {
        checkAll.classList.toggle("checked");
    } else if (checkAll.classList.contains("checked")) {
        checkAll.classList.toggle("checked");
    }
})

// 기록 삭제
deleteBtn.addEventListener("click", () => {
    let contentGroup = document.getElementsByClassName("checked");
    let contentArray = Array.from(contentGroup);
    for (let content of contentArray) {
        if (content.classList.contains("check__all")) {
            continue;
        }
        content.remove();
    }

    if (checkAll.classList.contains("checked")) {
        checkAll.classList.toggle("checked");
    }
})

// 전체 선택 버튼
checkAll.addEventListener("click", (e) => {
    e.target.classList.toggle("checked");
    let contentGroup = document.getElementsByClassName("record__content");
    let contentArray = Array.from(contentGroup);
    
    if (e.target.classList.contains("checked")) {
        for (let content of contentArray) {
            if (!content.classList.contains("checked")) {
                content.classList.toggle("checked");
            }
        }
    } else {
        for (let content of contentArray) {
             content.classList.toggle("checked");
        }
    }
})