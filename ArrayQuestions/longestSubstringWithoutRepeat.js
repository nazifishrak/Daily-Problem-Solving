function lengthOfLongestSubstring(s) {
  let l = 0,
    r = 0,
    ans = 0,
    n = s.length;
  const charSeen = {};
  function invalidWindow(char) {
    return charSeen[char] > 1;
  }
  for (; r < n; r++) {
    if (!charSeen[s[r]]) {
      charSeen[s[r]] = 0;
    }
    charSeen[s[r]] += 1;

    for (; invalidWindow(s[r]); l++) {
      charSeen[s[r]] -= 1;
    }
    ans = Math.max(ans, r - l + 1);
  }

  return ans;
}

function runTests() {
  const testCases = [
    { input: "abcabcbb", expected: 3 },
    { input: "bbbbb", expected: 1 },
    { input: "pwwkew", expected: 3 },
    { input: "", expected: 0 },
    { input: "abcdef", expected: 6 },
    { input: "aab", expected: 2 },
    { input: "dvdf", expected: 3 },
    { input: "anviaj", expected: 5 },
    { input: "abcabcbb", expected: 3 },
    { input: "tmmzuxt", expected: 5 },
  ];

  testCases.forEach(({ input, expected }, index) => {
    const result = lengthOfLongestSubstring(input);
    console.log(
      `Test Case ${index + 1}: ${
        result === expected ? "Passed" : "Failed"
      } (Input: "${input}", Expected: ${expected}, Got: ${result})`
    );
  });
}

runTests();
