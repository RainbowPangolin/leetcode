// Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    //naive solution- find existing max num of candies all kids have, then iterate again checkign each kid's number of candies

    //probably better to sort by how manyh candies each kid has

    //or some sort od data structure that let's me select the set of kids who have >= X candies in O(1) time. 

    //Well it needs to be in an array so I need to iterate i by i anyway, and the naive solution is only O(2n), so that's not too bad. 

    let greatestNumCandies = findMaxCandies(candies);
    // how many candies a given kid needs to have the greatest number after getting extraCandies
    let cutOff = greatestNumCandies - extraCandies;

    const result = [];

    for(let i = 0; i < candies.length; i++){
        if(candies[i] >= cutOff){
            result[i] = true;
        } else {
            result[i] = false;
        }
    }

    return result;

};

function findMaxCandies(candiesArr){
    let max = 0;
    for (e of candiesArr){
        if (e > max){
            max = e
        }
    }

    return max;
}