class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map((str) => `${str.length}:${str}`).join('#');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let idx = 0;

        while (idx < str.length) {
            let colonIdx = str.indexOf(':', idx);
            let length = Number(str.slice(idx, colonIdx));
            let word = str.slice(colonIdx + 1, colonIdx + length + 1);
            res.push(word);

            idx = colonIdx + 1 + length + 1;
        }

        return res;
    }
}

// ["we","say",":","yes"]
// encoded: 2:we#3:say#::#3:yes#
// rules to decode:
//  1. 