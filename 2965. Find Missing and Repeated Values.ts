function findMissingAndRepeatedValues(grid: number[][]): number[] {
  const numbers: number[] = grid.flat();
  const set = new Set(numbers);

  let a = -1;
  let b = -1;

  for (let i = 1; i <= numbers.length; i += 1) {
    if (!set.has(i)) {
      b = i;
    }
  }

  numbers.forEach((n: number) => {
    if (set.has(n)) {
      set.delete(n);
    } else {
      a = n;
    }
  });

  return [a, b];
}
