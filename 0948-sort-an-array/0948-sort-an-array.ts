function sortArray(nums: number[]): number[] {
  if (nums.length <= 1) {
    return nums;
  }

  const pivotIndex = Math.floor(Math.random() * nums.length); // Random pivot
  const pivot = nums[pivotIndex];
  const l = [];
  const r = [];
  const mid = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < pivot) {
      l.push(nums[i]);
    } else if (nums[i] > pivot) {
      r.push(nums[i]);
    } else {
      mid.push(nums[i]);
    }
  }

  return [...sortArray(l), ...mid, ...sortArray(r)];
}