var pal = require("./palindrome");

test('works for all lower', () => {
  expect(pal.palindrome('racecar')).toBe(true);
})

test('works w/ capital letters', () => {
  expect(pal.palindrome("ciVic")).toBe(true);
})

test('correctly fails (letters)', () => {
  expect(pal.palindrome('nice')).toBe(false);
})

test('works for numbers', () => {
  expect(pal.palindrome(434)).toBe(true);
})

test('correctly fails (numbers)', () => {
  expect(pal.palindrome(123)).toBe(false);
})

test('challenge case 1', () => {
  expect(pal.palindrome("Sore was I ere I saw Eros")).toBe(true);
})