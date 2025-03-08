// 2161. Partition Array According to Given Pivot

function pivotArray(nums: number[], pivot: number): number[] {
  let [less, equal, greater] = getPartitions(nums, pivot);

  const newNums = new Array(nums.length);

  let lessStart = 0;
  let equalStart = less;
  let greaterStart = less + equal;

  for (const num of nums) {
    if (num < pivot) {
      newNums[lessStart] = num;
      lessStart += 1;
    } else if (num === pivot) {
      newNums[equalStart] = num;
      equalStart += 1;
    } else {
      newNums[greaterStart] = num;
      greaterStart += 1;
    }
  }

  return newNums;
}

function getPartitions(nums: number[], pivot: number): number[] {
  let less = 0;
  let equal = 0;
  let greater = 0;

  for (const num of nums) {
    if (num < pivot) less += 1;
    else if (num === pivot) equal += 1;
    else greater += 1;
  }

  return [less, equal, greater];
}

console.log(pivotArray([9, 12, 5, 10, 14, 3, 10], 10));
