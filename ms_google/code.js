if (typeof Logger == 'undefined') {
  globalThis.Logger = { log: (...args) => console.log(...args) };
}

const AGE = 23;
const NAME = 'Jane';

function isAdult() {
  var response = "We don't know yet";
  if (AGE < 18) {
    var response = NAME + ' is not an adult';
    Logger.log(response)
  } else {
    var response = NAME + ' is an adult';
    Logger.log(response);
  }
  Logger.log(response);
}

isAdult()
