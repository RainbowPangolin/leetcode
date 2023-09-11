// leetcode.com/problems/greatest-common-divisor-of-strings/

/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 * 
 * Problem:
 *  For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
 *  Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
 * Solution:
 *  With a brute force solution, the code can get very tedious. For an optimal solution, the code is braindead simple. You just concatenate the two strings, and see if they are the same. This works because if there exists a valid GCD, then both strings are just that valid GCD repeated a number of times, thus by adding the strings together, you are just repeating the GCD a different number of times. Then you just have to get the numerical GCD of the lengths and that gets you the length of the substring. 
 */
var gcdOfStrings = function(str1, str2) {
    //See if the two strings are the same
    if(str1.concat(str2) !== str2.concat(str1)){
        return '';
    } else {
        let GCD = findGCD(str1.length, str2.length);
        return (str1.substring(0, GCD))
    }

};

// Helper function since JS doesn't have an inbuilt one
function findGCD(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}