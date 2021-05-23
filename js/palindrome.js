exports.palindrome = function (word) {
  if (typeof word === "number") {
    word = word.toString()
  }

  let wordReversed = word.split("").reverse().join("");

  if (word.toLowerCase() === wordReversed.toLowerCase()) {
    return true;
  } else {
    return false;
  }
};
