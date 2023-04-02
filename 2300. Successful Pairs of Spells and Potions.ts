function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    potions.sort((a,b) => a-b);
    const answer: number[] = [];

    const m = potions.length;
    const maxPotion = potions[m-1];

    for (const spell of spells) {
        const minPotion = Math.ceil(success/spell);
        if (minPotion > maxPotion) {
            answer.push(0);
            continue;
        }
        const index = lowerBound(potions, minPotion);
        answer.push(m - index);
    }
    return answer;
};

function lowerBound(arr:number[],key:number):number {
    let low=0, high=arr.length;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}