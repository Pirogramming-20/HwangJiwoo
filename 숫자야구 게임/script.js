const randomNumbers = [];
let cnt = 9;

const number1 = document.getElementById("number1");
const number2 = document.getElementById("number2");
const number3 = document.getElementById("number3");

const resultDisplay = document.querySelector(".result-display");
const inputBoxes = document.querySelectorAll(".input-box input");
const gameResultImg = document.getElementById('game-result-img');
const submitBtn = document.querySelector('.submit-button');

// 3개의 random 숫자 선택
function chooseNumbers() {
    while (randomNumbers.length < 3) {
        const randomNumber = Math.floor(Math.random() * 9) + 1;

        if (!randomNumbers.includes(randomNumber)) {
            randomNumbers.push(randomNumber);
        }
    }
}

// 각 위치의 수 비교
function compareNumbers(chosenNumbers) {
    const result = [0, 0];

    for (let i = 0; i < 3; i++) {
        if (randomNumbers[i] === chosenNumbers[i]) {
            result[0]++;
        } else if (randomNumbers.includes(chosenNumbers[i])) {
            result[1]++;
        }
    }

    return result
}

function check_numbers() {
    if (number1.value === '' || number2.value === '' || number2.value === '') {
        inputBoxes.forEach((input) => {
            input.value = '';
        })

        return;
    }

    cnt--;

    const chosenNumbers = [Number(number1.value), Number(number2.value), Number(number3.value)];
    const result = compareNumbers(chosenNumbers);

    if (result[0] === 0 && result[1] === 0) {
        const newResultHTML = `
        <div class="check-result">
            <div class="left">${chosenNumbers[0]} ${chosenNumbers[1]} ${chosenNumbers[2]}</div>
            :
            <div class="right">
                <div class="out num-result">O</div>
            </div>
        </div>
        `;

        resultDisplay.insertAdjacentHTML('beforeend', newResultHTML);
    } else {
        const newResultHTML = `
        <div class="check-result">
            <div class="left">${chosenNumbers[0]} ${chosenNumbers[1]} ${chosenNumbers[2]}</div>
            :
            <div class="right">
                ${result[0]} <div class="strike num-result">S</div>
                ${result[1]} <div class="ball num-result">B</div>
            </div>
        </div>
        `;

        resultDisplay.insertAdjacentHTML('beforeend', newResultHTML);
    }
    
    if (result[0] === 3) {
        gameResultImg.src = 'success.png';
        submitBtn.disabled = true;
    } else if (cnt === 0) {
        gameResultImg.src = 'fail.png';
        submitBtn.disabled = true;
    }

    inputBoxes.forEach((input) => {
        input.value = '';
    })
}

chooseNumbers();