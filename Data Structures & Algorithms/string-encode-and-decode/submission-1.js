class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map((str) => `${str.length}#${str}`).join('');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log(str);
        let res = [], idx = 0;

        while (idx < str.length) {
            let specialCharIdx = str.indexOf('#', idx);
            let length = Number(str.slice(idx, specialCharIdx));
            let word = str.slice(specialCharIdx + 1, specialCharIdx + length + 1);
            res.push(word);

            idx = specialCharIdx + length + 1;
        }

        return res;
    }
}